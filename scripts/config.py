"""全局配置：所有脚本从这里读取路径、模型和参数（单一数据源）。

以后改模型、改路径、改 k 值，只改这一个文件。
"""

from pathlib import Path

# 项目根目录（config.py 在 scripts/ 下，往上一级就是项目根）
KB_DIR = Path(__file__).parent.parent

# ---- 数据路径 ----
RAW_DIR = KB_DIR / "data" / "raw"                  # 原始语料
CHROMA_DIR = KB_DIR / "data" / "chroma_db_zh"      # 当前向量库（bge 中文模型）
QUESTIONS_PATH = KB_DIR / "tests" / "questions.md"  # 评估测试集
ANSWERS_PATH = KB_DIR / "tests" / "answers.md"      # 评估结果输出

# ---- 模型配置 ----
EMBEDDING_MODEL = "BAAI/bge-small-zh-v1.5"        # 中文优化 embedding（召回瓶颈修复的关键）
RERANK_MODEL = "BAAI/bge-reranker-base"           # 重排模型（Cross-Encoder）
LLM_MODEL = "deepseek-v4-flash"
API_KEY = "sk-REVOKED_KEY_REMOVED"
BASE_URL = "https://api.deepseek.com/v1"
TEMPERATURE = 0                                    # 问答要确定性，不要创意

# ---- 检索参数 ----
K = 5                                              # 检索返回的候选块数

# ---- 环境开关 ----
# 模型已缓存时开 True 可加速启动；需要联网下载模型时改成 False
HF_OFFLINE = True
