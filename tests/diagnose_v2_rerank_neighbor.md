# 检索命中诊断报告（混合+重排+邻居，k=10）

文件hit@5=40/40 | 短语hit@5=25/40 | 覆盖缺口=15 | 块级漏召回=0

## 一、事实题（10 题） Q1 [文件HIT5] [短语MISS] 覆盖缺口

Q: RAG 的全称和核心思想是什么？

来源: 02_rag实战指南_langchain.md | 语料中存在: True

A(要点): Retrieval-Augmented Generation（检索增强生成）；核心思想是让大模型「先查资料，再回答」

top-5 短语命中: （无）

top-5 短语缺失: ['Retrieval-Augmented Generation', '检索增强生成', '核心思想是让大模型「先查资料']

全库也缺失: ['Retrieval-Augmented Generation', '检索增强生成', '核心思想是让大模型「先查资料']

1. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 一、什么是 RAG？为什么它如此重要？
RAG 的核心思想很简单：让大模型"先查资料，再回答"。传统的 R

2. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 一、什么是 RAG？为什么它如此重要？ / RAG 的核心优势
- 降低幻觉：答案基于事实依据，而非模型的

3. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 五、总结与展望
RAG 技术不再追求让模型"记住"一切，而是让模型"学会"如何高效地利用外部知识。随着技术

4. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / RAG 的起源
RAG 模型将预先训练的参数记忆（预训练语言模型）和非参数记忆（通过检索机制访问的外部知识库，如维基百科的密集向量索引）结合

5. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / LangChain 框架：RAG 系统的技术基础
LangChain 已成为 RAG 应用开发的主流框架

6. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / GraphRAG
GraphRAG 利用实体间的结构信息，实现更精确、更全面的检索，捕捉关系知识。工作流程包括基于图形的索引（G-Index

7. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 发展历程
自 2021 年 RAG 技术出现之后，RAG 首先被用于 LLMs 的预训练阶段来增强语言模型，随后被用于微调与推理任务中。自 

8. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 工程实践工具
常用的 RAG 系统构建工具包括 LangChain 和 LlamaIndex（完整框架），以及 FlashRAG（模块化开源

9. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / Agentic RAG
Agentic RAG 将 ReAct 的推理能力与 Agent 的任务执行能力相结合，创建一个动态和自适应的系统。

10. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 高级 RAG（Advanced RAG）
高级 RAG 引入了具体的改进措施，以克服 Naive RAG 的局限性：

- 为了提高检索质量

## 一、事实题（10 题） Q2 [文件HIT5] [短语HIT5]

Q: 传统 RAG 流程的三个主要步骤是什么？

来源: 02_rag实战指南_langchain.md | 语料中存在: True

A(要点): 检索（Retrieval）→ 增强（Augmentation）→ 生成（Generation）

top-5 短语命中: ['Retrieval', 'Augmentation', 'Generation']

top-5 短语缺失: （无）

1. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 一、什么是 RAG？为什么它如此重要？
RAG 的核心思想很简单：让大模型"先查资料，再回答"。传统的 R

2. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / RAG 简单流程与总览
应用于问答的 RAG 过程主要包括 3 个步骤：

1. 索引：文档被分割成块，编码成向量，存储在向量数据库中。
2

3. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 模块化 RAG（Modular RAG）
模块化 RAG 架构超越了前两种范式，具有更强的适应性和多功能性。它将复杂的 RAG 系统分解为独

4. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / GraphRAG
GraphRAG 利用实体间的结构信息，实现更精确、更全面的检索，捕捉关系知识。工作流程包括基于图形的索引（G-Index

5. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 二、RAG 的技术架构深度解析 / 4. 检索与重排序（Retrieval & Reranking）
初步

6. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / 文档处理与分块策略
RAG 系统的关键步骤是文档的处理与分块，包括：文档加载、将文档分割为适当大小的块、

7. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / RAG 流程集成
```python
from langchain.chains import Retr

8. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / LangChain 框架：RAG 系统的技术基础
LangChain 已成为 RAG 应用开发的主流框架

9. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 高级 RAG（Advanced RAG）
高级 RAG 引入了具体的改进措施，以克服 Naive RAG 的局限性：

- 为了提高检索质量

10. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 工程实践工具
常用的 RAG 系统构建工具包括 LangChain 和 LlamaIndex（完整框架），以及 FlashRAG（模块化开源

## 一、事实题（10 题） Q3 [文件HIT5] [短语MISS] 覆盖缺口

Q: RAG 相比纯大模型回答有哪四个核心优势？

来源: 02_rag实战指南_langchain.md | 语料中存在: True

A(要点): 降低幻觉、数据私有化（无需微调即可用私有数据）、可解释性（可提供引用来源）、成本效益（避免全量微调）

top-5 短语命中: （无）

top-5 短语缺失: ['无需微调即可用私有数据', '可提供引用来源', '避免全量微调']

全库也缺失: ['无需微调即可用私有数据', '可提供引用来源', '避免全量微调']

1. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 一、什么是 RAG？为什么它如此重要？ / RAG 的核心优势
- 降低幻觉：答案基于事实依据，而非模型的

2. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 为什么需要 RAG？
大型语言模型在处理特定领域或知识密集型任务时存在很大局限性，特别是在处理超出其训练数据或需要当前信息的查询时，会产生"

3. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 一、什么是 RAG？为什么它如此重要？
RAG 的核心思想很简单：让大模型"先查资料，再回答"。传统的 R

4. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / RAG 的起源
RAG 模型将预先训练的参数记忆（预训练语言模型）和非参数记忆（通过检索机制访问的外部知识库，如维基百科的密集向量索引）结合

5. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 五、总结与展望
RAG 技术不再追求让模型"记住"一切，而是让模型"学会"如何高效地利用外部知识。随着技术

6. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / RAG 技术概述及其重要性
传统语言模型如 GPT-4 尽管功能强大，但其知识库受限于训练数据，无法有效

7. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 四、进阶优化：解决 RAG 的常见陷阱 / 3. 引入重排序（Reranking）
向量检索虽然快，但不够

8. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 四、进阶优化：解决 RAG 的常见陷阱 / 4. 评估体系（RAG Evaluation）
使用 RAGA

9. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / LangChain 框架：RAG 系统的技术基础
LangChain 已成为 RAG 应用开发的主流框架

10. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / 总结
通过上述方法可以构建一个能够基于特定文档集合回答问题的完整 RAG 系统。同样的技术架构适用于任何

## 一、事实题（10 题） Q4 [文件HIT5] [短语HIT5]

Q: 为什么 RAG 要把文档切分成小块（chunk）？两种切分策略各有什么特点？

来源: 02_rag实战指南_langchain.md | 语料中存在: True

A(要点): 小块是检索和生成的最小单位；固定大小切分简单但可能切断语义完整性，递归字符切分按段落/句子边界切、保留更多语义结构

top-5 短语命中: ['保留更多语义结构']

top-5 短语缺失: ['小块是检索和生成的最小单位', '固定大小切分简单但可能切断语义完整性', '递归字符切分按段落/句子边界切']

全库也缺失: ['小块是检索和生成的最小单位', '固定大小切分简单但可能切断语义完整性', '递归字符切分按段落/句子边界切']

1. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 二、RAG 的技术架构深度解析 / 1. 文档加载与分割（Loading & Splitting）
原始数

2. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 四、进阶优化：解决 RAG 的常见陷阱 / 1. 改进文本分割（Chunking Strategy）
- 

3. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / 文档处理与分块策略
# 将文档拆分成更小的块，以便更好地检索
text_splitter = Chara

4. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / LangChain 框架：RAG 系统的技术基础
LangChain 已成为 RAG 应用开发的主流框架

5. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / 文档分块策略优化
分块方式对检索质量有重大影响，尝试递归字符分割：

```python
from la

6. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 为什么需要 RAG？
大型语言模型在处理特定领域或知识密集型任务时存在很大局限性，特别是在处理超出其训练数据或需要当前信息的查询时，会产生"

7. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / 文档处理与分块策略
RAG 系统的关键步骤是文档的处理与分块，包括：文档加载、将文档分割为适当大小的块、

8. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 四、进阶优化：解决 RAG 的常见陷阱 / 2. 查询改写（Query Rewriting）
- HyDE

9. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 一、什么是 RAG？为什么它如此重要？
RAG 的核心思想很简单：让大模型"先查资料，再回答"。传统的 R

10. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / 常见问题及解决方案
- 检索质量差：使用更高质量的嵌入模型（如 all-mpnet-base-v2）、调

## 一、事实题（10 题） Q5 [文件HIT5] [短语HIT5]

Q: 什么是文本嵌入（Embedding）？语义相似的文本在向量空间中有什么关系？

来源: 02_rag实战指南_langchain.md | 语料中存在: True

A(要点): 把文本转换为数值向量；语义相似的文本，向量在空间中的距离也相近

top-5 短语命中: ['语义相似的文本']

top-5 短语缺失: ['把文本转换为数值向量', '向量在空间中的距离也相近']

全库也缺失: ['把文本转换为数值向量', '向量在空间中的距离也相近']

1. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 二、RAG 的技术架构深度解析 / 2. 向量化与嵌入（Embedding）
计算机无法直接理解语义，需要

2. (langchain_002.md)
[来源] langchain_002.md | base / ClassDef EmbeddingsFunAdapter / FunctionDef embed_documents(self, texts)
**embed_document

3. (langchain_002.md)
[来源] langchain_002.md | base / ClassDef EmbeddingsFunAdapter / FunctionDef aembed_documents(self, texts)
**aembed_docume

4. (langchain_002.md)
[来源] langchain_002.md | base / ClassDef EmbeddingsFunAdapter / FunctionDef embed_query(self, text)
**embed_query**: 该函数的

5. (langchain_002.md)
[来源] langchain_002.md | base / ClassDef EmbeddingsFunAdapter
在项目中，EmbeddingsFunAdapter类被多个模块调用，用于处理不同场景下的文本嵌入需求。例如，在知识库聊

6. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef ApiRequest / FunctionDef embed_texts(self, texts, embed_model, to_query)
**embe

7. (langchain_002.md)
[来源] langchain_002.md | base / ClassDef EmbeddingsFunAdapter
**属性**:
- `embed_model`: 嵌入模型的名称，用于指定使用哪个预训练模型进行文本嵌入。

**代码

8. (langchain_005.md)
[来源] langchain_005.md | base / ClassDef ApiEmbeddingsParams
ApiEmbeddingsParams类在项目中主要用于处理文本的向量化请求，通过与不同的模型工作器（如MiniMaxW

9. (langchain_002.md)
[来源] langchain_002.md | base / FunctionDef normalize(embeddings)
**normalize**: 此函数的功能是对输入的嵌入向量进行L2范数归一化处理。

**参数**:
- *

10. (langchain_020.md)
[来源] langchain_020.md | pg_kb_service / ClassDef PGKBService / FunctionDef _load_pg_vector(self)
**_load_pg_vector**: 此函

## 一、事实题（10 题） Q6 [文件HIT5] [短语HIT5]

Q: ReAct 的全称是什么？它的核心目标是什么？

来源: 04_react核心范式详解.md | 语料中存在: True

A(要点): Reasoning（推理）+ Acting（行动）；打破「输入-输出」单向链路，构建「感知-决策-执行-反馈」闭环

top-5 短语命中: ['Reasoning', '+ Acting']

top-5 短语缺失: ['打破「输入-输出」单向链路', '构建「感知-决策-执行-反馈」闭环']

全库也缺失: ['打破「输入-输出」单向链路', '构建「感知-决策-执行-反馈」闭环']

1. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / 什么是 ReAct？
ReAct = Reasoning（推理）+ Acting（行动），是一种让语言模型通过与外部工具、环境动

2. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / ReAct 工作原理 / 循环迭代阶段
每轮迭代严格遵循"推理-行动-观察"的顺序：

1. Thought（推理）：模型基于"

3. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / ReAct 工作原理 / 终止输出阶段
- 正常终止：模型输出 finish 行动，表明已完成任务目标；
- 超时终止：达到预设

4. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / 核心思想：模拟人类认知的 TAO 闭环
ReAct 将"Thought（推理）→Act（行动）→Observe（观察）"抽象为 

5. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / ReAct 工作原理 / 初始化阶段
接收自然语言任务目标，明确任务类型与核心约束；输入 1-3 个 Few-shot 示例；创

6. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / ReAct 解决了什么问题？
- 破解"事实幻觉"难题：将推理过程锚定到真实数据。实验数据显示，在 FEVER 事实核查任务中，

7. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / 四大设计理念
- 环境锚定原则：强制模型在涉及事实性问题时优先调用外部工具获取证据，禁止仅凭内部知识生成结论。
- 可解释性优先

8. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / ReAct 技术架构（三层）
- 核心逻辑层：智能体的"决策大脑"，由"LLM+提示工程模块"构成，包括推理引擎、行动规划器、提

9. (05_react手写实现指南.md)
[来源] 05_react手写实现指南.md | ReAct 代理裸机编码指南：不依赖任何框架的 LLM 自主决策实现 / 一、ReAct 模式：AI 代理的"思考-行动"循环
ReAct（Reasoning + Action）是一种让大语

10. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / ReAct 的局限
ReAct 依赖 LLM 的上下文窗口存储历史 TAO 轨迹，当任务步骤超过 10 轮时，需通过"裁剪-摘要

## 一、事实题（10 题） Q7 [文件HIT5] [短语HIT5]

Q: ReAct 的 TAO 循环由哪三部分组成？各自的作用是什么？

来源: 04_react核心范式详解.md | 语料中存在: True

A(要点): Thought（推理：分析任务目标与历史反馈）、Act（行动：调用工具）、Observe（观察：获取环境反馈）；反馈驱动下一轮推理

top-5 短语命中: ['Thought', 'Observe']

top-5 短语缺失: ['分析任务目标与历史反馈', '获取环境反馈', '反馈驱动下一轮推理']

全库也缺失: ['分析任务目标与历史反馈', '获取环境反馈', '反馈驱动下一轮推理']

1. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / ReAct 技术架构（三层）
- 核心逻辑层：智能体的"决策大脑"，由"LLM+提示工程模块"构成，包括推理引擎、行动规划器、提

2. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / ReAct 工作原理 / 循环迭代阶段
每轮迭代严格遵循"推理-行动-观察"的顺序：

1. Thought（推理）：模型基于"

3. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / 核心思想：模拟人类认知的 TAO 闭环
ReAct 将"Thought（推理）→Act（行动）→Observe（观察）"抽象为 

4. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / 极简代码框架
def react_core_loop(task, tools, llm, max_steps=6):
    "

5. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / 极简代码框架
关键点：通过"构建提示词→调用 LLM→解析行动→执行工具→更新上下文"的流程控制 TAO 循环；工具层面替换为专

6. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / ReAct 工作原理 / 初始化阶段
接收自然语言任务目标，明确任务类型与核心约束；输入 1-3 个 Few-shot 示例；创

7. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / ReAct 的局限
ReAct 依赖 LLM 的上下文窗口存储历史 TAO 轨迹，当任务步骤超过 10 轮时，需通过"裁剪-摘要

8. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / 什么是 ReAct？
ReAct = Reasoning（推理）+ Acting（行动），是一种让语言模型通过与外部工具、环境动

9. (05_react手写实现指南.md)
[来源] 05_react手写实现指南.md | ReAct 代理裸机编码指南：不依赖任何框架的 LLM 自主决策实现 / 一、ReAct 模式：AI 代理的"思考-行动"循环
ReAct（Reasoning + Action）是一种让大语

10. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / 四大设计理念
- 环境锚定原则：强制模型在涉及事实性问题时优先调用外部工具获取证据，禁止仅凭内部知识生成结论。
- 可解释性优先

## 一、事实题（10 题） Q8 [文件HIT5] [短语HIT5]

Q: RAG 系统自动化评估中常用的三个指标是什么？

来源: 02_rag实战指南_langchain.md | 语料中存在: True

A(要点): 上下文召回率（Context Recall）、上下文精确率（Context Precision）、答案相关性（Answer Relevance）

top-5 短语命中: ['上下文召回率', 'Context Recall', '上下文精确率', 'Context Precision', 'Answer Relevance']

top-5 短语缺失: （无）

1. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 四、进阶优化：解决 RAG 的常见陷阱 / 4. 评估体系（RAG Evaluation）
使用 RAGA

2. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 工程实践工具
常用的 RAG 系统构建工具包括 LangChain 和 LlamaIndex（完整框架），以及 FlashRAG（模块化开源

3. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 四、进阶优化：解决 RAG 的常见陷阱 / 3. 引入重排序（Reranking）
向量检索虽然快，但不够

4. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 二、RAG 的技术架构深度解析 / 4. 检索与重排序（Retrieval & Reranking）
初步

5. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / LangChain 框架：RAG 系统的技术基础
LangChain 已成为 RAG 应用开发的主流框架

6. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 一、什么是 RAG？为什么它如此重要？
RAG 的核心思想很简单：让大模型"先查资料，再回答"。传统的 R

7. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 一、什么是 RAG？为什么它如此重要？ / RAG 的核心优势
- 降低幻觉：答案基于事实依据，而非模型的

8. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 四、进阶优化：解决 RAG 的常见陷阱 / 2. 查询改写（Query Rewriting）
- HyDE

9. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 为什么需要 RAG？
大型语言模型在处理特定领域或知识密集型任务时存在很大局限性，特别是在处理超出其训练数据或需要当前信息的查询时，会产生"

10. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 五、总结与展望
RAG 技术不再追求让模型"记住"一切，而是让模型"学会"如何高效地利用外部知识。随着技术

## 一、事实题（10 题） Q9 [文件HIT5] [短语MISS] 覆盖缺口

Q: 什么是 GraphRAG？它主要擅长解决哪类问题？

来源: 03_rag五大范式与演进.md | 语料中存在: True

A(要点): 融合知识图谱的 RAG；利用实体间结构信息做更精确全面的检索，擅长全局性问题（如「数据集的主要主题是什么」）

top-5 短语命中: （无）

top-5 短语缺失: ['融合知识图谱的 RAG', '利用实体间结构信息做更精确全面的检索', '擅长全局性问题', '如「数据集的主要主题是什么」']

全库也缺失: ['融合知识图谱的 RAG', '利用实体间结构信息做更精确全面的检索', '擅长全局性问题', '如「数据集的主要主题是什么」']

1. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / GraphRAG
GraphRAG 利用实体间的结构信息，实现更精确、更全面的检索，捕捉关系知识。工作流程包括基于图形的索引（G-Index

2. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 高级 RAG（Advanced RAG）
高级 RAG 引入了具体的改进措施，以克服 Naive RAG 的局限性：

- 为了提高检索质量

3. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 发展历程
自 2021 年 RAG 技术出现之后，RAG 首先被用于 LLMs 的预训练阶段来增强语言模型，随后被用于微调与推理任务中。自 

4. (wiki_005.md)
[来源] wiki_005.md | 计算机科学 / 人工智能
这个计算机科学分支旨在创造可以解决计算问题，以及像动物和人类一样思考与交流的人造系统。无论是在理论还是应用上，都要求研究者在多个学科领域具备细致的、综合的专长，比如应用数学，逻

5. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 为什么需要 RAG？
大型语言模型在处理特定领域或知识密集型任务时存在很大局限性，特别是在处理超出其训练数据或需要当前信息的查询时，会产生"

6. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 一、什么是 RAG？为什么它如此重要？
RAG 的核心思想很简单：让大模型"先查资料，再回答"。传统的 R

7. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / 常见问题及解决方案
- 检索质量差：使用更高质量的嵌入模型（如 all-mpnet-base-v2）、调

8. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / RAG 技术概述及其重要性
传统语言模型如 GPT-4 尽管功能强大，但其知识库受限于训练数据，无法有效

9. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 一、什么是 RAG？为什么它如此重要？ / RAG 的核心优势
- 降低幻觉：答案基于事实依据，而非模型的

10. (wiki_079.md)
[来源] wiki_079.md | 人工智能 / 乐观学派
主要是Google、Facebook等AI的主要技术发展者，他们对AI持乐观看法的理由：

## 一、事实题（10 题） Q10 [文件HIT5] [短语HIT5]

Q: 用 LangChain 构建 RAG 需要哪些核心组件？

来源: 01_langchain_rag入门教程.md | 语料中存在: True

A(要点): 文档加载器、文本分割器、向量存储、文本嵌入模型、检索机制、链式处理流程

top-5 短语命中: ['文本嵌入模型', '链式处理流程']

top-5 短语缺失: （无）

1. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / LangChain 框架：RAG 系统的技术基础
LangChain 已成为 RAG 应用开发的主流框架

2. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 一、什么是 RAG？为什么它如此重要？
RAG 的核心思想很简单：让大模型"先查资料，再回答"。传统的 R

3. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 三、实战：使用 LangChain 构建 RAG 应用 / 第四步：构建问答链（QA Chain）
Con

4. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 一、什么是 RAG？为什么它如此重要？ / RAG 的核心优势
- 降低幻觉：答案基于事实依据，而非模型的

5. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 三、实战：使用 LangChain 构建 RAG 应用 / 第二步：向量化并存储
```python
fr

6. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 三、实战：使用 LangChain 构建 RAG 应用 / 第三步：构建检索器
```python
def

7. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 三、实战：使用 LangChain 构建 RAG 应用 / 代码运行逻辑分析
- 用户输入问题后，Retr

8. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 四、进阶优化：解决 RAG 的常见陷阱 / 4. 评估体系（RAG Evaluation）
使用 RAGA

9. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 三、实战：使用 LangChain 构建 RAG 应用 / 第一步：加载文档与分割
```python
f

10. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 三、实战：使用 LangChain 构建 RAG 应用 / 第四步：构建问答链（QA Chain）
```

## 二、综合题（4 题） Q11 [文件HIT5] [短语MISS] 覆盖缺口

Q: CharacterTextSplitter 和 RecursiveCharacterTextSplitter 在切分策略上有什么区别？为什么后者通常更好？

来源: 01_langchain_rag入门教程.md + 02_rag实战指南_langchain.md | 语料中存在: True

A(要点): 前者按固定字符数硬切；后者按分隔符层级（段落\n\n→句子\n→词）递归切，尽量保留语义边界；边界干净检索才准

top-5 短语命中: （无）

top-5 短语缺失: ['前者按固定字符数硬切', '后者按分隔符层级', '段落\\n\\n→句子\\n→词', '尽量保留语义边界', '边界干净检索才准']

全库也缺失: ['前者按固定字符数硬切', '后者按分隔符层级', '段落\\n\\n→句子\\n→词', '尽量保留语义边界', '边界干净检索才准']

