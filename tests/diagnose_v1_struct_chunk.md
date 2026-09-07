# 检索命中诊断报告（混合检索，k=10）

文件hit@5=40/40 | 短语hit@5=23/40 | 覆盖缺口=15 | 块级漏召回=2

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
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 二、RAG 的技术架构深度解析 / 4. 检索与重排序（Retrieval & Reranking）
初步

4. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / RAG 的起源
RAG 模型将预先训练的参数记忆（预训练语言模型）和非参数记忆（通过检索机制访问的外部知识库，如维基百科的密集向量索引）结合

5. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 为什么需要 RAG？
大型语言模型在处理特定领域或知识密集型任务时存在很大局限性，特别是在处理超出其训练数据或需要当前信息的查询时，会产生"

6. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / GraphRAG
GraphRAG 利用实体间的结构信息，实现更精确、更全面的检索，捕捉关系知识。工作流程包括基于图形的索引（G-Index

7. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / LangChain 框架：RAG 系统的技术基础
LangChain 已成为 RAG 应用开发的主流框架

8. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / RAG 简单流程与总览
应用于问答的 RAG 过程主要包括 3 个步骤：

1. 索引：文档被分割成块，编码成向量，存储在向量数据库中。
2

9. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 发展历程
自 2021 年 RAG 技术出现之后，RAG 首先被用于 LLMs 的预训练阶段来增强语言模型，随后被用于微调与推理任务中。自 

10. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 工程实践工具
常用的 RAG 系统构建工具包括 LangChain 和 LlamaIndex（完整框架），以及 FlashRAG（模块化开源

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
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / Agentic RAG
Agentic RAG 将 ReAct 的推理能力与 Agent 的任务执行能力相结合，创建一个动态和自适应的系统。

5. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 发展历程
自 2021 年 RAG 技术出现之后，RAG 首先被用于 LLMs 的预训练阶段来增强语言模型，随后被用于微调与推理任务中。自 

6. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 为什么需要 RAG？
大型语言模型在处理特定领域或知识密集型任务时存在很大局限性，特别是在处理超出其训练数据或需要当前信息的查询时，会产生"

7. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / GraphRAG
GraphRAG 利用实体间的结构信息，实现更精确、更全面的检索，捕捉关系知识。工作流程包括基于图形的索引（G-Index

8. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 高级 RAG（Advanced RAG）
高级 RAG 引入了具体的改进措施，以克服 Naive RAG 的局限性：

- 为了提高检索质量

9. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / RAG 的起源
RAG 模型将预先训练的参数记忆（预训练语言模型）和非参数记忆（通过检索机制访问的外部知识库，如维基百科的密集向量索引）结合

10. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / RAG 流程集成
```python
from langchain.chains import Retr

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
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / RAG 的起源
RAG 模型将预先训练的参数记忆（预训练语言模型）和非参数记忆（通过检索机制访问的外部知识库，如维基百科的密集向量索引）结合

3. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 发展历程
自 2021 年 RAG 技术出现之后，RAG 首先被用于 LLMs 的预训练阶段来增强语言模型，随后被用于微调与推理任务中。自 

4. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 为什么需要 RAG？
大型语言模型在处理特定领域或知识密集型任务时存在很大局限性，特别是在处理超出其训练数据或需要当前信息的查询时，会产生"

5. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 一、什么是 RAG？为什么它如此重要？
RAG 的核心思想很简单：让大模型"先查资料，再回答"。传统的 R

6. (langchain_003.md)
[来源] langchain_003.md | utils / ClassDef ChatMessage / ClassDef Config
**Config**: Config 类的功能是提供一个示例配置，用于说明如何处理和响应工伤保险相

7. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / RAG 技术概述及其重要性
传统语言模型如 GPT-4 尽管功能强大，但其知识库受限于训练数据，无法有效

8. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 高级 RAG（Advanced RAG）
高级 RAG 引入了具体的改进措施，以克服 Naive RAG 的局限性：

- 为了提高检索质量

9. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / 总结
通过上述方法可以构建一个能够基于特定文档集合回答问题的完整 RAG 系统。同样的技术架构适用于任何

10. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / Agentic RAG
Agentic RAG 将 ReAct 的推理能力与 Agent 的任务执行能力相结合，创建一个动态和自适应的系统。

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

2. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / 文档处理与分块策略
# 将文档拆分成更小的块，以便更好地检索
text_splitter = Chara

3. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 四、进阶优化：解决 RAG 的常见陷阱 / 1. 改进文本分割（Chunking Strategy）
- 

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

7. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 一、什么是 RAG？为什么它如此重要？
RAG 的核心思想很简单：让大模型"先查资料，再回答"。传统的 R

8. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / 文档处理与分块策略
RAG 系统的关键步骤是文档的处理与分块，包括：文档加载、将文档分割为适当大小的块、

9. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 一、什么是 RAG？为什么它如此重要？ / RAG 的核心优势
- 降低幻觉：答案基于事实依据，而非模型的

10. (langchain_004.md)
[来源] langchain_004.md | utils / ClassDef KnowledgeFile / FunctionDef docs2texts(self, docs, zh_title_enhance, refresh, c

## 一、事实题（10 题） Q5 [文件HIT5] [短语HIT5]

Q: 什么是文本嵌入（Embedding）？语义相似的文本在向量空间中有什么关系？

来源: 02_rag实战指南_langchain.md | 语料中存在: True

A(要点): 把文本转换为数值向量；语义相似的文本，向量在空间中的距离也相近

top-5 短语命中: ['语义相似的文本']

top-5 短语缺失: ['把文本转换为数值向量', '向量在空间中的距离也相近']

全库也缺失: ['把文本转换为数值向量', '向量在空间中的距离也相近']

1. (langchain_002.md)
[来源] langchain_002.md | base / ClassDef EmbeddingsFunAdapter / FunctionDef embed_documents(self, texts)
**embed_document

2. (langchain_002.md)
[来源] langchain_002.md | base / ClassDef EmbeddingsFunAdapter
**EmbeddingsFunAdapter**: EmbeddingsFunAdapter类的功能是对文本进行嵌入表

3. (langchain_002.md)
[来源] langchain_002.md | base / ClassDef EmbeddingsFunAdapter
在项目中，EmbeddingsFunAdapter类被多个模块调用，用于处理不同场景下的文本嵌入需求。例如，在知识库聊

4. (langchain_002.md)
[来源] langchain_002.md | base / ClassDef EmbeddingsFunAdapter
**属性**:
- `embed_model`: 嵌入模型的名称，用于指定使用哪个预训练模型进行文本嵌入。

**代码

5. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 二、RAG 的技术架构深度解析 / 2. 向量化与嵌入（Embedding）
计算机无法直接理解语义，需要

6. (langchain_002.md)
[来源] langchain_002.md | base / ClassDef EmbeddingsFunAdapter / FunctionDef embed_documents(self, texts)
**注意**:
- 确保传入的`

7. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef ApiRequest / FunctionDef embed_texts(self, texts, embed_model, to_query)
**embe

8. (langchain_005.md)
[来源] langchain_005.md | base / ClassDef ApiEmbeddingsParams
ApiEmbeddingsParams类在项目中主要用于处理文本的向量化请求，通过与不同的模型工作器（如MiniMaxW

9. (langchain_006.md)
[来源] langchain_006.md | base / ClassDef EmbeddingsPool / FunctionDef load_embeddings(self, model, device)
在项目中，`load_emb

10. (langchain_002.md)
[来源] langchain_002.md | base / ClassDef EmbeddingsFunAdapter / FunctionDef aembed_documents(self, texts)
**aembed_docume

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
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / ReAct 工作原理 / 初始化阶段
接收自然语言任务目标，明确任务类型与核心约束；输入 1-3 个 Few-shot 示例；创

3. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / ReAct 的局限
ReAct 依赖 LLM 的上下文窗口存储历史 TAO 轨迹，当任务步骤超过 10 轮时，需通过"裁剪-摘要

4. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / ReAct 解决了什么问题？
- 破解"事实幻觉"难题：将推理过程锚定到真实数据。实验数据显示，在 FEVER 事实核查任务中，

5. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / ReAct 工作原理 / 终止输出阶段
- 正常终止：模型输出 finish 行动，表明已完成任务目标；
- 超时终止：达到预设

6. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / 核心思想：模拟人类认知的 TAO 闭环
ReAct 将"Thought（推理）→Act（行动）→Observe（观察）"抽象为 

7. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / ReAct 工作原理 / 循环迭代阶段
每轮迭代严格遵循"推理-行动-观察"的顺序：

1. Thought（推理）：模型基于"

8. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / ReAct 技术架构（三层）
- 核心逻辑层：智能体的"决策大脑"，由"LLM+提示工程模块"构成，包括推理引擎、行动规划器、提

9. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / GraphRAG
GraphRAG 利用实体间的结构信息，实现更精确、更全面的检索，捕捉关系知识。工作流程包括基于图形的索引（G-Index

10. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / 极简代码框架
关键点：通过"构建提示词→调用 LLM→解析行动→执行工具→更新上下文"的流程控制 TAO 循环；工具层面替换为专

## 一、事实题（10 题） Q7 [文件HIT5] [短语HIT5]

Q: ReAct 的 TAO 循环由哪三部分组成？各自的作用是什么？

来源: 04_react核心范式详解.md | 语料中存在: True

A(要点): Thought（推理：分析任务目标与历史反馈）、Act（行动：调用工具）、Observe（观察：获取环境反馈）；反馈驱动下一轮推理

top-5 短语命中: ['Thought', 'Observe']

top-5 短语缺失: ['分析任务目标与历史反馈', '获取环境反馈', '反馈驱动下一轮推理']

全库也缺失: ['分析任务目标与历史反馈', '获取环境反馈', '反馈驱动下一轮推理']

1. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / 核心思想：模拟人类认知的 TAO 闭环
ReAct 将"Thought（推理）→Act（行动）→Observe（观察）"抽象为 

2. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / ReAct 工作原理 / 循环迭代阶段
每轮迭代严格遵循"推理-行动-观察"的顺序：

1. Thought（推理）：模型基于"

3. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / ReAct 工作原理 / 初始化阶段
接收自然语言任务目标，明确任务类型与核心约束；输入 1-3 个 Few-shot 示例；创

4. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / ReAct 技术架构（三层）
- 核心逻辑层：智能体的"决策大脑"，由"LLM+提示工程模块"构成，包括推理引擎、行动规划器、提

5. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / ReAct 的局限
ReAct 依赖 LLM 的上下文窗口存储历史 TAO 轨迹，当任务步骤超过 10 轮时，需通过"裁剪-摘要

6. (05_react手写实现指南.md)
[来源] 05_react手写实现指南.md | ReAct 代理裸机编码指南：不依赖任何框架的 LLM 自主决策实现 / 五、Prompt 工程：驱动推理的核心
经典模板：

```
你是一个自主代理，请通过以下步骤解决问题：
1. 思考

7. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / 极简代码框架
关键点：通过"构建提示词→调用 LLM→解析行动→执行工具→更新上下文"的流程控制 TAO 循环；工具层面替换为专

8. (05_react手写实现指南.md)
[来源] 05_react手写实现指南.md | ReAct 代理裸机编码指南：不依赖任何框架的 LLM 自主决策实现 / 一、ReAct 模式：AI 代理的"思考-行动"循环
ReAct（Reasoning + Action）是一种让大语

9. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / 什么是 ReAct？
ReAct = Reasoning（推理）+ Acting（行动），是一种让语言模型通过与外部工具、环境动

10. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / ReAct 解决了什么问题？
- 破解"事实幻觉"难题：将推理过程锚定到真实数据。实验数据显示，在 FEVER 事实核查任务中，

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
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 二、RAG 的技术架构深度解析 / 4. 检索与重排序（Retrieval & Reranking）
初步

4. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 一、什么是 RAG？为什么它如此重要？
RAG 的核心思想很简单：让大模型"先查资料，再回答"。传统的 R

5. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 五、总结与展望
RAG 技术不再追求让模型"记住"一切，而是让模型"学会"如何高效地利用外部知识。随着技术

6. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 一、什么是 RAG？为什么它如此重要？ / RAG 的核心优势
- 降低幻觉：答案基于事实依据，而非模型的

7. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / GraphRAG
GraphRAG 利用实体间的结构信息，实现更精确、更全面的检索，捕捉关系知识。工作流程包括基于图形的索引（G-Index

8. (wiki_029.md)
[来源] wiki_029.md | 农业 / 农业自动化
农业自动化多种不同定义。其中一种定义认为，自动化是指机械设备在没有人类干预的情况下自动执行任务。而另一种定义认为，自动化是借由便捷、自主、拥有决策能力的机械电子设备的辅助完成各类生

9. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / LangChain 框架：RAG 系统的技术基础
LangChain 已成为 RAG 应用开发的主流框架

10. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 四、进阶优化：解决 RAG 的常见陷阱 / 3. 引入重排序（Reranking）
向量检索虽然快，但不够

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

2. (langchain_017.md)
[来源] langchain_017.md | README / 概述
🤖️ 一种利用 [langchain](https://github.com/langchain-ai/langchain)
思想实现的基于本地知识库的问答应用，目标期

3. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 一、什么是 RAG？为什么它如此重要？
RAG 的核心思想很简单：让大模型"先查资料，再回答"。传统的 R

4. (wiki_005.md)
[来源] wiki_005.md | 计算机科学 / 人工智能
这个计算机科学分支旨在创造可以解决计算问题，以及像动物和人类一样思考与交流的人造系统。无论是在理论还是应用上，都要求研究者在多个学科领域具备细致的、综合的专长，比如应用数学，逻

5. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 一、什么是 RAG？为什么它如此重要？ / RAG 的核心优势
- 降低幻觉：答案基于事实依据，而非模型的

6. (wiki_036.md)
[来源] wiki_036.md | 克利斯登·奈加特 / 生平
克利斯登·奈加特在1995年—1999年的研究与分布式系统有关。他是GOODS项目（General Object-Oriented Distributed Systems，通

7. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 发展历程
自 2021 年 RAG 技术出现之后，RAG 首先被用于 LLMs 的预训练阶段来增强语言模型，随后被用于微调与推理任务中。自 

8. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / RAG 技术概述及其重要性
传统语言模型如 GPT-4 尽管功能强大，但其知识库受限于训练数据，无法有效

9. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 为什么需要 RAG？
大型语言模型在处理特定领域或知识密集型任务时存在很大局限性，特别是在处理超出其训练数据或需要当前信息的查询时，会产生"

10. (wiki_036.md)
[来源] wiki_036.md | 克利斯登·奈加特 / 生平
克利斯登·奈加特在1980年代的头半个时期是斯堪的纳维亚各国间的一个研究项目SYDPOL（System Development and Profession Oriented

## 一、事实题（10 题） Q10 [文件HIT5] [短语HIT5]

Q: 用 LangChain 构建 RAG 需要哪些核心组件？

来源: 01_langchain_rag入门教程.md | 语料中存在: True

A(要点): 文档加载器、文本分割器、向量存储、文本嵌入模型、检索机制、链式处理流程

top-5 短语命中: ['文本嵌入模型', '链式处理流程']

top-5 短语缺失: （无）

1. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / LangChain 框架：RAG 系统的技术基础
LangChain 已成为 RAG 应用开发的主流框架

2. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / 总结
通过上述方法可以构建一个能够基于特定文档集合回答问题的完整 RAG 系统。同样的技术架构适用于任何

3. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 三、实战：使用 LangChain 构建 RAG 应用 / 代码运行逻辑分析
- 用户输入问题后，Retr

4. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 三、实战：使用 LangChain 构建 RAG 应用 / 第一步：加载文档与分割
```python
f

5. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手
> 来源：https://developer.aliyun.com/article/1660267

6. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 三、实战：使用 LangChain 构建 RAG 应用 / 第三步：构建检索器
```python
def

7. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / RAG 技术概述及其重要性
传统语言模型如 GPT-4 尽管功能强大，但其知识库受限于训练数据，无法有效

8. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 工程实践工具
常用的 RAG 系统构建工具包括 LangChain 和 LlamaIndex（完整框架），以及 FlashRAG（模块化开源

9. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 三、实战：使用 LangChain 构建 RAG 应用 / 第二步：向量化并存储
```python
fr

10. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 二、RAG 的技术架构深度解析 / 4. 检索与重排序（Retrieval & Reranking）
初步

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
[来源] langchain_004.md | utils / ClassDef KnowledgeFile / FunctionDef docs2texts(self, docs, zh_title_enhance, refresh, c

3. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / 文档分块策略优化
分块方式对检索质量有重大影响，尝试递归字符分割：

```python
from la

4. (langchain_013.md)
[来源] langchain_013.md | ChatGLM3Agent
**注意**:
- 在使用此函数时，需要确保传入的文本格式正确，特别是当文本中包含动作描述时，需要遵循特定的格式（例如，动作和参数的正确分隔）。
- 如果在解析过程

5. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 三、实战：使用 LangChain 构建 RAG 应用 / 第一步：加载文档与分割
```python
f

6. (langchain_013.md)
[来源] langchain_013.md | ChatGLM3Agent
**注意**:
- 在使用 StructuredChatOutputParserWithRetries 类时，需要确保传入的文本格式符合预期，特别是当涉及到特殊标记

7. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / 文档处理与分块策略
# 将文档拆分成更小的块，以便更好地检索
text_splitter = Chara

8. (langchain_013.md)
[来源] langchain_013.md | ChatGLM3Agent
该类的核心方法是 parse，它接受一个字符串 text 作为输入，并尝试解析这个字符串以生成一个代理动作（AgentAction）或代理完成信号（AgentFin

9. (langchain_004.md)
[来源] langchain_004.md | utils / FunctionDef make_text_splitter(splitter_name, chunk_size, chunk_overlap, llm_model)
**代码

10. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / 文档处理与分块策略
RAG 系统的关键步骤是文档的处理与分块，包括：文档加载、将文档分割为适当大小的块、

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
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 高级 RAG（Advanced RAG）
高级 RAG 引入了具体的改进措施，以克服 Naive RAG 的局限性：

- 为了提高检索质量

3. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式
> 来源：https://cloud.tencent.cn/developer/article/2498870

4. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 为什么需要 RAG？
大型语言模型在处理特定领域或知识密集型任务时存在很大局限性，特别是在处理超出其训练数据或需要当前信息的查询时，会产生"

5. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / RAG 简单流程与总览
应用于问答的 RAG 过程主要包括 3 个步骤：

1. 索引：文档被分割成块，编码成向量，存储在向量数据库中。
2

6. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / GraphRAG
GraphRAG 利用实体间的结构信息，实现更精确、更全面的检索，捕捉关系知识。工作流程包括基于图形的索引（G-Index

7. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / RAG 的起源
RAG 模型将预先训练的参数记忆（预训练语言模型）和非参数记忆（通过检索机制访问的外部知识库，如维基百科的密集向量索引）结合

8. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / Agentic RAG
Agentic RAG 将 ReAct 的推理能力与 Agent 的任务执行能力相结合，创建一个动态和自适应的系统。

9. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 工程实践工具
常用的 RAG 系统构建工具包括 LangChain 和 LlamaIndex（完整框架），以及 FlashRAG（模块化开源

10. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 模块化 RAG（Modular RAG）
模块化 RAG 架构超越了前两种范式，具有更强的适应性和多功能性。它将复杂的 RAG 系统分解为独

## 二、综合题（4 题） Q13 [文件HIT5] [短语HIT10] 块级漏召回

Q: 为什么说「检索质量决定 RAG 回答的上限」？有哪些手段改进检索？

来源: 02_rag实战指南_langchain.md | 语料中存在: True

A(要点): 检索到的块不相关，生成阶段无法补救；手段包括重排序（Reranker）、查询改写（HyDE）、多跳检索、更高质量的嵌入模型

top-5 短语命中: （无）

top-5 短语缺失: ['检索到的块不相关', '生成阶段无法补救', '手段包括重排序', 'Reranker', '更高质量的嵌入模型']

全库也缺失: ['检索到的块不相关', '生成阶段无法补救', '手段包括重排序']

1. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 高级 RAG（Advanced RAG）
高级 RAG 引入了具体的改进措施，以克服 Naive RAG 的局限性：

- 为了提高检索质量

2. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 一、什么是 RAG？为什么它如此重要？
RAG 的核心思想很简单：让大模型"先查资料，再回答"。传统的 R

3. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / RAG 简单流程与总览
应用于问答的 RAG 过程主要包括 3 个步骤：

1. 索引：文档被分割成块，编码成向量，存储在向量数据库中。
2

4. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / RAG 技术概述及其重要性
传统语言模型如 GPT-4 尽管功能强大，但其知识库受限于训练数据，无法有效

5. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 四、进阶优化：解决 RAG 的常见陷阱 / 4. 评估体系（RAG Evaluation）
使用 RAGA

6. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / 常见问题及解决方案
- 检索质量差：使用更高质量的嵌入模型（如 all-mpnet-base-v2）、调

7. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 为什么需要 RAG？
大型语言模型在处理特定领域或知识密集型任务时存在很大局限性，特别是在处理超出其训练数据或需要当前信息的查询时，会产生"

8. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 四、进阶优化：解决 RAG 的常见陷阱 / 3. 引入重排序（Reranking）
向量检索虽然快，但不够

9. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 二、RAG 的技术架构深度解析 / 4. 检索与重排序（Retrieval & Reranking）
初步

10. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 四、进阶优化：解决 RAG 的常见陷阱 / 2. 查询改写（Query Rewriting）
- HyDE

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
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / ReAct 的局限
ReAct 依赖 LLM 的上下文窗口存储历史 TAO 轨迹，当任务步骤超过 10 轮时，需通过"裁剪-摘要

4. (05_react手写实现指南.md)
[来源] 05_react手写实现指南.md | ReAct 代理裸机编码指南：不依赖任何框架的 LLM 自主决策实现 / 一、ReAct 模式：AI 代理的"思考-行动"循环
ReAct（Reasoning + Action）是一种让大语

5. (05_react手写实现指南.md)
[来源] 05_react手写实现指南.md | ReAct 代理裸机编码指南：不依赖任何框架的 LLM 自主决策实现 / 三、ReAct 代理的工作原理
ReAct 代理以"思考 → 行动 → 观察"的循环方式运行，重复进行直到找到解决方

6. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / 什么是 ReAct？
ReAct = Reasoning（推理）+ Acting（行动），是一种让语言模型通过与外部工具、环境动

7. (05_react手写实现指南.md)
[来源] 05_react手写实现指南.md | ReAct 代理裸机编码指南：不依赖任何框架的 LLM 自主决策实现 / 六、优化：超越基础实现
- 短路机制：当工具返回明确结果时跳过冗余思考，提前终止循环
- 错误回退：工具调用失败时尝

8. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / 极简代码框架
def react_core_loop(task, tools, llm, max_steps=6):
    "

9. (05_react手写实现指南.md)
[来源] 05_react手写实现指南.md | ReAct 代理裸机编码指南：不依赖任何框架的 LLM 自主决策实现
> 来源：https://cloud.tencent.com.cn/developer/article/2551972

10. (05_react手写实现指南.md)
[来源] 05_react手写实现指南.md | ReAct 代理裸机编码指南：不依赖任何框架的 LLM 自主决策实现 / 七、与框架的共生关系
原生实现：完全掌控底层逻辑，适合研究/定制化场景，但需自行处理并发/监控。

框架（CrewA

## 三、无答案题（4 题，测幻觉防线） Q15 [文件MISS] [短语MISS] 覆盖缺口

Q: 请介绍 OpenAI GPT-5 模型的参数规模和发布日期。

来源: （无来源/语料无） | 语料中存在: None

A(要点): 语料中没有 → 应回答「资料中没有相关信息」

top-5 短语命中: （无）

top-5 短语缺失: ['语料中没有 → 应回答「资料中没有相关信息」']

全库也缺失: ['语料中没有 → 应回答「资料中没有相关信息」']

1. (langchain_017.md)
[来源] langchain_017.md | README / 概述
![](docs/img/langchain_chatchat_0.3.0.png)

✅ 本项目支持市面上主流的开源 LLM、 Embedding 模型与向量数据库，

2. (langchain_003.md)
[来源] langchain_003.md | utils / FunctionDef get_OpenAI(model_name, temperature, max_tokens, streaming, echo, callbacks, 

3. (langchain_017.md)
[来源] langchain_017.md | README / 功能介绍 / 已支持的模型部署框架与模型
除上述本地模型加载框架外，项目中也为可接入在线 API 的 [One API](https://github.com/songqua

4. (langchain_017.md)
[来源] langchain_017.md | README / 功能介绍 / 已支持的模型部署框架与模型
| OpenAI API 接口对齐    | ✅                                          

5. (langchain_003.md)
[来源] langchain_003.md | utils / FunctionDef get_ChatOpenAI(model_name, temperature, max_tokens, streaming, callbacks, ve

6. (langchain_017.md)
[来源] langchain_017.md | README / 功能介绍 / 已支持的模型部署框架与模型
本项目中已经支持市面上主流的如 [GLM-4-Chat](https://github.com/THUDM/GLM-4)
与 [Qw

7. (langchain_006.md)
[来源] langchain_006.md | base / ClassDef EmbeddingsPool
**输出示例**:
调用 `load_embeddings` 方法可能返回的嵌入向量对象示例：
```python
embeddi

8. (langchain_017.md)
[来源] langchain_017.md | README / 项目里程碑
+ `2023年4月`: `Langchain-ChatGLM 0.1.0` 发布，支持基于 ChatGLM-6B 模型的本地知识库问答。
+ `2023年8月`

9. (langchain_018.md)
[来源] langchain_018.md | api / 常用 API 接口调用方式 / RAG 接口 （/knowledge_base/chat/compleitons）
'出处 [2] [test_files/test.txt](ht

10. (langchain_007.md)
[来源] langchain_007.md | startup / FunctionDef create_model_worker_app(log_level)
**create_model_worker_app**: 此函数的功能是创建并

## 三、无答案题（4 题，测幻觉防线） Q16 [文件MISS] [短语MISS] 覆盖缺口

Q: 今天（2026年8月5日）的 AI 行业新闻有哪些？

来源: （无来源/语料无） | 语料中存在: None

A(要点): 语料中没有实时信息 → 应回答「资料中没有相关信息」

top-5 短语命中: （无）

top-5 短语缺失: ['语料中没有实时信息 → 应回答「资料中没有相关信息」']

全库也缺失: ['语料中没有实时信息 → 应回答「资料中没有相关信息」']

1. (wiki_079.md)
[来源] wiki_079.md | 人工智能 / 发展史
2016年，在机器学习会议上，与技术滥用成为突出话题；相关论文发表数量急剧增加，研究经费随之提供，众多研究人员转而聚焦这些议题。对齐问题逐渐成为学术探讨的重要议题。
2010年代末

2. (cmrc_012.md)
[来源] cmrc_012.md | 2008年夏季奥林匹克运动会中国摔跤队
焦华锋、盛江、李岩岩、常永祥、马三义、姜华琛、刘德利女运动员（4人）：黎笑媚、许莉、许海燕、王娇官员与管理人员（10人）领队：周进强，副领队：董生辉教练员（6人）

3. (thucnews_0140.md)
[来源] thucnews_0140.md | 1月28日美股专家坐堂实录
网友[匿名]问： 老师你好!AIG有投资前景吗(2009-01-28 20:41:57)

4. (thucnews_0137.md)
[来源] thucnews_0137.md | 1月23日美股专家坐堂实录
网友[匿名]问： 老师，中概念股中你比较看好的有哪些？(2009-01-23 13:05:08) 　　专家[曾文俊]答： 在危机的大背景下，暂时还不能看出哪个能够生

5. (wiki_079.md)
[来源] wiki_079.md | 人工智能 / 经济冲击
2017年6月份马云在美国底特律举行「链结世界」（Gateway 17）产业大会，会上提出人工智慧可能导致第三次世界大战，因为前两次产业革命都导致两次大战，战争原因并非这些创新发

6. (wiki_057.md)
[来源] wiki_057.md | 亳州市 / 气候
亳州处于秦岭－淮河天然气候分界线上，位于亚热带季风气候与温带季风气候的过渡地带。季风影响显著，四季分明，雨量适中，光照充足。1月平均气温0.6℃，极端最低气温-20.6℃（1969年2

7. (wiki_079.md)
[来源] wiki_079.md | 人工智能 / 乐观学派
主要是Google、Facebook等AI的主要技术发展者，他们对AI持乐观看法的理由：

8. (wiki_060.md)
[来源] wiki_060.md | 上海市 / 气候
上海的气候类型属于亚热带季风气候夏季高温多雨，冬季温和少雨，四季分明，日照充分，雨量充沛。气候温和湿润，年平均气温17.0 °C。春（4月-5月）、秋（10月-11月）较短，冬（12月

9. (wiki_079.md)
[来源] wiki_079.md | 人工智能 / AI对人类的威胁
此议题目前分成两个学派：

10. (cmrc_012.md)
[来源] cmrc_012.md | 2008年夏季奥林匹克运动会中国摔跤队
，以6：11遭淘汰。（2008年8月13日）男子古典式摔跤55公斤级中国有常永祥参加该项目，1/8决赛淘汰。1/8决赛常永祥Vs保加利亚亚沃尔·亚娜基耶夫，以4：

## 三、无答案题（4 题，测幻觉防线） Q17 [文件MISS] [短语MISS] 覆盖缺口

Q: 如何调用 DeepSeek 的 API 完成一次对话？

来源: （无来源/语料无） | 语料中存在: None

A(要点): 语料只讲 RAG/ReAct 原理，没有 DeepSeek API 代码 → 应回答「资料中没有相关信息」

top-5 短语命中: （无）

top-5 短语缺失: ['语料只讲 RAG/ReAct 原理', '没有 DeepSeek API 代码 → 应回答「资料中没有相关信息」']

全库也缺失: ['语料只讲 RAG/ReAct 原理', '没有 DeepSeek API 代码 → 应回答「资料中没有相关信息」']

1. (langchain_018.md)
[来源] langchain_018.md | api / 常用 API 接口调用方式 / 通用对话接口（/chat/chat/completions）
最主要的对话接口，兼容 openai sdk 格式。它支持以下3种对话模式：  
- 

2. (langchain_018.md)
[来源] langchain_018.md | api / 常用 API 接口调用方式 / 通用对话接口（/chat/chat/completions）
输入参数：与 openai sdk 参数一致。针对 chatchat 做了以下优化： 

3. (langchain_018.md)
[来源] langchain_018.md | api / 常用 API 接口调用方式 / 通用对话接口（/chat/chat/completions）
to the given question is 85. \n\nJSON Objec

4. (langchain_021.md)
[来源] langchain_021.md | dialogue / FunctionDef dialogue_page(api, is_lite)
**dialogue_page**: 此函数用于处理对话页面的逻辑，包括初始化会话、处理用

5. (langchain_018.md)
[来源] langchain_018.md | api / 常用 API 接口调用方式 / 通用对话接口（/chat/chat/completions）
import requests
    response = requests.pos

6. (langchain_013.md)
[来源] langchain_013.md | ChatGLM3Agent
```
"This was your previous work (but I haven't seen any of it! I only see what yo

7. (langchain_018.md)
[来源] langchain_018.md | api / 常用 API 接口调用方式 / 通用对话接口（/chat/chat/completions）
"messages": [
            {"role": "user", 

8. (langchain_018.md)
[来源] langchain_018.md | api / 常用 API 接口调用方式 / 通用对话接口（/chat/chat/completions）
调用示例：
- 纯 LLM 对话：
    ```python3
    base_u

9. (langchain_018.md)
[来源] langchain_018.md | api / 常用 API 接口调用方式 / 通用对话接口（/chat/chat/completions）
ChatCompletionChunk(id='chat68511ba1-3426-1

10. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef ApiRequest
在项目中，ApiRequest 类被多个模块调用，例如 `dialogue_page`、`knowledge_base_page` 和 

## 三、无答案题（4 题，测幻觉防线） Q18 [文件MISS] [短语MISS] 覆盖缺口

Q: 什么是多模态 RAG？请给出具体实现方案。

来源: （无来源/语料无） | 语料中存在: None

A(要点): 语料没有多模态 RAG 的实现细节 → 应回答「资料中没有相关信息」

top-5 短语命中: （无）

top-5 短语缺失: ['语料没有多模态 RAG 的实现细节 → 应回答「资料中没有相关信息」']

全库也缺失: ['语料没有多模态 RAG 的实现细节 → 应回答「资料中没有相关信息」']

1. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 一、什么是 RAG？为什么它如此重要？
RAG 的核心思想很简单：让大模型"先查资料，再回答"。传统的 R

2. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 为什么需要 RAG？
大型语言模型在处理特定领域或知识密集型任务时存在很大局限性，特别是在处理超出其训练数据或需要当前信息的查询时，会产生"

3. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 一、什么是 RAG？为什么它如此重要？ / RAG 的核心优势
- 降低幻觉：答案基于事实依据，而非模型的

4. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 工程实践工具
常用的 RAG 系统构建工具包括 LangChain 和 LlamaIndex（完整框架），以及 FlashRAG（模块化开源

5. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 高级 RAG（Advanced RAG）
高级 RAG 引入了具体的改进措施，以克服 Naive RAG 的局限性：

- 为了提高检索质量

6. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / RAG 简单流程与总览
应用于问答的 RAG 过程主要包括 3 个步骤：

1. 索引：文档被分割成块，编码成向量，存储在向量数据库中。
2

7. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / Agentic RAG
Agentic RAG 将 ReAct 的推理能力与 Agent 的任务执行能力相结合，创建一个动态和自适应的系统。

8. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 模块化 RAG（Modular RAG）
模块化 RAG 架构超越了前两种范式，具有更强的适应性和多功能性。它将复杂的 RAG 系统分解为独

9. (langchain_017.md)
[来源] langchain_017.md | README / 功能介绍 / 0.3.x 版本功能一览
0.3.x 版本的核心功能由 Agent 实现,但用户也可以手动实现工具调用:

|操作方式|实现的功能|适用场景|
|-------

10. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / 常见问题及解决方案
- 检索质量差：使用更高质量的嵌入模型（如 all-mpnet-base-v2）、调

## 四、概念辨析（2 题） Q19 [文件HIT5] [短语MISS] 覆盖缺口

Q: ReAct 中 Thought、Act、Observe 为什么要按顺序循环？少了 Observe 会怎样？

来源: 04_react核心范式详解.md + 05_react手写实现指南.md | 语料中存在: True

A(要点): 顺序构成「推理→执行→反馈」闭环；少了 Observe 就没有真实数据支撑，推理会退回凭记忆，幻觉无法被抑制

top-5 短语命中: （无）

top-5 短语缺失: ['顺序构成「推理→执行→反馈」闭环', '少了 Observe 就没有真实数据支撑', '推理会退回凭记忆', '幻觉无法被抑制']

全库也缺失: ['顺序构成「推理→执行→反馈」闭环', '少了 Observe 就没有真实数据支撑', '推理会退回凭记忆', '幻觉无法被抑制']

1. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / 核心思想：模拟人类认知的 TAO 闭环
ReAct 将"Thought（推理）→Act（行动）→Observe（观察）"抽象为 

2. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / ReAct 工作原理 / 循环迭代阶段
每轮迭代严格遵循"推理-行动-观察"的顺序：

1. Thought（推理）：模型基于"

3. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / 极简代码框架
else:
            observation = f"无效行动：{action}"
        

4. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / 什么是 ReAct？
ReAct = Reasoning（推理）+ Acting（行动），是一种让语言模型通过与外部工具、环境动

5. (05_react手写实现指南.md)
[来源] 05_react手写实现指南.md | ReAct 代理裸机编码指南：不依赖任何框架的 LLM 自主决策实现 / 三、ReAct 代理的工作原理
ReAct 代理以"思考 → 行动 → 观察"的循环方式运行，重复进行直到找到解决方

6. (05_react手写实现指南.md)
[来源] 05_react手写实现指南.md | ReAct 代理裸机编码指南：不依赖任何框架的 LLM 自主决策实现 / 六、优化：超越基础实现
- 短路机制：当工具返回明确结果时跳过冗余思考，提前终止循环
- 错误回退：工具调用失败时尝

7. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / 极简代码框架
class ContextManager:
    """上下文管理器：存储、裁剪与提取历史 TAO 轨迹"""


8. (05_react手写实现指南.md)
[来源] 05_react手写实现指南.md | ReAct 代理裸机编码指南：不依赖任何框架的 LLM 自主决策实现 / 一、ReAct 模式：AI 代理的"思考-行动"循环
ReAct（Reasoning + Action）是一种让大语

9. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / 极简代码框架
thought = parse_thought(llm_output)
        action = pars

10. (05_react手写实现指南.md)
[来源] 05_react手写实现指南.md | ReAct 代理裸机编码指南：不依赖任何框架的 LLM 自主决策实现 / 二、为什么需要 ReAct？突破 LLM 的固有局限
- 传统 LLM 依赖预训练知识，无法获取实时数据 → ReA

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

2. (01_langchain_rag入门教程.md)
[来源] 01_langchain_rag入门教程.md | LangChain RAG 入门教程：构建基于私有文档的智能问答助手 / RAG 技术概述及其重要性
传统语言模型如 GPT-4 尽管功能强大，但其知识库受限于训练数据，无法有效

3. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 四、进阶优化：解决 RAG 的常见陷阱 / 2. 查询改写（Query Rewriting）
- HyDE

4. (wiki_074.md)
[来源] wiki_074.md | 计算语言学 / 产出门径
最早期著名的自然交谈程式之一是ELIZA，1966年由约瑟夫·维森鲍姆在麻省理工学院发展而成。该程式回答使用者提出的文字陈述或问题时，模拟一位罗杰斯式心理治疗师。它看似能够理解

5. (langchain_003.md)
[来源] langchain_003.md | utils / ClassDef ChatMessage / ClassDef Config
**Config**: Config 类的功能是提供一个示例配置，用于说明如何处理和响应工伤保险相

6. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 一、什么是 RAG？为什么它如此重要？ / RAG 的核心优势
- 降低幻觉：答案基于事实依据，而非模型的

7. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / GraphRAG
GraphRAG 利用实体间的结构信息，实现更精确、更全面的检索，捕捉关系知识。工作流程包括基于图形的索引（G-Index

8. (02_rag实战指南_langchain.md)
[来源] 02_rag实战指南_langchain.md | 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南 / 二、RAG 的技术架构深度解析 / 4. 检索与重排序（Retrieval & Reranking）
初步

9. (langchain_003.md)
[来源] langchain_003.md | utils / ClassDef ChatMessage
- `question` 属性定义了提问的文本内容，是一个字符串类型。
- `response` 属性定义了对提问的回答，同样是一个字

10. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / RAG 简单流程与总览
应用于问答的 RAG 过程主要包括 3 个步骤：

1. 索引：文档被分割成块，编码成向量，存储在向量数据库中。
2

## 五、百科（6 题，语料：中文维基） Q21 [文件HIT5] [短语HIT5]

Q: 数学属于哪一类学科？它的核心研究对象是什么？

来源: wiki_001.md | 语料中存在: True

A(要点): 数学属于形式科学；研究数量、结构以及空间等概念及其变化

top-5 短语命中: ['结构以及空间等概念及其变化']

top-5 短语缺失: ['数学属于形式科学']

全库也缺失: ['数学属于形式科学']

1. (wiki_001.md)
[来源] wiki_001.md | 数学 / 数学的各领域
如上所述，数学主要的学科最先产生于商业上计算的需要、了解数字间的关系、测量土地及预测天文事件。这四种需要大致地与数量、结构、空间及变化（即算术、代数、几何及分析）等数学上广泛的子

2. (wiki_001.md)
[来源] wiki_001.md | 数学
# 数学

数学是研究数量、结构以及空间等概念及其变化的一门学科，属于形式科学的一种。数学利用抽象化和逻辑推理，从计数、计算、量度、对物体形状及运动的观察发展而成。数学家们拓展这些概念，以公式化新

3. (wiki_011.md)
[来源] wiki_011.md | 政治学 / 研究对象
基于对政治的不同看法，对政治学的研究对象也有不同的见解。
国家科学认为政治本身是一种国家活动，因此政治学是研究国家现象的科学。而以大卫·伊斯顿为首的政治学者则认为政治学的研究对象是

4. (wiki_028.md)
[来源] wiki_028.md | 测绘学
# 测绘学

测绘学研究测定和推算地面几何位置、地球形状及地球重力场，据此测量地球表面自然物体和人工设施的几何分布，编制各种比例尺地图的理论和技术的学科。测绘学的研究对象是地球的形态、位置、重力

5. (wiki_001.md)
[来源] wiki_001.md | 数学 / 形成、纯数学与应用数学及美学
每当有涉及数量、结构、空间及变化等方面的问题时，通常就需要用到数学去解决问题，而这往往也拓展了数学的研究范畴。一开始，数学的运用可见于贸易、土地测量及之后的天文学

6. (wiki_051.md)
[来源] wiki_051.md | 植物学 / 系统植物学
系统植物学属于系统生物学的一个分支，该学科关注各生物的分布范围、差异及相互关系，尤其注重生物的演化历史。它的相关学科包括生物分类、科学分类学和系统发生学。植物学家在分类物种时会依

7. (wiki_001.md)
[来源] wiki_001.md | 数学 / 数学作为科学
另一观点则为某些科学领域（如理论物理）是其公理为尝试著符合现实的数学。而事实上，理论物理学家齐曼（John Ziman）即认为科学是一种公众知识，因此亦包含著数学。在任何的情况下

8. (wiki_013.md)
[来源] wiki_013.md | 社会学
社会学的研究范围广泛，包括了由微观社会学层级的机构或人际互动，至宏观社会学层级的社会系统或结构，社会学的本体有社会中的个人、社会结构、社会变迁、社会问题和社会控制，因此社会学通常跟财政学、经济学

9. (wiki_001.md)
[来源] wiki_001.md | 数学 / 数学作为科学
数学家对此的态度并不一致。一些研究应用数学的数学家觉得他们是科学家，而那些研究纯数学的数学家则时常觉得他们是在一门较接近逻辑的领域内工作，且因此基本上是个哲学家。许多数学家认为称

10. (04_react核心范式详解.md)
[来源] 04_react核心范式详解.md | Agent 全面爆发！一文搞懂背后的核心范式 ReAct / ReAct 工作原理 / 循环迭代阶段
每轮迭代严格遵循"推理-行动-观察"的顺序：

1. Thought（推理）：模型基于"

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

3. (wiki_019.md)
[来源] wiki_019.md | 化学 / 词源
英语中的「化学」（chemistry）一字的语源有多种说法。一种说法认为是由「炼金术」（alchemy）得名的。英语中「alchemy」一词源于古法语的「alkemie」和阿拉伯语的「a

4. (wiki_001.md)
[来源] wiki_001.md | 数学
# 数学

数学是研究数量、结构以及空间等概念及其变化的一门学科，属于形式科学的一种。数学利用抽象化和逻辑推理，从计数、计算、量度、对物体形状及运动的观察发展而成。数学家们拓展这些概念，以公式化新

5. (wiki_024.md)
[来源] wiki_024.md | 心理学 / 词源
西语中的“心理学”（psychology）一词由希腊语词根，「灵魂」（gre|ψυχή）和「研究」（gre|λόγος）所组成，最早由克罗地亚诗人马尔科·马鲁利奇使用。
「心理学」汉译

6. (wiki_001.md)
[来源] wiki_001.md | 数学 / 数学作为科学
卡尔·弗里德里希·高斯称数学为「科学的皇后」。在拉丁原文"Regina Scientiarum"，以及其德语"Königin der Wissenschaften"中，对应于「科

7. (wiki_016.md)
[来源] wiki_016.md | 物理学 / 历史
「物理」一词在英文里是「physics」，最先出自于古希腊文「φύσις」，原意是「自然」。在中文里，「物理」最早可在战国时期佚书《鹖冠子·王𫓧篇》「愿闻其人情物理所以啬万物与天地总与

8. (wiki_003.md)
[来源] wiki_003.md | 文学 / 名称
西欧literature的狭义，其中文或日语的对译「文学」始于1908年颜惠庆主编的《英华大辞典》。《英华大辞典》的literature词条有4条释义，明定了以「文学」对译第3义「除哲理

9. (wiki_053.md)
[来源] wiki_053.md | Wiki / 词源
"wiki" 取自夏威夷的Wiki Wiki公车，源自夏威夷语「wiki」，本是「快速」之意。wiki的中文翻译有维客、围纪、快纪、共笔和维基等等，其中「维基」一词是中文维基百科人特

10. (wiki_002.md)
[来源] wiki_002.md | 哲学 / 古希腊-罗马
古希腊-罗马哲学是西方哲学的一个时期，时间为公元前6世纪到公元6世纪。它一般被分为三个时期：前苏格拉底时期、柏拉图和亚里士多德的古典希腊时期、和后亚里士多德（或希腊化）时期：有时

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
[来源] wiki_001.md | 数学 / 数学作为科学
卡尔·弗里德里希·高斯称数学为「科学的皇后」。在拉丁原文"Regina Scientiarum"，以及其德语"Königin der Wissenschaften"中，对应于「科

4. (wiki_001.md)
[来源] wiki_001.md | 数学 / 数学的各领域
如上所述，数学主要的学科最先产生于商业上计算的需要、了解数字间的关系、测量土地及预测天文事件。这四种需要大致地与数量、结构、空间及变化（即算术、代数、几何及分析）等数学上广泛的子

5. (wiki_001.md)
[来源] wiki_001.md | 数学 / 形成、纯数学与应用数学及美学
每当有涉及数量、结构、空间及变化等方面的问题时，通常就需要用到数学去解决问题，而这往往也拓展了数学的研究范畴。一开始，数学的运用可见于贸易、土地测量及之后的天文学

6. (wiki_088.md)
[来源] wiki_088.md | 数论 / 古代
数论早期也称为算术，而算术一词则表示「基本运算」，在现代数论诞生前，早期铺垫有三大内容：

7. (wiki_001.md)
[来源] wiki_001.md | 数学 / 历史
在最初有历史记录的时候，数学内的主要原理是为了做税务和贸易等相关计算，为了解数字间的关系，为了测量土地，以及为了预测天文事件而形成的。这些可以简单地被概括为数学对数量、结构、空间及时间方

8. (wiki_002.md)
[来源] wiki_002.md | 哲学
# 哲学

哲学是研究普遍的、基本问题的学科，包括存在、知识、价值、理智、心灵、语言、人生、道德等领域。哲学与其他学科不同之处在于哲学有独特之思考方式，例如批判的方式、通常是系统化的方法，并以理性

9. (wiki_001.md)
[来源] wiki_001.md | 数学
# 数学

数学是研究数量、结构以及空间等概念及其变化的一门学科，属于形式科学的一种。数学利用抽象化和逻辑推理，从计数、计算、量度、对物体形状及运动的观察发展而成。数学家们拓展这些概念，以公式化新

10. (wiki_001.md)
[来源] wiki_001.md | 数学 / 符号、语言与精确性
我们现今所使用的大部分数学符号在16世纪后才被发明出来的。在此之前，数学以文字的形式书写出来，这种形式会限制了数学的发展。现今的符号使得数学对于专家而言更容易掌握，但初学者

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

2. (wiki_011.md)
[来源] wiki_011.md | 政治学 / 政治哲学
传统的政治哲学研究政治问题主要从哲学思辨的角度，从形而上的角度探讨政治生活中的最高准则，民主、正义、自由、平等等价值取向和相应的政体设计是其研究的重点。大多数政治学家一般先通过先验

3. (wiki_002.md)
[来源] wiki_002.md | 哲学 / 研究基础
古希腊哲学家经常提出问题，他们所提出的问题大概可以归类为三类，这三类问题分别形成了哲学的基础学科——分别是形而上学、伦理学、认识论 。
现代哲学上出现"不要求精确理由"之哲学理论，例

4. (wiki_023.md)
[来源] wiki_023.md | 生物学 / 尚未解决的生物学基本问题
尽管我们近几十年来对于生命的基本过程的认识取得了的深刻进步，一些基本的问题仍然没有得到解决。例如，在生物学的主要未解决的问题之一是性别的主要自适应功能，和特别是在真

5. (wiki_002.md)
[来源] wiki_002.md | 哲学 / 哲学的定义
哲学家们对哲学本身的定义存在分歧。没有共同的共识，这归因于哲学本身的性质是一个开放的哲学问题。许多伟大的哲学家，如柏拉图、黑格尔等，对问题“什么是哲学？”提出了答案，但这些答案在今

6. (thucnews_0058.md)
[来源] thucnews_0058.md | 留学访谈实录：澳际专家谈国际教育巡回展
主持人：其实常规的教育展或者是比较大型的教育展一年只有四次，而且每年秋天的这一次是规模最大的。今年的的这一次叫做2007金秋国际教育巡回展，今年的巡回展

7. (wiki_002.md)
[来源] wiki_002.md | 哲学 / 黑格尔
他认为，为了达到这个“绝对精神”，需要经过三个阶段，从逻辑、自然到精神，即是从思维到存在，再到两者统一的过程，从而完成他的统一论。
就此，社会和历史的现象，便被赋予一种在哲学史上还是崭

8. (wiki_009.md)
[来源] wiki_009.md | 音乐 / 理论
古希腊哲学家毕达哥拉斯，将音乐解释为“数”的和谐在时间中的表达。
古代伟大音乐家的创作和民歌的流行基本是凭借灵感产生的，后来的学者在研究这些能流行多年的音乐，逐渐总结出理论，其后的音乐家

9. (wiki_002.md)
[来源] wiki_002.md | 哲学 / 前苏格拉底时期
公元前6世纪末，以毕达哥拉斯为主的毕达哥拉斯学派所主张的哲学与前述的观点既相近又有不同。罗马古代的历史上记载毕达哥拉斯第一个称自己为哲学家，或者说是爱智慧。他认为“一切都是数字

10. (wiki_005.md)
[来源] wiki_005.md | 计算机科学 / 计算理论
按照Peter J. Denning的说法，计算机科学的最根本问题是“什么能够被有效地自动化？”计算理论的研究就是专注于回答这个根本问题，关于什么能够被计算，去实施这些计算又需

## 五、百科（6 题，语料：中文维基） Q25 [文件HIT5] [短语HIT5]

Q: 现代意义上的哲学主要与哪些学科相关？

来源: wiki_002.md | 语料中存在: True

A(要点): 形而上学、认识论、伦理学和美学

top-5 短语命中: ['伦理学和美学']

top-5 短语缺失: （无）

1. (wiki_002.md)
[来源] wiki_002.md | 哲学 / 现代哲学（19-20世纪）
从19世纪中叶开始，西方哲学就进入现代哲学阶段。因为在19世纪中期，欧洲的工业革命几近完成。
现代哲学，特别是19世纪中后期的哲学流派，有叔本华的意志主义，新康德主

2. (wiki_002.md)
[来源] wiki_002.md | 哲学
# 哲学

哲学是研究普遍的、基本问题的学科，包括存在、知识、价值、理智、心灵、语言、人生、道德等领域。哲学与其他学科不同之处在于哲学有独特之思考方式，例如批判的方式、通常是系统化的方法，并以理性

3. (wiki_002.md)
[来源] wiki_002.md | 哲学 / 早期近代哲学
西方哲学史上的近代早期一般指17世纪和18世纪，其中18世纪常被称为启蒙时代。现代哲学不同于其前身，它和传统权威例如教会、学院、亚里士多德的关系更加独立，出现了对知识基础和形而上

4. (wiki_002.md)
[来源] wiki_002.md | 哲学 / 特殊分支
这些分支是应用在其他学科，或者交叉学科的哲学研究。

5. (wiki_002.md)
[来源] wiki_002.md | 哲学 / 主分支
哲学可以分为很多不同的分支，主要包括形而上学、知识论、伦理学、逻辑学和美学。

6. (wiki_020.md)
[来源] wiki_020.md | 地理学 / 研究范畴
古代的地理学主要探索测量地球形状、大小的方法，描述已知的国家和地区。传统上，地理学有四个基本的研究范畴：
相比之下，现代地理学则是涵盖多重学科的大学问。历经科学化的辩证和计量革命，

7. (wiki_002.md)
[来源] wiki_002.md | 哲学 / 后古典现代哲学
分析哲学：
实证主义：
新康德主义：
逻辑实证主义：
语言哲学：
现象学：
唯物论：
新托马斯主义：

8. (wiki_002.md)
[来源] wiki_002.md | 哲学 / 希腊化时代
亚里士多德死后，整个哲学界陷入了独立时期，称为希腊化哲学时期。因为整个社会和政治陷入混乱。这段时期产生了斯多葛学派和伊壁鸠鲁学派，以及怀疑主义派、新柏拉图派和新毕达哥拉斯主义。这些

9. (wiki_002.md)
[来源] wiki_002.md | 哲学 / 研究基础
古希腊哲学家经常提出问题，他们所提出的问题大概可以归类为三类，这三类问题分别形成了哲学的基础学科——分别是形而上学、伦理学、认识论 。
现代哲学上出现"不要求精确理由"之哲学理论，例

10. (wiki_001.md)
[来源] wiki_001.md | 数学 / 数学的各领域
如上所述，数学主要的学科最先产生于商业上计算的需要、了解数字间的关系、测量土地及预测天文事件。这四种需要大致地与数量、结构、空间及变化（即算术、代数、几何及分析）等数学上广泛的子

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
[来源] wiki_003.md | 文学
文学（literature），在狭义上，是一种语言艺术，亦即使用语言文字为手段，形象化地反映客观社会生活、表达主观作者思想感情的一种艺术。文学不仅强调传达思想观念，更强调传达方式的独特性，且讲究辞

3. (wiki_003.md)
[来源] wiki_003.md | 文学 / 文学史
许多古文明都有其对哲学或是相关观点的文学，像是古中国、古印度、波斯及希腊罗马古典时代的作品。许多古代的作品，就算是叙事的形式，都还是有道德或是教诲上的目的，像梵语的《五卷书》或是奥维德

4. (wiki_065.md)
[来源] wiki_065.md | 中国 / 文学及书籍
中国文学从先秦始，通过诗经、楚辞、汉赋、晋书、唐诗、宋词、元曲，以及明清章回小说、民国杂文、共产文学、网路文章等持续发扬。「文学」一词最早见于《论语·先进篇》。经史子集是传统中国的

5. (wiki_003.md)
[来源] wiki_003.md | 文学 / 中文文学史
在很长一段时间，中国的文学与史学和神话并无明显的界限，最早的文学是对历史和神话的记录。但纯粹的文学早在周时就已出现，例如《诗经》。中国古代的文学主要著重在哲学、史学史、军事学、农业

6. (wiki_003.md)
[来源] wiki_003.md | 文学 / 文学史
各种文学都可以视为是文字的纪录，文学本身可能是写实或是虚构，但都可以描绘出一些事实，例如主角的动作及言语、作者的写作风格，以及文字后的含义等。这些情节不只是娱乐性的，其中也包括了经济、

7. (wiki_003.md)
[来源] wiki_003.md | 文学 / 文学技巧
是文学创作者应用在文学中，制造特别效果的方式。文学技巧的范围很广，包括作品是否要用第一人称或是其他人称、用传统的线性叙事或是、或是文类选择都包括在内。这可以让读者感受到一些熟悉的结构

8. (wiki_003.md)
[来源] wiki_003.md | 文学 / 文学体裁
中国古典文学分为诗和文，文又分为韵文和散文，中国的抒情诗和文言文最早而比较发达。
文学一般分为小说、散文、诗歌、剧本，并称为四大文学体裁；

9. (wiki_067.md)
[来源] wiki_067.md | 中华民国 / 文学出版
台湾原住民族口传文学是最早开始流传的台湾文学。古典汉诗文学源于17世纪，在明郑时期、清治时期、日治时期持续维持一定创作人口，但其内容因身份认同而有所转变。在日治时期还发展出吸收西

10. (wiki_004.md)
[来源] wiki_004.md | 历史 / 史学史
原始社会中人类没有文字，只能通过诸如结绳记事和口传等方法作记录，一些历史的痕迹通过“传说”保存了下来，例如中国上古传说“黄帝战蚩尤”、“女娲补天”、“大禹治水”等。国家出现后，则开始有

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

3. (thucnews_0089.md)
[来源] thucnews_0089.md | 调查：哪个星座最容易出改变世界的人物(图)
今天我们就想出一个话题：你觉得哪个星座最容易出改变世界的人物？

4. (wiki_068.md)
[来源] wiki_068.md | 宗教 / 词源
在汉语中，宗、教二词各有其义，本不为一个统一的联缀词。按《说文解字》：「宗者，尊祖庙也，以宗从示。」，「示者，天垂象见吉凶所以示人也，从二。三垂，日月星也，观乎天文以察时变示神事也。」故

5. (wiki_105.md)
[来源] wiki_105.md | 广东省 / 伊斯兰教
目前仅广州、肇庆有约2万名穆斯林。建于广州的怀圣寺光塔可以追溯到唐宋时期。
现代，主要来自新疆的穆斯林小群落近年也开始迁入深圳市，经营标榜清真风味的面馆。在梅林附近有一所清真寺，文

6. (cmrc_001.md)
[来源] cmrc_001.md | 范廷颂
# 范廷颂

7. (wiki_065.md)
[来源] wiki_065.md | 中国 / 基督宗教
道方向，给中国教会制订了一套全备的传教典章，为中国教务竖立了一个新的里程碑。会议中主教们决定了把中国奉托给圣母照顾保护，并奉圣母为「中华母后」，事经圣座核准施行，会议开幕时举行了隆重

8. (wiki_115.md)
[来源] wiki_115.md | 江苏省 / 宗教
江苏省佛教、道教、伊斯兰教、天主教、基督新教五大宗教齐全。全省有信教群众570多万人，各类宗教教职人员9千多人，有5名宗教人士担任全国宗教团体的负责人。全省登记的宗教活动场所6100多

9. (wiki_110.md)
[来源] wiki_110.md | 海南省 / 宗教
在内地文化还未深入海南岛之前，海南岛的黎苗地区盛行原始崇拜，尤以祖先崇拜与自然崇拜为主，崇拜对象繁多，生产生活中处处伴随着原始崇拜，影响很深，处于原始宗教信仰阶段。
748年，汉传佛教

10. (wiki_068.md)
[来源] wiki_068.md | 宗教 / 儒教的宗教性争议
清末救亡图存的动乱中，康有为等人，试图仿效西方基督教国家的国教习惯，将儒家改造成宗教，立为国教。此举引发了孔教争论。1917年中，「将孔教立为国教」的方案受到挫败。另一方面，

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
[来源] wiki_056.md | 中国历史 / 民变与灭亡
元廷派兵镇压各地红巾军，丞相脱脱亲自率军南下攻陷徐州芝麻李军，一度压制民变军。然而脱脱在1354年南攻高邮张士诚军之际，被元廷大臣弹劾而功亏一篑。徐寿辉部最后分裂成两湖的陈友谅

4. (cmrc_001.md)
[来源] cmrc_001.md | 范廷颂
# 范廷颂

5. (wiki_056.md)
[来源] wiki_056.md | 中国历史 / 建国与统一
元朝末期，官员贪污，朝政腐败。为消除赤字，元廷加重赋税，大量滥印新钞“至正宝钞”，随之产生的通货膨胀加上荒灾、黄河泛滥等天灾使得民不聊生。1351年元顺帝派贾鲁治理黄河，征调各

6. (wiki_110.md)
[来源] wiki_110.md | 海南省 / 古代史
五代十国，海南岛属于南汉。
宋朝，海南岛与今广西壮族自治区的大部分一起属于广南西路。
元朝，原广南西路划归湖广行省管辖，海南岛亦随同划到湖广行省之下。
明朝，琼州府隶属于广东省，治所

7. (wiki_056.md)
[来源] wiki_056.md | 中国历史 / 危机与改革
隆庆帝和万历帝初期，在内阁首辅高拱和张居正及宦官冯保的辅政之下曾一度中兴，国势鼎盛，此时银钱透过国际贸易流入中国，明朝经济达到全盛。万历年间，日本太合丰臣秀吉发动朝鲜之役，使明

8. (cmrc_004.md)
[来源] cmrc_004.md | NGC 6231
# NGC 6231

NGC 6231是一个位于天蝎座的疏散星团，天球座标为赤经16时54分，赤纬-41度48分，视觉观测大小约45角分，亮度约2.6视星等，距地球5900光年。NG

9. (wiki_043.md)
[来源] wiki_043.md | 孙中山 / 惠州起义与赴美
1900年1月，孙中山为菲律宾起义军购妥第二批军械。1月24日，杨衢云辞去兴中会会长职，次日陈少白在香港创办《中国日报》。在义和团运动浪潮下，英国竭力保全既得利益，主导「东南

10. (thucnews_0140.md)
[来源] thucnews_0140.md | 1月28日美股专家坐堂实录
网友[匿名]问： 首先感谢老师假日期间仍不辞劳苦为大家服务，祝老师新年里身体健康，万事如意。今天想请教老师，中信国安可以持有吗？他压力位及支撑位在哪儿？中金岭南还能

## 六、百科问答（6 题，语料：CMRC2018 / DRCD） Q29 [文件HIT5] [短语HIT5]

Q: 范廷颂在 1995 年至 2001 年期间担任过什么职务？

来源: cmrc_001.md | 语料中存在: True

A(要点): 天主教越南主教团主席

top-5 短语命中: ['天主教越南主教团主席']

top-5 短语缺失: （无）

1. (cmrc_001.md)
[来源] cmrc_001.md | 范廷颂
范廷颂枢机（，），圣名保禄·若瑟（），是越南罗马天主教枢机。1963年被任为主教；1990年被擢升为天主教河内总教区宗座署理；1994年被擢升为总主教，同年年底被擢升为枢机；2009年2月离世。

2. (cmrc_001.md)
[来源] cmrc_001.md | 范廷颂
我信天主的爱」。由于范廷颂被越南政府软禁差不多30年，因此他无法到所属堂区进行牧灵工作而专注研读等工作。范廷颂除了面对战争、贫困、被当局迫害天主教会等问题外，也秘密恢复修院、创建女修会团体等。1

3. (cmrc_001.md)
[来源] cmrc_001.md | 范廷颂
# 范廷颂

4. (03_rag五大范式与演进.md)
[来源] 03_rag五大范式与演进.md | 最全梳理：一文搞懂 RAG 技术的 5 种范式 / 发展历程
自 2021 年 RAG 技术出现之后，RAG 首先被用于 LLMs 的预训练阶段来增强语言模型，随后被用于微调与推理任务中。自 

5. (cmrc_077.md)
[来源] cmrc_077.md | 胡燕泳
胡燕泳（），香港新闻从业员。2001年胡在香港中文大学新闻与传播学院毕业，曾经从事公关工作。2003年转职香港有线电视新闻主播，并于同年转职到24小时亚视新闻台。2006年获奖学金，留学伦敦大学

6. (thucnews_0042.md)
[来源] thucnews_0042.md | 彩云追福双色球08099期条件分析：红球三区有反弹
2 5 8 11 14 17 20 23 26 29 32 2-3重点码 11 14 17 20 29 条件错误，出号11

7. (cmrc_099.md)
[来源] cmrc_099.md | 郑国光
任职资格；1997年9月—1998年7月，挂职任福建省气象局副局长、党组成员）。1998年12月，任中国气象局监测网络司司长。1999年8月，任中国气象局党组成员、副局长。2007年3月，任中国

8. (thucnews_0042.md)
[来源] thucnews_0042.md | 彩云追福双色球08099期条件分析：红球三区有反弹
1 12 13 24 25 1-2重点12 13 25 条件错误，未出号

9. (wiki_064.md)
[来源] wiki_064.md | 高德纳 / 学术成就
1979年卡特总统颁与国家科学奖。1996年11月荣获京都奖。

10. (thucnews_0042.md)
[来源] thucnews_0042.md | 彩云追福双色球08099期条件分析：红球三区有反弹
2 5 8 11 14 17 20 23 26 29 32 2-3重点码14 17 23 26 29

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

3. (wiki_034.md)
[来源] wiki_034.md | 中华人民共和国 / 交通运输
中华人民共和国拥有发展中国家里最完善的交通网络，拥有堪比发达国家的基础建设，并且还有大量的高铁，高速公路和机场在建设中。拥有由铁路系统、公路系统、航空系统、船运系统、管道构

4. (wiki_105.md)
[来源] wiki_105.md | 广东省 / 公路
广东高速公路是中国华南地区重要的交通网络系统。广东省内的第一条高速公路是1989年建成通车的广佛高速公路，2014年全省高速公路通车里程突破6000公里，跃居全国第一；2015年，高速

5. (drcd_002.md)
[来源] drcd_002.md | 广州
# 广州

广州是京广铁路、广深铁路、广茂铁路、广梅汕铁路的终点站。2009年末，武广客运专线投入运营，多单元列车覆盖980公里的路程，最高时速可达350公里/小时。2011年1月7日，广珠城际铁

6. (wiki_034.md)
[来源] wiki_034.md | 中华人民共和国 / 能源与矿产
中华人民共和国经济具高度能源密集和耗能倾向，为能源消耗量最大（温室气体排放量最大）、及能源生产最多的国家。2014年生产约5.523兆千瓦·时电力，发电装机容量有13.6

7. (drcd_039.md)
[来源] drcd_039.md | 广州
塞的问题，广州市目前正进行大规模的地铁扩建，在建里程超过300公里。计划到2020年，广州地铁将运行15条线路，总长度超过500公里。广州市第一条有轨电车线路海珠有轨电车目前已在2014年12月3

8. (wiki_105.md)
[来源] wiki_105.md | 广东省 / 天主教
广东天主教信徒计有20万人，大部分属于汕头教区。肇庆是明代传教士利玛窦首先进入的中国城市（1583年）。广州教区的石室圣心大教堂是一座著名的哥德式建筑，建在潮州市的圣母进教之佑大堂规

9. (drcd_034.md)
[来源] drcd_034.md | 广州
# 广州

广州的对外交流始于汉朝，历经多个朝代后，航运商业仍旧相当发达，至今与多个国家建立交流平台。中国实施改革开放后，美国率先于1979年在广州开设领事馆，之后外国驻穗领馆不断增加，至2016

10. (thucnews_0034.md)
[来源] thucnews_0034.md | 湖南福彩彩民中奖700万被疑假票关押三年
次日，即12月17日，曹鹏飞遇到了于海。“什么时候能兑奖？”于海问。“彩票已经送到省里去了。等通知。”曹鹏飞说，“不过，彩票有些对不上唉。”“有这样的

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

3. (drcd_002.md)
[来源] drcd_002.md | 广州
# 广州

广州是京广铁路、广深铁路、广茂铁路、广梅汕铁路的终点站。2009年末，武广客运专线投入运营，多单元列车覆盖980公里的路程，最高时速可达350公里/小时。2011年1月7日，广珠城际铁

4. (wiki_105.md)
[来源] wiki_105.md | 广东省 / 航空
，广东省境内已有民用运输机场9座、通用机场9座，公共运输航空公司8家（中国南方航空、汕头航空、珠海航空、九元航空、深圳航空、东海航空、顺丰航空、中航货运航空）。

5. (wiki_034.md)
[来源] wiki_034.md | 中华人民共和国 / 航空航天
1954年7月3日，中华人民共和国生产的第一架飞机初教-5在南昌首飞成功，结束了中国不能制造飞机的历史。1956年7月19日，中华人民共和国首架喷气式歼击机歼5原型机在沈阳

6. (wiki_034.md)
[来源] wiki_034.md | 中华人民共和国 / 交通运输
，2019年底建成的北京大兴国际机场被誉为“新国门”，成都天府国际机场等大型机场在疫情后也呈现客流量增加的趋势。波音公司估计中华人民共和国的民航机数量从2014年的2570

7. (wiki_060.md)
[来源] wiki_060.md | 上海市 / 航空
上海是中国的三大航空枢纽之一，拥有虹桥与浦东两座国际机场，2019年运送旅客1亿2179万人次，年货邮吞吐量405.7万吨。两机场年起降飞机78.4万架次，均被中国东方航空与中国国际航

8. (wiki_106.md)
[来源] wiki_106.md | 贵州省 / 航空
贵州省有民航机场11个，其中，4E级干线机场1个，为贵阳龙洞堡国际机场；4C级支线机场10个，分别为遵义茅台机场、铜仁凤凰机场、黔西南兴义万峰林机场、安顺黄果树机场、遵义新舟机场、黔东

9. (wiki_112.md)
[来源] wiki_112.md | 黑龙江省 / 航空
省内有两座国际机场：哈尔滨太平国际机场、牡丹江海浪国际机场，三座国内机场：齐齐哈尔三家子机场、萨尔图机场和佳木斯东郊机场，航线通往全国重要城市和境外城市。支线机场数量居国内前列，覆盖

10. (wiki_110.md)
[来源] wiki_110.md | 海南省 / 航空
总部设于海口的海南航空是海南省唯一一家基地航空公司，通航航线覆盖五大洲。
海南省共有4个民用机场：

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

2. (drcd_013.md)
[来源] drcd_013.md | 广州
历年来，广州当局积极进行各类政府工程。广州市自1990年开始参与「创建全国卫生城市」，于2008年成功取得该「称号」。1998年开始「创建全国文明城市」，2011年成功。「创卫」期间，广州市区的卫

3. (drcd_010.md)
[来源] drcd_010.md | 广州
# 广州

作为近代革命发源地之一，广州自中华民国代时就是中国社会运动的中心之一。每次全国性的社会运动都有广州民众的响应和参与。以广州为中心的较具规模的社会运动，最早有1925年至1926年在广州

4. (drcd_033.md)
[来源] drcd_033.md | 广州
广州作为中国近现代革命的策源地，19世纪末，辛亥革命元老中国现代教育奠基人何子渊、丘逢甲等于此地积极创办和推广新式学堂，不仅培育一大批思想进步锐意创新的社会精英，而且还催生「折衷中西，融汇古今」的

5. (drcd_036.md)
[来源] drcd_036.md | 广州
# 广州

1949年后，所有的学校的校舍或组织均陆续被解放军广州市军事管制委员会接管，所有私立或教会学校在解放后陆续合并撤销，其中一些学校迁至澳门、香港等地。1954年广州改省辖市。1956年，

6. (drcd_009.md)
[来源] drcd_009.md | 广州
清朝末期，广州爆发了数次武装起义，均以失败告终。1911年10月10日武昌起义后，广东省独立，11月10日成立军政府，推选胡汉民为都督。12月初，广东临时省议会成立，公布21岁以上广东籍人皆有选举

7. (drcd_026.md)
[来源] drcd_026.md | 广州
# 广州

广州在明清时期，曾有18座城门。1920年广州大举开路时全部清拆，现时只剩下西门口等遗址，而由城门衍生出来的地名如大东门、西门口、小北路等仍然使用至今。骑楼是岭南一带常见的建筑形式，广

8. (drcd_009.md)
[来源] drcd_009.md | 广州
占领广州，28日成立广州市军事管理委员会，叶剑英任主席。目前广州市在中华人民共和国政制架构下实行人民代表大会制度，市政府在中共广州市委的领导下运作，政府驻地越秀区。作为广东省的省会，广州市是广东省

9. (drcd_038.md)
[来源] drcd_038.md | 广州
目前广州市辖11个市辖区：荔湾区、越秀区、海珠区、天河区、白云区、黄埔区、番禺区、花都区、南沙区、增城区、从化区。现时的广州市区主要位于越秀区，历史上的广州城区面积一直在扩张；由建城伊始的越秀、东

10. (drcd_027.md)
[来源] drcd_027.md | 广州
北京街曾矗立自清末以来广州最大古书院群。大小马站古书院群，分布于北京路西边的大小马站、流水井街巷两侧约20000平方米的范围内，现存书院12间。其中大马站西侧5间；小马站两侧4间；流水井两侧3间。

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
[来源] langchain_001.md | utils / ClassDef AsyncApiRequest
**AsyncApiRequest**: AsyncApiRequest 类的功能是提供异步 API 请求的封装。

**属性

3. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef AsyncApiRequest
在项目中，AsyncApiRequest 类与 ApiRequest 类共同构成了 API 请求的核心处理机制。ApiRequ

4. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef ApiRequest
- `client` 属性负责创建和获取 httpx 客户端实例。如果当前实例未创建或已关闭，它会根据配置重新创建一个。
- `get`

5. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef ApiRequest / FunctionDef update_docs_by_id(self, knowledge_base_name, docs)
在函数

6. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef ApiRequest / FunctionDef __init__(self, base_url, timeout)
**__init__**: 此函数的功能

7. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef ApiRequest
在项目中，ApiRequest 类被多个模块调用，例如 `dialogue_page`、`knowledge_base_page` 和 

8. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef ApiRequest / FunctionDef client(self)
**输出示例**: 由于此函数的输出是一个 httpx 客户端实例，输出示例将依赖

9. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef ApiRequest / FunctionDef __init__(self, base_url, timeout)
从功能角度看，`__init__`函数通

10. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef ApiRequest / FunctionDef client(self)
**注意**:
- `_client` 是 `ApiRequest` 类的一个私有

## 七、技术文档（6 题，语料：Langchain-Chatchat 中文文档） Q34 [文件HIT5] [短语MISS] 块级漏召回

Q: ApiRequest 类支持同步和异步请求吗？请求失败时会怎样？

来源: langchain_001.md | 语料中存在: True

A(要点): 支持同步和异步请求；请求失败时自动重试

top-5 短语命中: （无）

top-5 短语缺失: ['支持同步和异步请求', '请求失败时自动重试']

全库也缺失: ['支持同步和异步请求']

1. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef AsyncApiRequest / FunctionDef __init__(self, base_url, timeout)
接着，函数设置了一个私有属性`

2. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef AsyncApiRequest
在项目中，AsyncApiRequest 类与 ApiRequest 类共同构成了 API 请求的核心处理机制。ApiRequ

3. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef AsyncApiRequest
**AsyncApiRequest**: AsyncApiRequest 类的功能是提供异步 API 请求的封装。

**属性

4. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef ApiRequest
**ApiRequest**: ApiRequest 类的功能是封装 HTTP 请求，简化与 API 服务器的交互过程。

**属性**

5. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef ApiRequest
在项目中，ApiRequest 类被多个模块调用，例如 `dialogue_page`、`knowledge_base_page` 和 

6. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef ApiRequest / FunctionDef __init__(self, base_url, timeout)
从功能角度看，`__init__`函数通

7. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef ApiRequest / FunctionDef __init__(self, base_url, timeout)
**__init__**: 此函数的功能

8. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef ApiRequest / FunctionDef delete(self, url, data, json, retry, stream)
**输出示例**:

9. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef ApiRequest / FunctionDef _get_response_value(self, response, as_json, value_fun

10. (langchain_001.md)
[来源] langchain_001.md | utils / ClassDef ApiRequest / FunctionDef client(self)
**输出示例**: 由于此函数的输出是一个 httpx 客户端实例，输出示例将依赖

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
[来源] langchain_002.md | base / ClassDef EmbeddingsFunAdapter / FunctionDef aembed_documents(self, texts)
从功能角度看，`aembed_

3. (langchain_002.md)
[来源] langchain_002.md | base / FunctionDef normalize(embeddings)
**注意**:
- 输入的嵌入向量列表需要确保每个向量的维度相同，因为归一化过程涉及到按元素的运算。
- 该函

4. (drcd_049.md)
[来源] drcd_049.md | 函数
# 函数

函数这个数学名词是莱布尼兹在1694年开始使用的，用来描述跟曲线相关的一个量，如曲线的斜率或者曲线上的某一点。莱布尼兹所指的函数现在被称作可导函数，数学家之外的普通人一般接触到的函数即

5. (langchain_002.md)
[来源] langchain_002.md | base / ClassDef EmbeddingsFunAdapter / FunctionDef embed_documents(self, texts)
**embed_document

6. (drcd_050.md)
[来源] drcd_050.md | 函数
# 函数

函数的定义得以扩展之后，数学家便能对一些「奇怪」的数学对象进行研究，例如处处不可导的连续函数。这些函数曾经被认为只具有理论价值，迟至20世纪初时它们仍被视作「怪物」。稍后，人们发现这些

7. (langchain_016.md)
[来源] langchain_016.md | zilliz_kb_service / ClassDef ZillizKBService / FunctionDef vs_type(self)
**vs_type**: vs_type函数的

8. (wiki_097.md)
[来源] wiki_097.md | TeX / 数学公式范例
以二次方程为例，
所有方程式在TeX中都是以一对codice_7符号围住。如果要使公式另起一行居中，那么就用codice_8取代codice_7。例如：

9. (langchain_006.md)
[来源] langchain_006.md | base / ClassDef CachePool / FunctionDef keys(self)
**keys**: 此函数的作用是获取缓存中所有键的列表。

**参数**: 此函数没有参

10. (langchain_021.md)
[来源] langchain_021.md | dialogue / FunctionDef parse_command(text, modal)
**注意**:
- 在使用此函数时，需要确保`modal`对象已正确初始化，以便在需要时能够

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
[来源] langchain_002.md | base / ClassDef EmbeddingsFunAdapter
在项目中，EmbeddingsFunAdapter类被多个模块调用，用于处理不同场景下的文本嵌入需求。例如，在知识库聊

3. (langchain_002.md)
[来源] langchain_002.md | base / ClassDef EmbeddingsFunAdapter / FunctionDef __init__(self, embed_model)
**__init__**: 该函数

4. (langchain_006.md)
[来源] langchain_006.md | base / ClassDef CachePool / FunctionDef load_kb_embeddings(self, kb_name, embed_device, default_

5. (langchain_002.md)
[来源] langchain_002.md | base / ClassDef EmbeddingsFunAdapter / FunctionDef aembed_documents(self, texts)
从功能角度看，`aembed_

6. (langchain_006.md)
[来源] langchain_006.md | base / ClassDef EmbeddingsPool / FunctionDef load_embeddings(self, model, device)
在项目中，`load_emb

7. (langchain_002.md)
[来源] langchain_002.md | base / ClassDef EmbeddingsFunAdapter / FunctionDef aembed_documents(self, texts)
**aembed_docume

8. (langchain_005.md)
[来源] langchain_005.md | base / ClassDef ApiModelWorker / FunctionDef do_embeddings(self, params)
**注意**:
- 在调用`do_embedd

9. (langchain_005.md)
[来源] langchain_005.md | base / ClassDef ApiModelWorker / FunctionDef can_embedding(cls)
**输出示例**: 假设某个类的 `DEFAULT_EMBED_

10. (langchain_002.md)
[来源] langchain_002.md | base / ClassDef EmbeddingsFunAdapter
**EmbeddingsFunAdapter**: EmbeddingsFunAdapter类的功能是对文本进行嵌入表

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

3. (langchain_019.md)
[来源] langchain_019.md | knowledge_file_repository / FunctionDef list_file_num_docs_id_by_kb_name_and_file_name(session, 

4. (langchain_019.md)
[来源] langchain_019.md | knowledge_file_repository / FunctionDef list_docs_from_db(session, kb_name, file_name, metadata)

5. (langchain_010.md)
[来源] langchain_010.md | kb_doc_api / FunctionDef update_info(knowledge_base_name, kb_info)
**update_info**: 此函数用于更新知识库的介

6. (langchain_002.md)
[来源] langchain_002.md | base / ClassDef KBService / FunctionDef exists(self, kb_name)
**exists**: 此函数的功能是检查指定名称的知识库是否存在。

7. (langchain_005.md)
[来源] langchain_005.md | base / ClassDef ApiModelWorker / FunctionDef validate_messages(self, messages)
在项目中，`validate_me

8. (langchain_019.md)
[来源] langchain_019.md | knowledge_file_repository / FunctionDef get_file_detail(session, kb_name, filename)
**注意**:
- 在使

9. (langchain_010.md)
[来源] langchain_010.md | kb_doc_api / FunctionDef download_doc(knowledge_base_name, file_name, preview)
**download_doc**:

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
**validate_kb_name**: 此函数用于验证知识库名称的合法性。


2. (langchain_004.md)
[来源] langchain_004.md | utils / FunctionDef validate_kb_name(knowledge_base_id)
**注意**:
- 在使用此函数时，需要确保传入的参数是字符串类型。
- 函数的

3. (langchain_012.md)
[来源] langchain_012.md | chromadb_kb_service / ClassDef ChromaKBService / FunctionDef get_kb_path(self)
**注意**: 在使用 `get_

4. (langchain_002.md)
[来源] langchain_002.md | base / ClassDef KBService / FunctionDef update_info(self, kb_info)
`add_kb_to_db`函数负责将知识库信息添加或更新

5. (langchain_002.md)
[来源] langchain_002.md | base / FunctionDef get_kb_file_details(kb_name)
**注意**:
- 确保传入的 `kb_name` 在系统中是存在的，否则函数将返回空列表。
-

6. (langchain_018.md)
[来源] langchain_018.md | api / 常用 API 接口调用方式 / RAG 接口 （/knowledge_base/chat/compleitons）
相比于 /chat/chat/completions 接口，本接

7. (langchain_009.md)
[来源] langchain_009.md | faiss_kb_service / ClassDef FaissKBService / FunctionDef get_kb_path(self)
**注意**: 使用`get_kb_pat

8. (langchain_010.md)
[来源] langchain_010.md | kb_doc_api / FunctionDef update_info(knowledge_base_name, kb_info)
**update_info**: 此函数用于更新知识库的介

9. (langchain_008.md)
[来源] langchain_008.md | faiss_cache / FunctionDef _new_ds_search(self, search)
**注意**:
- 函数返回值的类型依赖于查找结果。如果未找到对应的条目，将返回一

10. (langchain_002.md)
[来源] langchain_002.md | base / ClassDef KBServiceFactory / FunctionDef get_service_by_name(kb_name)
**注意**:
- 在调用此函数之前，确

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

5. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
不管怎样的渠道，胡蝶在当选为最美丽的女明星之后，得到的实惠是数不尽的。当时的一些杂志报纸关注胡蝶的一举一动，把胡蝶的打扮从头到脚分析给读者看，以她作为最

6. (thucnews_0034.md)
[来源] thucnews_0034.md | 湖南福彩彩民中奖700万被疑假票关押三年
从资深彩民到诈骗嫌犯，一个手持700万元大奖彩票的人经历怎样的故事？

7. (thucnews_0077.md)
[来源] thucnews_0077.md | 时尚评论：两个中国人在巴黎(图)
尽管早在2001 年就在巴黎开店，这却是夏姿-陈第一次参加巴黎时装周。“我深知只要做过一次，下次就一定要再来，不管是财力还是设计水准，都要足以支持这种连续的发

8. (thucnews_0034.md)
[来源] thucnews_0034.md | 湖南福彩彩民中奖700万被疑假票关押三年
“这样的过程我没有经历过，但我感觉把票给他们不大妥，毕竟于海不在现场。”曹鹏飞说，当时他问了福彩中心在现场的领导：我们要不要打个电话给于海，问个究竟，

9. (thucnews_0077.md)
[来源] thucnews_0077.md | 时尚评论：两个中国人在巴黎(图)
这是设计师谢锋第五次在巴黎时装周上亮相。两年多来，他和他的团队对发布会的制作流程已经上手，但忐忑不安的心情却从没改变。这是台湾时装品牌夏姿-陈首次参加巴黎时装

10. (thucnews_0058.md)
[来源] thucnews_0058.md | 留学访谈实录：澳际专家谈国际教育巡回展
主持人：中国的需求情况到底是怎么样的，据您的了解？

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

4. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
有一次，陈蝶衣下班回家，路途侯车，听得几个人议论胡蝶与阮玲玉谁更美，争执不下，竟吵了起来。

5. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
不管怎样的渠道，胡蝶在当选为最美丽的女明星之后，得到的实惠是数不尽的。当时的一些杂志报纸关注胡蝶的一举一动，把胡蝶的打扮从头到脚分析给读者看，以她作为最

6. (wiki_084.md)
[来源] wiki_084.md | 游戏 / 游戏元素及分类
游戏可以依「玩家要做什么？」分类，一般会称为游戏性，游戏的主要元素也包括道具及规则。

7. (thucnews_0064.md)
[来源] thucnews_0064.md | “欲望都市”：留学生美国风格初体验
虽然这种衣服貌似是魔鬼身材的专利，可也不乏带着游泳圈或者拜拜袖的“XXL”们，也硬是将自己塞了进去，虽然是将自己的缺点暴露无遗，却依然是自信满满的“Who 

8. (wiki_065.md)
[来源] wiki_065.md | 中国 / 城市规划
中国古城邑在规划上，很早便有在水利、交通运输、排水、防灾、工业配套、军事防御等范筹上的考量，对于世界城市规划史发展有显著的影响。
对于古代城市的选址，《管子》一书中就反对商周以来用占

9. (thucnews_0077.md)
[来源] thucnews_0077.md | 时尚评论：两个中国人在巴黎(图)
到目前为止，参加过巴黎高级成衣发布的中国品牌一共有三个：Jefen byFrankie、Wuyong 和夏姿-陈。其中Wuyong 只做了一季展示，Jefen

10. (thucnews_0111.md)
[来源] thucnews_0111.md | 中国肯德基突破3000家 提出生活如此多娇新愿景
不可否认，当下这个年代，精神飞扬，物质丰富，科技昌明，社会进步，但大家是否真正感受到了幸福？早些年前，一件新衣服、一根棒棒糖、一顿肯德基，就可

## 八、资讯新闻（6 题，语料：THUCNews 镜像） Q41 [文件HIT5] [短语HIT5]

Q: 「电影皇后」选举中，胡蝶和阮玲玉分别得第几名？票数是多少？

来源: thucnews_0021.md | 语料中存在: True

A(要点): 胡蝶以21334票评为第一名，阮玲玉只得第三名

top-5 短语命中: ['胡蝶以21334票评为第一名', '阮玲玉只得第三名']

top-5 短语缺失: （无）

1. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
此后，在1934年的十大影星选举中，胡蝶当选的是最美丽的女明星，而阮玲玉则被选为演技最佳的女明星。

2. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
最后，胡蝶以21334票评为第一名，而阮玲玉只得第三名。

3. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
看看老照片，不难发现，胡蝶的姿色并不在阮玲玉之上，阮玲玉本人比照片还要美丽，在过去的一些电影片花中，阮玲玉秀气中有一种妩媚，内里的妖娆与悲哀的性情并存，

4. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
说起来，胡蝶还是比阮玲玉更会做人吧。她们也是共事过的。在影片《白云塔》中，导演张石川要胡蝶演一个正派的小姐，要阮玲玉演一个品质比较坏的小姐。原因是导演喜

5. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
有一次，陈蝶衣下班回家，路途侯车，听得几个人议论胡蝶与阮玲玉谁更美，争执不下，竟吵了起来。

6. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
在这期间，明星公司的胡蝶、联华公司的阮玲玉及天一公司的陈玉梅选票遥遥领先其他演员。

7. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
这给了陈蝶衣一个启发。既然是明星日报，为何不搞个选美活动，这样不是能与大众共鸣互动吗？有了这个想法，陈蝶衣马上行动，这个选美活动定为“电影皇后的选举大会

8. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
不管怎样的渠道，胡蝶在当选为最美丽的女明星之后，得到的实惠是数不尽的。当时的一些杂志报纸关注胡蝶的一举一动，把胡蝶的打扮从头到脚分析给读者看，以她作为最

9. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
究竟什么样的女人才算第一美女？是姿色、名气还是好的人际关系？就说当今的美丽级天后张曼玉、巩俐以及章子怡，谁又是真正的第一美女呢？就连西施、貂婵、杨贵妃也

10. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
说到中国历史上第一次大众参与的选美活动，不得不提到陈蝶衣。陈蝶衣是流行歌曲之王，比较有名的歌曲《南屏晚钟》、《凤凰于飞》、《我的眼里只有你没有他》均出自

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
最后，胡蝶以21334票评为第一名，而阮玲玉只得第三名。

3. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
说起来，胡蝶还是比阮玲玉更会做人吧。她们也是共事过的。在影片《白云塔》中，导演张石川要胡蝶演一个正派的小姐，要阮玲玉演一个品质比较坏的小姐。原因是导演喜

4. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
看看老照片，不难发现，胡蝶的姿色并不在阮玲玉之上，阮玲玉本人比照片还要美丽，在过去的一些电影片花中，阮玲玉秀气中有一种妩媚，内里的妖娆与悲哀的性情并存，

5. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
在这期间，明星公司的胡蝶、联华公司的阮玲玉及天一公司的陈玉梅选票遥遥领先其他演员。

6. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
有一次，陈蝶衣下班回家，路途侯车，听得几个人议论胡蝶与阮玲玉谁更美，争执不下，竟吵了起来。

7. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
不管怎样的渠道，胡蝶在当选为最美丽的女明星之后，得到的实惠是数不尽的。当时的一些杂志报纸关注胡蝶的一举一动，把胡蝶的打扮从头到脚分析给读者看，以她作为最

8. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
究竟什么样的女人才算第一美女？是姿色、名气还是好的人际关系？就说当今的美丽级天后张曼玉、巩俐以及章子怡，谁又是真正的第一美女呢？就连西施、貂婵、杨贵妃也

9. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
这给了陈蝶衣一个启发。既然是明星日报，为何不搞个选美活动，这样不是能与大众共鸣互动吗？有了这个想法，陈蝶衣马上行动，这个选美活动定为“电影皇后的选举大会

10. (drcd_052.md)
[来源] drcd_052.md | 摩爾多瓦
元首的总统职权在国家事务中的权力被削弱。总理作为政府首脑，由议会选举产生。摩议会实行一院制，任期四年。2001年，摩尔多瓦共产党人党在议会选举中获胜，成为当时世界上仅有的三个通过议会民主方式取

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
最后，胡蝶以21334票评为第一名，而阮玲玉只得第三名。

3. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
看看老照片，不难发现，胡蝶的姿色并不在阮玲玉之上，阮玲玉本人比照片还要美丽，在过去的一些电影片花中，阮玲玉秀气中有一种妩媚，内里的妖娆与悲哀的性情并存，

4. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
此后，在1934年的十大影星选举中，胡蝶当选的是最美丽的女明星，而阮玲玉则被选为演技最佳的女明星。

5. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
有一次，陈蝶衣下班回家，路途侯车，听得几个人议论胡蝶与阮玲玉谁更美，争执不下，竟吵了起来。

6. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
在这期间，明星公司的胡蝶、联华公司的阮玲玉及天一公司的陈玉梅选票遥遥领先其他演员。

7. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
不管怎样的渠道，胡蝶在当选为最美丽的女明星之后，得到的实惠是数不尽的。当时的一些杂志报纸关注胡蝶的一举一动，把胡蝶的打扮从头到脚分析给读者看，以她作为最

8. (thucnews_0021.md)
[来源] thucnews_0021.md | 民国时期最美的电影女明星到底是谁(图)
究竟什么样的女人才算第一美女？是姿色、名气还是好的人际关系？就说当今的美丽级天后张曼玉、巩俐以及章子怡，谁又是真正的第一美女呢？就连西施、貂婵、杨贵妃也

9. (cmrc_068.md)
[来源] cmrc_068.md | 林翠
，新天影业的《马路小天使》（1957）、〈流浪儿〉（1958）等。也曾为邵氏拍摄《夜来香》（1957）、《移花接木》（1957）、《千金小姐》（1959）等。1957年11月加盟国际电影懋业(电懋

10. (thucnews_0019.md)
[来源] thucnews_0019.md | 练束梅客串一天得一部戏 《圣天门口》感恩张黎
对于自己能获得“麦香”这个角色，练束梅首当其冲要感谢张黎导演。在《人间正道是沧桑》中，练束梅曾客串了一天戏，而就是这几场戏让黎叔看到了她身上的多面

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
新浪体育讯　记者邱星报道  汤姆-希伯杜，这个名字大家不会陌生。虽然这只是他作为NBA主教练的第一个赛季，但是此前几年，还是助理教练的希伯杜就已

4. (thucnews_0011.md)
[来源] thucnews_0011.md | 希伯杜防守体系初见成效 芝加哥铁牛阵已显露真容
正是这样认真的职业精神，打动了他的同僚和队员。别看希伯杜执教公牛没多久，他在球队中的威信却和一些有着多年经验的老教练无异。

5. (thucnews_0011.md)
[来源] thucnews_0011.md | 希伯杜防守体系初见成效 芝加哥铁牛阵已显露真容
希伯杜一心想要做主教练，公牛满足了他的这个愿望，并引进了卡洛斯·布泽，志在和热火、魔术一较高下。不过，他们的运气不好，布泽一场没打就因伤要休息一

6. (thucnews_0011.md)
[来源] thucnews_0011.md | 希伯杜防守体系初见成效 芝加哥铁牛阵已显露真容
在未来一个赛季里，希伯杜会用球队的表现证明自己的执教水平。其实，他的水平，一些和他合作过的主教练都心知肚明。火箭前主帅杰夫·范甘迪就和希伯杜有过

7. (thucnews_0011.md)
[来源] thucnews_0011.md | 希伯杜防守体系初见成效 芝加哥铁牛阵已显露真容
这些交流都建立在对对手比较了解的基础上，这些了解源于研究，源于大量系统的研究。这些研究，大都是希伯杜一个人整理和完成的，他就是一个工作狂。曾经和

8. (thucnews_0011.md)
[来源] thucnews_0011.md | 希伯杜防守体系初见成效 芝加哥铁牛阵已显露真容
接下来的比赛里，希伯杜考虑给年轻人一些机会，板凳席上表现出色的约翰逊就是其中一员，他有望获得更多的上场时间。希伯杜不会固定使用一套轮换阵容，而任

9. (thucnews_0011.md)
[来源] thucnews_0011.md | 希伯杜防守体系初见成效 芝加哥铁牛阵已显露真容
防守成了这支公牛的一大特色，其实，他们的单兵防守并不算突出，除了诺阿是一个顶尖篮板球员，其他人的防守其实比较一般，可是希伯杜却能通过有效协防战术

10. (thucnews_0011.md)
[来源] thucnews_0011.md | 希伯杜防守体系初见成效 芝加哥铁牛阵已显露真容
新赛季，在他的执教下，公牛已经打了三场比赛，2胜1负，虽然只是三场球，但是已经能看出希伯杜给公牛带来了什么。总结起来很简单，那就是———出色的防

