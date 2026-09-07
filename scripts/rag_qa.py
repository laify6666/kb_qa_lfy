"""混合检索问答：向量+BM25 RRF → 可选改写 → 重排 → 邻居 → 抽取压缩 → 生成。

诊断 / 评估 / Web 必须走 retrieve_hybrid，禁止再单独 similarity_search 当「来源」。
BM25 语料优先读 bm25_corpus.jsonl。有 session 时先改写追问再检索；生成仍用原话 + 短历史。
有 user_id 时读长期偏好（域限制），写入独立 json，不进向量库。
"""

import json
import os
import time
from datetime import datetime

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from rank_bm25 import BM25Okapi

from chunking import split_document
from config import (
    API_KEY, BASE_URL, BM25_CORPUS_PATH, CHROMA_DIR, CHUNK_OVERLAP, CHUNK_SIZE,
    CONTEXT_MAX_CHARS, CONTEXT_MAX_CHUNKS, EMBEDDING_MODEL, HF_OFFLINE, K, LLM_MODEL,
    NEIGHBOR_RADIUS, QA_LOG_PATH, RAW_DIR, RERANK_CANDIDATES, RERANK_MODEL, TEMPERATURE,
)
from context_compress import compress_hits
from corpus_index import (
    index_rows, load_rows, rows_from_chroma, rows_from_lists, save_rows,
)
from load_documents import load_documents
from long_term_memory import (
    extract_preference_update, format_profile_block, is_preference_only,
    known_domains, load_facts, resolve_domain, upsert_facts,
)
from query_rewrite import rewrite_query
from session_memory import (
    commit_turn, format_history_block, get_session, history_for_prompt,
)

if HF_OFFLINE:
    os.environ["HF_HUB_OFFLINE"] = "1"

embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
db = Chroma(persist_directory=str(CHROMA_DIR), embedding_function=embeddings)

llm = ChatOpenAI(model=LLM_MODEL, openai_api_key=API_KEY,
                 base_url=BASE_URL, temperature=TEMPERATURE)

SYSTEM_PROMPT = (
    "你是一个严谨的知识库问答助手，只依据本轮参考资料回答，不编造。\n"
    "如果资料中有相关内容，请务必根据最相关的资料尽力回答，并完整列出所有要点、分点作答；\n"
    "关键结论后用 [1][2] 标注对应参考资料编号；没有依据不要编造编号。\n"
    "对话历史只用于理解「它/这个/刚才」等指代，不能把历史里助手的旧回答当作事实依据。\n"
    "用户侧写只表示偏好（例如只要某业务域），不能当作资料来回答事实问题。\n"
    "只有当你确信本轮资料与问题完全无关、确实没有可依据的信息时，才回答“资料中没有相关信息”。"
)

_reranker = None
_reranker_failed = False


def _zh_tokens(text: str):
    """中文用字符 2-gram 分词，适配 rank_bm25（免 jieba 依赖）。"""
    t = text.lower()
    return [t[i:i + 2] for i in range(max(len(t) - 1, 0))]


def _rows_from_raw():
    """旁路和向量库都没有时的最后退路：现场切原文（慢，只应发生一次）。"""
    texts, metas, ids = [], [], []
    for _name, text, meta in load_documents(RAW_DIR):
        chunks = split_document(text, source=meta["source"],
                                chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP)
        for i, c in enumerate(chunks):
            texts.append(c.text)
            metas.append({**meta, "chunk_index": i, "heading": c.heading})
            ids.append(f"{meta.get('path', meta['source'])}#{i}")
    return rows_from_lists(texts, metas, ids)


def _load_corpus():
    """启动加载顺序：jsonl → Chroma 导出 → 切原文。命中后回写 jsonl，下次可秒开。"""
    rows = load_rows(BM25_CORPUS_PATH)
    src = "jsonl"
    if not rows:
        try:
            rows = rows_from_chroma(db._collection)
            src = "chroma"
        except Exception as e:
            print(f"[BM25] 从向量库导出失败: {e}")
            rows = []
    if not rows:
        print("[BM25] 旁路与向量库皆空，回退为现场切分（较慢）")
        rows = _rows_from_raw()
        src = "raw"
    if src != "jsonl" and rows:
        save_rows(BM25_CORPUS_PATH, rows)
        print(f"[BM25] 已缓存 {len(rows)} 行 -> {BM25_CORPUS_PATH.name}")
    else:
        print(f"[BM25] 从 {BM25_CORPUS_PATH.name} 加载 {len(rows)} 块")
    items, by_path, text_loc = index_rows(rows)
    return items, BM25Okapi([_zh_tokens(t) for t, *_ in items]), by_path, text_loc


