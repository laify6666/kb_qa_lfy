"""建库脚本：加载 -> 结构感知切分 -> 向量化 -> 入库。

用法（在项目根目录运行）：
  python scripts/build_vectorstore.py               # 全量重建（默认，安全）
  python scripts/build_vectorstore.py --incremental # 增量 upsert（按 id 去重，不删旧数据）
  python scripts/build_vectorstore.py --dry-run     # 只统计不写库，录入前核对用

切分必须走 chunking.split_corpus；入库后写 bm25_corpus.jsonl，供 rag_qa 启动加载。
  python scripts/build_vectorstore.py --export-corpus  # 只从现有向量库导出旁路语料，不重建
"""

import os
import sys
from collections import Counter

import chromadb
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from chunking import split_corpus
from config import (
    BM25_CORPUS_PATH, CHROMA_DIR, CHUNK_OVERLAP, CHUNK_SIZE, EMBEDDING_MODEL,
    HF_OFFLINE, K, RAW_DIR,
)
from corpus_index import rows_from_chroma, rows_from_lists, save_rows
from load_documents import load_documents

if HF_OFFLINE:
    os.environ["HF_HUB_OFFLINE"] = "1"


def main():
    incremental = "--incremental" in sys.argv
    dry_run = "--dry-run" in sys.argv
    export_only = "--export-corpus" in sys.argv

    if export_only:
        client = chromadb.PersistentClient(path=str(CHROMA_DIR))
        col = client.get_or_create_collection("langchain")
        dumped = rows_from_chroma(col)
        save_rows(BM25_CORPUS_PATH, dumped)
        print(f"[BM25] 从向量库导出 {len(dumped)} 行 -> {BM25_CORPUS_PATH}")
        return

    docs = load_documents(RAW_DIR)
    texts, metadatas, ids, strategies = split_corpus(
        docs, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP,
    )
    print(f"共加载 {len(docs)} 篇文档，切分 {len(texts)} 个块")
    print("切分策略（按块计）:")
    for name, n in strategies.most_common():
        print(f"  [{name}] {n} 个块")
    for domain, n in Counter(m["domain"] for m in metadatas).most_common():
        print(f"  业务域 [{domain}] {n} 个块")

    if dry_run:
        print("[dry-run] 未写入向量库，请核对统计后再正式建库。")
        return

    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    if not incremental:
        for col in client.list_collections():
            client.delete_collection(col.name)
        print("[重建] 已清空旧集合")

    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    # Chroma 单批上限约 5461；新切分后块数更多，必须分批写
    batch = 128
    col = client.get_or_create_collection("langchain")
    for i in range(0, len(texts), batch):
        sl = slice(i, i + batch)
        col.upsert(
            ids=ids[sl],
            embeddings=embeddings.embed_documents(texts[sl]),
            documents=texts[sl],
            metadatas=metadatas[sl],
        )
        print(f"  已写入 {min(i + batch, len(texts))}/{len(texts)}")
    print(f"{'[增量] 已 upsert' if incremental else '已入库'} {len(texts)} 个文本块")

    # 旁路语料必须在入库后从集合重读一份，增量模式才能包含旧块
    col = client.get_or_create_collection("langchain")
    dumped = rows_from_chroma(col)
    if not dumped:
        dumped = rows_from_lists(texts, metadatas, ids)
    save_rows(BM25_CORPUS_PATH, dumped)
    print(f"[BM25] 已写入旁路语料 {len(dumped)} 行 -> {BM25_CORPUS_PATH.name}")

    db = Chroma(persist_directory=str(CHROMA_DIR), embedding_function=embeddings)
    for doc, score in db.similarity_search_with_score("什么是 RAG？", k=K):
        print(f"相似度 {score:.4f}: {doc.page_content[:60]}")


if __name__ == "__main__":
    main()
