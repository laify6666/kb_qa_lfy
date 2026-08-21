"""第 4 步：单题问答演示（混合检索[向量+BM25 RRF 融合] + 生成）"""

import os
from pathlib import Path

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from rank_bm25 import BM25Okapi

from config import (
    API_KEY, BASE_URL, CHROMA_DIR, EMBEDDING_MODEL, HF_OFFLINE,
    K, LLM_MODEL, TEMPERATURE,
)
from load_documents import load_documents

if HF_OFFLINE:
    os.environ["HF_HUB_OFFLINE"] = "1"

RAW_DIR = Path(__file__).parent.parent / "data" / "raw"

embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
db = Chroma(persist_directory=str(CHROMA_DIR), embedding_function=embeddings)

llm = ChatOpenAI(model=LLM_MODEL, openai_api_key=API_KEY,
                 base_url=BASE_URL, temperature=TEMPERATURE)

SYSTEM_PROMPT = (
    "你是一个严谨的知识库问答助手，只依据参考资料回答，不编造。\n"
    "如果资料中有相关内容，请务必根据最相关的资料尽力回答，并完整列出所有要点、分点作答；\n"
    "只有当你确信资料与问题完全无关、确实没有可依据的信息时，才回答“资料中没有相关信息”。"
)


def _zh_tokens(text: str):
    """中文用字符 2-gram 分词，适配 rank_bm25（免 jieba 依赖）。"""
    t = text.lower()
    return [t[i:i + 2] for i in range(max(len(t) - 1, 0))]


def _build_bm25():
    """用与 build_vectorstore 相同的切分参数重建块，保证与向量库块一致。"""
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    items = []
    for _name, text, meta in load_documents(RAW_DIR):
        for c in splitter.split_text(text):
            items.append((c, meta["source"]))
    return items, BM25Okapi([_zh_tokens(t) for t, _ in items])


_CORPUS_ITEMS, _BM25 = _build_bm25()


def retrieve_hybrid(question: str, k: int = K):
    """向量粗召回 2K + BM25 粗召回 2K -> RRF 融合取前 k，返回 [(文本, 来源), ...]。

    与生成共用同一套检索，保证诊断/评估口径一致。
    """
    vec_docs = db.similarity_search(question, k=K * 2)
    vec_items = [(d.page_content, d.metadata.get("source", "")) for d in vec_docs]

    scores = _BM25.get_scores(_zh_tokens(question))
    idx = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:K * 2]
    bm_items = [(_CORPUS_ITEMS[i][0], _CORPUS_ITEMS[i][1]) for i in idx]

    ranks = {}
    for i, (t, _s) in enumerate(vec_items):
        ranks[t] = ranks.get(t, 0) + 1 / (60 + i + 1)
    for i, (t, _s) in enumerate(bm_items):
        ranks[t] = ranks.get(t, 0) + 1 / (60 + i + 1)
    merged = {t: s for t, s in vec_items}
    for t, s in bm_items:
        merged.setdefault(t, s)
    fused = sorted(merged, key=lambda t: -ranks.get(t, 0))[:k]
    return [(t, merged[t]) for t in fused]


def ask_rag(question: str) -> str:
    """混合检索 + 生成"""
    context = "\n\n".join(t for t, _ in retrieve_hybrid(question, k=K))
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"请只根据下面的参考资料回答问题。\n\n参考资料：\n{context}\n\n问题：{question}\n"},
    ]
    return llm.invoke(messages).content


if __name__ == "__main__":
    question = "什么是 RAG？"
    print(ask_rag(question))