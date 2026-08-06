"""第 3 步：加载 -> 切分 -> 向量化 -> 入库"""

import os

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from config import CHROMA_DIR, EMBEDDING_MODEL, HF_OFFLINE, K, RAW_DIR
from load_documents import load_documents

if HF_OFFLINE:
    os.environ["HF_HUB_OFFLINE"] = "1"


if __name__ == "__main__":
    docs = load_documents(RAW_DIR)

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = []
    for name, text in docs:
        chunks.extend(splitter.split_text(text))

    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    db = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        persist_directory=str(CHROMA_DIR),
    )
    print(f"已入库 {len(chunks)} 个文本块")

    # 入库自检：随便查一句，确认检索能用
    for doc, score in db.similarity_search_with_score("什么是 RAG？", k=K):
        print(f"相似度 {score:.4f}: {doc.page_content[:60]}")