_CORPUS_ITEMS, _BM25, _BY_PATH, _TEXT_LOC = _load_corpus()


def _normalize_domains(domain):
    """None / 字符串 / 列表 → None 或去空后的域名列表。None 表示不按业务域过滤。"""
    if domain is None or domain == "":
        return None
    if isinstance(domain, str):
        parts = [x.strip() for x in domain.split(",") if x.strip()]
        return parts or None
    parts = [str(x).strip() for x in domain if str(x).strip()]
    return parts or None


def _chroma_where(domains):
    """Chroma where 条件。单值用等值，多值用 $in。"""
    if not domains:
        return None
    if len(domains) == 1:
        return {"domain": domains[0]}
    return {"domain": {"$in": domains}}


def _get_reranker():
    """加载 bge-reranker-base。加载失败返回 None，由调用方降级，不让问答挂掉。"""
    global _reranker, _reranker_failed
    if _reranker_failed:
        return None
    if _reranker is None:
        try:
            from sentence_transformers import CrossEncoder
            _reranker = CrossEncoder(RERANK_MODEL)
        except Exception as e:
            print(f"[重排] 模型加载失败，降级为 RRF 顺序: {e}")
            _reranker_failed = True
            return None
    return _reranker


def _rrf_fuse(vec_items, bm_items, pool: int):
    """RRF 融合两路排序。k=60 是标准阻尼，避免某一路分数尺度把另一路淹没。"""
    ranks = {}
    merged = {}
    for i, (t, s) in enumerate(vec_items):
        ranks[t] = ranks.get(t, 0) + 1 / (60 + i + 1)
        merged[t] = s
    for i, (t, s) in enumerate(bm_items):
        ranks[t] = ranks.get(t, 0) + 1 / (60 + i + 1)
        merged.setdefault(t, s)
    fused = sorted(merged, key=lambda t: -ranks.get(t, 0))[:pool]
    return [(t, merged[t]) for t in fused]


def _rerank_hits(question: str, cands, k: int):
    """Cross-Encoder 精排。失败或空候选时原样截断，保证主路径可降级。"""
    if not cands:
        return []
    model = _get_reranker()
    if model is None:
        return cands[:k]
    try:
        pairs = [[question, t] for t, _ in cands]
        scores = model.predict(pairs)
        ranked = sorted(zip(cands, scores), key=lambda x: -float(x[1]))
        return [c for c, _ in ranked[:k]]
    except Exception as e:
        print(f"[重排] 推理失败，降级为 RRF 顺序: {e}")
        return cands[:k]


def _expand_neighbors(hits, radius: int = NEIGHBOR_RADIUS, max_total: int = CONTEXT_MAX_CHUNKS):
    """同文档 chunk_index±radius 补进上下文，但排在精排结果后面。"""
    if radius <= 0 or max_total <= len(hits):
        return hits
    seen = {t for t, _ in hits}
    extra = []
    for t, _s in hits:
        loc = _TEXT_LOC.get(t)
        if not loc:
            continue
        path, idx = loc
        bucket = _BY_PATH.get(path, {})
        for j in range(idx - radius, idx + radius + 1):
            if j == idx:
                continue
            item = bucket.get(j)
            if not item or item[0] in seen:
                continue
            seen.add(item[0])
            extra.append(item)
            if len(hits) + len(extra) >= max_total:
                return hits + extra
    return hits + extra


def _bm25_topk(question: str, pool: int, domains=None):
    """BM25 取 top-pool；若指定业务域，未命中域的块直接沉底。"""
    scores = list(_BM25.get_scores(_zh_tokens(question)))
    if domains:
        allowed = set(domains)
        for i, item in enumerate(_CORPUS_ITEMS):
            if item[4] not in allowed:
                scores[i] = -1e18
    idx = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:pool]
    if domains:
        idx = [i for i in idx if _CORPUS_ITEMS[i][4] in set(domains)][:pool]
    return [(_CORPUS_ITEMS[i][0], _CORPUS_ITEMS[i][1]) for i in idx]


