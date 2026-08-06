"""第 5 步：RAG Web 服务（FastAPI）——把 ask_rag 包成浏览器能用的 HTTP 接口

启动方式（在 scripts 目录下）：
    python app.py
然后浏览器打开 http://127.0.0.1:8000

接口一览：
    GET  /         首页（提问页面，适合现场演示）
    POST /ask      核心接口，入参 {"question": "..."}，返回答案 + 参考片段
    GET  /health   健康检查，确认服务活着
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from config import K             # 复用全局配置：检索返回几条
from rag_qa import ask_rag, db   # 复用已测好的问答逻辑和向量库

app = FastAPI(title="知识库问答 RAG 服务")


class AskRequest(BaseModel):
    """接口入参格式：请求体必须是 JSON，至少带 question 字段"""
    question: str


@app.get("/", response_class=HTMLResponse)
def home():
    """首页：一个简单的提问页面"""
    return HTML_PAGE


@app.post("/ask")
def ask(req: AskRequest):
    """核心接口：POST {"question": "..."} → {"answer": ..., "sources": [...]}"""
    answer = ask_rag(req.question)                                # 复用已有逻辑，不改一行
    hits = db.similarity_search_with_score(req.question, k=K)     # 再查一次，拿参考片段
    sources = [
        {"score": round(float(score), 4), "preview": doc.page_content[:120]}
        for doc, score in hits
    ]
    return {"answer": answer, "sources": sources}


@app.get("/health")
def health():
    """健康检查：部署到服务器后用来确认服务还活着"""
    return {"status": "ok"}


HTML_PAGE = """<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="utf-8">
<title>知识库问答（RAG 演示）</title>
<style>
  body { font-family: "Microsoft YaHei", sans-serif; max-width: 760px; margin: 40px auto; padding: 0 16px; color: #222; }
  textarea { width: 100%; height: 80px; font-size: 16px; padding: 8px; box-sizing: border-box; border: 1px solid #ccc; border-radius: 6px; }
  button { margin-top: 10px; padding: 8px 22px; font-size: 15px; background: #2f6fed; color: #fff; border: none; border-radius: 6px; cursor: pointer; }
  button:disabled { background: #aaa; }
  .card { border: 1px solid #ddd; border-radius: 8px; padding: 14px; margin-top: 14px; }
  .src { font-size: 13px; color: #666; margin-top: 6px; border-top: 1px dashed #eee; padding-top: 6px; }
  .loading { color: #888; }
</style>
</head>
<body>
<h2>📚 知识库问答（RAG 演示）</h2>
<p>回答只依据知识库语料生成，不编造。试试输入：<b>什么是 RAG？</b></p>
<textarea id="q" placeholder="在这里输入你的问题…"></textarea>
<br>
<button id="btn" onclick="ask()">提问</button>
<div id="result"></div>

<script>
async function ask() {
  const q = document.getElementById("q").value.trim();
  if (!q) return;
  const btn = document.getElementById("btn");
  btn.disabled = true;
  btn.textContent = "思考中…";
  document.getElementById("result").innerHTML = '<div class="card loading">正在检索知识库并生成回答…</div>';
  try {
    const res = await fetch("/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question: q }),
    });
    const data = await res.json();
    const srcs = (data.sources || [])
      .map(s => `<div class="src">相似度 ${s.score} | ${escapeHtml(s.preview)}…</div>`)
      .join("");
    document.getElementById("result").innerHTML =
      `<div class="card"><b>回答：</b><p>${escapeHtml(data.answer)}</p></div>` +
      `<div class="card"><b>参考片段（来自知识库）：</b>${srcs}</div>`;
  } catch (err) {
    document.getElementById("result").innerHTML = `<div class="card">请求失败：${err}</div>`;
  }
  btn.disabled = false;
  btn.textContent = "提问";
}

function escapeHtml(s) {
  return (s || "").replace(/[&<>"']/g, c => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  }[c]));
}
</script>
</body>
</html>
"""


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
