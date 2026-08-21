"""实验：混合检索 top-10 之后，再加 Cross-Encoder 重排取 top-5，对比重排前后 hit@5 与 top-5 组成。

只跑检索，不调 LLM；使用已缓存的 bge-reranker-base，零下载。
"""
import os, sys
from pathlib import Path
sys.path.insert(0, 'scripts')

from sentence_transformers import CrossEncoder

from config import HF_OFFLINE, RERANK_MODEL
from rag_qa import retrieve_hybrid
from diagnose import parse_questions

if HF_OFFLINE:
    os.environ["HF_HUB_OFFLINE"] = "1"

reranker = CrossEncoder(RERANK_MODEL)
qs = parse_questions(Path("tests/questions_full.md"))

hit_b, hit_a = 0, 0
changed = 0
judgeable = 0
print("Q   重排前top5来源                          重排后top5来源")
for cat, no, q, srcs, _points in qs:
    if not srcs:
        continue
    judgeable += 1
    cands = retrieve_hybrid(q, k=10)                 # [(text, source), ...]
    src_b = [s for _t, s in cands[:5]]
    hit_b += any(x in s or s in x for s in src_b for x in srcs)

    pairs = [[q, t] for t, _ in cands]
    scores = reranker.predict(pairs)
    ranked = sorted(zip(cands, scores), key=lambda x: -x[1])[:5]
    src_a = [s for (_t, s), _sc in ranked]
    hit_a += any(x in s or s in x for s in src_a for x in srcs)

    if src_a != src_b:
        changed += 1
    print(f"Q{no:<3} {'/'.join(sorted(set(src_b)))[:44]:<46} {'/'.join(sorted(set(src_a)))[:44]}")

print(f"\n可判题 {judgeable} | 重排前 hit@5 = {hit_b} ({hit_b/judgeable:.0%}) | 重排后 hit@5 = {hit_a} ({hit_a/judgeable:.0%})")
print(f"top-5 组成发生变化的题数: {changed}")