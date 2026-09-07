"""抽取式上下文压缩：按当前查询留下相关句子，原文照抄。

接在 retrieve_hybrid 之后、拼生成 prompt 之前。不调 LLM，避免 8 块各调一次更贵。
编号仍对应未压缩的 hits，Web 来源预览用原块。
"""

from __future__ import annotations

import re

from config import CONTEXT_MAX_CHARS, K

_SENT_SPLIT = re.compile(r"(?<=[。！？；\n])")


def _grams(text: str) -> set[str]:
    t = (text or "").lower()
    if len(t) < 2:
        return {t} if t else set()
    return {t[i:i + 2] for i in range(len(t) - 1)}


def _split_sents(text: str) -> list[str]:
    parts = _SENT_SPLIT.split(text or "")
    return [p for p in parts if p.strip()]


def _score(sent: str, qgrams: set[str]) -> float:
    if not qgrams:
        return 0.0
    sg = _grams(sent)
    if not sg:
        return 0.0
    return len(sg & qgrams) / len(qgrams)


def compress_hits(hits, query: str, max_chars: int = CONTEXT_MAX_CHARS):
    """按查询抽取句子，直到接近 max_chars。

    精排靠前的块至少留一句，避免 [1] 被压空。未超预算则原样返回。

    Args:
        hits: [(块文本, 来源), ...]，顺序与引用编号一致。
        query: 检索用的独立问题（改写句），不要用「它」。
        max_chars: 资料正文总字符上限。

    Returns:
        (packed_hits, stats)
        packed_hits 与 hits 等长同序；stats 含 raw_chars / kept_chars / compressed。
    """
    raw = sum(len(t or "") for t, _ in hits)
    stats = {"raw_chars": raw, "kept_chars": raw, "compressed": False}
    if not hits or raw <= max_chars:
        return list(hits), stats

    qgrams = _grams(query)
    split_chunks = [_split_sents(t) or [t] for t, _ in hits]
    selected = [set() for _ in hits]
    used = 0

    def try_add(ci: int, j: int) -> bool:
        nonlocal used
        if j in selected[ci]:
            return True
        sent = split_chunks[ci][j]
        # 该块还没有任何句子时，允许略超，保证引用编号不空
        if used + len(sent) > max_chars and selected[ci]:
            return False
        if used + len(sent) > max_chars and selected[ci] == set():
            sent_keep = sent[: max(40, max_chars - used)]
            split_chunks[ci][j] = sent_keep
            selected[ci].add(j)
            used += len(sent_keep)
            return True
        if used >= max_chars:
            return False
        selected[ci].add(j)
        used += len(sent)
        return True

    # 先保住精排前 K 块各一句（优先高分，并列取原文更靠前的）
    for ci in range(min(len(hits), K)):
        sents = split_chunks[ci]
        ranked = sorted(range(len(sents)), key=lambda j: (-_score(sents[j], qgrams), j))
        if ranked:
            try_add(ci, ranked[0])

    rest = []
    for ci, sents in enumerate(split_chunks):
        for j, sent in enumerate(sents):
            rest.append((_score(sent, qgrams), -ci, j, ci))
    rest.sort(reverse=True)
    for _sc, _pri, j, ci in rest:
        if used >= max_chars:
            break
        try_add(ci, j)

    packed = []
    for ci, (_text, src) in enumerate(hits):
        sents = split_chunks[ci]
        if selected[ci]:
            kept = "".join(sents[j] for j in sorted(selected[ci]))
        else:
            kept = (_text or "")[:80]
        packed.append((kept, src))
    stats["kept_chars"] = sum(len(t) for t, _ in packed)
    stats["compressed"] = stats["kept_chars"] < raw
    return packed, stats
