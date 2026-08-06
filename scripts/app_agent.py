"""第 8 步：Agent Web 服务——把多工具 Agent 接进浏览器

启动（在 scripts 目录下）：
    python app_agent.py
浏览器打开 http://127.0.0.1:8001

与 app.py 的区别：
- app.py：普通 RAG 问答，直接查知识库回答
- app_agent.py：Agent 自主决策——查知识库 / 联网搜索 / 写文件，并返回决策轨迹

接口一览：
    GET  /         首页（浏览器演示入口）
    POST /ask      入参 {"question": "..."}，返回答案 + 决策轨迹（调了哪些工具）
    GET  /health   健康检查
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from agent_multi import agent  # 复用多工具 Agent（决策 + 工具调用），不触发它的命令行循环

app = FastAPI(title="Agent 工作流演示")


class AskRequest(BaseModel):
    """接口入参格式：请求体必须是 JSON，至少带 question 字段"""
    question: str


@app.get("/", response_class=HTMLResponse)
def home():
    """首页：一个提问页面，展示回答和 Agent 决策轨迹"""
    return HTML_PAGE


@app.post("/ask")
def ask(req: AskRequest):
    """核心接口：POST {"question": "..."} → {"answer": ..., "steps": [...]}"""
    try:
        result = agent.invoke({"input": req.question})
    except Exception as e:
        # API 防御：绝不裸抛 500，把错误转成可读信息返回给前端
        return {"answer": f"❌ Agent 执行出错：{str(e)[:200]}", "steps": []}
    steps = []
    for action, observation in result.get("intermediate_steps", []):
        obs = str(observation)
        steps.append({
            "tool": str(action.tool),
            "args": str(action.tool_input),
            "result": obs[:150] + ("…" if len(obs) > 150 else ""),
        })
    return {"answer": result.get("output", ""), "steps": steps}


@app.get("/health")
def health():
    """健康检查：部署后确认服务活着"""
    return {"status": "ok"}


HTML_PAGE = """<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="utf-8">
<title>Agent 工作流演示</title>
<style>
  body { font-family: "Microsoft YaHei", sans-serif; max-width: 780px; margin: 40px auto; padding: 0 16px; color: #222; }
  textarea { width: 100%; height: 80px; font-size: 16px; padding: 8px; box-sizing: border-box; border: 1px solid #ccc; border-radius: 6px; }
  button { margin-top: 10px; padding: 8px 22px; font-size: 15px; background: #2f6fed; color: #fff; border: none; border-radius: 6px; cursor: pointer; }
  button:disabled { background: #aaa; }
  .card { border: 1px solid #ddd; border-radius: 8px; padding: 14px; margin-top: 14px; }
  .step { border-left: 3px solid #2f6fed; background: #f6f8ff; padding: 8px 12px; margin-top: 8px; font-size: 13px; }
  .step .args { color: #666; margin-top: 4px; word-break: break-all; }
  .step .ret { color: #888; margin-top: 4px; word-break: break-all; }
  .loading { color: #888; }
</style>
</head>
<body>
<h2>🤖 Agent 工作流演示</h2>
<p>Agent 自主决定：查知识库 / 联网搜索 / 写文件。试试输入：<b>什么是 RAG？然后保存成 report.md</b></p>
<textarea id="q" placeholder="在这里输入你的任务…"></textarea>
<br>
<button id="btn" onclick="ask()">执行</button>
<div id="result"></div>

<script>
async function ask() {
  const q = document.getElementById("q").value.trim();
  if (!q) return;
  const btn = document.getElementById("btn");
  btn.disabled = true;
  btn.textContent = "Agent 思考中…";
  document.getElementById("result").innerHTML = '<div class="card loading">Agent 正在决策并调用工具…</div>';
  try {
    const res = await fetch("/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question: q }),
    });
    const data = await res.json();
    const stepHtml = (data.steps || []).map((s, i) =>
      `<div class="step"><b>第 ${i + 1} 步：${escapeHtml(s.tool)}</b>` +
      `<div class="args">参数：${escapeHtml(s.args)}</div>` +
      `<div class="ret">返回：${escapeHtml(s.result)}</div></div>`
    ).join("");
    document.getElementById("result").innerHTML =
      `<div class="card"><b>✅ 最终回答：</b><p>${escapeHtml(data.answer)}</p></div>` +
      (stepHtml ? `<div class="card"><b>🧠 决策轨迹：</b>${stepHtml}</div>` : "");
  } catch (err) {
    document.getElementById("result").innerHTML = `<div class="card">请求失败：${err}</div>`;
  }
  btn.disabled = false;
  btn.textContent = "执行";
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
    uvicorn.run(app, host="127.0.0.1", port=8001)
