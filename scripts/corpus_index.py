"""块级语料旁路索引：BM25 / 邻居查找的事实源，与 Chroma 同源。

向量库仍是检索索引；本 jsonl 避免每次 import rag_qa 都对 400+ 篇再切一遍。
建库脚本写入；问答启动时优先读这里，缺失再从 Chroma 导出，最后才回退切原文。
"""

from __future__ import annotations

import json
from pathlib import Path


def save_rows(path: Path, rows: list[dict]):
    """按行写入 jsonl。text 可能含换行，必须 dumps 一整行，不能手拼。"""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def load_rows(path: Path) -> list[dict]:
    """读取 jsonl。坏行跳过，避免半次写入把启动整死。"""
    path = Path(path)
    rows = []
    if not path.exists():
        return rows
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return rows


def rows_from_lists(texts, metadatas, ids=None) -> list[dict]:
    """建库当下的 texts/metadatas 转成旁路行，保证与刚写入的向量块一致。"""
    rows = []
    for i, (text, meta) in enumerate(zip(texts, metadatas)):
        m = meta or {}
        rows.append({
            "id": (ids[i] if ids else f"{m.get('path', '')}#{i}"),
            "text": text,
            "source": m.get("source", ""),
            "path": m.get("path", m.get("source", "")),
            "chunk_index": int(m.get("chunk_index", i)),
            "heading": m.get("heading", ""),
            "domain": m.get("domain", "通用"),
        })
    return rows


def rows_from_chroma(collection, batch: int = 500) -> list[dict]:
    """从已有 Chroma 集合导出。jsonl 丢失或旧库未写旁路时用。"""
    def _pack(got):
        docs = got.get("documents") or []
        metas = got.get("metadatas") or []
        ids = got.get("ids") or [""] * len(docs)
        return rows_from_lists(docs, metas, ids)

    try:
        n = collection.count()
    except Exception:
        n = 0
    if n <= 0:
        return _pack(collection.get(include=["documents", "metadatas"]))
    try:
        rows = []
        offset = 0
        while offset < n:
            got = collection.get(
                include=["documents", "metadatas"],
                limit=min(batch, n - offset),
                offset=offset,
            )
            chunk = _pack(got)
            if not chunk:
                break
            rows.extend(chunk)
            offset += len(chunk)
        return rows
    except TypeError:
        # 旧版 Chroma 没有 offset 参数，一次取出
        return _pack(collection.get(include=["documents", "metadatas"]))


def index_rows(rows: list[dict]):
    """把 jsonl 行建成 BM25 / 邻居查找需要的结构。

    Returns:
        items: [(text, source, path, chunk_index, domain), ...]
        by_path: path -> {chunk_index: (text, source)}
        text_loc: text -> (path, chunk_index)
    """
    from collections import defaultdict

    items = []
    by_path = defaultdict(dict)
    text_loc = {}
    for row in rows:
        text = row.get("text") or ""
        source = row.get("source") or ""
        path = row.get("path") or source
        idx = int(row.get("chunk_index") or 0)
        domain = row.get("domain") or "通用"
        items.append((text, source, path, idx, domain))
        by_path[path][idx] = (text, source)
        text_loc[text] = (path, idx)
    return items, by_path, text_loc
