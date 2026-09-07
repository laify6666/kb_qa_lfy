"""短期会话记忆：按 session_id 保存最近若干轮原文与槽位。

只服务本进程、本会话的指代消解；重启即丢。长期偏好、跨用户档案不放这里。
检索块原文不要写进 messages，否则下一轮会把旧资料再拼进 prompt。
"""

from __future__ import annotations

import threading
from dataclasses import dataclass, field

from config import HISTORY_ANSWER_CHARS, HISTORY_TURNS


@dataclass
class SessionState:
    """一个浏览器会话的短期状态。

    messages: [{role: user|assistant, content: str}, ...]，成对追加。
    last_paths: 上一轮命中块的 path，给改写 prompt 当消解线索。
    last_anchors: [(path, chunk_index), ...]，追问时注入同文档邻块再重排。
    last_entities: 上一轮话题实体，改写步骤再填。
    """

    messages: list[dict] = field(default_factory=list)
    last_paths: list[str] = field(default_factory=list)
    last_anchors: list[tuple] = field(default_factory=list)
    last_entities: list[str] = field(default_factory=list)


_LOCK = threading.Lock()
_SESSIONS: dict[str, SessionState] = {}


def _trim_messages(messages: list[dict]) -> list[dict]:
    """只保留最近 HISTORY_TURNS 轮（每轮 user+assistant 两条）。"""
    cap = max(HISTORY_TURNS, 0) * 2
    if cap <= 0 or len(messages) <= cap:
        return messages
    return messages[-cap:]


def get_session(session_id: str | None) -> SessionState | None:
    """读取会话。空 id 视为单轮，不建档。"""
    if not session_id or not str(session_id).strip():
        return None
    sid = str(session_id).strip()
    with _LOCK:
        state = _SESSIONS.get(sid)
        if state is None:
            return SessionState()
        return SessionState(
            messages=list(state.messages),
            last_paths=list(state.last_paths),
            last_anchors=list(state.last_anchors),
            last_entities=list(state.last_entities),
        )


def history_for_prompt(state: SessionState | None) -> list[dict]:
    """生成用的历史：用户原句保留，助手旧答截断，避免挤掉本轮检索块。"""
    if not state:
        return []
    out = []
    for msg in state.messages:
        role = msg.get("role") or ""
        content = (msg.get("content") or "").strip()
        if not content:
            continue
        if role == "assistant" and len(content) > HISTORY_ANSWER_CHARS:
            content = content[:HISTORY_ANSWER_CHARS] + "…"
        out.append({"role": role, "content": content})
    return out


def format_history_block(history: list[dict]) -> str:
    """拼进 user prompt 的可读历史。空则返回空串，调用方不要包一层空标题。"""
    if not history:
        return ""
    lines = ["对话历史（仅用于理解指代，不得作为答案依据）："]
    for msg in history:
        label = "用户" if msg.get("role") == "user" else "助手"
        lines.append(f"{label}: {msg.get('content', '')}")
    return "\n".join(lines)


def commit_turn(session_id: str | None, question: str, answer: str,
                paths: list[str] | None = None, anchors: list[tuple] | None = None):
    """本轮结束后追加 Q/A，并刷新 last_paths / last_anchors。无 session_id 则什么都不做。"""
    if not session_id or not str(session_id).strip():
        return
    sid = str(session_id).strip()
    with _LOCK:
        state = _SESSIONS.setdefault(sid, SessionState())
        state.messages.append({"role": "user", "content": question})
        state.messages.append({"role": "assistant", "content": answer or ""})
        state.messages = _trim_messages(state.messages)
        if paths is not None:
            # 去空去重、保序，槽位保持很短
            seen = set()
            cleaned = []
            for p in paths:
                p = (p or "").strip()
                if p and p not in seen:
                    seen.add(p)
                    cleaned.append(p)
            state.last_paths = cleaned[:8]
        if anchors is not None:
            state.last_anchors = [(p, int(i)) for p, i in anchors if p][:8]


def clear_session(session_id: str | None):
    """演示页「新会话」用。id 无效则忽略。"""
    if not session_id or not str(session_id).strip():
        return
    with _LOCK:
        _SESSIONS.pop(str(session_id).strip(), None)
