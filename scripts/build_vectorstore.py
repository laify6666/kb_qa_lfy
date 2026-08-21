"""建库脚本：加载 -> 切分 -> 向量化 -> 入库。

用法（在项目根目录运行）：
  python scripts\build_vectorstore.py               # 全量重建（默认，安全）
  python scripts\build_vectorstore.py --incremental # 增量 upsert（按 id 去重，不删旧数据）
  python scripts\build_vectorstore.py --dry-run     # 只统计不写库，录入前核对用

设计：
- 全量重建：先清空集合再入库，避免重复/脏数据；
- 增量模式：用「相对路径#块序号」作为 id 做 upsert，同一文档重复执行不会翻倍；
- 元数据：每块记录 source / domain / path / chunk_index，便于按业务域过滤检索。
"""

import os
import sys
from collections import Counter

import chromadb
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from config import CHROMA_DIR, EMBEDDING_MODEL, HF_OFFLINE, K, RAW_DIR
from load_documents import load_documents

if HF_OFFLINE:
    os.environ["HF_HUB_OFFLINE"] = "1"


def main():
    incremental = "--incremental" in sys.argv
    dry_run = "--dry-run" in sys.argv

    docs = load_documents(RAW_DIR)
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    texts, metadatas, ids = [], [], []
    for name, text, meta in docs:
        chunks = splitter.split_text(text)
        for i, c in enumerate(chunks):
            texts.append(c)
            metadatas.append({**meta, "chunk_index": i})
            ids.append(f"{meta['path']}#{i}")
    print(f"共加载 {len(docs)} 篇文档，切分 {len(texts)} 个块")
    for domain, n in Counter(m["domain"] for m in metadatas).most_common():
        print(f"  [{domain}] {n} 个块")

    if dry_run:
        print("[dry-run] 未写入向量库，请核对统计后再正式建库。")
        return

    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    if not incremental:
        for col in client.list_collections():
            client.delete_collection(col.name)
        print("[重建] 已清空旧集合")

    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    if incremental:
        col = client.get_or_create_collection("langchain")
        for i in range(0, len(texts), 128):
            col.upsert(ids=ids[i:i + 128],
                       embeddings=embeddings.embed_documents(texts[i:i + 128]),
                       documents=texts[i:i + 128],
                       metadatas=metadatas[i:i + 128])
        print(f"[增量] 已 upsert {len(texts)} 个块")
    else:
        Chroma.from_texts(texts=texts, embedding=embeddings, metadatas=metadatas,
                          ids=ids, persist_directory=str(CHROMA_DIR))
        print(f"已入库 {len(texts)} 个文本块")

    db = Chroma(persist_directory=str(CHROMA_DIR), embedding_function=embeddings)
    for doc, score in db.similarity_search_with_score("什么是 RAG？", k=K):
        print(f"相似度 {score:.4f}: {doc.page_content[:60]}")


if __name__ == "__main__":
    main()