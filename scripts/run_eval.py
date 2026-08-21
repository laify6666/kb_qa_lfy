"""第 6 步：跑完整测试集，输出每题的问答报告（复用 rag_qa.ask_rag 的混合检索+生成）"""

import os
from pathlib import Path

from config import ANSWERS_PATH, QUESTIONS_PATH
from rag_qa import ask_rag


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