def _merge_anchor_chunks(fused, anchors, radius: int = 1):
    """把上一轮命中块及其左右邻块补进候选。追加在末尾，由重排决定最终名次。

    只在追问时调用。换题不加，以免旧文档压过新问题。
    """
    if not anchors:
        return fused
    seen = {t for t, _ in fused}
    extra = []
    for path, idx in anchors:
        bucket = _BY_PATH.get(path) or {}
        try:
            idx = int(idx)
        except (TypeError, ValueError):
            continue
        for j in range(idx - radius, idx + radius + 1):
            item = bucket.get(j)
            if not item or item[0] in seen:
                continue
            seen.add(item[0])
            extra.append(item)
    return fused + extra


def retrieve_hybrid(question: str, k: int = K, rerank: bool = True, expand: bool = True,
                    domain=None, session_anchors=None):
    """向量 + BM25 → RRF →（会话锚点注入）→（重排）→（邻居补全）。

    Args:
        question: 用户问题。
        k: 精排后保留的块数；诊断看 top-10 时传入 10。
        rerank: False 时只返回 RRF 顺序（给 exp_rerank 做对照实验）。
        expand: False 时不补邻居。
        domain: 可选业务域（如「百科」或「百科,百科问答」）。默认不过滤，避免评估回退。
        session_anchors: 追问时传入上一轮 [(path, chunk_index)]；评估不要传。

    Returns:
        [(块文本, 来源文件名), ...]；expand 打开时长度可能大于 k，但前 k 条仍是精排结果。
    """
    domains = _normalize_domains(domain)
    pool = max(k, RERANK_CANDIDATES)
    where = _chroma_where(domains)
    search_kw = {"k": pool}
    if where:
        search_kw["filter"] = where
    vec_docs = db.similarity_search(question, **search_kw)
    vec_items = [(d.page_content, d.metadata.get("source", "")) for d in vec_docs]
    bm_items = _bm25_topk(question, pool, domains)

    fused = _rrf_fuse(vec_items, bm_items, pool)
    fused = _merge_anchor_chunks(fused, session_anchors)
    primary = _rerank_hits(question, fused, k) if rerank else fused[:k]
    if expand:
        cap = CONTEXT_MAX_CHUNKS if k <= K else k + 3
        return _expand_neighbors(primary, radius=NEIGHBOR_RADIUS, max_total=cap)
    return primary


