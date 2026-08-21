# data/raw 语料目录说明

- 按业务域分子目录存放（例如 `产品手册/`、`客服FAQ/`、`内部制度/`、`技术文档/`、`通用/`）。
- 只放**来源明确**的资料；每篇入库前在 `data/source_manifest.md` 登记来源。
- 支持格式：.md / .markdown / .txt；如需 .pdf / .docx，先 `pip install pypdf python-docx`。
- 建库命令（项目根目录）：
  - `python scripts\build_vectorstore.py --dry-run`      # 录入前核对
  - `python scripts\build_vectorstore.py`                # 全量重建
  - `python scripts\build_vectorstore.py --incremental`  # 增量 upsert