"""跑测试集：调用 ask_rag，并按答案要点自动打分。

用法（scripts 目录）：
  python run_eval.py              # 调 LLM 逐题问答 + 打分
  python run_eval.py --score-only # 只对已有 answers.md 打分，不花 API
"""

import argparse
import re
import sys
from pathlib import Path

from config import ANSWERS_PATH, QUESTIONS_PATH
from diagnose import extract_phrases, parse_questions

REFUSAL = "资料中没有相关信息"
# --score-only 写到旁路文件，避免覆盖原始 answers.md
SCORE_PATH = ANSWERS_PATH.with_name("eval_score.md")


def score_one(answer: str, srcs, points: str):
    """对照要点短语给单题打档。

    无来源题只看是否拒答；有来源题看答案里覆盖了多少要点短语。
    阈值 50% 算「正确」是为了容忍措辞不完全一致，不是放水到瞎答。

    Returns:
        (档位, 命中短语, 缺失短语)
    """
    ans = answer or ""
    refused = REFUSAL in ans or "没有相关信息" in ans
    if not srcs:
        return ("正确拒答" if refused else "幻觉", [], [])
    if refused:
        return ("过度拒答", [], [])
    phrases = extract_phrases(points)
    if not phrases:
        return ("无法自动判", [], [])
    blob = ans.lower()
    found = [p for p in phrases if p.lower() in blob]
    missing = [p for p in phrases if p.lower() not in blob]
    ratio = len(found) / len(phrases)
    if ratio >= 0.5:
        return ("正确", found, missing)
    if found:
        return ("部分", found, missing)
    return ("漏答", found, missing)


def parse_saved_answers(path: Path):
    """解析 answers.md -> {题号: (问题, 答案)}。"""
    text = path.read_text(encoding="utf-8")
    out = {}
    chunks = re.split(r"^## 第\s*(\d+)\s*题", text, flags=re.M)
    # split 后: [前言, no1, body1, no2, body2, ...]
    for i in range(1, len(chunks), 2):
        no = int(chunks[i])
        body = chunks[i + 1]
        q, a = "", ""
        m_q = re.search(r"^Q:\s*(.*)$", body, re.M)
        if m_q:
            q = m_q.group(1).strip()
        # 不要带 $：re.M 下 $ 会停在首行，多段答案会被截断
        m_a = re.search(r"^A:\s*(.*)", body, re.M | re.S)
        if m_a:
            a = m_a.group(1).strip()
        out[no] = (q, a)
    return out


def format_report(questions, answers_by_no, scored):
    """生成带汇总表的 markdown 报告。"""
    counts = {}
    for status, *_ in scored.values():
        counts[status] = counts.get(status, 0) + 1
    lines = ["# 评估报告（自动对照要点）\n", "## 汇总\n"]
    for k in ("正确", "部分", "漏答", "过度拒答", "正确拒答", "幻觉", "无法自动判", "执行出错"):
        if k in counts:
            lines.append(f"- {k}: {counts[k]}")
    n_ans = sum(counts.get(k, 0) for k in ("正确", "部分", "漏答", "过度拒答"))
    n_ok = counts.get("正确", 0)
    n_ref = counts.get("正确拒答", 0)
    n_hall = counts.get("幻觉", 0)
    if n_ans:
        lines.append(f"- 可答题正确（含阈值）: {n_ok}/{n_ans} ({n_ok / n_ans:.0%})")
    lines.append(f"- 无答案题拒答: {n_ref} | 幻觉: {n_hall}")
    lines.append("\n## 逐题\n")
    for _cat, no, q, srcs, points in questions:
        ans_q, answer = answers_by_no.get(no, (q, ""))
        status, found, missing = scored[no]
        lines.append(f"## 第 {no} 题 [{status}]\n")
        lines.append(f"Q: {q}\n")
        if found or missing:
            lines.append(f"要点命中: {found or '（无）'}")
            lines.append(f"要点缺失: {missing or '（无）'}\n")
        lines.append(f"A: {answer}\n")
    return "\n".join(lines), counts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--score-only", action="store_true", help="只打分，不调用 LLM")
    args = ap.parse_args()

    questions = parse_questions(QUESTIONS_PATH)
    print(f"共 {len(questions)} 题")

    answers_by_no = {}
    if args.score_only:
        if not ANSWERS_PATH.exists():
            sys.exit(f"找不到 {ANSWERS_PATH}，请先跑完整评估")
        parsed = parse_saved_answers(ANSWERS_PATH)
        for _cat, no, q, _srcs, _pts in questions:
            _pq, a = parsed.get(no, (q, ""))
            answers_by_no[no] = (q, a)
    else:
        from rag_qa import ask_rag
        for cat, no, q, srcs, points in questions:
            try:
                answer = ask_rag(q)
                preview = answer.replace("\n", " ")[:32]
                print(f"[{no}/{len(questions)}] {q[:20]}… -> {preview}…")
            except Exception as e:
                answer = f"执行出错：{e}"
                print(f"[{no}/{len(questions)}] 出错：{e}")
            answers_by_no[no] = (q, answer)

    scored = {}
    for _cat, no, q, srcs, points in questions:
        _pq, answer = answers_by_no[no]
        if answer.startswith("执行出错"):
            scored[no] = ("执行出错", [], [])
        else:
            scored[no] = score_one(answer, srcs, points)
        print(f"  Q{no} {scored[no][0]}")

    report, counts = format_report(questions, answers_by_no, scored)
    out = SCORE_PATH if args.score_only else ANSWERS_PATH
    out.write_text(report, encoding="utf-8")
    print(f"\n汇总: {counts}")
    print(f"已写入 {out}")


if __name__ == "__main__":
    main()
