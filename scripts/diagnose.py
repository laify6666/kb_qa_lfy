"""分层诊断脚本：与生产同源的检索（复用 rag_qa.retrieve_hybrid：混合+重排+邻居）。

用法（在 scripts 目录或项目根、且能 import config 时）：
  python diagnose.py --questions ../tests/questions_full.md
  python diagnose.py --k 10

指标口径（必须分开看，不能混成一个数）：
  - 文件 hit@5 / @10：来源文件名是否出现在 top-k 块的 metadata 里（粗筛，容易虚高）
  - 短语 hit@5 / @10（库内可检）：金标短语至少有一条出现在全库时，才进入分母；
    命中 = 这些短语是否出现在 top-k **块文本**里。覆盖缺口不进分母，避免把「评估措辞≠原文」算成检索失败。
  - 字面口径（含缺口）：旧算法，缺口题也进分母，仅作对照，不作主指标。
  - 覆盖缺口：一条短语在全语料都找不到 → 金标/语料问题，不是检索问题
  - 块级漏召回：短语在语料里有，但 top-5 块没有 → 切分/排序问题

无答案题（来源为空）不进入命中率分母。
"""

import argparse
import os
import re
from pathlib import Path

from config import HF_OFFLINE
from load_documents import load_documents

if HF_OFFLINE:
    os.environ["HF_HUB_OFFLINE"] = "1"

RAW_DIR = Path(__file__).parent.parent / "data" / "raw"


def parse_questions(path: Path):
    """解析测试集为结构化题目列表。

    Returns:
        [(类别, 序号, 问题, 来源列表或 None, 答案要点), ...]
        来源为 None 表示无答案题，不能计入检索命中率。
    """
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


def extract_phrases(points: str):
    """从「A(要点)」里切出可检索的短语。

    用标点切开是为了避免整句过长导致几乎永远匹配失败；
    长度下限 6 是为了丢掉「的」「以及」这类没有区分度的碎片。
    """
    if not points:
        return []
    return [x.strip() for x in re.split(r"[；;。，,、\n:：()（）]", points) if len(x.strip()) >= 6]


def coverage_check(phrases, corpus_text: str):
    """检查短语是否存在于全语料（小写后子串匹配）。

    Returns:
        (是否整题覆盖缺口, 命中短语, 缺失短语)
        覆盖缺口 = 一条短语都找不到，说明不是检索问题，是语料没写。
    """
    if not phrases:
        return None, [], []
    found = [p for p in phrases if p.lower() in corpus_text]
    missing = [p for p in phrases if p.lower() not in corpus_text]
    return (len(found) == 0), found, missing


def phrase_hit_in_text(phrases, blob: str):
    """短语是否出现在给定文本（通常是 top-k 块拼接）里。"""
    if not phrases:
        return None, [], []
    blob_l = blob.lower()
    found = [p for p in phrases if p.lower() in blob_l]
    missing = [p for p in phrases if p.lower() not in blob_l]
    return (len(found) > 0), found, missing


