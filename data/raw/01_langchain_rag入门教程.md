# LangChain RAG 入门教程：构建基于私有文档的智能问答助手

> 来源：https://developer.aliyun.com/article/1660267

## RAG 技术概述及其重要性

传统语言模型如 GPT-4 尽管功能强大，但其知识库受限于训练数据，无法有效访问新增信息或特定领域文档。RAG 技术通过融合两个关键功能模块解决了这一局限：

- 检索系统：从文档集合中精确定位相关信息
- 生成机制：基于检索到的上下文信息生成准确、相关的响应

这种结构设计的优势在于能够构建一个基于特定知识库的 AI 问答系统，有效降低了幻觉（hallucination）现象，显著提升了回答的事实准确性。

## LangChain 框架：RAG 系统的技术基础

LangChain 已成为 RAG 应用开发的主流框架，提供了构建完整 RAG 系统所需的全部核心组件：

- 多格式文档加载器，支持各类文件类型的处理
- 文本分割器，用于将文档切分为可处理的数据块
- 向量存储系统，提供高效的内容索引功能
- 文本嵌入模型，实现文本到向量的转换
- 检索机制，用于查找相关信息
- 链式处理流程，协调整个系统的运行逻辑

## 文档处理与分块策略

RAG 系统的关键步骤是文档的处理与分块，包括：文档加载、将文档分割为适当大小的块、为每个文本块生成向量表示。

```python
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
import os

# 从文件夹加载所有文本文件
documents = []
for filename in os.listdir("documents"):
    if filename.endswith(".txt"):
        loader = TextLoader(os.path.join("documents", filename))
        documents.extend(loader.load())

# 将文档拆分成更小的块，以便更好地检索
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
docs = text_splitter.split_documents(documents)
```

## 向量数据库构建

向量数据库实现基于语义的高效搜索。本实现采用 FAISS 作为向量存储引擎，结合句子转换模型构建嵌入表示：

```python
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"  # 速度和质量的良好平衡
)
vectorstore = FAISS.from_documents(docs, embedding_model)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})  # 检索前 3 个最相关的块
```

## 提示模板设计

RAG 系统的输出质量很大程度上取决于提示模板的设计：

```python
from langchain.prompts import PromptTemplate

prompt_template = """
Answer the question based only on the following context:

Context:
{context}

Question: {query}

Helpful Answer:
"""
prompt = PromptTemplate(input_variables=["query", "context"], template=prompt_template)
```

## RAG 流程集成

```python
from langchain.chains import RetrievalQA

retrieval_qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",  # "stuff" 只是将所有检索到的文档放入提示中
    retriever=retriever,
    return_source_documents=True,  # 在响应中包含源文档
    chain_type_kwargs={"prompt": prompt}
)
result = retrieval_qa({"query": question})
# result["result"] 是回答，result["source_documents"] 是引用来源
```

## 检索策略优化

- 使用 MMR（最大边际相关性）检索器，确保检索到的文档的多样性
- 混合搜索：结合语义和关键词搜索
- 使用 ContextualCompressionRetriever 压缩器，仅提取文档的相关部分

## 文档分块策略优化

分块方式对检索质量有重大影响，尝试递归字符分割：

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", "\n", ". ", " ", ""]  # 尝试在段落/句子边界处分割
)
```

## 常见问题及解决方案

- 检索质量差：使用更高质量的嵌入模型（如 all-mpnet-base-v2）、调整块大小和重叠参数、增加检索文档数量、实现重排序
- 响应质量差：应用更强大的语言模型、优化提示模板、尝试不同的链式策略（如 refine 替代 stuff）、加入示例实现少样本学习
- 性能慢：使用更轻量级的嵌入模型、减小块大小和检索数量、对模型量化、使用更高效的向量存储（Chroma 或 Qdrant）

## 总结

通过上述方法可以构建一个能够基于特定文档集合回答问题的完整 RAG 系统。同样的技术架构适用于任何规模的文档集合。RAG 让开发者能够创建将大型语言模型的通用能力与特定领域知识相结合的系统。
