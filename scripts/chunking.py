"""结构感知切分：有结构按结构切，没有则降级。

建库（build_vectorstore）和 BM25（rag_qa._build_bm25）必须调用本模块的
split_document，禁止再各自 new 一套 RecursiveCharacterTextSplitter，
否则向量块和关键词块会对不齐。

降级链（按篇检测，不按文件扩展名）：
  1. Markdown 标题（# / ## / ###），跳过代码块里的 # 注释
  2. 维基小节（独占一行、短、以「.」或「。」结尾，如「词源.」）
  3. 空行 / 全角缩进「　　」段落（新闻、OCR）
  4. 仍是超长整段 → RecursiveCharacter 滑窗（与旧基线同参数）

每一块都会带上「[来源] 文件名 | 标题路径」前缀，避免检索到后段却丢了文章主题。
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from langchain.text_splitter import RecursiveCharacterTextSplitter

# 至少要切出这么多段，才认为「识别到了结构」；否则继续降级。
# 门槛=2：只有文件头一个 # 标题的文档（新闻/DRCD）不会误走标题路径。
MIN_SECTIONS = 2

# 维基 dump 的小节标题通常很短；过长会把「历史上曾有过许多不同的记数系统。」
# 这类短句误当成标题。24 字能盖住「形成、纯数学与应用数学及美学」。
_WIKI_HEADING = re.compile(r"^(.{1,24})[.。]$")
_MD_HEADING = re.compile(r"^(#{1,3})\s+(.+?)\s*$")
_SENTENCE_PUNCT = re.compile(r"[，,；;：:！？!?]")


@dataclass
class Chunk:
    """切分产物。text 已含来源前缀，可直接入库 / 建 BM25。"""

    text: str
    heading: str
    strategy: str  # md / wiki / para / window


def extract_title(text: str, source: str = "") -> str:
    """取文档标题：正文第一个 Markdown H1；没有则退回文件名。"""
    in_code = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = _MD_HEADING.match(stripped)
        if m and len(m.group(1)) == 1:
            return m.group(2).strip()
        if stripped:
            # 第一行非空又不是 H1，不再往下找，避免把后文的 H2 当标题
            break
    return Path(source).stem if source else ""


def _heading_path(stack: dict) -> str:
    """把 H1/H2/H3 栈拼成「一级 / 二级 / 三级」，空级跳过。"""
    return " / ".join(stack[lv] for lv in (1, 2, 3) if stack[lv])


def split_by_markdown_headings(text: str) -> list[tuple[str, str]]:
    """按 # / ## / ### 切成 (标题路径, 正文) 列表。

    代码围栏内的「# 注释」不当标题，否则 01_ 教程会在 Python 注释处被切碎。
    标题行本身不写入正文，检索前缀会带上标题。
    """
    lines = text.splitlines(keepends=True)
    in_code = False
    stack = {1: "", 2: "", 3: ""}
    sections: list[tuple[str, list[str]]] = []
    current: list[str] = []

    def flush():
        body = "".join(current).strip()
        heading = _heading_path(stack)
        if body:
            sections.append((heading, body))
        current.clear()

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            current.append(line)
            continue
        if not in_code:
            m = _MD_HEADING.match(stripped)
            if m:
                flush()
                level = len(m.group(1))
                name = m.group(2).strip()
                stack[level] = name
                for lv in range(level + 1, 4):
                    stack[lv] = ""
                continue
        current.append(line)
    flush()
    return [(h, b) for h, b in sections]


def _is_wiki_heading(line: str) -> bool:
    """判断是否为维基 dump 小节标题（「词源.」「历史.」）。

    排除带逗号/冒号的正常句子，以及 Markdown/表格/缩进行。
    """
    s = line.strip()
    if not s or s.startswith("#") or s.startswith("|") or s.startswith("　"):
        return False
    m = _WIKI_HEADING.match(s)
    if not m:
        return False
    title = m.group(1)
    if _SENTENCE_PUNCT.search(title):
        return False
    # 「一环。」「系统。」这种短句末字偏叙述，仍可能误伤；靠 MIN_SECTIONS 和
    # 「下一行足够长」在调用处再过滤意义不大，过切后滑窗也不会丢内容。
    return True


def split_by_wiki_headings(text: str, doc_title: str) -> list[tuple[str, str]]:
    """按「短行 + 句点」切维基正文。导言（第一个小节标题之前）归到文档标题下。"""
    lines = text.splitlines(keepends=True)
    sections: list[tuple[str, list[str]]] = []
    heading = doc_title or "导言"
    current: list[str] = []

    def flush():
        body = "".join(current).strip()
        if body:
            sections.append((heading, body))
        current.clear()

    in_code = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            current.append(line)
            continue
        if not in_code and _is_wiki_heading(stripped):
            flush()
            heading = stripped.rstrip("。.").strip()
            if doc_title and heading != doc_title:
                heading = f"{doc_title} / {heading}"
            continue
        current.append(line)
    flush()
    return sections


def split_by_paragraphs(text: str, doc_title: str) -> list[tuple[str, str]]:
    """按空行、再按 THUCNews 的全角缩进切段。

    新闻没有 ##，但「　　」是稳定的段落边界；切开后每段仍挂同一文档标题。
    """
    blocks = re.split(r"\n\s*\n+", text)
    parts: list[str] = []
    for block in blocks:
        # 前瞻「行首全角空格」，把同一块里的新闻段落再切开
        parts.extend(re.split(r"\n(?=　　)", block))
    sections = []
    for i, p in enumerate(parts, 1):
        body = p.strip()
        if not body:
            continue
        heading = doc_title or f"段{i}"
        sections.append((heading, body))
    return sections


def _is_shell_section(body: str) -> bool:
    """整段只剩一行 Markdown 标题、没有正文时丢掉。

    否则像 drcd_001 会被空行切成「# 广州」+ 长段，凑满 MIN_SECTIONS=2
    后误走段落路径，长段不再降级滑窗，机场/禁摩仍挤在一块里。
    """
    s = (body or "").strip()
    if not s:
        return True
    return bool(_MD_HEADING.fullmatch(s))


def _window_split(body: str, chunk_size: int, overlap: int) -> list[str]:
    """结构内仍然超长时，退回已验证过的递归字符切分。"""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap,
    )
    chunks = splitter.split_text(body)
    return chunks or ([body] if body.strip() else [])


def _prefix(source: str, heading: str, body: str) -> str:
    """检索前缀：让后段块也能被「这是哪篇文章」问到。"""
    src = source or ""
    head = heading or src
    return f"[来源] {src} | {head}\n{body}".strip()


def split_document(
    text: str,
    source: str = "",
    chunk_size: int = 500,
    overlap: int = 100,
) -> list[Chunk]:
    """对单篇文档走降级链，返回带前缀的块列表。

    Args:
        text: 原文（入库后的 Markdown）。
        source: 文件名，写入每块前缀和来源元数据。
        chunk_size: 滑窗大小；结构切出的短段不会被再切。
        overlap: 仅用于最后一级滑窗，结构边界本身不重叠。

    Returns:
        Chunk 列表；strategy 标明本篇实际走了哪一级，便于建库时统计。
    """
    text = (text or "").replace("\r\n", "\n")
    if not text.strip():
        return []

    doc_title = extract_title(text, source)

    md_secs = [s for s in split_by_markdown_headings(text) if not _is_shell_section(s[1])]
    # 去掉「只有文件头 H1、正文还是一整坨」的假结构：真正有用的是多个小节
    if len(md_secs) >= MIN_SECTIONS:
        sections, strategy = md_secs, "md"
    else:
        wiki_secs = [s for s in split_by_wiki_headings(text, doc_title)
                     if not _is_shell_section(s[1])]
        if len(wiki_secs) >= MIN_SECTIONS:
            sections, strategy = wiki_secs, "wiki"
        else:
            para_secs = [s for s in split_by_paragraphs(text, doc_title)
                         if not _is_shell_section(s[1])]
            if len(para_secs) >= MIN_SECTIONS:
                sections, strategy = para_secs, "para"
            else:
                sections, strategy = [(doc_title, text.strip())], "window"

    chunks: list[Chunk] = []
    for heading, body in sections:
        heading = heading or doc_title
        if len(body) <= chunk_size:
            chunks.append(Chunk(
                text=_prefix(source, heading, body),
                heading=heading,
                strategy=strategy,
            ))
            continue
        # 标题切出来的节仍可能很长（维基「历史」），必须二次滑窗
        for part in _window_split(body, chunk_size, overlap):
            chunks.append(Chunk(
                text=_prefix(source, heading, part),
                heading=heading,
                strategy=strategy if strategy != "window" else "window",
            ))
    return chunks


def split_corpus(docs, chunk_size: int = 500, overlap: int = 100):
    """批量切分 load_documents 的返回值。

    Args:
        docs: [(文件名, 文本, 元数据), ...]
        chunk_size / overlap: 同 split_document。

    Returns:
        (texts, metadatas, ids, strategy_counter)
        ids 仍用「相对路径#块序号」，与旧建库脚本兼容增量 upsert。
    """
    from collections import Counter

    texts, metadatas, ids = [], [], []
    strategies = Counter()
    for _name, text, meta in docs:
        source = meta.get("source", _name)
        parts = split_document(text, source=source, chunk_size=chunk_size, overlap=overlap)
        for i, c in enumerate(parts):
            texts.append(c.text)
            metadatas.append({**meta, "chunk_index": i, "heading": c.heading, "strategy": c.strategy})
            ids.append(f"{meta.get('path', source)}#{i}")
            strategies[c.strategy] += 1
    return texts, metadatas, ids, strategies


if __name__ == "__main__":
    # 抽查四类真实语料，确认降级链有没有走错
    from load_documents import load_documents
    from config import RAW_DIR, CHUNK_SIZE, CHUNK_OVERLAP

    samples = [
        "02_rag实战指南_langchain.md",
        "wiki_001.md",
        "thucnews_0021.md",
        "drcd_001.md",
        "langchain_002.md",
        "sample_img.md",
    ]
    docs = load_documents(RAW_DIR)
    by_name = {name: (text, meta) for name, text, meta in docs}
    for name in samples:
        if name not in by_name:
            print(f"— 找不到 {name}")
            continue
        text, meta = by_name[name]
        chunks = split_document(text, source=name, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP)
        print(f"{name}: {len(chunks)} 块  strategy={chunks[0].strategy if chunks else '-'}  "
              f"首块标题={chunks[0].heading[:40] if chunks else '-'}")
