"""分层诊断脚本：与生产同源的混合检索（复用 rag_qa.retrieve_hybrid）。

用法（项目根目录）：
  python scripts\diagnose.py --questions tests\questions_full.md
  python scripts\diagnose.py --k 10

输出：每题 hit@5/hit@10 + 疑似覆盖缺口标记；汇总；tests\diagnose_report.md
"""

import argparse
import os
import re
from pathlib import Path

from config import HF_OFFLINE
from load_documents import load_documents
from rag_qa import retrieve_hybrid

if HF_OFFLINE:
    os.environ["HF_HUB_OFFLINE"] = "1"

RAW_DIR = Path(__file__).parent.parent / "data" / "raw"


def parse_questions(path: Path):
    """解析 -> [(类别, 序号, 问题, 来源列表或None, 答案要点), ...]"""
    questions = []
    category = "未分类"
    cur = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("## ") and not line.startswith("###"):
            category = line.lstrip("# ").strip()
            continue
        m = re.match(r"^(\d+)\.\s*Q:", line)
        if m:
            if cur:
                questions.append(cur)
            cur = [category, int(m.group(1)), line.split("Q:", 1)[1].strip(), None, ""]
            continue
        if cur and line.startswith("A(要点)"):
            cur[4] = line.split(":", 1)[1].strip()
            continue
        if cur and line.startswith("来源:"):
            raw_src = line.split(":", 1)[1].strip()
            parts = [x.strip() for x in raw_src.split("+") if x.strip() and x.strip() != "语料无"]
            cur[3] = parts or None
    if cur:
        questions.append(cur)
    return questions


def coverage_check(points: str, corpus_text: str):
    if not points:
        return None, [], []
    phrases = [x.strip() for x in re.split(r"[；;。，,、\n:：()（）]", points) if len(x.strip()) >= 6]
    if not phrases:
        return None, [], []
    found = [p for p in phrases if p.lower() in corpus_text]
    missing = [p for p in phrases if p.lower() not in corpus_text]
    return (len(found) == 0), found, missing


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--questions", type=Path,
                    default=Path(__file__).parent.parent / "tests" / "questions_full.md")
    ap.add_argument("--k", type=int, default=10)
    args = ap.parse_args()

    docs = load_documents(RAW_DIR)
    source_set = {meta["source"] for _, _, meta in docs}
    corpus_text = "\n".join(text for _, text, _ in docs).lower()
    print(f"[语料] {len(docs)} 篇文档 | [检索] 混合检索(向量+BM25 RRF)，k={args.k}")

    questions = parse_questions(args.questions)
    print(f"[测试集] {len(questions)} 题\n")

    rows = []
    stats = {}
    gap_count = 0
    for category, no, q, srcs, points in questions:
        hits = retrieve_hybrid(q, k=args.k)          # [(text, source), ...]
        chunk_srcs = [s for _t, s in hits]
        in_top = [i for i, s in enumerate(chunk_srcs)
                  if srcs and any(x in s or s in x for x in srcs)]
        hit5 = any(i < 5 for i in in_top)
        hitK = bool(in_top)
        exist = (all(x in source_set for x in srcs)) if srcs else None
        gap, found, missing = coverage_check(points, corpus_text)
        if gap:
            gap_count += 1

        s = stats.setdefault(category, {"total": 0, "hit5": 0, "hit10": 0, "manual": 0})
        if srcs:
            s["total"] += 1
            s["hit5"] += int(hit5)
            s["hit10"] += int(hitK)
        else:
            s["manual"] += 1

        rows.append((category, no, q, srcs, exist, hit5, hitK, points, gap, found, missing, hits))
        mark = "HIT5" if hit5 else ("HIT10" if hitK else "MISS")
        gap_s = "⚠️疑似缺口" if gap else ("有料" if points else "")
        if srcs:
            print(f"[{category}] Q{no} {mark} {gap_s} | {q[:38]}")
        else:
            print(f"[{category}] Q{no} {mark}(无来源,需人工) {gap_s} | {q[:38]}")

    print("\n===== 汇总（仅统计有来源、可自动判的题）=====")
    all_t = all5 = all10 = manual = 0
    for cat, s in stats.items():
        print(f"{cat}: 可判 {s['total']} 题 | hit@5 = {s['hit5']} ({s['hit5']/max(s['total'],1):.0%}) | 需人工 {s['manual']}")
        all_t += s["total"]; all5 += s["hit5"]; all10 += s["hit10"]; manual += s["manual"]
    if all_t:
        print(f"总计: 可判 {all_t} 题 | hit@5 = {all5} ({all5/all_t:.0%}) | hit@10 = {all10} | 需人工 {manual} 题")
    print(f"疑似语料覆盖缺口: {gap_count} 题 —— 需人工确认（逐字匹配的粗筛，多为误报）")

    out = Path(__file__).parent.parent / "tests" / "diagnose_report.md"
    with open(out, "w", encoding="utf-8") as f:
        f.write(f"# 检索命中诊断报告（混合检索，k={args.k}）\n\n")
        for category, no, q, srcs, exist, hit5, hitK, points, gap, found, missing, hits in rows:
            mark = "HIT5" if hit5 else ("HIT10" if hitK else "MISS")
            src_str = " + ".join(srcs) if srcs else "（无来源/语料无）"
            f.write(f"## {category} Q{no} [{mark}] {'⚠️疑似缺口' if gap else ''}\n\n")
            f.write(f"Q: {q}\n\n来源: {src_str} | 语料中存在: {exist}\n\n")
            if points:
                f.write(f"A(要点): {points}\n\n要点短语命中: {found if found else '（无）'}\n\n要点短语缺失: {missing if missing else '（无）'}\n\n")
            for i, (t, s) in enumerate(hits[:args.k], 1):
                f.write(f"{i}. ({s})\n{t[:100]}\n\n")
    print(f"\n详细报告已写入: {out}")


if __name__ == "__main__":
    main()