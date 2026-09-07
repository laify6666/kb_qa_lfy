# data/raw 语料目录

按业务域分子目录（如 `技术文档/`、`百科/`、`百科问答/`、`资讯新闻/`、`测试资料/`）。只放来源明确的资料，入库前在 `data/source_manifest.md` 登记。

已入库文本是 `.md`。其它格式先走统一转换：

```powershell
python scripts\ingest_files.py --input <文件或文件夹> --domain 通用 [--build]
```

支持：Markdown/TXT 直拷；Office/HTML/CSV/JSON/EPUB/文本 PDF → MarkItDown；扫描 PDF / 图片 → RapidOCR。

建库（先 `cd scripts`，以便 `import config` / `chunking`）：

```powershell
python build_vectorstore.py --dry-run
python build_vectorstore.py
python build_vectorstore.py --incremental
```

切分由 `scripts/chunking.py` 完成，参数只读 `config.py` 的 `CHUNK_SIZE` / `CHUNK_OVERLAP`。向量目录 `data/chroma_db_zh/` 已 git 忽略，克隆后必须重建。
