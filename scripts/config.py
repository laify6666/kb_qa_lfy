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
BM25_CORPUS_PATH = CHROMA_DIR / "bm25_corpus.jsonl"  # 与向量块同源的旁路语料，供 BM25 启动加载
QA_LOG_PATH = KB_DIR / "data" / "logs" / "qa.jsonl"  # 问答审计日志（无密钥）
LTM_PATH = KB_DIR / "data" / "memory" / "ltm.json"  # 长期偏好；禁止写入 Chroma/BM25

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

# ---- 切分参数（建库与 BM25 必须读这里，禁止在脚本里再写一份 500/100）----
CHUNK_SIZE = 500                                   # 结构内超长时的滑窗大小
CHUNK_OVERLAP = 100                                # 仅用于最后一级滑窗，结构边界不重叠

# ---- 检索参数 ----
K = 5                                              # 送入 LLM 的精排块数（邻居补全前）
RERANK_CANDIDATES = 20                             # 混合召回池；重排只看这些，不整池喂给 LLM
NEIGHBOR_RADIUS = 1                                # 命中块左右各取几块（同文档 chunk_index）
CONTEXT_MAX_CHUNKS = 8                             # 邻居补全后的上限，防止上下文膨胀
CONTEXT_MAX_CHARS = 2800                           # 送进生成的资料正文上限；超了才抽取压缩

# ---- 多轮短期记忆 ----
HISTORY_TURNS = 3                                  # 只留最近 3 轮，对齐 Dify 工业实践
HISTORY_ANSWER_CHARS = 400                         # 写入 prompt 的旧答案截断；用户原句不截，以免指代丢失
REWRITE_MAX_CHARS = 80                             # 改写结果超长视为模型跑题，丢弃改回原问
LTM_MAX_FACTS = 8                                  # 每用户最多几条短偏好，本身就该短

# ---- 环境开关 ----
HF_OFFLINE = True