def _file_hit_ranks(chunk_srcs, srcs):
    """返回来源文件出现在检索结果中的下标列表（0-based）。"""
    if not srcs:
        return []
    return [i for i, s in enumerate(chunk_srcs)
            if any(x in s or s in x for x in srcs)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--questions", type=Path,
                    default=Path(__file__).parent.parent / "tests" / "questions_full.md")
    ap.add_argument("--k", type=int, default=10)
    args = ap.parse_args()

    # 延后 import：run_eval --score-only 只用 parse_questions，不应拉起向量模型
    from rag_qa import retrieve_hybrid

    docs = load_documents(RAW_DIR)
    source_set = {meta["source"] for _, _, meta in docs}
    corpus_text = "\n".join(text for _, text, _ in docs).lower()
    print(f"[语料] {len(docs)} 篇文档 | [检索] 混合+重排+邻居，k={args.k}")

    questions = parse_questions(args.questions)
    print(f"[测试集] {len(questions)} 题\n")

    rows = []
    stats = {}
    corpus_gap_n = 0
    chunk_miss_n = 0
    for category, no, q, srcs, points in questions:
        hits = retrieve_hybrid(q, k=args.k)
        chunk_srcs = [s for _t, s in hits]
        in_top = _file_hit_ranks(chunk_srcs, srcs)
        file_hit5 = any(i < 5 for i in in_top)
        file_hitK = bool(in_top)
        exist = (all(x in source_set for x in srcs)) if srcs else None

        phrases = extract_phrases(points)
        # 覆盖缺口看全库；短语命中只看检索到的块——这是本轮口径修正的核心
        corpus_gap, corpus_found, corpus_missing = coverage_check(phrases, corpus_text)
        top5_blob = "\n".join(t for t, _ in hits[:5])
        topk_blob = "\n".join(t for t, _ in hits)
        phrase5, ph5_found, ph5_missing = phrase_hit_in_text(phrases, top5_blob)
        phraseK, phk_found, phk_missing = phrase_hit_in_text(phrases, topk_blob)

        if srcs and corpus_gap:
            corpus_gap_n += 1
        # 块级漏召回：料在库里，但 top-5 块没拿到要点
        chunk_miss = bool(srcs and phrases and corpus_gap is False and phrase5 is False)
        if chunk_miss:
            chunk_miss_n += 1

        s = stats.setdefault(category, {
            "total": 0, "file5": 0, "file10": 0,
            "ph_eligible": 0, "ph5": 0, "ph10": 0,
            "ph_literal": 0, "ph5_literal": 0, "gap": 0, "manual": 0,
        })
        if srcs:
            s["total"] += 1
            s["file5"] += int(file_hit5)
            s["file10"] += int(file_hitK)
            if phrases:
                # 字面口径仍把缺口题算进分母，只用来对照旧 62%
                s["ph_literal"] += 1
                s["ph5_literal"] += int(bool(phrase5))
                if corpus_gap:
                    s["gap"] += 1
                else:
                    # 主指标：库里至少有一条金标短语，才谈得上「检索有没有拿到」
                    s["ph_eligible"] += 1
                    s["ph5"] += int(bool(phrase5))
                    s["ph10"] += int(bool(phraseK))
        else:
            s["manual"] += 1

        rows.append({
            "category": category, "no": no, "q": q, "srcs": srcs, "exist": exist,
            "file_hit5": file_hit5, "file_hitK": file_hitK,
            "phrase5": phrase5, "phraseK": phraseK,
            "corpus_gap": corpus_gap, "chunk_miss": chunk_miss,
            "points": points, "ph5_found": ph5_found, "ph5_missing": ph5_missing,
            "corpus_found": corpus_found, "corpus_missing": corpus_missing,
            "hits": hits,
        })

        if srcs:
            fmark = "文件HIT5" if file_hit5 else ("文件HIT10" if file_hitK else "文件MISS")
            pmark = "短语HIT5" if phrase5 else ("短语HIT10" if phraseK else "短语MISS")
            extra = "覆盖缺口" if corpus_gap else ("块级漏召回" if chunk_miss else "")
            print(f"[{category}] Q{no} {fmark} {pmark} {extra} | {q[:36]}")
        else:
            print(f"[{category}] Q{no} （无来源,不计入命中率） | {q[:36]}")

    print("\n===== 汇总（仅统计有来源、可自动判的题）=====")
    all_t = all_f5 = all_f10 = 0
    all_el = all_p5 = all_p10 = 0
    all_lit = all_lit5 = all_gap = manual = 0
    for cat, s in stats.items():
        f5 = s["file5"] / s["total"] if s["total"] else 0
        p5 = s["ph5"] / s["ph_eligible"] if s["ph_eligible"] else 0
        print(
            f"{cat}: 可判 {s['total']} | 文件hit@5={s['file5']} ({f5:.0%}) | "
            f"短语hit@5(库内可检)={s['ph5']}/{s['ph_eligible']} ({p5:.0%}) | "
            f"覆盖缺口 {s['gap']} | 需人工 {s['manual']}"
        )
        all_t += s["total"]
        all_f5 += s["file5"]
        all_f10 += s["file10"]
        all_el += s["ph_eligible"]
        all_p5 += s["ph5"]
        all_p10 += s["ph10"]
        all_lit += s["ph_literal"]
        all_lit5 += s["ph5_literal"]
        all_gap += s["gap"]
        manual += s["manual"]
    if all_t:
        print(
            f"总计: 可判 {all_t} 题 | 文件hit@5={all_f5} ({all_f5/all_t:.0%}) | "
            f"文件hit@10={all_f10}"
        )
    if all_el:
        print(
            f"       短语hit@5（库内可检）={all_p5}/{all_el} ({all_p5/all_el:.0%}) | "
            f"短语hit@10={all_p10}/{all_el} ({all_p10/all_el:.0%})"
        )
    if all_lit:
        print(
            f"       字面口径（含缺口，旧）={all_lit5}/{all_lit} "
            f"({all_lit5/all_lit:.0%})  ← 不作为主指标"
        )
    print(f"覆盖缺口（不进短语分母）: {corpus_gap_n} 题")
    print(f"块级漏召回（库里有、top-5 块没有）: {chunk_miss_n} 题  ← 切分/排序应打这里")

    out = Path(__file__).parent.parent / "tests" / "diagnose_report.md"
    with open(out, "w", encoding="utf-8") as f:
        f.write(f"# 检索命中诊断报告（混合+重排+邻居，k={args.k}）\n\n")
        f.write(
            "口径：短语 hit 只统计「库内可检」题（金标短语至少一条能在全库找到）；"
            "覆盖缺口单独报，不进分母。字面口径仅对照旧 62%。\n\n"
        )
        f.write(
            f"文件hit@5={all_f5}/{all_t} | "
            f"短语hit@5（库内可检）={all_p5}/{all_el} | "
            f"覆盖缺口={corpus_gap_n}（不进短语分母） | "
            f"块级漏召回={chunk_miss_n}\n\n"
        )
        if all_lit:
            f.write(
                f"字面口径（含缺口，旧）={all_lit5}/{all_lit} "
                f"({all_lit5/all_lit:.0%})\n\n"
            )
        for r in rows:
            fmark = "文件HIT5" if r["file_hit5"] else ("文件HIT10" if r["file_hitK"] else "文件MISS")
            if r["phrase5"] is True:
                pmark = "短语HIT5"
            elif r["phraseK"] is True:
                pmark = "短语HIT10"
            elif r["phrase5"] is False:
                pmark = "短语MISS"
            else:
                pmark = "短语—"
            tag = ""
            if r["corpus_gap"]:
                tag = " 覆盖缺口"
            elif r["chunk_miss"]:
                tag = " 块级漏召回"
            src_str = " + ".join(r["srcs"]) if r["srcs"] else "（无来源/语料无）"
            f.write(f"## {r['category']} Q{r['no']} [{fmark}] [{pmark}]{tag}\n\n")
            f.write(f"Q: {r['q']}\n\n来源: {src_str} | 语料中存在: {r['exist']}\n\n")
            if r["points"]:
                f.write(f"A(要点): {r['points']}\n\n")
                f.write(f"top-5 短语命中: {r['ph5_found'] if r['ph5_found'] else '（无）'}\n\n")
                f.write(f"top-5 短语缺失: {r['ph5_missing'] if r['ph5_missing'] else '（无）'}\n\n")
                if r["corpus_missing"]:
                    f.write(f"全库也缺失: {r['corpus_missing']}\n\n")
            for i, (t, s) in enumerate(r["hits"][:args.k], 1):
                f.write(f"{i}. ({s})\n{t[:120]}\n\n")
    print(f"\n详细报告已写入: {out}")


if __name__ == "__main__":
    main()
