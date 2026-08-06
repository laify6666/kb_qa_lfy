# 解锁企业知识库：基于 LangChain 的 RAG 技术实战指南

> 来源：https://bbs.huaweicloud.com/blogs/480524

## 一、什么是 RAG？为什么它如此重要？

RAG 的核心思想很简单：让大模型"先查资料，再回答"。传统的 RAG 流程通常包含三个主要步骤：

- 检索（Retrieval）：当用户提出问题时，系统先从外部知识库（如向量数据库、文档）中检索出与问题最相关的片段。
- 增强（Augmentation）：将检索到的相关片段与用户的问题拼接，形成一个新的、包含上下文提示的 Prompt。
- 生成（Generation）：将增强后的 Prompt 发送给 LLM，LLM 基于提供的参考资料生成最终答案。

### RAG 的核心优势

- 降低幻觉：答案基于事实依据，而非模型的"记忆"。
- 数据私有化：无需微调模型，即可利用企业私有数据。
- 可解释性：可以提供引用来源，用户可以验证答案的真伪。
- 成本效益：避免了高昂的全量微调成本。

## 二、RAG 的技术架构深度解析

### 1. 文档加载与分割（Loading & Splitting）

原始数据（PDF、Word、网页等）通常是非结构化的。需要将其加载为文本，并切分成较小的块（Chunks）。切分策略直接影响检索质量：

- 固定大小切分：简单但可能切断语义完整性。
- 递归字符切分：按段落、句子递归切分，保留更多语义结构。

### 2. 向量化与嵌入（Embedding）

计算机无法直接理解语义，需要将其转换为数值向量。Embedding 模型将文本映射到多维向量空间中，语义相似的文本，其向量距离在空间中也会相近。

### 3. 向量存储（Vector Store）

将向量化后的数据存入向量数据库（如 Pinecone, Milvus, FAISS, ChromaDB）。这些数据库支持高效的近似最近邻搜索（ANN），能在毫秒级内从百万级数据中找出最相似的向量。

### 4. 检索与重排序（Retrieval & Reranking）

初步检索可能会引入噪声。高级 RAG 系统会引入重排序模型（Reranker），对初步检索结果进行精排，剔除不相关内容，保留最精准的片段。

### 5. 提示工程与生成（Prompt Engineering & Generation）

最终，将检索结果以特定模板注入 Prompt，引导 LLM 基于给定上下文作答。

## 三、实战：使用 LangChain 构建 RAG 应用

### 第一步：加载文档与分割

```python
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

loader = PyPDFLoader("company_manual.pdf")
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)
```

### 第二步：向量化并存储

```python
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

embeddings = OpenAIEmbeddings()
db = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory="./chroma_db")
db.persist()
```

### 第三步：构建检索器

```python
def get_retriever(db, k=3):
    return db.as_retriever(search_type="similarity", search_kwargs={"k": k})
```

### 第四步：构建问答链（QA Chain）

```python
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

template = """
You are an assistant for question-answering tasks.
Use the following pieces of retrieved context to answer the question.
If you don't know the answer, just say that you don't know.
Do not try to make up an answer.
Keep the answer concise.

Context: {context}
Question: {question}

Answer:
"""
prompt = ChatPromptTemplate.from_template(template)
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",  # "stuff" 会将所有检索到的内容拼入一个 prompt
    retriever=retriever,
    chain_type_kwargs={"prompt": prompt}
)
result = qa_chain.invoke({"query": "员工出差住宿费的报销上限是多少？"})
```

### 代码运行逻辑分析

- 用户输入问题后，RetrievalQA 调用 retriever，在向量数据库中搜索与问题语义最接近的 Chunk。
- LangChain 找到 Top 3 的相关段落，将其填入 template 中的 {context} 位置。
- LLM 接收到增强后的 Prompt，阅读上下文，并生成最终答案。

## 四、进阶优化：解决 RAG 的常见陷阱

### 1. 改进文本分割（Chunking Strategy）

- 基于语义的分割：根据语义边界而非固定字符数切分文档。
- 元数据保留：在分割时保留页码、章节标题等元数据，有助于更精准的检索。

### 2. 查询改写（Query Rewriting）

- HyDE（Hypothetical Document Embeddings）：先让 LLM 生成一个"假设的答案"，然后用这个假设答案去检索文档。因为假设答案的语义分布更接近文档中的事实描述，检索效果往往更好。
- 多跳检索（Multi-hop Retrieval）：对于复杂问题，将问题拆解为子问题，分别检索后再综合。

### 3. 引入重排序（Reranking）

向量检索虽然快，但不够精确。使用 Cross-Encoder 模型（如 BGE-Reranker）对向量检索出的 Top-K 结果进行精排。虽然增加了计算延迟，但能显著提升最终答案的准确性。

### 4. 评估体系（RAG Evaluation）

使用 RAGAS 或 DeepEval 等框架对 RAG 系统进行自动化评估，衡量指标包括：

- 上下文召回率（Context Recall）：检索到的内容是否覆盖了答案所需的所有事实。
- 上下文精确率（Context Precision）：检索到的内容是否真的有助于回答。
- 答案相关性（Answer Relevance）：生成的答案是否与问题相关且准确。

## 五、总结与展望

RAG 技术不再追求让模型"记住"一切，而是让模型"学会"如何高效地利用外部知识。随着技术的演进，RAG 正与 Agent（智能体）技术深度融合。未来的 RAG 系统将不仅是被动的问答机器，更是能够主动规划、调用工具、验证信息的智能助手。
