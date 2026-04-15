Source: [[Qdrant_Official_Overview.md]]

## Summary
- **Qdrant** is a high-performance vector similarity search engine and database written in **Rust**.
- Designed for production-grade AI applications requiring fast "Top-K" retrieval and filtering.
- Supports both dense and sparse vectors, making it highly versatile for semantic search.

## Core Concepts
- **Collections**: Groupings of **Points** (vectors + JSON payloads).
- **Distance Metrics**: Supports Cosine, Euclidean, and Dot Product for similarity calculation.
- **HNSW Indexing**: Uses Hierarchical Navigable Small World graphs for fast approximate nearest neighbor search.

## Deployment Models
- **Managed**: Available via Qdrant Cloud.
- **Self-Hosted**: Can be deployed via Docker or Kubernetes.
- **Local Mode**: Supports a local, in-memory mode for development and smaller scale agentic tasks.

---
**See also:** [[LanceDB]], [[AI Memory]], [[GraphRAG]].
