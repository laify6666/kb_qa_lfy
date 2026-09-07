"""长期记忆：按 user_id 存短偏好，落在独立 json。

只记「只要百科域」这类约束，不记世界知识，也不 upsert 进 Chroma / BM25。
空 user_id 视为关闭（评估 / 单轮脚本不要传）。抽取只看用户原话，不看助手回答。
"""

from __future__ import annotations

import json
import threading
from datetime import datetime
from pathlib import Path

from config import LTM_MAX_FACTS, LTM_PATH, RAW_DIR

_LOCK = threading.Lock()
_ALIASES = {
    "维基": "百科",
    "维基百科": "百科",
    "wiki": "百科",
}

# 没有这些字就不当偏好，避免「什么是百科」被写成域限制
_PREF_HINTS = (
    "只要", "只看", "只用", "仅用", "仅看", "只检索",
    "限定到", "限定在", "限定域", "以后都用", "记住我只要",
)
_FORGET_HINTS = (
    "取消只要", "取消域偏好", "不要只看", "不要限定",
    "恢复全库", "改回全库", "不要只要", "取消业务域",
)


def known_domains(raw_dir: Path | None = None) -> list[str]:
    """data/raw 一级子目录名，按长到短排，避免「百科」抢「百科问答」。"""
    root = raw_dir or RAW_DIR
    if not root.is_dir():
        return []
    names = [p.name for p in root.iterdir() if p.is_dir()]
    names.sort(key=len, reverse=True)
    return names


def _empty_store() -> dict:
    return {"users": {}}


def _read_store(path: Path) -> dict:
    if not path.is_file():
        return _empty_store()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return _empty_store()
    if not isinstance(data, dict) or "users" not in data:
        return _empty_store()
    return data


