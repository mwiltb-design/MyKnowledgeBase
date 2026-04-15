# LanceDB Overview

LanceDB is an open-source database for vector search built with persistent storage, which greatly simplifies retrieval, filtering and management of embeddings.

## Key Features
- **Embedded & Serverless**: No database server to manage. It runs in-process with your application, similar to SQLite.
- **Scale to Billions**: Built on the Lance columnar format, which is up to 100x faster than Parquet for random access. It can handle massive datasets on local disk.
- **Full-Text & Vector Search**: Supports hybrid search combining semantic vector search with traditional keyword search (FTS).
- **Zero-Copy**: Leverages Arrow for zero-copy data transport, ensuring extreme performance when moving data between the database and AI models.
- **SQL Compatible**: You can use standard SQL to filter and query your data alongside vector search.

## Integration
LanceDB provides first-class support for Python and Javascript/Typescript, making it the ideal choice for local-first AI agents and RAG applications.
