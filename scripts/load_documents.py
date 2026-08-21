"""文档加载器：递归扫描语料目录，支持多格式，返回带元数据的文档列表。

支持格式：.md / .markdown / .txt（内置）；.pdf / .docx（需安装 pypdf / python-docx）。
元数据：source（文件名）、domain（一级子目录名，未分类为"通用"）、path（相对路径）。

返回：[(文件名, 文本, 元数据字典), ...]
"""

from pathlib import Path

TEXT_EXTS = {".md", ".markdown", ".txt"}


def _read_text(file_path: Path) -> str:
    with open(file_path, encoding="utf-8") as f:
        return f.read()


def _read_pdf(file_path: Path) -> str:
    from pypdf import PdfReader
    reader = PdfReader(str(file_path))
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def _read_docx(file_path: Path) -> str:
    import docx
    document = docx.Document(str(file_path))
    return "\n".join(p.text for p in document.paragraphs)


_READERS = {".pdf": _read_pdf, ".docx": _read_docx}


def load_documents(folder: Path, recursive: bool = True):
    results = []
    it = folder.rglob("*") if recursive else folder.glob("*")
    for file_path in it:
        if not file_path.is_file():
            continue
        suffix = file_path.suffix.lower()
        if suffix in TEXT_EXTS:
            try:
                text = _read_text(file_path)
            except Exception as e:
                print(f"跳过 {file_path.name}: {e}")
                continue
        elif suffix in _READERS:
            try:
                text = _READERS[suffix](file_path)
            except Exception as e:
                print(f"跳过 {file_path.name}: {e}（可能需要 pip install pypdf / python-docx）")
                continue
        else:
            continue
        if not text.strip():
            print(f"跳过空文件 {file_path.name}")
            continue
        rel = file_path.relative_to(folder)
        domain = str(rel.parent) if str(rel.parent) != "." else "通用"
        results.append((file_path.name, text, {
            "source": file_path.name,
            "domain": domain,
            "path": str(rel).replace("\\", "/"),
        }))
    return results


if __name__ == "__main__":
    raw_dir = Path(__file__).parent.parent / "data" / "raw"
    docs = load_documents(raw_dir)
    total = sum(len(t) for _, t, _ in docs)
    print(f"共加载 {len(docs)} 篇文档，总字符数 {total}")
    from collections import Counter
    for domain, n in Counter(m["domain"] for _, _, m in docs).most_common():
        print(f"  [{domain}] {n} 篇")