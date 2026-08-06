"""第 6 步：跑完整测试集，输出每题的问答报告"""

import os
from pathlib import Path

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI

from config import (
    ANSWERS_PATH,
    API_KEY,
    BASE_URL,
    CHROMA_DIR,
    EMBEDDING_MODEL,
    HF_OFFLINE,
    K,
    LLM_MODEL,
    QUESTIONS_PATH,
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


def load_questions(path: Path) -> list:
    """从 questions.md 里提取所有问题"""
    questions = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if "Q: " in line:
            questions.append(line.split("Q: ", 1)[1].strip())
    return questions


if __name__ == "__main__":
    questions = load_questions(QUESTIONS_PATH)
    print(f"共 {len(questions)} 题，开始逐题运行…")

    report_lines = []
    for i, q in enumerate(questions, start=1):
        try:
            answer = ask_rag(q)
            print(f"[{i}/{len(questions)}] {q[:20]}… -> {answer[:30]}…")
        except Exception as e:
            answer = f"❌ 执行出错：{e}"
            print(f"[{i}/{len(questions)}] 出错：{e}")
        report_lines.append(f"## 第 {i} 题\n\nQ: {q}\n\nA: {answer}\n")

    ANSWERS_PATH.write_text("\n".join(report_lines), encoding="utf-8")
    print(f"\n完成！答案已保存到 {ANSWERS_PATH}")
