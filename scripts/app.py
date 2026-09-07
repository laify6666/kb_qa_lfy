"""第 5 步：RAG Web 服务（FastAPI）——把 ask_rag 包成浏览器能用的 HTTP 接口

启动方式（在 scripts 目录下）：
    python app.py
然后浏览器打开 http://127.0.0.1:8000

接口一览：
    GET  /         多轮演示页（同一 session_id 连续追问）
    POST /ask      入参 {"question", "domain?", "session_id?", "user_id?"}
    POST /session/clear  清空该 session 的短期记忆（长期偏好保留）
    POST /memory/clear   清空该 user_id 的长期偏好
    GET  /domains  一级业务域列表
    GET  /health   健康检查
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from config import RAW_DIR
from long_term_memory import clear_user
from rag_qa import ask_rag_with_hits
from session_memory import clear_session

app = FastAPI(title="知识库问答 RAG 服务")


class AskRequest(BaseModel):
    """question 必填；其余均可空。空 session 不写短期；空 user 不写长期。"""
    question: str
    domain: str | None = None
    session_id: str | None = None
    user_id: str | None = None


class SessionClearRequest(BaseModel):
    """演示页点「新会话」时带上当前 session_id，服务端丢掉该档短期记忆。"""
    session_id: str | None = None


class MemoryClearRequest(BaseModel):
    """清除跨会话偏好。不影响当前气泡和短期历史。"""
    user_id: str | None = None


@app.get("/", response_class=HTMLResponse)
def home():
    """首页：多轮对话演示"""
    return HTML_PAGE


@app.post("/ask")
def ask(req: AskRequest):
    """核心接口：POST {"question": "...", "session_id": "...", "user_id": "..."}。

    sources 必须来自 ask_rag_with_hits 的同一批块，不能再走纯向量二次检索。
    used_domain / domain_source 便于确认是否套用了长期域偏好。
    """
    answer, hits, standalone, meta = ask_rag_with_hits(
        req.question, domain=req.domain, session_id=req.session_id,
        user_id=req.user_id,
    )
    sources = [
        {"source": src, "preview": text[:160]}
        for text, src in hits
    ]
    return {
        "answer": answer,
        "sources": sources,
        "session_id": req.session_id or "",
        "user_id": req.user_id or "",
        "standalone_query": standalone,
        "used_domain": meta.get("used_domain") or "",
        "domain_source": meta.get("domain_source") or "",
    }


@app.post("/session/clear")
def session_clear(req: SessionClearRequest):
    """清空指定会话的短期历史。id 为空则什么都不做。长期偏好不动。"""
    clear_session(req.session_id)
    return {"ok": True}


@app.post("/memory/clear")
def memory_clear(req: MemoryClearRequest):
    """清空该用户的长期偏好。user_id 为空则什么都不做。"""
    clear_user(req.user_id)
    return {"ok": True}


@app.get("/domains")
def domains():
    """列出 data/raw 下一级子目录名。空目录不出现；评估默认不过滤，演示页可选。"""
    names = []
    if RAW_DIR.is_dir():
        names = sorted(p.name for p in RAW_DIR.iterdir() if p.is_dir())
    return {"domains": names}


@app.get("/health")
def health():
    """健康检查：部署到服务器后用来确认服务还活着"""
    return {"status": "ok"}


HTML_PAGE = """<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="utf-8">
<title>知识库问答（多轮演示）</title>
<style>
  body { font-family: "Microsoft YaHei", sans-serif; max-width: 760px; margin: 24px auto; padding: 0 16px; color: #222; }
  textarea, select { width: 100%; font-size: 16px; padding: 8px; box-sizing: border-box; border: 1px solid #ccc; border-radius: 6px; }
  textarea { height: 72px; resize: vertical; }
  label { display: block; margin-top: 10px; font-size: 14px; color: #555; }
  .row { display: flex; gap: 8px; align-items: center; margin-top: 10px; flex-wrap: wrap; }
  button { padding: 8px 18px; font-size: 15px; background: #2f6fed; color: #fff; border: none; border-radius: 6px; cursor: pointer; }
  button.ghost { background: #fff; color: #2f6fed; border: 1px solid #2f6fed; }
  button:disabled { background: #aaa; color: #fff; border: none; }
  #log { margin-top: 16px; min-height: 200px; }
  .bubble { border: 1px solid #ddd; border-radius: 8px; padding: 12px 14px; margin-top: 10px; }
  .bubble.user { background: #f4f7ff; }
  .bubble.assistant { background: #fff; }
  .bubble .role { font-size: 12px; color: #888; margin-bottom: 6px; }
  .src { font-size: 13px; color: #666; margin-top: 6px; border-top: 1px dashed #eee; padding-top: 6px; }
  .rewrite { font-size: 12px; color: #888; margin-top: 8px; }
  .sid { font-size: 12px; color: #888; }
  .loading { color: #888; }
</style>
</head>
<body>
<h2>知识库问答（多轮）</h2>
<p>同一会话可追问「它 / 刚才那个」。回答只依据本轮检索资料。长期偏好跟浏览器用户走，「新会话」不清偏好。</p>
<p>试试：<b>以后只要百科域</b> → 点「新会话」→ 再问百科题。短期没了，域限制还在。</p>
<div class="row">
  <span class="sid">会话 <code id="sid">-</code></span>
  <span class="sid">用户 <code id="uid">-</code></span>
  <button type="button" class="ghost" id="newbtn" onclick="newSession()">新会话</button>
  <button type="button" class="ghost" id="membtn" onclick="clearMemory()">清除偏好</button>
</div>
<div id="log"></div>
<label for="domain">业务域（可选，默认全库）</label>
<select id="domain"><option value="">全库</option></select>
<label for="q">问题</label>
<textarea id="q" placeholder="输入问题，Enter 发送，Shift+Enter 换行"></textarea>
<div class="row">
  <button type="button" id="btn" onclick="ask()">发送</button>
</div>

<script>
function getSessionId() {
  let id = sessionStorage.getItem("rag_session_id");
  if (!id) {
    id = (crypto.randomUUID && crypto.randomUUID()) || ("s-" + Date.now());
    sessionStorage.setItem("rag_session_id", id);
  }
  return id;
}

function getUserId() {
  let id = localStorage.getItem("rag_user_id");
  if (!id) {
    id = (crypto.randomUUID && crypto.randomUUID()) || ("u-" + Date.now());
    localStorage.setItem("rag_user_id", id);
  }
  return id;
}

function showSession() {
  const id = getSessionId();
  document.getElementById("sid").textContent = id.slice(0, 8);
  document.getElementById("uid").textContent = getUserId().slice(0, 8);
}

function escapeHtml(s) {
  return (s || "").replace(/[&<>"']/g, c => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  }[c]));
}

function appendBubble(role, innerHtml) {
  const log = document.getElementById("log");
  const div = document.createElement("div");
  div.className = "bubble " + role;
  const label = role === "user" ? "你" : "助手";
  div.innerHTML = '<div class="role">' + label + "</div>" + innerHtml;
  log.appendChild(div);
  log.scrollTop = log.scrollHeight;
  return div;
}

async function loadDomains() {
  try {
    const res = await fetch("/domains");
    const data = await res.json();
    const sel = document.getElementById("domain");
    (data.domains || []).forEach(name => {
      const opt = document.createElement("option");
      opt.value = name;
      opt.textContent = name;
      sel.appendChild(opt);
    });
  } catch (_err) { /* 下拉失败时仍可全库提问 */ }
}

async function newSession() {
  const old = sessionStorage.getItem("rag_session_id");
  // 先清界面和本地 id，避免 /session/clear 稍慢时气泡还挂着
  sessionStorage.removeItem("rag_session_id");
  document.getElementById("log").innerHTML = "";
  showSession();
  try {
    if (old) {
      await fetch("/session/clear", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ session_id: old }),
      });
    }
  } catch (_err) { /* 服务端清失败时本地已经是新会话 */ }
}

async function clearMemory() {
  const uid = localStorage.getItem("rag_user_id");
  try {
    if (uid) {
      await fetch("/memory/clear", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_id: uid }),
      });
    }
  } catch (_err) { /* 清失败时下一轮仍可能带旧偏好 */ }
  appendBubble("assistant", "<p>已清除跨会话偏好。对话气泡还在，需要的话请点「新会话」。</p>");
}

async function ask() {
  const qEl = document.getElementById("q");
  const q = qEl.value.trim();
  if (!q) return;
  const domain = document.getElementById("domain").value.trim();
  const btn = document.getElementById("btn");
  btn.disabled = true;
  btn.textContent = "思考中…";
  qEl.value = "";
  appendBubble("user", "<p>" + escapeHtml(q) + "</p>");
  const wait = appendBubble("assistant", '<p class="loading">正在检索知识库并生成回答…</p>');
  try {
    const payload = { question: q, session_id: getSessionId(), user_id: getUserId() };
    if (domain) payload.domain = domain;
    const res = await fetch("/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    const data = await res.json();
    const srcs = (data.sources || [])
      .map(s => '<div class="src">' + escapeHtml(s.source || "") + " | " + escapeHtml(s.preview) + "…</div>")
      .join("");
    let extra = "";
    if (data.standalone_query && data.standalone_query !== q) {
      extra += '<div class="rewrite">检索句：' + escapeHtml(data.standalone_query) + "</div>";
    }
    if (data.used_domain && data.domain_source && data.domain_source !== "request" && data.domain_source !== "none") {
      extra += '<div class="rewrite">限定域：' + escapeHtml(data.used_domain)
        + "（" + escapeHtml(data.domain_source) + "）</div>";
    }
    wait.innerHTML =
      '<div class="role">助手</div><p>' + escapeHtml(data.answer) + "</p>" + extra + srcs;
  } catch (err) {
    wait.innerHTML = '<div class="role">助手</div><p>请求失败：' + escapeHtml(String(err)) + "</p>";
  }
  btn.disabled = false;
  btn.textContent = "发送";
  qEl.focus();
}

document.getElementById("q").addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    ask();
  }
});

showSession();
loadDomains();
</script>
</body>
</html>
"""


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
