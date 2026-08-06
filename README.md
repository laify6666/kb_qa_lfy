# 知识库问答系统（RAG）

基于 LangChain + DeepSeek 的中文知识库问答系统。输入一篇技术文章语料，系统自动完成「加载 → 切分 → 向量化 → 检索 → 生成」，回答问题时只依据知识库内容，不编造。

## 功能

- 文档加载与切分（`RecursiveCharacterTextSplitter`，chunk_size=500, overlap=100）
- 向量化入库（Chroma + 中文优化 embedding `bge-small-zh-v1.5`）
- 语义检索（Top-K 相似度检索）
- DeepSeek 带引用生成（temperature=0，不知道就说不知道）
- 20 题测试集自动评估（`run_eval.py`）

## 目录结构

```
kb_qa/
├── data/
│   ├── raw/                # 原始语料（5 篇中文技术文章）
│   └── chroma_db_zh/       # 向量库（git 忽略，可重建）
├── scripts/
│   ├── config.py           # 全局配置（模型/路径/参数，单一数据源）
│   ├── load_documents.py   # 文档加载
│   ├── build_vectorstore.py# 切分 + 向量化 + 入库
│   ├── rag_qa.py           # 单题问答
│   ├── run_eval.py         # 20 题评估
│   └── rerank_test.py      # 重排对比实验
├── tests/
│   ├── questions.md        # 测试集（20 题 + 答案要点 + 出处）
│   └── answers.md          # 评估输出
└── README.md
```

## 快速开始

```powershell
conda activate ai
cd D:\桌面\learn\kb_qa
python scripts\build_vectorstore.py   # 首次会下载 embedding 模型，然后建库
python scripts\rag_qa.py              # 单题问答演示
python scripts\run_eval.py            # 跑完整 20 题评估
```

依赖：`pip install langchain==0.1.0 langchain-community==0.0.29 langchain-openai chromadb sentence-transformers`

## 评估结果

20 题测试集（10 事实题 + 4 综合题 + 4 无答案题 + 2 概念辨析），人工对照答案要点打分：

| 指标 | MiniLM（英文模型） | bge-small-zh（中文模型） |
|---|---|---|
| 回答正确率 | 60% ± 8%（三轮） | **77.5% ± 2.5%（两轮）** |
| 有依据命中率 | 80% | **92.5% ± 2.5%** |

无答案题（15-18）在两种模型下均为 4/4 正确拒答——「不知道就说不知道」的幻觉防线有效。

## 优化历程（评估驱动的诊断链条）

1. **k=3 → k=5**：正确率 50% → 65%（一个参数，肉眼可见）
2. **重排实验**：Cross-Encoder 能把噪声块压到末尾，但「重排不能无中生有」——答案块不在候选集就救不回来
3. **分层诊断**：打印 top-5 定位问题层——「检索稳定、生成波动」（同一批材料，模型有时用不全）
4. **换中文 embedding（关键）**：`all-MiniLM-L6-v2`（英文为主）→ `bge-small-zh-v1.5`（中文优化），正确率 +17 个百分点，验证了「embedding 是召回瓶颈」

## 已知问题与后续方向

- Q11（切分器对比）、Q12（Modular RAG 特点）存在检索召回缺口 → 尝试 Markdown 感知切分、查询改写（HyDE）
- Q13/Q14/Q19 有生成波动 → 提示词要求「完整列出所有要点」，或多次运行取平均
- API Key 目前硬编码在 `config.py`，生产环境应改用环境变量
- 后续可接入重排管线（召回 k=10 + 重排取 3）、Web 界面（FastAPI）
