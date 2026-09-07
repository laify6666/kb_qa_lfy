"""多轮查询改写：把带指代的追问变成可独立检索的问题。

对齐 LangChain history_aware_retriever / Haystack rephrase：
空历史不改写；已是完整新问题也不改写，避免把旧实体灌进检索。
改写失败或输出不像查询时，调用方必须退回原问。
"""

from __future__ import annotations

from config import REWRITE_MAX_CHARS

# 这些字出现时，几乎一定依赖上文；短问（「全称呢」）即使没有这些字也要改写
_FOLLOWUP_MARKERS = (
    "它", "他", "她", "这", "那", "该", "此",
    "刚才", "上述", "前者", "后者", "上面", "之前",
    "还有呢", "然后呢", "呢？", "呢?",
)

REWRITE_SYSTEM = (
    "你把用户的追问改写成一条不依赖对话也能检索的独立问题。\n"
    "只补全指代和省略的实体，不要回答问题，不要扩展，不要引入对话里没有出现过的专名或事实。\n"
    "如果追问本身已经是完整问题，原样输出。\n"
    "只输出一行查询文本，不要引号，不要解释。"
)


def needs_rewrite(question: str, history: list[dict] | None) -> bool:
    """是否值得花一次 LLM 改写。

    Returns:
        False 表示直接用原问检索（第一轮、换题、或没有历史）。
    """
    if not history:
        return False
    q = (question or "").strip()
    if not q:
        return False
    if any(m in q for m in _FOLLOWUP_MARKERS):
        return True
    # 已经像完整问句、又没有指代，当成新问题，避免「换题仍改写成上一题」
    if len(q) >= 8:
        return False
    return True


def _clean_rewritten(text: str, original: str) -> str | None:
    """校验改写结果。不合格返回 None，由调用方降级为原问。"""
    if not text:
        return None
    line = text.strip().splitlines()[0].strip().strip("「」\"'")
    # 模型有时会写成「独立问题：xxx」
    for prefix in ("独立问题：", "独立问题:", "查询：", "查询:", "Standalone question:"):
        if line.lower().startswith(prefix.lower()):
            line = line[len(prefix):].strip()
    if not line or line == original.strip():
        return line or None
    if len(line) > REWRITE_MAX_CHARS:
        return None
    # 改写成了回答而不是查询
    if "资料中没有相关信息" in line or len(line) > max(len(original) * 4, 40) and "。" in line:
        return None
    return line


def build_rewrite_messages(question: str, history: list[dict], last_paths: list[str] | None = None):
    """构造改写用的 chat messages，不在这里调模型，便于单测。"""
    hist_lines = []
    for msg in history:
        label = "用户" if msg.get("role") == "user" else "助手"
        hist_lines.append(f"{label}: {msg.get('content', '')}")
    extra = ""
    if last_paths:
        extra = "\n上一轮检索过的文档（仅供消解指代，不要写成文件名查询）：" + "、".join(last_paths[:4])
    user = (
        f"对话历史：\n" + "\n".join(hist_lines) + extra
        + f"\n\n追问：{question}\n独立问题："
    )
    return [
        {"role": "system", "content": REWRITE_SYSTEM},
        {"role": "user", "content": user},
    ]


def rewrite_query(llm, question: str, history: list[dict] | None, last_paths: list[str] | None = None):
    """得到用于检索的独立问题。

    Args:
        llm: 带 invoke(messages).content 的聊天模型。
        question: 用户本轮原话。
        history: 已截断的短期历史；空则跳过。
        last_paths: 可选，上一轮命中路径。

    Returns:
        (standalone_query, source)
        source: skip_empty | skip_new | llm | fallback
    """
    q = (question or "").strip()
    if not needs_rewrite(q, history):
        why = "skip_empty" if not history else "skip_new"
        return q, why
    messages = build_rewrite_messages(q, history, last_paths=last_paths)
    try:
        raw = llm.invoke(messages).content
        cleaned = _clean_rewritten(raw, q)
        if cleaned:
            return cleaned, "llm"
    except Exception as e:
        print(f"[改写] 失败，改用原问检索: {e}")
    return q, "fallback"
