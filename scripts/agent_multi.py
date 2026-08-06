"""第 7 步：多工具 Agent 工作流——一个 Agent 拥有知识库、联网搜索、文件读写四种能力

启动（在 scripts 目录下）：
    python agent_multi.py

与 agent_rag.py 的区别：
- agent_rag.py：只有知识库一个工具，Agent 学会「要不要查」
- agent_multi.py：四个工具，Agent 学会「怎么编排」——先查知识库，再联网补充，最后存成文件

从 team_agent.py 带过来的三个教训：
1. 保存文件的内容必须用工具的真实返回值，回读校验，不信 LLM 转述
2. max_iterations 限制 + 硬超时，防止死循环
3. 裸 JSON 兼容解析器，防止 DeepSeek 输出格式问题
"""

import json
import os
import re
from pathlib import Path

from langchain.agents import initialize_agent, AgentType
from langchain.agents.structured_chat.output_parser import StructuredChatOutputParser
from langchain.tools import tool
from langchain_core.agents import AgentAction, AgentFinish
from langchain_core.exceptions import OutputParserException
from langchain_openai import ChatOpenAI
from ddgs import DDGS

from config import API_KEY, BASE_URL, LLM_MODEL
from rag_qa import ask_rag


# 报告保存目录：kb_qa/reports/（与 scripts 同级，不存在会自动创建）
REPORTS_DIR = Path(__file__).resolve().parent.parent / "reports"
os.makedirs(REPORTS_DIR, exist_ok=True)


# ================== 1. 配置 DeepSeek ==================
llm = ChatOpenAI(
    model=LLM_MODEL,
    openai_api_key=API_KEY,
    base_url=BASE_URL,
    temperature=0.3,
)


# ================== 2. 裸 JSON 兼容解析器（复用） ==================

def _extract_first_json_object(text: str):
    """扫描文本，返回第一个完整的 JSON 对象（跳过字符串内的花括号）"""
    start = text.find("{")
    while start != -1:
        depth = 0
        in_string = False
        escape = False
        end = -1
        for i in range(start, len(text)):
            ch = text[i]
            if in_string:
                if escape:
                    escape = False
                elif ch == "\\":
                    escape = True
                elif ch == '"':
                    in_string = False
            elif ch == '"':
                in_string = True
            elif ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    end = i
                    break
        if end != -1:
            return text[start:end + 1]
        start = text.find("{", start + 1)
    return None


class LenientStructuredChatOutputParser(StructuredChatOutputParser):
    """兼容 DeepSeek 输出裸 JSON 的情况"""

    def parse(self, text):
        if self.pattern.search(text) is not None:
            return super().parse(text)
        blob = _extract_first_json_object(text)
        if blob is not None:
            try:
                response = json.loads(blob, strict=False)
            except Exception:
                response = None
            if isinstance(response, dict) and "action" in response:
                if response["action"] == "Final Answer":
                    return AgentFinish({"output": str(response.get("action_input", ""))}, text)
                action_input = response.get("action_input", {})
                if action_input in ({}, "", None):
                    raise OutputParserException(
                        f"工具 {response['action']} 的参数为空，请重新输出完整参数"
                    )
                return AgentAction(
                    str(response["action"]),
                    action_input,
                    text,
                )
        return AgentFinish({"output": text}, text)


# ================== 3. 广告过滤（从 team_agent.py 复用） ==================

AD_KEYWORDS = [
    "网赚", "日入", "月入", "变现", "起号", "爆文", "附工具", "资源站",
    "加V", "加微信", "吃瓜", "爆料", "黑料", "约炮", "刺激", "VIP软件",
    "最新电影", "隐藏内容", "私密", "成人", "做爱",
]

AD_SITES = ["kanliao.one", "51淘金网", "木木哥", "yeyulingfeng.com", "91黑料", "今日看料"]
AD_HINT_WORDS = ["收益", "赚钱", "副业", "教程", "下载", "推广", "广告", "免费"]
NEWS_SIGNALS = ["报道", "记者", "发布", "宣布", "据悉", "来源", "专访", "官方"]
TRUSTED_SOURCES = ["bbc", "abc news", "reuters", "apnews", "nytimes", "theguardian", "新华", "人民网", "央视"]