1. (langchain_024.md)
[来源] langchain_024.md | search_engine_chat / FunctionDef metaphor_search(text, result_len, split_result, chunk_size, chu

2. (langchain_004.md)
[来源] langchain_004.md | utils / FunctionDef make_text_splitter(splitter_name, chunk_size, chunk_overlap, llm_model)
**代码

3. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / 文档分块策略优化
分块方式对检索质量有重大影响，尝试递归字符分割：

```python
from la

4. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 三、实战：使用 LangChain 构建 RAG 应用 / 第一步：加载文档与分割
```python
f

5. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / 文档处理与分块策略
# 将文档拆分成更小的块，以便更好地检索
text_splitter = Chara

6. (langchain_004.md)
[来源] langchain_004.md | utils / ClassDef KnowledgeFile / FunctionDef file2text(self, zh_title_enhance, refresh, chunk_si

7. (langchain_004.md)
[来源] langchain_004.md | utils / ClassDef KnowledgeFile / FunctionDef docs2texts(self, docs, zh_title_enhance, refresh, c

8. (langchain_004.md)
[来源] langchain_004.md | utils / ClassDef KnowledgeFile / FunctionDef file2text(self, zh_title_enhance, refresh, chunk_si

9. (langchain_004.md)
[来源] langchain_004.md | utils / ClassDef KnowledgeFile / FunctionDef docs2texts(self, docs, zh_title_enhance, refresh, c

10. (langchain_004.md)
[来源] langchain_004.md | utils / FunctionDef make_text_splitter(splitter_name, chunk_size, chunk_overlap, llm_model)
**ma

## 二、综合题（4 题） Q12 [文件HIT5] [短语MISS] 覆盖缺口

Q: RAG 技术经历了哪些范式演进？各范式的主要特点是什么？

来源: 03_rag五大范式与演进.md | 语料中存在: True

A(要点): Naive（简单三段式）→ Advanced（检索前/后优化、滑动窗口、元数据）→ Modular（模块化可重组、路由调度）→ Graph（知识图谱）→ Agentic（ReAct 动态协调、主动规划）

top-5 短语命中: （无）

top-5 短语缺失: ['→ Advanced', '检索前/后优化', '→ Modular', '模块化可重组', '→ Graph', '→ Agentic', 'ReAct 动态协调']

全库也缺失: ['→ Advanced', '检索前/后优化', '→ Modular', '模块化可重组', '→ Graph', '→ Agentic', 'ReAct 动态协调']

1. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 发展历程
自 2021 年 RAG 技术出现之后，RAG 首先被用于 LLMs 的预训练阶段来增强语言模型，随后被用于微调与推理任务中。自 

2. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / GraphRAG
GraphRAG 利用实体间的结构信息，实现更精确、更全面的检索，捕捉关系知识。工作流程包括基于图形的索引（G-Index

3. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 模块化 RAG（Modular RAG）
模块化 RAG 架构超越了前两种范式，具有更强的适应性和多功能性。它将复杂的 RAG 系统分解为独

4. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 高级 RAG（Advanced RAG）
高级 RAG 引入了具体的改进措施，以克服 Naive RAG 的局限性：

- 为了提高检索质量

5. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / RAG 的起源
RAG 模型将预先训练的参数记忆（预训练语言模型）和非参数记忆（通过检索机制访问的外部知识库，如维基百科的密集向量索引）结合

6. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / Agentic RAG
Agentic RAG 将 ReAct 的推理能力与 Agent 的任务执行能力相结合，创建一个动态和自适应的系统。

7. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 工程实践工具
常用的 RAG 系统构建工具包括 LangChain 和 LlamaIndex（完整框架），以及 FlashRAG（模块化开源

8. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 为什么需要 RAG？
大型语言模型在处理特定领域或知识密集型任务时存在很大局限性，特别是在处理超出其训练数据或需要当前信息的查询时，会产生"

9. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / RAG 简单流程与总览
应用于问答的 RAG 过程主要包括 3 个步骤：

1. 索引：文档被分割成块，编码成向量，存储在向量数据库中。
2

10. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式
> 来源：https://cloud.tencent.cn/developer/article/2498870

## 二、综合题（4 题） Q13 [文件HIT5] [短语HIT5]

Q: 为什么说「检索质量决定 RAG 回答的上限」？有哪些手段改进检索？

来源: 02_rag实战指南_langchain.md | 语料中存在: True

A(要点): 检索到的块不相关，生成阶段无法补救；手段包括重排序（Reranker）、查询改写（HyDE）、多跳检索、更高质量的嵌入模型

top-5 短语命中: ['更高质量的嵌入模型']

top-5 短语缺失: ['检索到的块不相关', '生成阶段无法补救', '手段包括重排序', 'Reranker']

全库也缺失: ['检索到的块不相关', '生成阶段无法补救', '手段包括重排序']

1. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 四、进阶优化：解决 RAG 的常见陷阱 / 2. 查询改写（Query Rewriting）
- HyDE

2. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 四、进阶优化：解决 RAG 的常见陷阱 / 4. 评估体系（RAG Evaluation）
使用 RAGA

3. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / 常见问题及解决方案
- 检索质量差：使用更高质量的嵌入模型（如 all-mpnet-base-v2）、调

4. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 二、RAG 的技术架构深度解析 / 1. 文档加载与分割（Loading & Splitting）
原始数

5. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 高级 RAG（Advanced RAG）
高级 RAG 引入了具体的改进措施，以克服 Naive RAG 的局限性：

- 为了提高检索质量

6. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 四、进阶优化：解决 RAG 的常见陷阱 / 3. 引入重排序（Reranking）
向量检索虽然快，但不够

7. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 一、什么是 RAG？为什么它如此重要？
RAG 的核心思想很简单：让大模型"先查资料，再回答"。传统的 R

8. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 四、进阶优化：解决 RAG 的常见陷阱 / 1. 改进文本分割（Chunking Strategy）
- 

9. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 二、RAG 的技术架构深度解析 / 4. 检索与重排序（Retrieval & Reranking）
初步

10. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / RAG 技术概述及其重要性
传统语言模型如 GPT-4 尽管功能强大，但其知识库受限于训练数据，无法有效

## 二、综合题（4 题） Q14 [文件HIT5] [短语HIT5]

Q: 相比纯思维链（CoT），ReAct 解决了 LLM 的哪些问题？

来源: 04_react核心范式详解.md | 语料中存在: True

A(要点): 事实幻觉（FEVER 上幻觉率 8.2% vs CoT 23.5%）、策略僵化、决策不可解释、多场景适配成本高

top-5 短语命中: ['决策不可解释']

top-5 短语缺失: ['FEVER 上幻觉率 8.2% vs CoT 23.5%', '多场景适配成本高']

全库也缺失: ['FEVER 上幻觉率 8.2% vs CoT 23.5%', '多场景适配成本高']

1. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / ReAct 解决了什么问题？
- 破解"事实幻觉"难题：将推理过程锚定到真实数据。实验数据显示，在 FEVER 事实核查任务中，

2. (05_react手写实现指南.md)
[来源] 05_react手写实现指南.md | ReAct 代理裸机编码指南：不依赖任何框架的 LLM 自主决策实现 / 二、为什么需要 ReAct？突破 LLM 的固有局限
- 传统 LLM 依赖预训练知识，无法获取实时数据 → ReA

3. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / 什么是 ReAct？
ReAct = Reasoning（推理）+ Acting（行动），是一种让语言模型通过与外部工具、环境动

4. (05_react手写实现指南.md)
[来源] 05_react手写实现指南.md | ReAct 代理裸机编码指南：不依赖任何框架的 LLM 自主决策实现 / 六、优化：超越基础实现
- 短路机制：当工具返回明确结果时跳过冗余思考，提前终止循环
- 错误回退：工具调用失败时尝

5. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / ReAct 的局限
ReAct 依赖 LLM 的上下文窗口存储历史 TAO 轨迹，当任务步骤超过 10 轮时，需通过"裁剪-摘要

6. (05_react手写实现指南.md)
[来源] 05_react手写实现指南.md | ReAct 代理裸机编码指南：不依赖任何框架的 LLM 自主决策实现 / 一、ReAct 模式：AI 代理的"思考-行动"循环
ReAct（Reasoning + Action）是一种让大语

7. (05_react手写实现指南.md)
[来源] 05_react手写实现指南.md | ReAct 代理裸机编码指南：不依赖任何框架的 LLM 自主决策实现 / 五、Prompt 工程：驱动推理的核心
经典模板：

```
你是一个自主代理，请通过以下步骤解决问题：
1. 思考

8. (05_react手写实现指南.md)
[来源] 05_react手写实现指南.md | ReAct 代理裸机编码指南：不依赖任何框架的 LLM 自主决策实现 / 七、与框架的共生关系
原生实现：完全掌控底层逻辑，适合研究/定制化场景，但需自行处理并发/监控。

框架（CrewA

9. (05_react手写实现指南.md)
[来源] 05_react手写实现指南.md | ReAct 代理裸机编码指南：不依赖任何框架的 LLM 自主决策实现 / 三、ReAct 代理的工作原理
ReAct 代理以"思考 → 行动 → 观察"的循环方式运行，重复进行直到找到解决方

10. (05_react手写实现指南.md)
[来源] 05_react手写实现指南.md | ReAct 代理裸机编码指南：不依赖任何框架的 LLM 自主决策实现 / 四、工具调用：代理的"双手"
工具是实现行动的关键，需满足 3 个设计原则：

- 原子性：每个工具只做一件事
- 

## 三、无答案题（4 题，测幻觉防线） Q15 [文件MISS] [短语MISS] 覆盖缺口

Q: 请介绍 OpenAI GPT-5 模型的参数规模和发布日期。

来源: （无来源/语料无） | 语料中存在: None

A(要点): 语料中没有 → 应回答「资料中没有相关信息」

top-5 短语命中: （无）

top-5 短语缺失: ['语料中没有 → 应回答「资料中没有相关信息」']

全库也缺失: ['语料中没有 → 应回答「资料中没有相关信息」']

1. (langchain_003.md)
[来源] langchain_003.md | utils / FunctionDef get_OpenAI(model_name, temperature, max_tokens, streaming, echo, callbacks, 

2. (langchain_018.md)
[来源] langchain_018.md | api / 常用 API 接口调用方式 / RAG 接口 （/knowledge_base/chat/compleitons）
相比于 /chat/chat/completions 接口，本接

3. (langchain_003.md)
[来源] langchain_003.md | utils / FunctionDef get_ChatOpenAI(model_name, temperature, max_tokens, streaming, callbacks, ve

4. (langchain_018.md)
[来源] langchain_018.md | api / 常用 API 接口调用方式 / RAG 接口 （/knowledge_base/chat/compleitons）
'出处 [2] [test_files/test.txt](ht

5. (langchain_003.md)
[来源] langchain_003.md | utils / FunctionDef get_ChatOpenAI(model_name, temperature, max_tokens, streaming, callbacks, ve

6. (langchain_017.md)
[来源] langchain_017.md | README / 概述
![](docs/img/langchain_chatchat_0.3.0.png)

✅ 本项目支持市面上主流的开源 LLM、 Embedding 模型与向量数据库，

7. (langchain_003.md)
[来源] langchain_003.md | utils / FunctionDef get_OpenAI(model_name, temperature, max_tokens, streaming, echo, callbacks, 

8. (langchain_007.md)
[来源] langchain_007.md | startup / FunctionDef run_model_worker(model_name, controller_address, log_level, q, started_eve

9. (langchain_003.md)
[来源] langchain_003.md | utils / FunctionDef load_local_embeddings(model, device)
**注意**:
- 使用此函数时，需要确保`model`参数对应的嵌入模型已经

10. (langchain_017.md)
[来源] langchain_017.md | README / 功能介绍 / 已支持的模型部署框架与模型
除上述本地模型加载框架外，项目中也为可接入在线 API 的 [One API](https://github.com/songqua

## 三、无答案题（4 题，测幻觉防线） Q16 [文件MISS] [短语MISS] 覆盖缺口

Q: 今天（2026年8月5日）的 AI 行业新闻有哪些？

来源: （无来源/语料无） | 语料中存在: None

A(要点): 语料中没有实时信息 → 应回答「资料中没有相关信息」

top-5 短语命中: （无）

top-5 短语缺失: ['语料中没有实时信息 → 应回答「资料中没有相关信息」']

全库也缺失: ['语料中没有实时信息 → 应回答「资料中没有相关信息」']

1. (wiki_079.md)
[来源] wiki_079.md | 人工智能 / 伦理管理
史蒂芬·霍金、比尔盖兹、埃隆·马斯克、Jaan Tallinn以及Nick Bostrom等人都对于人工智慧技术的未来公开表示忧心，人工智慧若在许多方面超越人类智慧水平的智能、不

2. (wiki_079.md)
[来源] wiki_079.md | 人工智能 / 经济冲击
2017年6月份马云在美国底特律举行「链结世界」（Gateway 17）产业大会，会上提出人工智慧可能导致第三次世界大战，因为前两次产业革命都导致两次大战，战争原因并非这些创新发

3. (wiki_079.md)
[来源] wiki_079.md | 人工智能 / 发展史
2016年，在机器学习会议上，与技术滥用成为突出话题；相关论文发表数量急剧增加，研究经费随之提供，众多研究人员转而聚焦这些议题。对齐问题逐渐成为学术探讨的重要议题。
2010年代末

4. (wiki_079.md)
[来源] wiki_079.md | 人工智能 / 经济冲击
CNN财经网数字媒体未来学家、美国在线等纷纷预测一些即将被机器人取代的职业，日本野村综合研究所也与英国牛津大学的研究学者共同调查指出，10至20年后，日本有49%的职业（235种

5. (wiki_079.md)
[来源] wiki_079.md | 人工智能 / 发展史
20世纪80年代初期，人工智能研究因专家系统的商业成功而再次活跃， 一种人工智能程序，旨在模拟人类专家的知识和分析技巧。到了1985年，AI市场估值超过10亿美元。与此同时，日本的

6. (wiki_079.md)
[来源] wiki_079.md | 人工智能 / 乐观学派
主要是Google、Facebook等AI的主要技术发展者，他们对AI持乐观看法的理由：

7. (langchain_017.md)
[来源] langchain_017.md | README / 项目里程碑
+ `2023年4月`: `Langchain-ChatGLM 0.1.0` 发布，支持基于 ChatGLM-6B 模型的本地知识库问答。
+ `2023年8月`

8. (thucnews_0076.md)
[来源] thucnews_0076.md | 80后女星引领时尚风潮(组图)
# 80后女星引领时尚风潮(组图)

范冰冰 1981年9月16日
黄圣依 1983年2月11日
刘亦菲 1986年8月25日
孙俪 1982年9月26日
李小

9. (thucnews_0140.md)
[来源] thucnews_0140.md | 1月28日美股专家坐堂实录
网友[匿名]问： 老师你好!AIG有投资前景吗(2009-01-28 20:41:57)

10. (wiki_079.md)
[来源] wiki_079.md | 人工智能 / AI对人类的威胁
此议题目前分成两个学派：

## 三、无答案题（4 题，测幻觉防线） Q17 [文件MISS] [短语MISS] 覆盖缺口

Q: 如何调用 DeepSeek 的 API 完成一次对话？

来源: （无来源/语料无） | 语料中存在: None

A(要点): 语料只讲 RAG/ReAct 原理，没有 DeepSeek API 代码 → 应回答「资料中没有相关信息」

top-5 短语命中: （无）

top-5 短语缺失: ['语料只讲 RAG/ReAct 原理', '没有 DeepSeek API 代码 → 应回答「资料中没有相关信息」']

全库也缺失: ['语料只讲 RAG/ReAct 原理', '没有 DeepSeek API 代码 → 应回答「资料中没有相关信息」']

1. (langchain_018.md)
[来源] langchain_018.md | api / 常用 API 接口调用方式 / 通用对话接口（/chat/chat/completions）
import requests
    response = requests.pos

2. (langchain_018.md)
[来源] langchain_018.md | api / 常用 API 接口调用方式 / 通用对话接口（/chat/chat/completions）
最主要的对话接口，兼容 openai sdk 格式。它支持以下3种对话模式：  
- 

3. (langchain_018.md)
[来源] langchain_018.md | api / 常用 API 接口调用方式 / 通用对话接口（/chat/chat/completions）
输出中包含一个 `message_type` 字段，代表输出内容的类型，主要用于前端渲

4. (langchain_018.md)
[来源] langchain_018.md | api / 常用 API 接口调用方式 / 通用对话接口（/chat/chat/completions）
调用示例：
- 纯 LLM 对话：
    ```python3
    base_u

5. (langchain_021.md)
[来源] langchain_021.md | dialogue / FunctionDef dialogue_page(api, is_lite)
**dialogue_page**: 此函数用于处理对话页面的逻辑，包括初始化会话、处理用

6. (langchain_018.md)
[来源] langchain_018.md | api / 常用 API 接口调用方式 / 通用对话接口（/chat/chat/completions）
"messages": [
            {"role": "user", 

7. (langchain_018.md)
[来源] langchain_018.md | api / 常用 API 接口调用方式 / 通用对话接口（/chat/chat/completions）
data: {"id": "chatdee106c6-42e6-41cf-b2df-6

8. (langchain_018.md)
[来源] langchain_018.md | api / 常用 API 接口调用方式 / 通用对话接口（/chat/chat/completions）
```python3
    base_url = "http://127.0.0.1

9. (langchain_018.md)
[来源] langchain_018.md | api / 常用 API 接口调用方式 / 通用对话接口（/chat/chat/completions）
to the given question is 85. \n\nJSON Objec

10. (langchain_018.md)
[来源] langchain_018.md | api / 常用 API 接口调用方式 / 通用对话接口（/chat/chat/completions）
输入参数：与 openai sdk 参数一致。针对 chatchat 做了以下优化： 

## 三、无答案题（4 题，测幻觉防线） Q18 [文件MISS] [短语MISS] 覆盖缺口

Q: 什么是多模态 RAG？请给出具体实现方案。

来源: （无来源/语料无） | 语料中存在: None

A(要点): 语料没有多模态 RAG 的实现细节 → 应回答「资料中没有相关信息」

top-5 短语命中: （无）

top-5 短语缺失: ['语料没有多模态 RAG 的实现细节 → 应回答「资料中没有相关信息」']

全库也缺失: ['语料没有多模态 RAG 的实现细节 → 应回答「资料中没有相关信息」']

1. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 模块化 RAG（Modular RAG）
模块化 RAG 架构超越了前两种范式，具有更强的适应性和多功能性。它将复杂的 RAG 系统分解为独

2. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / RAG 的起源
RAG 模型将预先训练的参数记忆（预训练语言模型）和非参数记忆（通过检索机制访问的外部知识库，如维基百科的密集向量索引）结合

3. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / Agentic RAG
Agentic RAG 将 ReAct 的推理能力与 Agent 的任务执行能力相结合，创建一个动态和自适应的系统。

4. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 为什么需要 RAG？
大型语言模型在处理特定领域或知识密集型任务时存在很大局限性，特别是在处理超出其训练数据或需要当前信息的查询时，会产生"

5. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 一、什么是 RAG？为什么它如此重要？
RAG 的核心思想很简单：让大模型"先查资料，再回答"。传统的 R

6. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / GraphRAG
GraphRAG 利用实体间的结构信息，实现更精确、更全面的检索，捕捉关系知识。工作流程包括基于图形的索引（G-Index

7. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 工程实践工具
常用的 RAG 系统构建工具包括 LangChain 和 LlamaIndex（完整框架），以及 FlashRAG（模块化开源

8. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / LangChain 框架：RAG 系统的技术基础
LangChain 已成为 RAG 应用开发的主流框架

9. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 发展历程
自 2021 年 RAG 技术出现之后，RAG 首先被用于 LLMs 的预训练阶段来增强语言模型，随后被用于微调与推理任务中。自 

10. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 高级 RAG（Advanced RAG）
高级 RAG 引入了具体的改进措施，以克服 Naive RAG 的局限性：

- 为了提高检索质量

## 四、概念辨析（2 题） Q19 [文件HIT5] [短语MISS] 覆盖缺口

Q: ReAct 中 Thought、Act、Observe 为什么要按顺序循环？少了 Observe 会怎样？

来源: 04_react核心范式详解.md + 05_react手写实现指南.md | 语料中存在: True

A(要点): 顺序构成「推理→执行→反馈」闭环；少了 Observe 就没有真实数据支撑，推理会退回凭记忆，幻觉无法被抑制

top-5 短语命中: （无）

top-5 短语缺失: ['顺序构成「推理→执行→反馈」闭环', '少了 Observe 就没有真实数据支撑', '推理会退回凭记忆', '幻觉无法被抑制']

全库也缺失: ['顺序构成「推理→执行→反馈」闭环', '少了 Observe 就没有真实数据支撑', '推理会退回凭记忆', '幻觉无法被抑制']

1. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / ReAct 工作原理 / 循环迭代阶段
每轮迭代严格遵循"推理-行动-观察"的顺序：

1. Thought（推理）：模型基于"

2. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / 核心思想：模拟人类认知的 TAO 闭环
ReAct 将"Thought（推理）→Act（行动）→Observe（观察）"抽象为 

3. (05_react手写实现指南.md)
[来源] 05_react手写实现指南.md | ReAct 代理裸机编码指南：不依赖任何框架的 LLM 自主决策实现 / 三、ReAct 代理的工作原理
ReAct 代理以"思考 → 行动 → 观察"的循环方式运行，重复进行直到找到解决方

4. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / 什么是 ReAct？
ReAct = Reasoning（推理）+ Acting（行动），是一种让语言模型通过与外部工具、环境动

5. (05_react手写实现指南.md)
[来源] 05_react手写实现指南.md | ReAct 代理裸机编码指南：不依赖任何框架的 LLM 自主决策实现 / 五、Prompt 工程：驱动推理的核心
经典模板：

```
你是一个自主代理，请通过以下步骤解决问题：
1. 思考

6. (05_react手写实现指南.md)
[来源] 05_react手写实现指南.md | ReAct 代理裸机编码指南：不依赖任何框架的 LLM 自主决策实现 / 二、为什么需要 ReAct？突破 LLM 的固有局限
- 传统 LLM 依赖预训练知识，无法获取实时数据 → ReA

7. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / 极简代码框架
def react_core_loop(task, tools, llm, max_steps=6):
    "

8. (05_react手写实现指南.md)
[来源] 05_react手写实现指南.md | ReAct 代理裸机编码指南：不依赖任何框架的 LLM 自主决策实现 / 六、优化：超越基础实现
- 短路机制：当工具返回明确结果时跳过冗余思考，提前终止循环
- 错误回退：工具调用失败时尝

9. (05_react手写实现指南.md)
[来源] 05_react手写实现指南.md | ReAct 代理裸机编码指南：不依赖任何框架的 LLM 自主决策实现 / 一、ReAct 模式：AI 代理的"思考-行动"循环
ReAct（Reasoning + Action）是一种让大语

10. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / 四大设计理念
- 环境锚定原则：强制模型在涉及事实性问题时优先调用外部工具获取证据，禁止仅凭内部知识生成结论。
- 可解释性优先

## 四、概念辨析（2 题） Q20 [文件HIT5] [短语MISS] 覆盖缺口

Q: 「回答正确」和「回答有依据」是一回事吗？RAG 评估里怎么区分它们？

来源: 02_rag实战指南_langchain.md | 语料中存在: True

A(要点): 不是；正确可能来自模型内部知识，有依据指关键事实能从检索资料中找到出处；评估时分别用答案相关性（答对没）和上下文召回/精确率（依据够不够）衡量

top-5 短语命中: （无）

top-5 短语缺失: ['正确可能来自模型内部知识', '有依据指关键事实能从检索资料中找到出处', '评估时分别用答案相关性', '和上下文召回/精确率']

全库也缺失: ['正确可能来自模型内部知识', '有依据指关键事实能从检索资料中找到出处', '评估时分别用答案相关性', '和上下文召回/精确率']

1. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 四、进阶优化：解决 RAG 的常见陷阱 / 4. 评估体系（RAG Evaluation）
使用 RAGA

2. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 一、什么是 RAG？为什么它如此重要？ / RAG 的核心优势
- 降低幻觉：答案基于事实依据，而非模型的

3. (langchain_003.md)
[来源] langchain_003.md | utils / ClassDef ChatMessage / ClassDef Config
- "question" 键对应的值是一个字符串，表示提出的问题。
- "response" 键对

4. (langchain_003.md)
[来源] langchain_003.md | utils / ClassDef ChatMessage
- `question` 属性定义了提问的文本内容，是一个字符串类型。
- `response` 属性定义了对提问的回答，同样是一个字

5. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / RAG 技术概述及其重要性
传统语言模型如 GPT-4 尽管功能强大，但其知识库受限于训练数据，无法有效

6. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 一、什么是 RAG？为什么它如此重要？
RAG 的核心思想很简单：让大模型"先查资料，再回答"。传统的 R

7. (langchain_003.md)
[来源] langchain_003.md | utils / ClassDef ChatMessage / ClassDef Config
**Config**: Config 类的功能是提供一个示例配置，用于说明如何处理和响应工伤保险相

8. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 四、进阶优化：解决 RAG 的常见陷阱 / 2. 查询改写（Query Rewriting）
- HyDE

9. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 四、进阶优化：解决 RAG 的常见陷阱 / 3. 引入重排序（Reranking）
向量检索虽然快，但不够

10. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / GraphRAG
GraphRAG 利用实体间的结构信息，实现更精确、更全面的检索，捕捉关系知识。工作流程包括基于图形的索引（G-Index

## 五、百科（6 题，语料：中文维基） Q21 [文件HIT5] [短语HIT5]

Q: 数学属于哪一类学科？它的核心研究对象是什么？

来源: wiki_001.md | 语料中存在: True

A(要点): 数学属于形式科学；研究数量、结构以及空间等概念及其变化

top-5 短语命中: ['结构以及空间等概念及其变化']

top-5 短语缺失: ['数学属于形式科学']

全库也缺失: ['数学属于形式科学']

1. (wiki_001.md)
[来源] wiki_001.md | 数学 / 形成、纯数学与应用数学及美学
每当有涉及数量、结构、空间及变化等方面的问题时，通常就需要用到数学去解决问题，而这往往也拓展了数学的研究范畴。一开始，数学的运用可见于贸易、土地测量及之后的天文学

2. (wiki_001.md)
[来源] wiki_001.md | 数学
# 数学

数学是研究数量、结构以及空间等概念及其变化的一门学科，属于形式科学的一种。数学利用抽象化和逻辑推理，从计数、计算、量度、对物体形状及运动的观察发展而成。数学家们拓展这些概念，以公式化新

3. (wiki_001.md)
[来源] wiki_001.md | 数学 / 数学的各领域
如上所述，数学主要的学科最先产生于商业上计算的需要、了解数字间的关系、测量土地及预测天文事件。这四种需要大致地与数量、结构、空间及变化（即算术、代数、几何及分析）等数学上广泛的子

4. (wiki_001.md)
[来源] wiki_001.md | 数学 / 历史
在最初有历史记录的时候，数学内的主要原理是为了做税务和贸易等相关计算，为了解数字间的关系，为了测量土地，以及为了预测天文事件而形成的。这些可以简单地被概括为数学对数量、结构、空间及时间方

5. (wiki_001.md)
[来源] wiki_001.md | 数学 / 词源
西方语言中“数学”（μαθηματικά）一词源自于古希腊语的μάθημα（máthēma），其有“学习”、“学问”、“科学”，还有个较狭义且技术性的意思－「数学研究」，即使在其语源内。

6. (wiki_001.md)
[来源] wiki_001.md | 数学 / 结构
许多如数及函数的集合等数学物件都有著内含的结构。这些物件的结构性质被探讨于群、环、-{zh-cn:域;zh-tw:体}-等抽象系统中，该些物件事实上也就是这样的系统。此为代数的领域。在此

7. (wiki_001.md)
[来源] wiki_001.md | 数学 / 数学作为科学
数学家对此的态度并不一致。一些研究应用数学的数学家觉得他们是科学家，而那些研究纯数学的数学家则时常觉得他们是在一门较接近逻辑的领域内工作，且因此基本上是个哲学家。许多数学家认为称

8. (wiki_088.md)
[来源] wiki_088.md | 数论
# 数论

数论（Number theory）是纯粹数学的分支之一，主要研究整数的性质，被称为「最纯」的数学领域。

9. (wiki_001.md)
[来源] wiki_001.md | 数学 / 数学作为科学
另一观点则为某些科学领域（如理论物理）是其公理为尝试著符合现实的数学。而事实上，理论物理学家齐曼（John Ziman）即认为科学是一种公众知识，因此亦包含著数学。在任何的情况下

10. (wiki_001.md)
[来源] wiki_001.md | 数学 / 数学作为科学
卡尔·弗里德里希·高斯称数学为「科学的皇后」。在拉丁原文"Regina Scientiarum"，以及其德语"Königin der Wissenschaften"中，对应于「科

## 五、百科（6 题，语料：中文维基） Q22 [文件HIT5] [短语HIT5]

Q: 西方语言中「数学」一词源自希腊语的哪个词？其含义是什么？

来源: wiki_001.md | 语料中存在: True

A(要点): 源自古希腊语 μάθημα（máthēma），意为学习、学问、科学

top-5 短语命中: ['máthēma']

top-5 短语缺失: ['源自古希腊语 μάθημα']

全库也缺失: ['源自古希腊语 μάθημα']

1. (wiki_001.md)
[来源] wiki_001.md | 数学 / 词源
西方语言中“数学”（μαθηματικά）一词源自于古希腊语的μάθημα（máthēma），其有“学习”、“学问”、“科学”，还有个较狭义且技术性的意思－「数学研究」，即使在其语源内。

2. (wiki_001.md)
[来源] wiki_001.md | 数学 / 历史
数学有着久远的历史。它被认为起源于人类早期的生产活动：中国古代的六艺之一就有「数」，数学一词在西方有希腊语词源μαθηματικός（mathematikós），意思是“学问的基础”，源

3. (wiki_001.md)
[来源] wiki_001.md | 数学 / 数学作为科学
卡尔·弗里德里希·高斯称数学为「科学的皇后」。在拉丁原文"Regina Scientiarum"，以及其德语"Königin der Wissenschaften"中，对应于「科

4. (wiki_010.md)
[来源] wiki_010.md | 经济学 / 词源
英文中的经济学，即“Economics”一词源于希腊文的“”，原意是「节约的人，负责管理家庭琐事的人」的意思；而这个词是另一个希腊名词“οικονομικός”转换写法而来，意思是“调

5. (wiki_088.md)
[来源] wiki_088.md | 数论 / 中世纪
在中世纪早期，除了1175年至1200年住在北非和君士坦丁堡的数学家斐波那契有关等差数列的研究外，西欧在数论上没有什么进展。
中世纪数论主要是指15-16世纪由费马、梅森、欧拉、高斯、

6. (wiki_001.md)
[来源] wiki_001.md | 数学 / 历史
在最初有历史记录的时候，数学内的主要原理是为了做税务和贸易等相关计算，为了解数字间的关系，为了测量土地，以及为了预测天文事件而形成的。这些可以简单地被概括为数学对数量、结构、空间及时间方

7. (wiki_001.md)
[来源] wiki_001.md | 数学
# 数学

数学是研究数量、结构以及空间等概念及其变化的一门学科，属于形式科学的一种。数学利用抽象化和逻辑推理，从计数、计算、量度、对物体形状及运动的观察发展而成。数学家们拓展这些概念，以公式化新

8. (wiki_088.md)
[来源] wiki_088.md | 数论 / 古代
数论早期也称为算术，而算术一词则表示「基本运算」，在现代数论诞生前，早期铺垫有三大内容：

9. (drcd_049.md)
[来源] drcd_049.md | 函数
# 函数

函数这个数学名词是莱布尼兹在1694年开始使用的，用来描述跟曲线相关的一个量，如曲线的斜率或者曲线上的某一点。莱布尼兹所指的函数现在被称作可导函数，数学家之外的普通人一般接触到的函数即

10. (wiki_024.md)
[来源] wiki_024.md | 心理学 / 词源
西语中的“心理学”（psychology）一词由希腊语词根，「灵魂」（gre|ψυχή）和「研究」（gre|λόγος）所组成，最早由克罗地亚诗人马尔科·马鲁利奇使用。
「心理学」汉译

## 五、百科（6 题，语料：中文维基） Q23 [文件HIT5] [短语HIT5]

Q: 汉字「数学」一词大约产生于什么时期？哪一年经确认表示今天意义上的数学含义？

来源: wiki_001.md | 语料中存在: True

A(要点): 大约产生于中国宋元时期；1939年经中国数学名词审查委员会确认

top-5 短语命中: ['大约产生于中国宋元时期']

top-5 短语缺失: ['1939年经中国数学名词审查委员会确认']

全库也缺失: ['1939年经中国数学名词审查委员会确认']

1. (wiki_001.md)
[来源] wiki_001.md | 数学 / 词源
西方语言中“数学”（μαθηματικά）一词源自于古希腊语的μάθημα（máthēma），其有“学习”、“学问”、“科学”，还有个较狭义且技术性的意思－「数学研究」，即使在其语源内。

2. (wiki_001.md)
[来源] wiki_001.md | 数学 / 历史
数学有着久远的历史。它被认为起源于人类早期的生产活动：中国古代的六艺之一就有「数」，数学一词在西方有希腊语词源μαθηματικός（mathematikós），意思是“学问的基础”，源

3. (wiki_001.md)
[来源] wiki_001.md | 数学 / 历史
在最初有历史记录的时候，数学内的主要原理是为了做税务和贸易等相关计算，为了解数字间的关系，为了测量土地，以及为了预测天文事件而形成的。这些可以简单地被概括为数学对数量、结构、空间及时间方

4. (wiki_088.md)
[来源] wiki_088.md | 数论 / 古代
数论早期也称为算术，而算术一词则表示「基本运算」，在现代数论诞生前，早期铺垫有三大内容：

5. (wiki_001.md)
[来源] wiki_001.md | 数学
# 数学

数学是研究数量、结构以及空间等概念及其变化的一门学科，属于形式科学的一种。数学利用抽象化和逻辑推理，从计数、计算、量度、对物体形状及运动的观察发展而成。数学家们拓展这些概念，以公式化新

6. (wiki_001.md)
[来源] wiki_001.md | 数学 / 符号、语言与精确性
我们现今所使用的大部分数学符号在16世纪后才被发明出来的。在此之前，数学以文字的形式书写出来，这种形式会限制了数学的发展。现今的符号使得数学对于专家而言更容易掌握，但初学者

7. (wiki_001.md)
[来源] wiki_001.md | 数学 / 形成、纯数学与应用数学及美学
每当有涉及数量、结构、空间及变化等方面的问题时，通常就需要用到数学去解决问题，而这往往也拓展了数学的研究范畴。一开始，数学的运用可见于贸易、土地测量及之后的天文学

8. (wiki_001.md)
[来源] wiki_001.md | 数学 / 数学的各领域
如上所述，数学主要的学科最先产生于商业上计算的需要、了解数字间的关系、测量土地及预测天文事件。这四种需要大致地与数量、结构、空间及变化（即算术、代数、几何及分析）等数学上广泛的子

9. (wiki_001.md)
[来源] wiki_001.md | 数学 / 数学作为科学
卡尔·弗里德里希·高斯称数学为「科学的皇后」。在拉丁原文"Regina Scientiarum"，以及其德语"Königin der Wissenschaften"中，对应于「科

10. (wiki_001.md)
[来源] wiki_001.md | 数学 / 形成、纯数学与应用数学及美学
如同大多数的研究领域，科学知识的爆发导致了数学的专业化。主要的分歧为纯数学和应用数学。在应用数学内，又被分成两大领域，并且变成了它们自身的学科——统计学和电脑科学

## 五、百科（6 题，语料：中文维基） Q24 [文件HIT5] [短语HIT5]

Q: 哲学研究哪些基本问题？其思考方式有何独特之处？

来源: wiki_002.md | 语料中存在: True

A(要点): 存在、知识、价值、理智、心灵、语言、人生、道德等；以理性论证为基础

top-5 短语命中: ['以理性论证为基础']

top-5 短语缺失: （无）

1. (wiki_002.md)
[来源] wiki_002.md | 哲学
# 哲学

哲学是研究普遍的、基本问题的学科，包括存在、知识、价值、理智、心灵、语言、人生、道德等领域。哲学与其他学科不同之处在于哲学有独特之思考方式，例如批判的方式、通常是系统化的方法，并以理性

2. (wiki_002.md)
[来源] wiki_002.md | 哲学 / 研究基础
古希腊哲学家经常提出问题，他们所提出的问题大概可以归类为三类，这三类问题分别形成了哲学的基础学科——分别是形而上学、伦理学、认识论 。
现代哲学上出现"不要求精确理由"之哲学理论，例

3. (wiki_002.md)
[来源] wiki_002.md | 哲学 / 前苏格拉底时期
公元前6世纪末，以毕达哥拉斯为主的毕达哥拉斯学派所主张的哲学与前述的观点既相近又有不同。罗马古代的历史上记载毕达哥拉斯第一个称自己为哲学家，或者说是爱智慧。他认为“一切都是数字

4. (wiki_002.md)
[来源] wiki_002.md | 哲学 / 前苏格拉底时期
在公元前6世纪的希腊，西方哲学就从古代神话和诗歌中脱颖而出，逐步开始对宇宙的组成以及本源的思考而开始了独立发展。前苏格拉底时期的自然派哲学家们多关注自然界，被认为是西方最早的哲

5. (wiki_002.md)
[来源] wiki_002.md | 哲学 / 古典希腊时期
在古典希腊时期西方哲学方法的关键特质被建立：依靠诉诸理性和论证，通过一种批判性的方法来接受或建立观点。这包括苏格拉底被称为苏格拉底反诘法或“反驳论证”方法的辩证法，他主要用其来检

6. (wiki_002.md)
[来源] wiki_002.md | 哲学 / 历史
很多人类社群思考过哲学问题并且互相学习建立了各种哲学流派。
东方哲学是通过每个地区的历史时期来组织的。西方哲学一般可以分为三个或更多时期，最重要的是古典哲学、中世纪哲学和近代哲学。

7. (wiki_011.md)
[来源] wiki_011.md | 政治学 / 政治哲学
传统的政治哲学研究政治问题主要从哲学思辨的角度，从形而上的角度探讨政治生活中的最高准则，民主、正义、自由、平等等价值取向和相应的政体设计是其研究的重点。大多数政治学家一般先通过先验

8. (wiki_002.md)
[来源] wiki_002.md | 哲学 / 哲学的定义
哲学家们对哲学本身的定义存在分歧。没有共同的共识，这归因于哲学本身的性质是一个开放的哲学问题。许多伟大的哲学家，如柏拉图、黑格尔等，对问题“什么是哲学？”提出了答案，但这些答案在今

9. (wiki_002.md)
[来源] wiki_002.md | 哲学 / 主分支
哲学可以分为很多不同的分支，主要包括形而上学、知识论、伦理学、逻辑学和美学。

10. (wiki_002.md)
[来源] wiki_002.md | 哲学 / 黑格尔
他认为，为了达到这个“绝对精神”，需要经过三个阶段，从逻辑、自然到精神，即是从思维到存在，再到两者统一的过程，从而完成他的统一论。
就此，社会和历史的现象，便被赋予一种在哲学史上还是崭

## 五、百科（6 题，语料：中文维基） Q25 [文件HIT5] [短语HIT5]

Q: 现代意义上的哲学主要与哪些学科相关？

来源: wiki_002.md | 语料中存在: True

A(要点): 形而上学、认识论、伦理学和美学

top-5 短语命中: ['伦理学和美学']

top-5 短语缺失: （无）

1. (wiki_002.md)
[来源] wiki_002.md | 哲学
# 哲学

哲学是研究普遍的、基本问题的学科，包括存在、知识、价值、理智、心灵、语言、人生、道德等领域。哲学与其他学科不同之处在于哲学有独特之思考方式，例如批判的方式、通常是系统化的方法，并以理性

2. (wiki_002.md)
[来源] wiki_002.md | 哲学 / 研究基础
古希腊哲学家经常提出问题，他们所提出的问题大概可以归类为三类，这三类问题分别形成了哲学的基础学科——分别是形而上学、伦理学、认识论 。
现代哲学上出现"不要求精确理由"之哲学理论，例

3. (wiki_002.md)
[来源] wiki_002.md | 哲学 / 后古典现代哲学
分析哲学：
实证主义：
新康德主义：
逻辑实证主义：
语言哲学：
现象学：
唯物论：
新托马斯主义：

4. (wiki_002.md)
[来源] wiki_002.md | 哲学 / 现代哲学（19-20世纪）
从19世纪中叶开始，西方哲学就进入现代哲学阶段。因为在19世纪中期，欧洲的工业革命几近完成。
现代哲学，特别是19世纪中后期的哲学流派，有叔本华的意志主义，新康德主

5. (wiki_002.md)
[来源] wiki_002.md | 哲学 / 主分支
哲学可以分为很多不同的分支，主要包括形而上学、知识论、伦理学、逻辑学和美学。

6. (wiki_002.md)
[来源] wiki_002.md | 哲学 / 早期近代哲学
西方哲学史上的近代早期一般指17世纪和18世纪，其中18世纪常被称为启蒙时代。现代哲学不同于其前身，它和传统权威例如教会、学院、亚里士多德的关系更加独立，出现了对知识基础和形而上

7. (wiki_024.md)
[来源] wiki_024.md | 心理学 / 起源
早期的心理学研究是属于哲学的范畴，称为哲学心理学。哲学心理学的研究可以追溯到埃及、希腊、印度和华夏等古代文明。中国古代认为人的性情思想是由一定的器官承担的，并且其活动会在器官上反映出来

8. (wiki_002.md)
[来源] wiki_002.md | 哲学 / 早期近代哲学
近现代政治哲学的鼻祖托马斯·霍布斯最早将这套方法论系统地应用在政治哲学上，包括"社会契约"的近代理论。早期近代哲学的学术经典一般包括笛卡尔、斯宾诺莎、莱布尼茨、洛克、贝克莱、休谟

9. (wiki_002.md)
[来源] wiki_002.md | 哲学 / 现象学
现象学是由德国哲学家胡塞尔在1900年提出的理论，强调对直接直观和经验感知的区分，认为哲学（或至少是现象学）的主要任务是厘清二者之间的关联，并且在直观中获得对本质的认识。现象学是对经验

10. (wiki_002.md)
[来源] wiki_002.md | 哲学 / 近代哲学（17-19世纪）
主条目：近代哲学

## 五、百科（6 题，语料：中文维基） Q26 [文件HIT5] [短语MISS] 覆盖缺口

Q: 若把文学定义为用文字记录的作品，最早的古代文学作品一般认为是哪个文明？最早已知的文学作品是哪部？

来源: wiki_003.md | 语料中存在: True

A(要点): 古埃及文学；公元前2700年由苏美人创作的《吉尔伽美什史诗》

top-5 短语命中: （无）

top-5 短语缺失: ['公元前2700年由苏美人创作的《吉尔伽美什史诗》']

全库也缺失: ['公元前2700年由苏美人创作的《吉尔伽美什史诗》']

1. (wiki_003.md)
[来源] wiki_003.md | 文学 / 文学史
文学的历史和文明发展有密切的关系。若将文学定义为用文字记录的作品，最早的古代文学作品一般认为是古埃及文学及。古埃及文学中主要的文类（赞美诗、祈祷文及故事）几乎都是以诗的方式写成的，不过

2. (wiki_003.md)
[来源] wiki_003.md | 文学 / 文学史
许多古文明都有其对哲学或是相关观点的文学，像是古中国、古印度、波斯及希腊罗马古典时代的作品。许多古代的作品，就算是叙事的形式，都还是有道德或是教诲上的目的，像梵语的《五卷书》或是奥维德

3. (wiki_003.md)
[来源] wiki_003.md | 文学 / 中文文学史
在很长一段时间，中国的文学与史学和神话并无明显的界限，最早的文学是对历史和神话的记录。但纯粹的文学早在周时就已出现，例如《诗经》。中国古代的文学主要著重在哲学、史学史、军事学、农业

4. (wiki_003.md)
[来源] wiki_003.md | 文学 / 文学史
各种文学都可以视为是文字的纪录，文学本身可能是写实或是虚构，但都可以描绘出一些事实，例如主角的动作及言语、作者的写作风格，以及文字后的含义等。这些情节不只是娱乐性的，其中也包括了经济、

5. (wiki_003.md)
[来源] wiki_003.md | 文学
文学（literature），在狭义上，是一种语言艺术，亦即使用语言文字为手段，形象化地反映客观社会生活、表达主观作者思想感情的一种艺术。文学不仅强调传达思想观念，更强调传达方式的独特性，且讲究辞

6. (wiki_065.md)
[来源] wiki_065.md | 中国 / 文学及书籍
中国文学从先秦始，通过诗经、楚辞、汉赋、晋书、唐诗、宋词、元曲，以及明清章回小说、民国杂文、共产文学、网路文章等持续发扬。「文学」一词最早见于《论语·先进篇》。经史子集是传统中国的

7. (wiki_003.md)
[来源] wiki_003.md | 文学 / 文学史
Harold’s Pilgrimage: Canto I》中借由主角Childe Harold提到西班牙文及法文，也提到作者的一些想法。借由文学人们可以继续的发现有关历史的新资讯，这个

8. (wiki_067.md)
[来源] wiki_067.md | 中华民国 / 文学出版
台湾原住民族口传文学是最早开始流传的台湾文学。古典汉诗文学源于17世纪，在明郑时期、清治时期、日治时期持续维持一定创作人口，但其内容因身份认同而有所转变。在日治时期还发展出吸收西

9. (wiki_061.md)
[来源] wiki_061.md | 历史学家 / 古希腊/罗马历史
而在古希腊/罗马，历史学家向来被视为文学家的一种，撰写历史的首务是将人物或事件写的生动，甚至某些「修饰」是被认为理所当然的。

10. (wiki_034.md)
[来源] wiki_034.md | 中华人民共和国 / 文学
中国文学始于先秦文学，当中古典典籍有著多元广泛的思想，包括诗歌、农历、军事、占星术、天文学、历法、中药、地理学，及阴阳、气功、八字、算命等命理学概念，并在西周时期奠定基础。中华

## 六、百科问答（6 题，语料：CMRC2018 / DRCD） Q27 [文件HIT5] [短语HIT5]

Q: 范廷颂是哪个国家的宗教人物？其圣名是什么？

来源: cmrc_001.md | 语料中存在: True

A(要点): 越南罗马天主教枢机；圣名保禄·若瑟

top-5 短语命中: ['越南罗马天主教枢机', '圣名保禄·若瑟']

top-5 短语缺失: （无）

1. (cmrc_001.md)
[来源] cmrc_001.md | 范廷颂
范廷颂枢机（，），圣名保禄·若瑟（），是越南罗马天主教枢机。1963年被任为主教；1990年被擢升为天主教河内总教区宗座署理；1994年被擢升为总主教，同年年底被擢升为枢机；2009年2月离世。

2. (cmrc_001.md)
[来源] cmrc_001.md | 范廷颂
我信天主的爱」。由于范廷颂被越南政府软禁差不多30年，因此他无法到所属堂区进行牧灵工作而专注研读等工作。范廷颂除了面对战争、贫困、被当局迫害天主教会等问题外，也秘密恢复修院、创建女修会团体等。1

3. (wiki_067.md)
[来源] wiki_067.md | 中华民国 / 宗教信仰
台湾民间信仰结合自然崇拜、儒家、佛教、道家等内容，相信人神灵三界相通。其中妈祖及王爷千岁为二大寺庙供奉神明系统，而不同庆典仪式、艺术装饰等则体现传统教义。每年各地会举办大型迎神赛

4. (cmrc_001.md)
[来源] cmrc_001.md | 范廷颂
# 范廷颂

5. (wiki_110.md)
[来源] wiki_110.md | 海南省 / 宗教
在内地文化还未深入海南岛之前，海南岛的黎苗地区盛行原始崇拜，尤以祖先崇拜与自然崇拜为主，崇拜对象繁多，生产生活中处处伴随着原始崇拜，影响很深，处于原始宗教信仰阶段。
748年，汉传佛教

6. (wiki_105.md)
[来源] wiki_105.md | 广东省 / 伊斯兰教
目前仅广州、肇庆有约2万名穆斯林。建于广州的怀圣寺光塔可以追溯到唐宋时期。
现代，主要来自新疆的穆斯林小群落近年也开始迁入深圳市，经营标榜清真风味的面馆。在梅林附近有一所清真寺，文

7. (wiki_065.md)
[来源] wiki_065.md | 中国 / 宗教
中国上古存在上帝及祖先崇拜等原始宗教信仰，祭神祀祖自商朝为中国的国家宗教，祖先神是人们祈求上帝的媒介。尧舜禹的臣子皋陶兴“五教”、定“五礼”、创“五刑”、立“九德”、亲“九族”。《尚书·

8. (wiki_068.md)
[来源] wiki_068.md | 宗教 / 起源
宗教源于准宗教现象，产生于原始宗教以前，为现今所知人类意识活动最早的形态之一，有一定程度的宗教因素，但当无超自然体的概念，对于客体尚未神化、无敬拜求告之念，一切全靠幻想，认为某些行动可影

9. (wiki_110.md)
[来源] wiki_110.md | 海南省 / 宗教
1630年，葡萄牙耶稣会派遣神甫比尼来琼传教，天主教传入海南。自传入起，法意西葡四国共派遣超过20名神甫传教，到了清朝，全岛天主教信徒已发展到5000余人。清末民初时期，天主教会在海南

10. (wiki_034.md)
[来源] wiki_034.md | 中华人民共和国 / 宗教
中华人民共和国政府官方立场为无神论，未设置法定宗教，政府支持并展开。宪法保障宗教自由并允许多种宗教；国家宗教事务局管理国内宗教事务，未获批准的宗教组织会遭到政府机关的压制。根据

## 六、百科问答（6 题，语料：CMRC2018 / DRCD） Q28 [文件HIT5] [短语HIT5]

Q: 范廷颂在哪一年被擢升为枢机？

来源: cmrc_001.md | 语料中存在: True

A(要点): 1994年（同年11月26日）

top-5 短语命中: ['同年11月26日']

top-5 短语缺失: （无）

1. (cmrc_001.md)
[来源] cmrc_001.md | 范廷颂
范廷颂枢机（，），圣名保禄·若瑟（），是越南罗马天主教枢机。1963年被任为主教；1990年被擢升为天主教河内总教区宗座署理；1994年被擢升为总主教，同年年底被擢升为枢机；2009年2月离世。

2. (cmrc_001.md)
[来源] cmrc_001.md | 范廷颂
我信天主的爱」。由于范廷颂被越南政府软禁差不多30年，因此他无法到所属堂区进行牧灵工作而专注研读等工作。范廷颂除了面对战争、贫困、被当局迫害天主教会等问题外，也秘密恢复修院、创建女修会团体等。1

3. (wiki_056.md)
[来源] wiki_056.md | 中国历史 / 前期的盛世
1661年顺治帝逝世，其子8岁的康熙帝即位，初由孝庄文皇后及索尼、遏必隆、苏克萨哈与鳌拜等四名辅政大臣辅政，四辅臣最终由鳌拜独专。1669年始亲政。三藩之乱于1681年清军攻入

4. (wiki_056.md)
[来源] wiki_056.md | 中国历史 / 北洋政府时期
1912年4月1日孙中山在南京辞去担任3个月的临时大总统职位，由袁世凯接任，并定都于北京，故又称北京政府。
袁世凯上台后不久，逼迫国会选他为大总统，之后就解散国会和终止临时约

5. (wiki_056.md)
[来源] wiki_056.md | 中国历史 / 危机与改革
英宗回到北京后，被亲弟景帝严密监视，但数年软禁中的他在1457年发动夺门之变复辟，改元天顺，他成为明朝唯一一个使用两个年号的皇帝。
英宗之后的成化帝早年勤政，后期宠信万贵妃与宦

6. (wiki_056.md)
[来源] wiki_056.md | 中国历史 / 中期的统治
1294年元世祖驾崩，元成宗继位。元成宗主要恪守元世祖时期的成宪，任用其侄海山（答剌麻八剌之子）镇守和林以平定西北海都之乱，并且下令停止征讨日本与安南。在内政方面专力整顿国内政

7. (wiki_060.md)
[来源] wiki_060.md | 上海市 / 改革开放后
1978年中国大陆实行改革开放，1980年7月，改革开放后上海第一家中外合资企业中国迅达电梯有限公司上海电梯厂成立。不过在1980年代，深圳等南方新兴经济特区经济发展迅速，上海作

8. (wiki_056.md)
[来源] wiki_056.md | 中国历史 / 建国与统一
元朝末期，官员贪污，朝政腐败。为消除赤字，元廷加重赋税，大量滥印新钞“至正宝钞”，随之产生的通货膨胀加上荒灾、黄河泛滥等天灾使得民不聊生。1351年元顺帝派贾鲁治理黄河，征调各

9. (wiki_056.md)
[来源] wiki_056.md | 中国历史 / 民变与灭亡
元廷派兵镇压各地红巾军，丞相脱脱亲自率军南下攻陷徐州芝麻李军，一度压制民变军。然而脱脱在1354年南攻高邮张士诚军之际，被元廷大臣弹劾而功亏一篑。徐寿辉部最后分裂成两湖的陈友谅

10. (wiki_056.md)
[来源] wiki_056.md | 中国历史 / 危机与改革
隆庆帝和万历帝初期，在内阁首辅高拱和张居正及宦官冯保的辅政之下曾一度中兴，国势鼎盛，此时银钱透过国际贸易流入中国，明朝经济达到全盛。万历年间，日本太合丰臣秀吉发动朝鲜之役，使明

## 六、百科问答（6 题，语料：CMRC2018 / DRCD） Q29 [文件HIT5] [短语HIT5]

Q: 范廷颂在 1995 年至 2001 年期间担任过什么职务？

来源: cmrc_001.md | 语料中存在: True

A(要点): 天主教越南主教团主席

top-5 短语命中: ['天主教越南主教团主席']

top-5 短语缺失: （无）

1. (cmrc_001.md)
[来源] cmrc_001.md | 范廷颂
我信天主的爱」。由于范廷颂被越南政府软禁差不多30年，因此他无法到所属堂区进行牧灵工作而专注研读等工作。范廷颂除了面对战争、贫困、被当局迫害天主教会等问题外，也秘密恢复修院、创建女修会团体等。1

2. (cmrc_001.md)
[来源] cmrc_001.md | 范廷颂
范廷颂枢机（，），圣名保禄·若瑟（），是越南罗马天主教枢机。1963年被任为主教；1990年被擢升为天主教河内总教区宗座署理；1994年被擢升为总主教，同年年底被擢升为枢机；2009年2月离世。

3. (cmrc_001.md)
[来源] cmrc_001.md | 范廷颂
# 范廷颂

4. (cmrc_077.md)
[来源] cmrc_077.md | 胡燕泳
胡燕泳（），香港新闻从业员。2001年胡在香港中文大学新闻与传播学院毕业，曾经从事公关工作。2003年转职香港有线电视新闻主播，并于同年转职到24小时亚视新闻台。2006年获奖学金，留学伦敦大学

5. (wiki_066.md)
[来源] wiki_066.md | 中华人民共和国历史 / 交接
江泽民是邓小平以及其它中共元老的折中选择，来取代当时指定的继任人赵紫阳。赵紫阳被认为对学生抗议过于容忍。虽然江泽民并没有直接卷入对示威的镇压，他因迅速稳定上海的局势而受到赏

6. (cmrc_094.md)
[来源] cmrc_094.md | 瓦尔迪斯·东布罗夫斯基斯
任期.他毕业于拉脱维亚大学物理与数学学院。1995年获得了里加工业大学工程方面的经济学学士学位，1996年获得拉脱维亚大学物理学硕士学位。他1995年至1996年在德国美因茨大

7. (cmrc_099.md)
[来源] cmrc_099.md | 郑国光
任职资格；1997年9月—1998年7月，挂职任福建省气象局副局长、党组成员）。1998年12月，任中国气象局监测网络司司长。1999年8月，任中国气象局党组成员、副局长。2007年3月，任中国

8. (cmrc_068.md)
[来源] cmrc_068.md | 林翠
及自导的《香港式离婚》（1976）。1977年移居美国旧金山，转而从事餐饮及租赁业。1980年末复出影坛，参与电影《海峡两岸》（1988）、《胭脂》（1991）及台湾电视剧《不了情》、《婆媳过招七

9. (wiki_091.md)
[来源] wiki_091.md | 中国共产党 / 集体领导
2017年10月中共十九大之后，中共中央政治局全体委员和常委被规定要向中共中央总书记述职。2018年3月，中共中央总书记习近平首次审阅各中央政治局委员提交的报告，他又向各政治局

10. (cmrc_041.md)
[来源] cmrc_041.md | 孙晋芳
# 孙晋芳

孙晋芳（），籍贯安徽省宿州市，生于江苏省苏州市，前中国女子排球队队长，现任国家体育总局网球运动管理中心主任。孙晋芳1971年入选江苏省女排，1976年被选入国家队，1981年率队夺

## 六、百科问答（6 题，语料：CMRC2018 / DRCD） Q30 [文件HIT5] [短语HIT5]

Q: 广州快速公交运输系统是什么时候引进的？规模在全球排名如何？

来源: drcd_001.md | 语料中存在: True

A(要点): 2010年引进；世界第二大快速公交系统，仅次于波哥大

top-5 短语命中: ['2010年引进', '世界第二大快速公交系统', '仅次于波哥大']

top-5 短语缺失: （无）

1. (drcd_001.md)
[来源] drcd_001.md | 广州
# 广州

2010年引进的广州快速公交运输系统，属世界第二大快速公交系统，日常载客量可达100万人次，高峰时期每小时单向客流高达26900人次，仅次于波哥大的快速交通系统，平均每10秒钟就有一辆

2. (drcd_039.md)
[来源] drcd_039.md | 广州
广州道路交通建设，尤其是高架桥与内外环路、高速公路非常发达。但由于私家车太多、道路通行能力低等原因，交通挤塞成为广州市内最常见的问题之一。公共运输方面，广州市内已有地铁、快速公交、公共汽车、无轨电

3. (drcd_007.md)
[来源] drcd_007.md | 广州
六朝时期的广州对外贸易已相当兴旺，外国海商「久停广州，往来求利」。隋唐时期广州对外贸易发展到一个顶峰，作为唐朝唯一设置市舶使的城市，外国人数量一度达到全城人口的30%以上，成为当时中国对外贸易的核

4. (wiki_034.md)
[来源] wiki_034.md | 中华人民共和国 / 交通运输
截至2022年，中国铁路总公司经营的铁路里程数共计约16万公里，其中高速铁路超4万公里，为全世界客运和货运最繁忙的网络，每年春节等假期都会出现人潮，通称春运。中华人民共和国

5. (wiki_034.md)
[来源] wiki_034.md | 中华人民共和国 / 能源与矿产
中华人民共和国经济具高度能源密集和耗能倾向，为能源消耗量最大（温室气体排放量最大）、及能源生产最多的国家。2014年生产约5.523兆千瓦·时电力，发电装机容量有13.6

6. (wiki_105.md)
[来源] wiki_105.md | 广东省 / 公路
广东高速公路是中国华南地区重要的交通网络系统。广东省内的第一条高速公路是1989年建成通车的广佛高速公路，2014年全省高速公路通车里程突破6000公里，跃居全国第一；2015年，高速

7. (drcd_002.md)
[来源] drcd_002.md | 广州
# 广州

广州是京广铁路、广深铁路、广茂铁路、广梅汕铁路的终点站。2009年末，武广客运专线投入运营，多单元列车覆盖980公里的路程，最高时速可达350公里/小时。2011年1月7日，广珠城际铁

8. (drcd_003.md)
[来源] drcd_003.md | 广州
# 广州

广州自古已是华南地区著名的商埠，拥有2000多年的开放贸易历史。1970年代末中国大陆改革开放后，广州经济发展迅速。2010年全市地区生产总值为10604.48亿元人民币，同比增长13

9. (drcd_034.md)
[来源] drcd_034.md | 广州
# 广州

广州的对外交流始于汉朝，历经多个朝代后，航运商业仍旧相当发达，至今与多个国家建立交流平台。中国实施改革开放后，美国率先于1979年在广州开设领事馆，之后外国驻穗领馆不断增加，至2016

10. (wiki_034.md)
[来源] wiki_034.md | 中华人民共和国 / 交通运输
中华人民共和国拥有发展中国家里最完善的交通网络，拥有堪比发达国家的基础建设，并且还有大量的高铁，高速公路和机场在建设中。拥有由铁路系统、公路系统、航空系统、船运系统、管道构

## 六、百科问答（6 题，语料：CMRC2018 / DRCD） Q31 [文件HIT5] [短语HIT5]

Q: 广州白云国际机场位于哪里？哪一年正式投入运营？

来源: drcd_001.md | 语料中存在: True

A(要点): 位于白云区与花都区交界；2004年8月5日正式投入运营

top-5 短语命中: ['位于白云区与花都区交界', '2004年8月5日正式投入运营']

top-5 短语缺失: （无）

1. (drcd_001.md)
[来源] drcd_001.md | 广州
# 广州

2010年引进的广州快速公交运输系统，属世界第二大快速公交系统，日常载客量可达100万人次，高峰时期每小时单向客流高达26900人次，仅次于波哥大的快速交通系统，平均每10秒钟就有一辆

2. (wiki_034.md)
[来源] wiki_034.md | 中华人民共和国 / 交通运输
底，中华人民共和国共有颁证民用航空运输机场254个（不含港、澳、台地区），定期航班航线里程超过838万公里。2015年机场旅客达9.15亿人次、货邮达1409万吨、飞机起降

3. (wiki_034.md)
[来源] wiki_034.md | 中华人民共和国 / 航空航天
1954年7月3日，中华人民共和国生产的第一架飞机初教-5在南昌首飞成功，结束了中国不能制造飞机的历史。1956年7月19日，中华人民共和国首架喷气式歼击机歼5原型机在沈阳

4. (drcd_002.md)
[来源] drcd_002.md | 广州
# 广州

广州是京广铁路、广深铁路、广茂铁路、广梅汕铁路的终点站。2009年末，武广客运专线投入运营，多单元列车覆盖980公里的路程，最高时速可达350公里/小时。2011年1月7日，广珠城际铁

5. (wiki_105.md)
[来源] wiki_105.md | 广东省 / 航空
，广东省境内已有民用运输机场9座、通用机场9座，公共运输航空公司8家（中国南方航空、汕头航空、珠海航空、九元航空、深圳航空、东海航空、顺丰航空、中航货运航空）。

6. (wiki_060.md)
[来源] wiki_060.md | 上海市 / 航空
上海是中国的三大航空枢纽之一，拥有虹桥与浦东两座国际机场，2019年运送旅客1亿2179万人次，年货邮吞吐量405.7万吨。两机场年起降飞机78.4万架次，均被中国东方航空与中国国际航

7. (wiki_034.md)
[来源] wiki_034.md | 中华人民共和国 / 交通运输
，2019年底建成的北京大兴国际机场被誉为“新国门”，成都天府国际机场等大型机场在疫情后也呈现客流量增加的趋势。波音公司估计中华人民共和国的民航机数量从2014年的2570

8. (drcd_007.md)
[来源] drcd_007.md | 广州
市场万客隆1996年在广州开设内地第一家分店，随后香港百佳超级市场等广州人熟悉的超市及便利店品牌陆续进入广州。因受交通压力及天河新区发展影响，90年代尾的人民南商圈开始衰落，成为电子服装批发集散地

9. (wiki_067.md)
[来源] wiki_067.md | 中华民国 / 交通运输
台湾四面环海，位处印度洋与太平洋交通枢纽。目前拥有7个国际商港和4个国内商港，前四大港口为高雄港、基隆港、台中港及台北港。主要是民营企业（如长荣海运、阳明海运等），拥有大量商船，

10. (wiki_120.md)
[来源] wiki_120.md | 山东省 / 航空
山东省民航在2014年初步形成济南、青岛两个干线机场和烟台、济宁、临沂、威海、东营、潍坊6个支线机场共同发展的格局。此外，2002年建成通航的蓬莱沙河口机场主要用于试飞、训练和旅游，日

## 六、百科问答（6 题，语料：CMRC2018 / DRCD） Q32 [文件HIT5] [短语HIT5]

Q: 广州市政府从哪一年开始禁止在市区内驾驶摩托车？

来源: drcd_001.md | 语料中存在: True

A(要点): 2007年1月16日

top-5 短语命中: ['2007年1月16日']

top-5 短语缺失: （无）

1. (drcd_001.md)
[来源] drcd_001.md | 广州
# 广州

2010年引进的广州快速公交运输系统，属世界第二大快速公交系统，日常载客量可达100万人次，高峰时期每小时单向客流高达26900人次，仅次于波哥大的快速交通系统，平均每10秒钟就有一辆

2. (drcd_009.md)
[来源] drcd_009.md | 广州
清朝末期，广州爆发了数次武装起义，均以失败告终。1911年10月10日武昌起义后，广东省独立，11月10日成立军政府，推选胡汉民为都督。12月初，广东临时省议会成立，公布21岁以上广东籍人皆有选举

3. (drcd_033.md)
[来源] drcd_033.md | 广州
广州作为中国近现代革命的策源地，19世纪末，辛亥革命元老中国现代教育奠基人何子渊、丘逢甲等于此地积极创办和推广新式学堂，不仅培育一大批思想进步锐意创新的社会精英，而且还催生「折衷中西，融汇古今」的

4. (drcd_033.md)
[来源] drcd_033.md | 广州
声称成立中华民国政府，选孙中山为大总统，在广州就职。1921年《广州市暂行条例》公布实施，广州市政厅成立，广州也因此成为中国第一个市。中国国民党1924年在广州举行第一次全国代表大会。同年孙中山在

5. (drcd_013.md)
[来源] drcd_013.md | 广州
历年来，广州当局积极进行各类政府工程。广州市自1990年开始参与「创建全国卫生城市」，于2008年成功取得该「称号」。1998年开始「创建全国文明城市」，2011年成功。「创卫」期间，广州市区的卫

6. (drcd_036.md)
[来源] drcd_036.md | 广州
# 广州

1949年后，所有的学校的校舍或组织均陆续被解放军广州市军事管制委员会接管，所有私立或教会学校在解放后陆续合并撤销，其中一些学校迁至澳门、香港等地。1954年广州改省辖市。1956年，

7. (drcd_038.md)
[来源] drcd_038.md | 广州
目前广州市辖11个市辖区：荔湾区、越秀区、海珠区、天河区、白云区、黄埔区、番禺区、花都区、南沙区、增城区、从化区。现时的广州市区主要位于越秀区，历史上的广州城区面积一直在扩张；由建城伊始的越秀、东

8. (drcd_008.md)
[来源] drcd_008.md | 广州
# 广州

从古至今，广州基本上是岭南地区的政治中心。秦末为南越国都城，汉朝征服南越国后立番禺为南海郡治。汉末郡治迁至龙湾与古坝之间。三国时，吴国步骘将郡治迁回番禺，后又设为交州治所。交广分治后为

9. (drcd_026.md)
[来源] drcd_026.md | 广州
# 广州

广州在明清时期，曾有18座城门。1920年广州大举开路时全部清拆，现时只剩下西门口等遗址，而由城门衍生出来的地名如大东门、西门口、小北路等仍然使用至今。骑楼是岭南一带常见的建筑形式，广

10. (drcd_039.md)
[来源] drcd_039.md | 广州
广州道路交通建设，尤其是高架桥与内外环路、高速公路非常发达。但由于私家车太多、道路通行能力低等原因，交通挤塞成为广州市内最常见的问题之一。公共运输方面，广州市内已有地铁、快速公交、公共汽车、无轨电

## 七、技术文档（6 题，语料：Langchain-Chatchat 中文文档） Q33 [文件HIT5] [短语HIT5]

Q: ApiRequest 类的主要功能是什么？它支持哪些 HTTP 方法？

来源: langchain_001.md | 语料中存在: True

A(要点): 封装 HTTP 请求、简化与 API 服务器的交互；支持 GET、POST、DELETE

top-5 短语命中: ['封装 HTTP 请求', '简化与 API 服务器的交互', '支持 GET', 'DELETE']

top-5 短语缺失: （无）

1. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef ApiRequest
**ApiRequest**: ApiRequest 类的功能是封装 HTTP 请求，简化与 API 服务器的交互过程。

**属性**

2. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef ApiRequest
在项目中，ApiRequest 类被多个模块调用，例如 `dialogue_page`、`knowledge_base_page` 和 

3. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef AsyncApiRequest
**AsyncApiRequest**: AsyncApiRequest 类的功能是提供异步 API 请求的封装。

**属性

4. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef ApiRequest / FunctionDef __init__(self, base_url, timeout)
**__init__**: 此函数的功能

5. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef ApiRequest / FunctionDef update_docs_by_id(self, knowledge_base_name, docs)
在函数

6. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef AsyncApiRequest / FunctionDef __init__(self, base_url, timeout)
接着，函数设置了一个私有属性`

7. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef AsyncApiRequest
在项目中，AsyncApiRequest 类与 ApiRequest 类共同构成了 API 请求的核心处理机制。ApiRequ

8. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef ApiRequest / FunctionDef get(self, url, params, retry, stream)
**get**: 此函数的功能是

9. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef ApiRequest / FunctionDef __init__(self, base_url, timeout)
从功能角度看，`__init__`函数通

10. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef ApiRequest / FunctionDef list_search_engines(self)
**注意**:
- 函数依赖于 `post` 方法来发送

## 七、技术文档（6 题，语料：Langchain-Chatchat 中文文档） Q34 [文件HIT5] [短语HIT5]

Q: ApiRequest 类支持同步和异步请求吗？请求失败时会怎样？

来源: langchain_001.md | 语料中存在: True

A(要点): 支持同步和异步请求；请求失败时自动重试

top-5 短语命中: ['请求失败时自动重试']

top-5 短语缺失: ['支持同步和异步请求']

全库也缺失: ['支持同步和异步请求']

1. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef ApiRequest
**ApiRequest**: ApiRequest 类的功能是封装 HTTP 请求，简化与 API 服务器的交互过程。

**属性**

2. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef AsyncApiRequest / FunctionDef __init__(self, base_url, timeout)
接着，函数设置了一个私有属性`

3. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef AsyncApiRequest
**AsyncApiRequest**: AsyncApiRequest 类的功能是提供异步 API 请求的封装。

**属性

4. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef AsyncApiRequest
在项目中，AsyncApiRequest 类与 ApiRequest 类共同构成了 API 请求的核心处理机制。ApiRequ

5. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef ApiRequest
- `client` 属性负责创建和获取 httpx 客户端实例。如果当前实例未创建或已关闭，它会根据配置重新创建一个。
- `get`

6. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef ApiRequest / FunctionDef client(self)
**注意**:
- `_client` 是 `ApiRequest` 类的一个私有

7. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef ApiRequest
在项目中，ApiRequest 类被多个模块调用，例如 `dialogue_page`、`knowledge_base_page` 和 

8. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef ApiRequest / FunctionDef _httpx_stream2generator(self, response, as_json)
**_ht

9. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef ApiRequest / FunctionDef __init__(self, base_url, timeout)
**__init__**: 此函数的功能

10. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef ApiRequest / FunctionDef list_search_engines(self)
**注意**:
- 函数依赖于 `post` 方法来发送

## 七、技术文档（6 题，语料：Langchain-Chatchat 中文文档） Q35 [文件HIT5] [短语MISS] 覆盖缺口

Q: normalize 函数的作用是什么？

来源: langchain_002.md | 语料中存在: True

A(要点): 对输入嵌入向量做 L2 范数归一化，使其规范化到单位球

top-5 短语命中: （无）

top-5 短语缺失: ['对输入嵌入向量做 L2 范数归一化', '使其规范化到单位球']

全库也缺失: ['对输入嵌入向量做 L2 范数归一化', '使其规范化到单位球']

1. (langchain_002.md)
[来源] langchain_002.md | base / FunctionDef normalize(embeddings)
**normalize**: 此函数的功能是对输入的嵌入向量进行L2范数归一化处理。

**参数**:
- *

2. (langchain_002.md)
[来源] langchain_002.md | base / FunctionDef normalize(embeddings)
**注意**:
- 输入的嵌入向量列表需要确保每个向量的维度相同，因为归一化过程涉及到按元素的运算。
- 该函

3. (langchain_002.md)
[来源] langchain_002.md | base / ClassDef EmbeddingsFunAdapter / FunctionDef aembed_documents(self, texts)
从功能角度看，`aembed_

4. (langchain_002.md)
[来源] langchain_002.md | base / ClassDef EmbeddingsFunAdapter / FunctionDef embed_documents(self, texts)
**embed_document

5. (langchain_011.md)
[来源] langchain_011.md | callbacks / ClassDef CustomAsyncIteratorCallbackHandler / FunctionDef on_tool_start(self, serial

6. (drcd_049.md)
[来源] drcd_049.md | 函数
# 函数

函数这个数学名词是莱布尼兹在1694年开始使用的，用来描述跟曲线相关的一个量，如曲线的斜率或者曲线上的某一点。莱布尼兹所指的函数现在被称作可导函数，数学家之外的普通人一般接触到的函数即

7. (langchain_021.md)
[来源] langchain_021.md | dialogue / FunctionDef parse_command(text, modal)
**注意**:
- 在使用此函数时，需要确保`modal`对象已正确初始化，以便在需要时能够

8. (langchain_021.md)
[来源] langchain_021.md | dialogue / FunctionDef dialogue_page(api, is_lite) / FunctionDef llm_model_format_func(x)
**llm_

9. (drcd_050.md)
[来源] drcd_050.md | 函数
# 函数

函数的定义得以扩展之后，数学家便能对一些「奇怪」的数学对象进行研究，例如处处不可导的连续函数。这些函数曾经被认为只具有理论价值，迟至20世纪初时它们仍被视作「怪物」。稍后，人们发现这些

10. (langchain_004.md)
[来源] langchain_004.md | utils / ClassDef KnowledgeFile / FunctionDef get_size(self)
**get_size**: 此函数的功能是获取文件的大小。

**参数*

## 七、技术文档（6 题，语料：Langchain-Chatchat 中文文档） Q36 [文件HIT5] [短语HIT5]

Q: normalize 函数被 EmbeddingsFunAdapter 中的哪些方法调用？

来源: langchain_002.md | 语料中存在: True

A(要点): embed_documents、embed_query、aembed_documents、aembed_query

top-5 短语命中: ['embed_documents', 'embed_query', 'aembed_documents', 'aembed_query']

top-5 短语缺失: （无）

1. (langchain_002.md)
[来源] langchain_002.md | base / FunctionDef normalize(embeddings)
**normalize**: 此函数的功能是对输入的嵌入向量进行L2范数归一化处理。

**参数**:
- *

2. (langchain_002.md)
[来源] langchain_002.md | base / ClassDef EmbeddingsFunAdapter / FunctionDef aembed_documents(self, texts)
从功能角度看，`aembed_

3. (langchain_002.md)
[来源] langchain_002.md | base / ClassDef EmbeddingsFunAdapter / FunctionDef aembed_documents(self, texts)
**aembed_docume

4. (langchain_002.md)
[来源] langchain_002.md | base / ClassDef EmbeddingsFunAdapter / FunctionDef embed_query(self, text)
**embed_query**: 该函数的

5. (langchain_002.md)
[来源] langchain_002.md | base / ClassDef EmbeddingsFunAdapter / FunctionDef embed_documents(self, texts)
**embed_document

6. (langchain_002.md)
[来源] langchain_002.md | base / ClassDef EmbeddingsFunAdapter
在项目中，EmbeddingsFunAdapter类被多个模块调用，用于处理不同场景下的文本嵌入需求。例如，在知识库聊

7. (langchain_016.md)
[来源] langchain_016.md | zilliz_kb_service / ClassDef ZillizKBService / FunctionDef do_search(self, query, top_k, score_t

8. (langchain_002.md)
[来源] langchain_002.md | base / ClassDef EmbeddingsFunAdapter
**属性**:
- `embed_model`: 嵌入模型的名称，用于指定使用哪个预训练模型进行文本嵌入。

**代码

9. (langchain_002.md)
[来源] langchain_002.md | base / ClassDef EmbeddingsFunAdapter / FunctionDef __init__(self, embed_model)
**__init__**: 该函数

10. (langchain_006.md)
[来源] langchain_006.md | base / ClassDef CachePool / FunctionDef load_kb_embeddings(self, kb_name, embed_device, default_

## 七、技术文档（6 题，语料：Langchain-Chatchat 中文文档） Q37 [文件HIT5] [短语MISS] 覆盖缺口

Q: validate_kb_name 函数检查什么？为什么需要它？

来源: langchain_004.md | 语料中存在: True

A(要点): 检查知识库名称是否包含 "../" 子串；用于防止路径遍历攻击

top-5 短语命中: （无）

top-5 短语缺失: ['检查知识库名称是否包含 "../" 子串', '用于防止路径遍历攻击']

全库也缺失: ['检查知识库名称是否包含 "../" 子串', '用于防止路径遍历攻击']

1. (langchain_004.md)
[来源] langchain_004.md | utils / FunctionDef validate_kb_name(knowledge_base_id)
**validate_kb_name**: 此函数用于验证知识库名称的合法性。


2. (langchain_004.md)
[来源] langchain_004.md | utils / FunctionDef validate_kb_name(knowledge_base_id)
**注意**:
- 在使用此函数时，需要确保传入的参数是字符串类型。
- 函数的

3. (langchain_010.md)
[来源] langchain_010.md | kb_doc_api / FunctionDef update_info(knowledge_base_name, kb_info)
**update_info**: 此函数用于更新知识库的介

4. (langchain_010.md)
[来源] langchain_010.md | kb_doc_api / FunctionDef download_doc(knowledge_base_name, file_name, preview)
**download_doc**:

5. (langchain_002.md)
[来源] langchain_002.md | base / ClassDef KBService / FunctionDef exists(self, kb_name)
**exists**: 此函数的功能是检查指定名称的知识库是否存在。

6. (langchain_019.md)
[来源] langchain_019.md | knowledge_file_repository / FunctionDef list_docs_from_db(session, kb_name, file_name, metadata)

7. (langchain_019.md)
[来源] langchain_019.md | knowledge_file_repository / FunctionDef list_file_num_docs_id_by_kb_name_and_file_name(session, 

8. (langchain_019.md)
[来源] langchain_019.md | knowledge_file_repository / FunctionDef get_file_detail(session, kb_name, filename)
**注意**:
- 在使

9. (langchain_019.md)
[来源] langchain_019.md | knowledge_file_repository / FunctionDef list_files_from_db(session, kb_name)
**list_files_from_d

10. (langchain_019.md)
[来源] langchain_019.md | knowledge_file_repository / FunctionDef get_file_detail(session, kb_name, filename)
**get_file_d

## 七、技术文档（6 题，语料：Langchain-Chatchat 中文文档） Q38 [文件HIT5] [短语MISS] 覆盖缺口

Q: validate_kb_name 的返回值是什么类型？名称包含 "../" 时返回什么？

来源: langchain_004.md | 语料中存在: True

A(要点): 返回布尔类型；包含 "../" 时返回 False（不合法）

top-5 短语命中: （无）

top-5 短语缺失: ['返回布尔类型', '包含 "../" 时返回 False']

全库也缺失: ['返回布尔类型', '包含 "../" 时返回 False']

1. (langchain_004.md)
[来源] langchain_004.md | utils / FunctionDef validate_kb_name(knowledge_base_id)
**注意**:
- 在使用此函数时，需要确保传入的参数是字符串类型。
- 函数的

2. (langchain_004.md)
[来源] langchain_004.md | utils / FunctionDef validate_kb_name(knowledge_base_id)
**validate_kb_name**: 此函数用于验证知识库名称的合法性。


3. (langchain_002.md)
[来源] langchain_002.md | base / ClassDef KBService / FunctionDef exists(self, kb_name)
**exists**: 此函数的功能是检查指定名称的知识库是否存在。

4. (langchain_012.md)
[来源] langchain_012.md | chromadb_kb_service / ClassDef ChromaKBService / FunctionDef get_kb_path(self)
**注意**: 在使用 `get_

5. (langchain_010.md)
[来源] langchain_010.md | kb_doc_api / FunctionDef update_info(knowledge_base_name, kb_info)
**update_info**: 此函数用于更新知识库的介

6. (langchain_009.md)
[来源] langchain_009.md | faiss_kb_service / ClassDef FaissKBService / FunctionDef get_kb_path(self)
**注意**: 使用`get_kb_pat

7. (langchain_019.md)
[来源] langchain_019.md | knowledge_file_repository / FunctionDef file_exists_in_db(session, kb_file)
**注意**:
- 确保传入的 `ses

8. (langchain_002.md)
[来源] langchain_002.md | base / ClassDef KBService / FunctionDef update_info(self, kb_info)
`add_kb_to_db`函数负责将知识库信息添加或更新

9. (langchain_018.md)
[来源] langchain_018.md | api / 常用 API 接口调用方式 / RAG 接口 （/knowledge_base/chat/compleitons）
相比于 /chat/chat/completions 接口，本接

10. (langchain_019.md)
[来源] langchain_019.md | knowledge_file_repository / FunctionDef get_file_detail(session, kb_name, filename)
**注意**:
- 在使

## 八、资讯新闻（6 题，语料：THUCNews 镜像） Q39 [文件HIT5] [短语MISS] 覆盖缺口

Q: 陈蝶衣的职业经历是怎样的？

来源: thucnews_0021.md | 语料中存在: True

A(要点): 既是流行歌曲之王（代表作《南屏晚钟》《凤凰于飞》），早期又是办报人，15岁在《新闻报》做实习生

top-5 短语命中: （无）

top-5 短语缺失: ['既是流行歌曲之王', '代表作《南屏晚钟》《凤凰于飞》', '早期又是办报人', '15岁在《新闻报》做实习生']

全库也缺失: ['既是流行歌曲之王', '代表作《南屏晚钟》《凤凰于飞》', '早期又是办报人', '15岁在《新闻报》做实习生']

1. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
可就是这样一个写流行歌曲的男子，早期却是个办报人。民国时期的小报也竞争激烈，陈蝶衣15岁就在《新闻报》做实习生，20岁在编辑部作校对，后来在办报上摸索出

2. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
这给了陈蝶衣一个启发。既然是明星日报，为何不搞个选美活动，这样不是能与大众共鸣互动吗？有了这个想法，陈蝶衣马上行动，这个选美活动定为“电影皇后的选举大会

3. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
说到中国历史上第一次大众参与的选美活动，不得不提到陈蝶衣。陈蝶衣是流行歌曲之王，比较有名的歌曲《南屏晚钟》、《凤凰于飞》、《我的眼里只有你没有他》均出自

4. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
有一次，陈蝶衣下班回家，路途侯车，听得几个人议论胡蝶与阮玲玉谁更美，争执不下，竟吵了起来。

5. (cmrc_077.md)
[来源] cmrc_077.md | 胡燕泳
胡燕泳（），香港新闻从业员。2001年胡在香港中文大学新闻与传播学院毕业，曾经从事公关工作。2003年转职香港有线电视新闻主播，并于同年转职到24小时亚视新闻台。2006年获奖学金，留学伦敦大学

6. (cmrc_065.md)
[来源] cmrc_065.md | 陈思荣
# 陈思荣

陈思荣（Chan Sze Wing，），生于香港，香港足球运动员，可司职左后卫和左中场，优点是速度快，不论快速短传或是长传能力亦属上乘。陈思荣自小学六年级加入香港体育学院。四年后足

7. (thucnews_0077.md)
[来源] thucnews_0077.md | 时尚评论：两个中国人在巴黎(图)
这是设计师谢锋第五次在巴黎时装周上亮相。两年多来，他和他的团队对发布会的制作流程已经上手，但忐忑不安的心情却从没改变。这是台湾时装品牌夏姿-陈首次参加巴黎时装

8. (thucnews_0011.md)
[来源] thucnews_0011.md | 希伯杜防守体系初见成效 芝加哥铁牛阵已显露真容
正是这样认真的职业精神，打动了他的同僚和队员。别看希伯杜执教公牛没多久，他在球队中的威信却和一些有着多年经验的老教练无异。

9. (thucnews_0034.md)
[来源] thucnews_0034.md | 湖南福彩彩民中奖700万被疑假票关押三年
从资深彩民到诈骗嫌犯，一个手持700万元大奖彩票的人经历怎样的故事？

10. (thucnews_0096.md)
[来源] thucnews_0096.md | 蟹女的三段感情经历
人说，恋爱使人成长，我很赞同这个观点。第一段情，让我懂得了怎样去爱一个人；第二段情，让我懂得了什么叫爱的滋味；第三段情，让我懂得了妥协的爱不是爱。经历了这些故事，让我的脑海

## 八、资讯新闻（6 题，语料：THUCNews 镜像） Q40 [文件HIT5] [短语MISS] 覆盖缺口

Q: 陈蝶衣策划的选美活动叫什么？

来源: thucnews_0021.md | 语料中存在: True

A(要点): 「电影皇后的选举大会」

top-5 短语命中: （无）

top-5 短语缺失: ['「电影皇后的选举大会」']

全库也缺失: ['「电影皇后的选举大会」']

1. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
这给了陈蝶衣一个启发。既然是明星日报，为何不搞个选美活动，这样不是能与大众共鸣互动吗？有了这个想法，陈蝶衣马上行动，这个选美活动定为“电影皇后的选举大会

2. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
说到中国历史上第一次大众参与的选美活动，不得不提到陈蝶衣。陈蝶衣是流行歌曲之王，比较有名的歌曲《南屏晚钟》、《凤凰于飞》、《我的眼里只有你没有他》均出自

3. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
可就是这样一个写流行歌曲的男子，早期却是个办报人。民国时期的小报也竞争激烈，陈蝶衣15岁就在《新闻报》做实习生，20岁在编辑部作校对，后来在办报上摸索出

4. (wiki_076.md)
[来源] wiki_076.md | 第二次世界大战 / 太平洋
早在1942年5月日本开始发起两栖作战的MO作战，准备占领莫士比港来阻断美国和澳洲之间的通讯以及物资流动。然而盟军成功在珊瑚海海战之中，阻止了日本海军持续往前推进。在美军成功

5. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
有一次，陈蝶衣下班回家，路途侯车，听得几个人议论胡蝶与阮玲玉谁更美，争执不下，竟吵了起来。

6. (drcd_010.md)
[来源] drcd_010.md | 广州
# 广州

作为近代革命发源地之一，广州自中华民国代时就是中国社会运动的中心之一。每次全国性的社会运动都有广州民众的响应和参与。以广州为中心的较具规模的社会运动，最早有1925年至1926年在广州

7. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
说起来，胡蝶还是比阮玲玉更会做人吧。她们也是共事过的。在影片《白云塔》中，导演张石川要胡蝶演一个正派的小姐，要阮玲玉演一个品质比较坏的小姐。原因是导演喜

8. (thucnews_0077.md)
[来源] thucnews_0077.md | 时尚评论：两个中国人在巴黎(图)
尽管早在2001 年就在巴黎开店，这却是夏姿-陈第一次参加巴黎时装周。“我深知只要做过一次，下次就一定要再来，不管是财力还是设计水准，都要足以支持这种连续的发

9. (thucnews_0077.md)
[来源] thucnews_0077.md | 时尚评论：两个中国人在巴黎(图)
这是设计师谢锋第五次在巴黎时装周上亮相。两年多来，他和他的团队对发布会的制作流程已经上手，但忐忑不安的心情却从没改变。这是台湾时装品牌夏姿-陈首次参加巴黎时装

10. (thucnews_0077.md)
[来源] thucnews_0077.md | 时尚评论：两个中国人在巴黎(图)
到目前为止，参加过巴黎高级成衣发布的中国品牌一共有三个：Jefen byFrankie、Wuyong 和夏姿-陈。其中Wuyong 只做了一季展示，Jefen

## 八、资讯新闻（6 题，语料：THUCNews 镜像） Q41 [文件HIT5] [短语HIT5]

Q: 「电影皇后」选举中，胡蝶和阮玲玉分别得第几名？票数是多少？

来源: thucnews_0021.md | 语料中存在: True

A(要点): 胡蝶以21334票评为第一名，阮玲玉只得第三名

top-5 短语命中: ['胡蝶以21334票评为第一名', '阮玲玉只得第三名']

top-5 短语缺失: （无）

1. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
最后，胡蝶以21334票评为第一名，而阮玲玉只得第三名。

2. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
说起来，胡蝶还是比阮玲玉更会做人吧。她们也是共事过的。在影片《白云塔》中，导演张石川要胡蝶演一个正派的小姐，要阮玲玉演一个品质比较坏的小姐。原因是导演喜

3. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
此后，在1934年的十大影星选举中，胡蝶当选的是最美丽的女明星，而阮玲玉则被选为演技最佳的女明星。

4. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
看看老照片，不难发现，胡蝶的姿色并不在阮玲玉之上，阮玲玉本人比照片还要美丽，在过去的一些电影片花中，阮玲玉秀气中有一种妩媚，内里的妖娆与悲哀的性情并存，

5. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
在这期间，明星公司的胡蝶、联华公司的阮玲玉及天一公司的陈玉梅选票遥遥领先其他演员。

6. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
究竟什么样的女人才算第一美女？是姿色、名气还是好的人际关系？就说当今的美丽级天后张曼玉、巩俐以及章子怡，谁又是真正的第一美女呢？就连西施、貂婵、杨贵妃也

7. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
有一次，陈蝶衣下班回家，路途侯车，听得几个人议论胡蝶与阮玲玉谁更美，争执不下，竟吵了起来。

8. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
不管怎样的渠道，胡蝶在当选为最美丽的女明星之后，得到的实惠是数不尽的。当时的一些杂志报纸关注胡蝶的一举一动，把胡蝶的打扮从头到脚分析给读者看，以她作为最

9. (wiki_060.md)
[来源] wiki_060.md | 上海市 / 电影与电视剧
1895年8月，上海出现了名为西洋影戏的电影。1909年，亚细亚影戏公司成立，为中国最早的电影公司。在1921年至1931年间，上海各类电影公司摄制的故事片有650余部。随着电

10. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
这给了陈蝶衣一个启发。既然是明星日报，为何不搞个选美活动，这样不是能与大众共鸣互动吗？有了这个想法，陈蝶衣马上行动，这个选美活动定为“电影皇后的选举大会

## 八、资讯新闻（6 题，语料：THUCNews 镜像） Q42 [文件HIT5] [短语MISS] 覆盖缺口

Q: 1934年十大影星选举中，胡蝶和阮玲玉分别当选什么称号？

来源: thucnews_0021.md | 语料中存在: True

A(要点): 胡蝶当选最美丽的女明星，阮玲玉当选演技最佳的女明星

top-5 短语命中: （无）

top-5 短语缺失: ['胡蝶当选最美丽的女明星', '阮玲玉当选演技最佳的女明星']

全库也缺失: ['胡蝶当选最美丽的女明星', '阮玲玉当选演技最佳的女明星']

1. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
此后，在1934年的十大影星选举中，胡蝶当选的是最美丽的女明星，而阮玲玉则被选为演技最佳的女明星。

2. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
说起来，胡蝶还是比阮玲玉更会做人吧。她们也是共事过的。在影片《白云塔》中，导演张石川要胡蝶演一个正派的小姐，要阮玲玉演一个品质比较坏的小姐。原因是导演喜

3. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
最后，胡蝶以21334票评为第一名，而阮玲玉只得第三名。

4. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
在这期间，明星公司的胡蝶、联华公司的阮玲玉及天一公司的陈玉梅选票遥遥领先其他演员。

5. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
看看老照片，不难发现，胡蝶的姿色并不在阮玲玉之上，阮玲玉本人比照片还要美丽，在过去的一些电影片花中，阮玲玉秀气中有一种妩媚，内里的妖娆与悲哀的性情并存，

6. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
有一次，陈蝶衣下班回家，路途侯车，听得几个人议论胡蝶与阮玲玉谁更美，争执不下，竟吵了起来。

7. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
究竟什么样的女人才算第一美女？是姿色、名气还是好的人际关系？就说当今的美丽级天后张曼玉、巩俐以及章子怡，谁又是真正的第一美女呢？就连西施、貂婵、杨贵妃也

8. (wiki_060.md)
[来源] wiki_060.md | 上海市 / 电影与电视剧
1895年8月，上海出现了名为西洋影戏的电影。1909年，亚细亚影戏公司成立，为中国最早的电影公司。在1921年至1931年间，上海各类电影公司摄制的故事片有650余部。随着电

9. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
不管怎样的渠道，胡蝶在当选为最美丽的女明星之后，得到的实惠是数不尽的。当时的一些杂志报纸关注胡蝶的一举一动，把胡蝶的打扮从头到脚分析给读者看，以她作为最

10. (wiki_066.md)
[来源] wiki_066.md | 中华人民共和国历史 / 建国会议
。9月30日下午三点，会议开始，先以整个名单付表决的方法，一致通过已经协商的政协第一届全国委员会，共180人；然后，以无记名联记投票的方法，选举中央人民政府委员会的主席

## 八、资讯新闻（6 题，语料：THUCNews 镜像） Q43 [文件HIT5] [短语MISS] 覆盖缺口

Q: 在影片《白云塔》中，导演分别让胡蝶和阮玲玉演什么角色？

来源: thucnews_0021.md | 语料中存在: True

A(要点): 胡蝶演正派的小姐，阮玲玉演品质比较坏的小姐

top-5 短语命中: （无）

top-5 短语缺失: ['胡蝶演正派的小姐', '阮玲玉演品质比较坏的小姐']

全库也缺失: ['胡蝶演正派的小姐', '阮玲玉演品质比较坏的小姐']

1. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
说起来，胡蝶还是比阮玲玉更会做人吧。她们也是共事过的。在影片《白云塔》中，导演张石川要胡蝶演一个正派的小姐，要阮玲玉演一个品质比较坏的小姐。原因是导演喜

2. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
有一次，陈蝶衣下班回家，路途侯车，听得几个人议论胡蝶与阮玲玉谁更美，争执不下，竟吵了起来。

3. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
看看老照片，不难发现，胡蝶的姿色并不在阮玲玉之上，阮玲玉本人比照片还要美丽，在过去的一些电影片花中，阮玲玉秀气中有一种妩媚，内里的妖娆与悲哀的性情并存，

4. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
最后，胡蝶以21334票评为第一名，而阮玲玉只得第三名。

5. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
此后，在1934年的十大影星选举中，胡蝶当选的是最美丽的女明星，而阮玲玉则被选为演技最佳的女明星。

6. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
究竟什么样的女人才算第一美女？是姿色、名气还是好的人际关系？就说当今的美丽级天后张曼玉、巩俐以及章子怡，谁又是真正的第一美女呢？就连西施、貂婵、杨贵妃也

7. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
在这期间，明星公司的胡蝶、联华公司的阮玲玉及天一公司的陈玉梅选票遥遥领先其他演员。

8. (wiki_060.md)
[来源] wiki_060.md | 上海市 / 电影与电视剧
1895年8月，上海出现了名为西洋影戏的电影。1909年，亚细亚影戏公司成立，为中国最早的电影公司。在1921年至1931年间，上海各类电影公司摄制的故事片有650余部。随着电

9. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
不管怎样的渠道，胡蝶在当选为最美丽的女明星之后，得到的实惠是数不尽的。当时的一些杂志报纸关注胡蝶的一举一动，把胡蝶的打扮从头到脚分析给读者看，以她作为最

10. (wiki_008.md)
[来源] wiki_008.md | 电影 / 默片
事实上，电影院老板经常替换掉讲评人，请乐师在电影放映时伴奏，若电影院有相应乐器的话，通常是钢琴师或风琴师。伴奏的音乐应该随时符合电影的情节气氛。

## 八、资讯新闻（6 题，语料：THUCNews 镜像） Q44 [文件HIT5] [短语HIT5]

Q: 罗斯是如何评价希伯杜教练的说话风格的？

来源: thucnews_0011.md | 语料中存在: True

A(要点): 希伯杜是个「话痨」，如果你不说话，他一个人能说两三个小时

top-5 短语命中: ['如果你不说话', '他一个人能说两三个小时']

top-5 短语缺失: ['希伯杜是个「话痨」']

全库也缺失: ['希伯杜是个「话痨」']

1. (thucnews_0011.md)
[来源] thucnews_0011.md | 希伯杜防守体系初见成效 芝加哥铁牛阵已显露真容
是的，多说多提醒，很多人都以为希伯杜教练不是很爱说话，他的外表看上去有些木讷，甚至不善言辞。事实上呢？队内的头号球星德里克·罗斯爆料了，希伯杜其

2. (thucnews_0011.md)
[来源] thucnews_0011.md | 希伯杜防守体系初见成效 芝加哥铁牛阵已显露真容
希伯杜不但自己爱说话，他希望自己的球员也都是如此，因为这是一套需要说话的防守体系。彼此间的协防保护需要说话，出现了意料之外的空当需要说话。一般情

3. (thucnews_0011.md)
[来源] thucnews_0011.md | 希伯杜防守体系初见成效 芝加哥铁牛阵已显露真容
公牛在防守上的进步，希伯杜都看在眼里，不过他认为目前球队的防守表现距离自己的期望值还有不小的差距。希伯杜是一个完美主义者，仅仅是联盟前5的防守水

4. (thucnews_0011.md)
[来源] thucnews_0011.md | 希伯杜防守体系初见成效 芝加哥铁牛阵已显露真容
防守成了这支公牛的一大特色，其实，他们的单兵防守并不算突出，除了诺阿是一个顶尖篮板球员，其他人的防守其实比较一般，可是希伯杜却能通过有效协防战术

5. (thucnews_0011.md)
[来源] thucnews_0011.md | 希伯杜防守体系初见成效 芝加哥铁牛阵已显露真容
正是这样认真的职业精神，打动了他的同僚和队员。别看希伯杜执教公牛没多久，他在球队中的威信却和一些有着多年经验的老教练无异。

6. (thucnews_0011.md)
[来源] thucnews_0011.md | 希伯杜防守体系初见成效 芝加哥铁牛阵已显露真容
新赛季，在他的执教下，公牛已经打了三场比赛，2胜1负，虽然只是三场球，但是已经能看出希伯杜给公牛带来了什么。总结起来很简单，那就是———出色的防

7. (thucnews_0011.md)
[来源] thucnews_0011.md | 希伯杜防守体系初见成效 芝加哥铁牛阵已显露真容
这些交流都建立在对对手比较了解的基础上，这些了解源于研究，源于大量系统的研究。这些研究，大都是希伯杜一个人整理和完成的，他就是一个工作狂。曾经和

8. (thucnews_0011.md)
[来源] thucnews_0011.md | 希伯杜防守体系初见成效 芝加哥铁牛阵已显露真容
“在球攻进禁区后，我们的内线防守表现不是太好，”希伯杜说，“我们有时候不够积极，交流不够，而在进攻上，切入也不够坚决。”在第一场比赛输给雷霆后，

9. (thucnews_0011.md)
[来源] thucnews_0011.md | 希伯杜防守体系初见成效 芝加哥铁牛阵已显露真容
数据说话--对手三分命中率18.0%

10. (thucnews_0011.md)
[来源] thucnews_0011.md | 希伯杜防守体系初见成效 芝加哥铁牛阵已显露真容
在未来一个赛季里，希伯杜会用球队的表现证明自己的执教水平。其实，他的水平，一些和他合作过的主教练都心知肚明。火箭前主帅杰夫·范甘迪就和希伯杜有过

