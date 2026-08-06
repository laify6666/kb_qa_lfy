"""第 6 步：Agent + RAG 融合——让 Agent 自主决定「什么时候查知识库」

启动（在 scripts 目录下）：
    python agent_rag.py

核心思路：
- 知识库问答（rag_qa.ask_rag）被包装成一个「工具」
- Agent（ReAct 模式）自己判断：这个问题要不要查资料？查什么关键词？
- 闲聊直接回答、技术问题自动调工具——这就是 Agent 的「决策能力」

与 team_agent.py 的关系：同样的 Agent 骨架（裸 JSON 兼容解析器、参数限制），
但这次工具换成了你自己的 RAG 知识库。
"""

import json
import re

from langchain.agents import initialize_agent, AgentType
from langchain.agents.structured_chat.output_parser import StructuredChatOutputParser
from langchain.tools import tool
from langchain_core.agents import AgentAction, AgentFinish
from langchain_core.exceptions import OutputParserException
from langchain_openai import ChatOpenAI

from config import API_KEY, BASE_URL, LLM_MODEL
from rag_qa import ask_rag   # 复用已测好的 RAG 问答（检索 + 生成），一行不改


# ================== 1. 配置 DeepSeek ==================
# 注意：Agent 层负责「决策」，temperature 用 0.3 保留一点灵活性；
# 知识库工具内部（ask_rag）用 temperature=0 保证事实性。
llm = ChatOpenAI(
    model=LLM_MODEL,
    openai_api_key=API_KEY,
    base_url=BASE_URL,
    temperature=0.3,
)


# ================== 2. 裸 JSON 兼容解析器（从 team_agent.py 复用） ==================
# DeepSeek 偶尔输出不带三反引号的 JSON，标准解析器会误判，这里兼容它。

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
        # 1) 标准格式：三反引号包裹的 JSON，交给父类处理
        if self.pattern.search(text) is not None:
            return super().parse(text)
        # 2) 兼容格式：直接从文本中提取裸 JSON 对象
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
        # 3) 兜底：未发现工具调用，视为最终回答
        return AgentFinish({"output": text}, text)


# ================== 3. 定义工具：把 RAG 问答包成 Agent 能调用的函数 ==================

@tool
def knowledge_base_qa(question: str) -> str:
    """查询本地知识库（RAG 技术语料：RAG、LangChain、向量检索、重排、ReAct、Agent 等）并返回基于资料的权威回答。
    当用户的问题涉及上述 AI 技术概念时，必须调用本工具；闲聊或无关话题不要调用。"""
    try:
        return ask_rag(question)
    except Exception as e:
        return f"知识库查询失败：{str(e)}"


# ================== 4. 创建 Agent ==================

agent = initialize_agent(
    tools=[knowledge_base_qa],
    llm=llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    max_iterations=3,                # 防死循环：最多思考 3 轮
    early_stopping_method="generate",
    max_execution_time=60,           # 硬超时，防止"文件已保存但程序不返回"
    return_intermediate_steps=True,  # 记录工具调用轨迹，方便展示决策过程
    handle_parsing_errors="输出格式有误：请严格按 JSON 输出工具调用，action_input 参数必须完整且非空。",
    agent_kwargs={
        "output_parser": LenientStructuredChatOutputParser(),
        "system_message": """你是一个知识库问答助手，配有一个工具 knowledge_base_qa。
使用规则：
1. 当用户问题涉及 RAG、LangChain、向量检索、重排、ReAct、Agent 等 AI 技术概念时，**必须调用 knowledge_base_qa** 获取资料后再回答。
2. 如果是闲聊（问候、自我介绍、无关话题），直接回答，**不要调用工具**。
3. 调用工具后，以工具返回的内容为事实依据组织最终回答；工具没提供的信息不要编造。
4. 最终回答直接输出纯文本，**严禁输出 JSON 或工具调用指令**。""",
    },
)


# ================== 5. 交互循环 ==================

print("=" * 60)
print("🤖 Agent + RAG 融合系统已启动")
print("Agent 会自己判断：要不要查知识库、查什么")
print("输入 q 退出")
print("=" * 60)
print("建议试试：")
print("  1. 什么是 RAG？                （会触发工具调用）")
print("  2. 介绍一下模块化 RAG 的特点    （会触发工具调用）")
print("  3. 你好，请自我介绍一下          （闲聊，不触发工具）")

while True:
    user_input = input("\n你：")
    if user_input.lower() in ["q", "退出"]:
        print("再见！")
        break

    try:
        result = agent.invoke({"input": user_input})

        # 打印工具调用轨迹——看 Agent 是怎么决策的
        steps = result.get("intermediate_steps", [])
        if steps:
            print("\n🧠 Agent 决策过程：")
            for action, observation in steps:
                obs = str(observation)
                print(f"   ⚙️ 调用工具：{action.tool}")
                print(f"      参数：{action.tool_input}")
                print(f"      返回：{obs[:100]}{'…' if len(obs) > 100 else ''}")

        print("\n✅ 最终回答：")
        print(result["output"])
    except Exception as e:
        print(f"❌ 执行出错：{str(e)}")