def _score_result(result: dict) -> int:
    """给单条结果打质量分：新闻信号加分，广告线索和低信息量减分"""
    title = result.get("title", "")
    body = result.get("body", "")
    text = f"{title} {body}".lower()
    score = 0
    score += sum(1 for signal in NEWS_SIGNALS if signal in text)
    score -= 2 * sum(1 for word in AD_HINT_WORDS if word in text)
    score += 3 * sum(1 for src in TRUSTED_SOURCES if src in text)
    if re.search(r"\d{4}年\d{1,2}月", text):
        score += 2
    if len(title) < 8:
        score -= 1
    if len(body) < 20:
        score -= 1
    return score


def filter_results(results: list, keep_top: int = 5, min_score: int = 1) -> list:
    """先硬杀广告指纹，再按质量分排序，保留前 keep_top 条"""
    if not results:
        return []
    kept, dropped = [], []
    for r in results:
        text = f"{r.get('title', '')} {r.get('body', '')}".lower()
        if any(kw in text for kw in AD_KEYWORDS) or any(site in text for site in AD_SITES):
            reason = "命中硬杀词"
            dropped.append((r, reason))
        elif _score_result(r) >= min_score:
            kept.append(r)
        else:
            reason = "评分不足"
            dropped.append((r, reason))
    kept.sort(key=_score_result, reverse=True)
    print(f"🧹 内容过滤：共 {len(results)} 条，过滤 {len(dropped)} 条，保留 {len(kept[:keep_top])} 条")
    for r, reason in dropped[:8]:
        print(f"   ✂️ 已过滤（{reason}）：{r.get('title', '')[:40]}")
    return kept[:keep_top]


# ================== 4. 定义四个工具 ==================

@tool
def knowledge_base_qa(question: str) -> str:
    """查询本地知识库（RAG 技术语料：RAG、LangChain、向量检索、重排、ReAct、Agent 等）并返回基于资料的权威回答。
    当用户的问题涉及上述 AI 技术概念时，必须调用本工具；需要实时新闻时用 search_web。"""
    try:
        return ask_rag(question)
    except Exception as e:
        return f"知识库查询失败：{str(e)}"


@tool
def search_web(query: str) -> str:
    """联网搜索实时信息（新闻、热点、最新动态），返回已过滤广告的结果。
    当用户需要最新信息、新闻头条时调用；AI 技术概念类问题请用 knowledge_base_qa。"""
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=10))
            if not results:
                return "未找到相关结果"
            results = filter_results(results)
            if not results:
                return "搜索到内容但全部被广告过滤，请换一个关键词再试"
            output = []
            for r in results:
                output.append(f"标题：{r.get('title', '')}\n内容：{r.get('body', '')}\n")
            return "\n".join(output)
    except Exception as e:
        return f"搜索失败：{str(e)}"


def _save_file(filename: str, content: str) -> str:
    """保存到 reports 目录（只取文件名，防止路径越权）"""
    try:
        safe_name = os.path.basename(filename)
        full_path = REPORTS_DIR / safe_name
        full_path.write_text(content, encoding="utf-8")
        return f"文件已保存：{full_path}"
    except Exception as e:
        return f"写入失败：{str(e)}"


@tool
def write_file(filename: str, content: str = "") -> str:
    """把内容保存到 reports 目录下的文件。当用户要求把结果保存/写入文件时调用；
    filename 只需给文件名（如 report.md），content 必须是你要保存的原始内容。"""
    if not content:
        return "错误：content 参数为空。请重新调用 write_file，并同时提供 filename 和完整的 content 内容。"
    return _save_file(filename, content)


@tool
def read_file(filename: str) -> str:
    """读取 reports 目录下文件的内容。"""
    try:
        safe_name = os.path.basename(filename)
        full_path = REPORTS_DIR / safe_name
        return full_path.read_text(encoding="utf-8")
    except Exception as e:
        return f"读取失败：{str(e)}"


# ================== 5. 创建 Agent ==================

