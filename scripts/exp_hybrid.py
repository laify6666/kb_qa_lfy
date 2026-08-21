"""实验：验证 BM25 混合检索（RRF 融合）能否把 Q5/Q11 的答案块捞回来。"""
import os, sys
sys.path.insert(0, 'scripts')
from pathlib import Path
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from rank_bm25 import BM25Okapi
from config import CHROMA_DIR, EMBEDDING_MODEL, HF_OFFLINE
from load_documents import load_documents

if HF_OFFLINE:
    os.environ["HF_HUB_OFFLINE"] = "1"

def tokens(text: str):
    """中文用字符 2-gram 分词（免 jieba 依赖）。"""
    t = text.lower()
    return [t[i:i+2] for i in range(max(len(t)-1, 0))]

def main():
    docs = load_documents(Path('data/raw'))
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    texts, srcs = [], []
    for _n, text, meta in docs:
        for c in splitter.split_text(text):
            texts.append(c)
            srcs.append(meta['source'])
    print(f"[块数] {len(texts)}")

    bm25 = BM25Okapi([tokens(t) for t in texts])
    emb = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    db = Chroma(persist_directory=str(CHROMA_DIR), embedding_function=emb)

    cases = [
        ("Q5", "什么是文本嵌入（Embedding）？语义相似的文本在向量空间中有什么关系？", ["数值向量", "向量空间"]),
        ("Q11", "CharacterTextSplitter 和 RecursiveCharacterTextSplitter 在切分策略上有什么区别？为什么后者通常更好？", ["CharacterTextSplitter", "RecursiveCharacterTextSplitter"]),
        ("Q15", "请介绍 OpenAI GPT-5 模型的参数规模和发布日期。", ["GPT-5"]),
        ("Q18", "什么是多模态 RAG？请给出具体实现方案。", ["多模态"]),
    ]
    for name, q, kws in cases:
        vec_docs = db.similarity_search(q, k=10)
        vec_texts = [d.page_content for d in vec_docs]
        bm_top = bm25.get_top_n(tokens(q), texts, n=10)

        # RRF 融合（按字符串值做 key）
        ranks = {}
        for i, t in enumerate(vec_texts):
            ranks[t] = ranks.get(t, 0) + 1 / (60 + i + 1)
        for i, t in enumerate(bm_top):
            ranks[t] = ranks.get(t, 0) + 1 / (60 + i + 1)
        fused = sorted(set(vec_texts + bm_top), key=lambda t: -ranks.get(t, 0))[:10]

        print(f"===== {name}: {q[:28]} =====")
        for kw in kws:
            n_corpus = sum(1 for t in texts if kw.lower() in t.lower())
            n_vec = sum(1 for t in vec_texts if kw.lower() in t.lower())
            n_bm = sum(1 for t in bm_top if kw.lower() in t.lower())
            n_fu = sum(1 for t in fused if kw.lower() in t.lower())
            print(f"  [{kw}] 语料含此词块数={n_corpus} | 向量top10={n_vec} | BM25top10={n_bm} | 融合top10={n_fu}")
        fused_srcs = []
        for t in fused[:5]:
            fused_srcs.append(srcs[texts.index(t)])
        print(f"  融合 top-5 来源: {fused_srcs}")
        print()

if __name__ == "__main__":
    main()