"""阶段 B：向量检索 -> Cross-Encoder 重排 对比实验"""

import os

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from sentence_transformers import CrossEncoder

from config import CHROMA_DIR, EMBEDDING_MODEL, HF_OFFLINE, K, RERANK_MODEL

if HF_OFFLINE:
    os.environ["HF_HUB_OFFLINE"] = "1"

embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
db = Chroma(persist_directory=str(CHROMA_DIR), embedding_function=embeddings)
reranker = CrossEncoder(RERANK_MODEL)

question = "用 LangChain 构建 RAG 需要哪些核心组件？"
results = db.similarity_search_with_score(question, k=K)

print("=== 重排前（向量检索顺序）===")
for i, (doc, score) in enumerate(results, 1):
    print(f"[{i}] 向量距离 {score:.4f} | {doc.page_content[:45]!r}")

pairs = [[question, doc.page_content] for doc, _ in results]
scores = reranker.predict(pairs)

print("\n=== 重排后（Cross-Encoder 打分）===")
ranked = sorted(zip(scores, results), key=lambda x: x[0], reverse=True)
for i, (s, (doc, _)) in enumerate(ranked, 1):
    print(f"[{i}] 重排分 {s:.4f} | {doc.page_content[:45]!r}")