agent = initialize_agent(
    tools=[knowledge_base_qa, search_web, write_file, read_file],
    llm=llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    max_iterations=4,                # 多步任务需要更多轮次，但仍有限制
    early_stopping_method="generate",
    max_execution_time=90,           # 硬超时，防止卡死
    return_intermediate_steps=True,
    handle_tool_error=True,          # 工具异常时把错误返回给 LLM 重试，而不是崩溃
    handle_parsing_errors="输出格式有误：请严格按 JSON 输出工具调用，action_input 参数必须完整且非空。",
    agent_kwargs={
        "output_parser": LenientStructuredChatOutputParser(),
        "system_message": """你是一个多工具工作流助手，按需使用以下工具：
- knowledge_base_qa(question)：本地知识库（RAG 技术语料），回答 RAG、LangChain、向量检索、重排、ReAct、Agent 等 AI 技术概念问题，内容权威。
- search_web(query)：联网搜索，获取新闻、热点、最新动态等实时信息。
- write_file(filename, content)：把内容保存为文件，filename 只给文件名（如 report.md）。
- read_file(filename)：读取已保存的文件。

使用规则：
1. AI 技术概念问题 → knowledge_base_qa；实时新闻/热点 → search_web；都不涉及 → 直接回答，不要调用工具。
2. 多步任务允许连续调用多个工具，例如：先查知识库/搜索，再把结果保存成文件。
3. write_file 必须同时提供 filename 和 content 两个参数；content 必须是你要保存的**原始内容**，不要加 JSON、不要加多余说明。
4. 最终回答直接输出纯文本，严禁输出 JSON 或工具调用指令。""",
    },
)


# ================== 6. 文件回读校验（不信转述，信文件） ==================

def _verify_written_files(steps):
    """检查 Agent 是否写过文件；写了就回读比对，不一致自动修复"""
    for action, observation in steps:
        if getattr(action, "tool", None) != "write_file":
            continue
        ti = action.tool_input
        if not isinstance(ti, dict):
            continue
        filename = ti.get("filename", "")
        content = ti.get("content", "")
        full_path = REPORTS_DIR / os.path.basename(filename)
        try:
            actual = full_path.read_text(encoding="utf-8")
        except Exception as e:
            print(f"\n⚠️ 回读失败：{str(e)}")
            continue
        if actual == content:
            print(f"\n📄 文件校验通过：{full_path}（{len(actual)} 字符）")
        else:
            _save_file(filename, content)
            print(f"\n⚠️ 文件内容与写入参数不一致，已自动修复为原始内容")


# ================== 7. 交互循环（仅直接运行时执行） ==================
# 用 if __name__ == "__main__" 包起来：
# 命令行跑 python agent_multi.py 时进入循环；
# 被 app_agent.py import 时只复用 agent，不会触发循环。

def main():
    print("=" * 60)
    print("🤖 多工具 Agent 工作流已启动")
    print("工具：知识库 / 联网搜索 / 写文件 / 读文件")
    print(f"📁 报告目录：{REPORTS_DIR}")
    print("输入 q 退出")
    print("=" * 60)
    print("建议试试：")
    print("  1. 用知识库回答什么是 RAG，然后保存成 report.md")
    print("  2. 搜索今天 AI 新闻，保存成 ai_news.md")
    print("  3. 你好（闲聊，不调用工具）")

    while True:
        user_input = input("\n你：")
        if user_input.lower() in ["q", "退出"]:
            print("再见！")
            break

        try:
            result = agent.invoke({"input": user_input})

            # 打印工具调用轨迹——看 Agent 是怎么编排多步任务的
            steps = result.get("intermediate_steps", [])
            if steps:
                print("\n🧠 Agent 决策过程：")
                for action, observation in steps:
                    obs = str(observation)
                    print(f"   ⚙️ 调用工具：{action.tool}")
                    print(f"      参数：{action.tool_input}")
                    print(f"      返回：{obs[:120]}{'…' if len(obs) > 120 else ''}")

            print("\n✅ 最终回答：")
            print(result["output"])

            # 写文件后回读校验
            _verify_written_files(steps)
        except Exception as e:
            print(f"❌ 执行出错：{str(e)}")


if __name__ == "__main__":
    main()