def _append_qa_log(record: dict):
    """追加一行问答日志。失败只打印，不影响回答。"""
    try:
        QA_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(QA_LOG_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
    except Exception as e:
        print(f"[日志] 写入失败: {e}")


def ask_rag_with_hits(question: str, domain=None, session_id=None, user_id=None):
    """检索+生成，同时返回实际送入模型的块（Web 引用必须用这份）。

    session_id / user_id 为空时与原来单轮行为一致，diagnose / run_eval 不要传。
    有历史时用改写句检索，生成仍看用户原问；改写失败则原问检索。
    资料超 CONTEXT_MAX_CHARS 时按改写句抽句子，hits 仍是未压缩原块（引用/来源用）。
    请求未带 domain 时，可用长期偏好限定业务域；侧写与资料分栏，不得当证据。
    """
    t0 = time.perf_counter()
    state = get_session(session_id)
    hist = history_for_prompt(state)
    last_paths = state.last_paths if state else []
    last_anchors = state.last_anchors if state else []
    ltm_facts = load_facts(user_id)
    domains = known_domains()
    pref_update = extract_preference_update(question, domains)
    used_domain, domain_src = resolve_domain(
        domain, user_id, question, domains=domains,
    )
    if is_preference_only(question, pref_update):
        upsert_facts(user_id, pref_update)
        if pref_update.get("forget_domain"):
            answer = "已取消业务域偏好，下次按全库检索。"
        else:
            answer = (
                f"已记住：只要「{pref_update['preferred_domain']}」域。"
                "点「新会话」后仍有效；这条偏好不会写入知识库。"
            )
        latency_ms = (time.perf_counter() - t0) * 1000
        commit_turn(session_id, question, answer, paths=[], anchors=[])
        _append_qa_log({
            "ts": datetime.now().isoformat(timespec="seconds"),
            "question": question,
            "standalone_query": question,
            "rewrite_source": "skip_pref",
            "domain": used_domain or "",
            "domain_source": domain_src,
            "user_id": user_id or "",
            "session_id": session_id or "",
            "n_history": len(hist),
            "n_ltm_facts": len(ltm_facts),
            "used_anchors": False,
            "latency_ms": round(latency_ms, 1),
            "n_hits": 0,
            "context_raw_chars": 0,
            "context_kept_chars": 0,
            "context_compressed": False,
            "chunks": [],
            "answer_chars": len(answer),
        })
        return answer, [], question, {
            "used_domain": used_domain or "",
            "domain_source": domain_src,
        }
    standalone, rewrite_src = rewrite_query(llm, question, hist, last_paths=last_paths)
    # 仅追问注入上一轮文档；换题（skip_new）不加，以免答非所问
    inject_anchors = last_anchors if rewrite_src in ("llm", "fallback") else None
    hits = retrieve_hybrid(
        standalone, k=K, rerank=True, expand=True, domain=used_domain,
        session_anchors=inject_anchors,
    )
    packed, cstats = compress_hits(hits, standalone, CONTEXT_MAX_CHARS)
    context = "\n\n".join(
        f"[{i}] ({src})\n{text}" for i, (text, src) in enumerate(packed, 1)
    )
    hist_block = format_history_block(hist)
    profile_block = format_profile_block(ltm_facts)
    # 本轮刚说的偏好还没落盘，侧写要带上，否则要等下一轮才看见
    if domain_src == "utterance" and used_domain:
        extra = f"- 用户只要「{used_domain}」域"
        profile_block = (
            profile_block + "\n" + extra
            if profile_block else
            "用户侧写（偏好与习惯，不是资料，禁止用来回答事实问题）：\n" + extra
        )
    elif domain_src == "forget":
        profile_block = ""
    user_parts = ["请只根据下面的参考资料回答问题。"]
    if profile_block:
        user_parts.append(profile_block)
    if hist_block:
        user_parts.append(hist_block)
    user_parts.append(f"参考资料：\n{context}")
    user_parts.append(f"问题：{question}")
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "\n\n".join(user_parts) + "\n"},
    ]
    try:
        answer = llm.invoke(messages).content
    except Exception as e:
        # DeepSeek 偶发把维基人物等判成 Content Exists Risk，不能让整页 500
        if "Content Exists Risk" in str(e):
            print(f"[生成] 接口拒答: {e}")
            answer = "本轮内容未能生成。请换一个问法，或换一篇资料里的题目。"
        else:
            raise
    latency_ms = (time.perf_counter() - t0) * 1000
    chunk_ids = []
    paths = []
    next_anchors = []
    for text, src in hits:
        loc = _TEXT_LOC.get(text)
        path = loc[0] if loc else ""
        idx = loc[1] if loc else None
        paths.append(path)
        if path and idx is not None:
            next_anchors.append((path, idx))
        chunk_ids.append({"source": src, "path": path, "chunk_index": idx})
    commit_turn(session_id, question, answer or "", paths, anchors=next_anchors)
    # 规则抽取 + 写 json 很快；同步落盘，避免「新会话」紧接着提问时偏好还没写上
    upsert_facts(user_id, pref_update)
    _append_qa_log({
        "ts": datetime.now().isoformat(timespec="seconds"),
        "question": question,
        "standalone_query": standalone,
        "rewrite_source": rewrite_src,
        "domain": used_domain or "",
        "domain_source": domain_src,
        "user_id": user_id or "",
        "session_id": session_id or "",
        "n_history": len(hist),
        "n_ltm_facts": len(ltm_facts),
        "used_anchors": bool(inject_anchors),
        "latency_ms": round(latency_ms, 1),
        "n_hits": len(hits),
        "context_raw_chars": cstats["raw_chars"],
        "context_kept_chars": cstats["kept_chars"],
        "context_compressed": cstats["compressed"],
        "chunks": chunk_ids,
        "answer_chars": len(answer or ""),
    })
    meta = {
        "used_domain": used_domain or "",
        "domain_source": domain_src,
    }
    return answer, hits, standalone, meta


def ask_rag(question: str, domain=None, session_id=None, user_id=None) -> str:
    """混合检索 + 重排 + 邻居补全 + 生成（给评估和 Agent 用的纯文本接口）。"""
    answer, _hits, _q, _meta = ask_rag_with_hits(
        question, domain=domain, session_id=session_id, user_id=user_id,
    )
    return answer


if __name__ == "__main__":
    question = "什么是 RAG？"
    print(ask_rag(question))
