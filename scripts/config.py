"""全局配置：所有脚本从这里读取路径、模型和参数（单一数据源）。

API Key 从环境变量读取，绝不写进代码或提交到仓库。
"""

import os
from pathlib import Path

# 项目根目录（config.py 在 scripts/ 下，往上一级就是项目根）
KB_DIR = Path(__file__).parent.parent

# ---- 数据路径 ----
RAW_DIR = KB_DIR / "data" / "raw"                  # 原始语料
CHROMA_DIR = KB_DIR / "data" / "chroma_db_zh"      # 当前向量库（bge 中文模型）
QUESTIONS_PATH = KB_DIR / "tests" / "questions_full.md"  # 评估测试集
ANSWERS_PATH = KB_DIR / "tests" / "answers.md"      # 评估结果输出

# ---- 模型配置 ----
EMBEDDING_MODEL = "BAAI/bge-small-zh-v1.5"        # 中文优化 embedding
RERANK_MODEL = "BAAI/bge-reranker-base"           # 重排模型
LLM_MODEL = "deepseek-v4-flash"
BASE_URL = "https://api.deepseek.com/v1"
TEMPERATURE = 0                                    # 问答要确定性

# ---- API Key（从环境变量读取，绝不硬编码） ----
API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
if not API_KEY:
    raise RuntimeError(
        "未检测到 DEEPSEEK_API_KEY 环境变量。\n"
        "请在 PowerShell 里设置后重试：\n"
        "  $env:DEEPSEEK_API_KEY='sk-你的key'"
    )

# ---- 检索参数 ----
K = 5                                              # 检索返回的候选块数

# ---- 环境开关 ----
HF_OFFLINE = True
