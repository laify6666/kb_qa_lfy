from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from load_documents import load_documents      # 直接复用第 1 步的函数
from pathlib import Path

def split_with(splitter, docs):
    """用给定切分器切所有文档，返回所有 chunk"""
    chunks = []
    for name, text in docs:
        chunks.extend(splitter.split_text(text))   # extend 是把列表展开追加
    return chunks

if __name__ == "__main__":
    raw_dir = Path(__file__).parent.parent / "data" / "raw"
    docs = load_documents(raw_dir)

    char_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)   # ① 填哪个类？
    rec_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)    # ② 填哪个类？

    char_chunks = split_with(char_splitter, docs)
    rec_chunks = split_with(rec_splitter, docs)

    print(f"CharacterTextSplitter: {len(char_chunks)} 块")
    print(f"RecursiveCharacterTextSplitter: {len(rec_chunks)} 块")

    for i in [29, 30, 31]:
        print(f"\n=== 第 {i} 块 ===")
        print(f"Character: {char_chunks[i][:50]}")
        print(f"Recursive: {rec_chunks[i][:50]}")