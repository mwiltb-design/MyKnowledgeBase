Source: [[LanceDB_Official_Overview.md]]

## Summary
- **LanceDB** is an open-source, embedded vector database built on the **Lance** columnar format.
- Serverless and in-process, designed to simplify the management of embeddings for **[[AI Memory]]**.
- Supports **Hybrid Search**, combining semantic vector search with traditional keyword search (**FTS**).

## Key Features
- **Scalability**: Designed to handle massive datasets (billions of vectors) on local disk with 100x faster random access than Parquet.
- **Zero-Copy**: Leverages **Apache Arrow** for efficient data transport between the database and AI models.
- **SQL Compatible**: Allows standard SQL filtering alongside vector similarity searches.

## Agentic Integration
- **[[AI Memory]]**: Ideal for local-first agents requiring persistent, high-performance retrieval-augmented generation (**RAG**).
- **[[Pi Coding Agent]]**: Can be used as a local memory backend for indexing project files.

---
**See also:** [[Qdrant]], [[AI Memory]], [[GraphRAG]].
