from pathlib import Path

def load_documents(folder):
    """读取文件夹下所有 .md 文件，返回 [(文件名, 文本), ...]"""
    results = []
    for file_path in folder.glob("*.md"):
        try:
            with open(file_path, encoding="utf-8") as f:
                text = f.read()
        except Exception as e:
            print(f"跳过 {file_path.name}: {e}")
            continue            # 这个文件失败了，直接去下一个
        results.append((file_path.name, text))   # 放 try 外面，bug 不会被藏起来
    return results

if __name__ == "__main__":
    raw_dir = Path(__file__).parent.parent / "data" / "raw"
    docs = load_documents(raw_dir)
    total = sum(len(text) for _, text in docs)
    print(f"共加载 {len(docs)} 篇文档，总字符数 {total}")