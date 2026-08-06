"""第 4 步：单题问答演示（检索 + 生成）"""

import os

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI

from config import (
    API_KEY,
    BASE_URL,
    CHROMA_DIR,
    EMBEDDING_MODEL,
    HF_OFFLINE,
    K,
    LLM_MODEL,
    TEMPERATURE,
)

if HF_OFFLINE:
    os.environ["HF_HUB_OFFLINE"] = "1"

embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
db = Chroma(persist_directory=str(CHROMA_DIR), embedding_function=embeddings)

llm = ChatOpenAI(
    model=LLM_MODEL,
    openai_api_key=API_KEY,
    base_url=BASE_URL,
    temperature=TEMPERATURE,
)


def ask_rag(question: str) -> str:
    """检索 + 生成，返回回答文本"""
    results = db.similarity_search_with_score(question, k=K)
    context = "\n\n".join(doc.page_content for doc, _ in results)
    messages = [
        {"role": "system", "content": "你是一个严谨的知识库问答助手，只依据参考资料回答，不编造。"},
        {"role": "user", "content": f"""请只根据下面的参考资料回答问题。如果资料中没有答案，请直接回答"资料中没有相关信息"。

参考资料：
{context}

问题：{question}
"""},
    ]
    return llm.invoke(messages).content


if __name__ == "__main__":
    question = "什么是 RAG？"
    print(ask_rag(question))
