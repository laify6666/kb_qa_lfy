# kb_qa：中文知识库问答（RAG）

LangChain + Chroma + DeepSeek 的中文 RAG。检索、评估、Web 演示走同一条 `retrieve_hybrid`，禁止评估用一套、线上用另一套。

当前链路：

```
改写（有历史才做）
  → 向量 + BM25 RRF
  → bge-reranker 精排
  → 同文档邻居补全
  → 抽取式压缩（超 2800 字才压）
  → DeepSeek 按编号资料生成
```

回答只依据**本轮**检索块。对话历史只解「它 / 刚才」，不能当证据。无答案题应回复「资料中没有相关信息」。

调优过程（问题 → 证据 → 改什么 → 怎么验收）见 [TUNING_LOG.md](TUNING_LOG.md)。

## 功能

- 结构感知切分（Markdown 标题 / 维基小节 / 段落，最后才滑窗），建库与 BM25 共用 `chunking.split_document`
- 混合检索：`bge-small-zh-v1.5` + BM25（RRF）→ `bge-reranker-base` → 邻居 ±1
- 多轮：短期 3 轮、查询改写、同文档锚点、抽取压缩、跨会话域偏好（`ltm.json`，**不写入向量库**）
- FastAPI 多轮演示页（`session_id` + `user_id`），答案带来源预览与 `[1][2]`
- 可选 ReAct Agent：知识库 / 联网搜索 / 文件读写（`agent_rag.py`、`agent_multi.py`）
- 44 题评测 + 分层诊断（文件 hit / 库内可检短语 hit / 覆盖缺口分开计）
- 多格式入库：Office / PDF / HTML / 图片 → Markdown（`ingest_files.py`）

## 指标（不要混成一个数）

| 指标 | 数值 | 说明 |
|---|---|---|
| 文件 hit@5 | **40/40（100%）** | 来源文件进 top-5；可自动判 40 题 |
| 短语 hit@5（库内可检） | **25/25（100%）** | 金标短语至少一条在全库里才进分母 |
| 块级漏召回 | **0** | 短语在库里，但 top-5 块没有 |
| 覆盖缺口 | **15** | 评估措辞在语料中不存在，**不是检索失败** |
| 可答题正确率 | **39/40（97.5%）** | 混合检索 + 新提示词后的 LLM 评估；切分/重排之后未再跑整表 LLM |
| 无答案题拒答 | **4/4** | Q15–18，零幻觉 |

字面短语口径（缺口进分母）曾是 25/40（62%），只作对照。`run_eval.py --score-only` 的词面分会同样偏低，不要当正确率。

报告：`tests/diagnose_report.md`。

## 快速开始

环境：conda `ai`，Python 3.10+。API Key **只走环境变量**。

```powershell
conda activate ai
$env:DEEPSEEK_API_KEY = "sk-你的key"
cd kb_qa\scripts

python build_vectorstore.py          # 首次建库；向量目录 git 忽略，克隆后必须重建
python rag_qa.py                     # 单题
python app.py                        # http://127.0.0.1:8000  多轮演示
```

演示：先问「什么是 RAG？」，再问「它的三个步骤是什么？」。长期偏好：发「以后只要百科域」，点「新会话」后再问百科题。

依赖（本机实际组合；仓库根 `requirements.txt` 里旧 pin 与 community 包互斥，勿照抄 0.1.0）：

```
langchain==0.1.20
langchain-community==0.0.38
langchain-openai==0.1.7
chromadb
sentence-transformers
rank_bm25
fastapi
uvicorn
```

入库额外：`markitdown`、`rapidocr_onnxruntime`、`pymupdf`。Embedding / 重排模型首次需能访问 Hugging Face；之后可 `HF_OFFLINE=True`（见 `config.py`）。

## 评估与诊断

在 `scripts/` 下：

```powershell
python diagnose.py --questions ../tests/questions_full.md --k 10
python run_eval.py                 # 调 LLM，产出 tests/answers.md
python run_eval.py --score-only    # 只对已有答案做词面分，不花 API
```

`diagnose` / `run_eval` **不要传** `session_id` / `user_id`，保持单轮。

## Web 接口

| 接口 | 作用 |
|---|---|
| `GET /` | 多轮演示页 |
| `POST /ask` | `{question, domain?, session_id?, user_id?}` → 答案、来源、改写句、所用域 |
| `POST /session/clear` | 清短期记忆，长期偏好保留 |
| `POST /memory/clear` | 清该 `user_id` 的域偏好 |
| `GET /domains` | `data/raw` 一级目录 |
| `GET /health` | 探活 |

Agent 演示（可选）：`python app_agent.py` → http://127.0.0.1:8001

## 语料

约 **481 篇**，按业务域放在 `data/raw/`，来源登记 `data/source_manifest.md`。

| 来源 | 约篇数 | 许可 |
|---|---|---|
| 中文维基百科快照 | 120 | CC BY-SA 4.0 |
| CMRC2018 | 100 | 学术用途 |
| DRCD（转简体） | 80 | CC BY-SA 3.0 |
| Langchain-Chatchat 文档 | 25 | 开源 |
| THUCNews 镜像 | 150 | Apache-2.0 |

```powershell
python ingest_sources.py                          # 批量公开语料
python ingest_files.py --input <文件> --domain 通用 --build
python build_vectorstore.py --dry-run
python build_vectorstore.py --incremental
```

## 目录

```
kb_qa/
├── data/raw/                 # 语料（按业务域）
├── data/chroma_db_zh/        # 向量库 + bm25_corpus.jsonl（git 忽略）
├── data/logs/                # qa.jsonl
├── data/memory/              # ltm.json（git 忽略，勿进向量库）
├── scripts/
│   ├── config.py             # 路径 / 模型 / K / 预算，单一数据源
│   ├── chunking.py           # 结构感知切分
│   ├── rag_qa.py             # retrieve_hybrid + 生成
│   ├── query_rewrite.py / session_memory.py / long_term_memory.py / context_compress.py
│   ├── diagnose.py / run_eval.py / build_vectorstore.py
│   ├── app.py / agent_*.py
│   └── ingest_*.py
├── tests/
│   ├── questions_full.md     # 44 题
│   ├── diagnose_report.md    # 当前检索诊断
│   └── answers*.md           # 各轮评估留档
├── README.md
└── TUNING_LOG.md
```

## 配置要点（`scripts/config.py`）

| 项 | 值 | 用意 |
|---|---|---|
| `K` | 5 | 精排后进生成的块数（扩邻居前） |
| `RERANK_CANDIDATES` | 20 | 只重排候选池，不把整库喂给 LLM |
| `NEIGHBOR_RADIUS` | 1 | 同文档左右各一块 |
| `CONTEXT_MAX_CHUNKS` | 8 | 邻居后的块数上限 |
| `CONTEXT_MAX_CHARS` | 2800 | 超了才抽句 |
| `HISTORY_TURNS` | 3 | 短期窗口 |
| `HF_OFFLINE` | True | 用本地已下载的 embedding / reranker |

## 刻意不做

更大 embedding、GraphRAG、默认走 Agent 检索、把长期记忆 upsert 进 Chroma。这些会打乱现有口径，或带偏 Q15–18 拒答。