def _write_store(path: Path, data: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(path)


def load_facts(user_id: str | None, path: Path | None = None) -> list[dict]:
    """读取该用户已存偏好。空 id 返回空列表。"""
    if not user_id or not str(user_id).strip():
        return []
    uid = str(user_id).strip()
    store_path = path or LTM_PATH
    with _LOCK:
        users = _read_store(store_path).get("users") or {}
        rec = users.get(uid) or {}
        facts = rec.get("facts") or []
    return [f for f in facts if isinstance(f, dict) and f.get("key")]


def preferred_domain(facts: list[dict]) -> str | None:
    """槽位里的业务域名；没有则 None。"""
    for f in facts:
        if f.get("key") == "preferred_domain":
            val = (f.get("value") or "").strip()
            return val or None
    return None


def format_profile_block(facts: list[dict]) -> str:
    """生成 prompt 里与资料分栏的侧写。空则返回空串。"""
    lines = []
    for f in facts:
        text = (f.get("text") or "").strip()
        if text:
            lines.append(f"- {text}")
    if not lines:
        return ""
    return (
        "用户侧写（偏好与习惯，不是资料，禁止用来回答事实问题）：\n"
        + "\n".join(lines)
    )


def _looks_like_forget(question: str) -> bool:
    return any(h in question for h in _FORGET_HINTS)


def _looks_like_preference(question: str) -> bool:
    return any(h in question for h in _PREF_HINTS)


def _match_domain(question: str, domains: list[str]) -> str | None:
    """用户话里出现的业务域名，别名映射到真实目录名。"""
    q = question.strip()
    ql = q.lower()
    for alias, target in sorted(_ALIASES.items(), key=lambda x: len(x[0]), reverse=True):
        if alias.lower() in ql and target in domains:
            return target
    for name in domains:
        if name and name in q:
            return name
    return None


def is_preference_only(question: str, update: dict) -> bool:
    """这句话只是在设/取消偏好，没有在问知识库。

    「以后只要百科域，陈蝶衣是谁？」带问号，仍走检索。
    """
    if not update or not (update.get("forget_domain") or update.get("preferred_domain")):
        return False
    q = (question or "").strip()
    if not q:
        return False
    if "？" in q or "?" in q:
        return False
    if len(q) > 40:
        return False
    return True


def extract_preference_update(question: str, domains: list[str] | None = None) -> dict:
    """只从用户原话抽偏好更新，不抽世界知识。

    Args:
        question: 本轮用户原句。
        domains: 已知业务域；默认读 data/raw。

    Returns:
        forget_domain: 是否清掉域偏好。
        preferred_domain: 新的域限制；与 forget 互斥。
    """
    q = (question or "").strip()
    names = domains if domains is not None else known_domains()
    out = {"forget_domain": False, "preferred_domain": None}
    if not q:
        return out
    if _looks_like_forget(q):
        out["forget_domain"] = True
        return out
    if not _looks_like_preference(q):
        return out
    name = _match_domain(q, names)
    if name:
        out["preferred_domain"] = name
    return out


def resolve_domain(requested, user_id: str | None, question: str,
                   domains: list[str] | None = None, path: Path | None = None):
    """本轮检索域：请求显式域 > 本轮新偏好/取消 > 已存偏好。

    Returns:
        (domain_or_none, source)
        source: request | utterance | ltm | forget | none
    """
    if requested:
        return requested, "request"
    names = domains if domains is not None else known_domains()
    update = extract_preference_update(question, names)
    if update["forget_domain"]:
        return None, "forget"
    if update["preferred_domain"]:
        return update["preferred_domain"], "utterance"
    pref = preferred_domain(load_facts(user_id, path=path))
    if pref:
        return pref, "ltm"
    return None, "none"


def upsert_facts(user_id: str | None, update: dict, path: Path | None = None):
    """按 key 覆盖写入。forget_domain 会删掉 preferred_domain。无 user_id 则忽略。"""
    if not user_id or not str(user_id).strip():
        return
    if not update or (not update.get("forget_domain") and not update.get("preferred_domain")):
        return
    uid = str(user_id).strip()
    store_path = path or LTM_PATH
    now = datetime.now().isoformat(timespec="seconds")
    with _LOCK:
        data = _read_store(store_path)
        rec = data.setdefault("users", {}).setdefault(uid, {"facts": []})
        facts = [f for f in rec.get("facts") or [] if isinstance(f, dict)]
        if update.get("forget_domain"):
            facts = [f for f in facts if f.get("key") != "preferred_domain"]
        elif update.get("preferred_domain"):
            name = update["preferred_domain"]
            facts = [f for f in facts if f.get("key") != "preferred_domain"]
            facts.insert(0, {
                "key": "preferred_domain",
                "value": name,
                "text": f"用户只要「{name}」域",
                "ts": now,
            })
        rec["facts"] = facts[: max(LTM_MAX_FACTS, 1)]
        rec["updated_at"] = now
        data["users"][uid] = rec
        _write_store(store_path, data)


def remember_async(user_id: str | None, question: str, domains: list[str] | None = None,
                   path: Path | None = None):
    """生成返回后再写盘，不堵回答。抽取失败只打印。"""
    if not user_id or not str(user_id).strip():
        return
    names = list(domains) if domains is not None else known_domains()
    store_path = path or LTM_PATH

    def _run():
        try:
            update = extract_preference_update(question, names)
            upsert_facts(user_id, update, path=store_path)
        except Exception as e:
            print(f"[长期记忆] 写入失败: {e}")

    threading.Thread(target=_run, daemon=True).start()


def clear_user(user_id: str | None, path: Path | None = None):
    """演示页「清除偏好」用。不影响短期 session。"""
    if not user_id or not str(user_id).strip():
        return
    uid = str(user_id).strip()
    store_path = path or LTM_PATH
    with _LOCK:
        data = _read_store(store_path)
        users = data.get("users") or {}
        users.pop(uid, None)
        data["users"] = users
        _write_store(store_path, data)
