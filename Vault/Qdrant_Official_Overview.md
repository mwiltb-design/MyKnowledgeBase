# Qdrant Documentation Overview

Qdrant (read: quadrant) is a vector similarity search engine and vector database. It provides a production-ready service with a convenient API to store, search, and manage points—vectors with an additional payload.

## Core Concepts
- **Collections**: A set of points (vectors) among which you can search.
- **Points**: The central entity in Qdrant, consisting of a vector and an optional JSON payload.
- **Distance Metrics**: Supports Cosine, Euclidean, and Dot Product distances for similarity calculations.
- **Payload Filtering**: Allows you to filter search results based on the associated JSON metadata.

## High Performance
Qdrant is written in Rust, which ensures high performance and memory safety even under heavy load. It implements various indexing strategies, including HNSW (Hierarchical Navigable Small World) for fast approximate nearest neighbor search.

## Deployment
Qdrant can be deployed as a standalone Docker container, on Kubernetes, or via the Qdrant Cloud managed service. It also offers a "local mode" for development and small-scale applications.
