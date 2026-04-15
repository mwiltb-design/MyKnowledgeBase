# AI Memory

## Summary
A foundational overview of the mathematical and hardware constraints governing LLM memory, specifically focusing on the "Memory Wall," KV caching, and the transition from compute-bound to memory-bound inference.

## The Memory Wall
LLM performance is often bottlenecked not by calculation speed (FLOPs), but by **Memory Bandwidth**—the speed at which data can move from VRAM to the GPU cores.
- **Memory Bound**: Latency is limited by VRAM loading speed (common for small batch sizes/single-user chat).
- **Compute Bound**: Latency is limited by mathematical throughput (common for massive batch processing).

## KV Cache (Working Memory)
The **Key-Value (KV) Cache** is the "short-term memory" of a Transformer.
- **Function**: Stores mathematical representations of previous tokens to avoid re-calculating them for every new token generated.
- **Complexity**: Reduces sampling from quadratic $O(T^2)$ to linear $O(T)$.
- **Scaling**: The KV cache grows linearly with sequence length. In long-context scenarios, the cache can exceed the size of the model weights (e.g., a 60GB model needing a 180GB cache).

## Precision & Optimization
- **Formula**: Memory (GB) = (Parameters × Bits) / 8.
- **Optimization**: Techniques like **Multi-Query Attention (MQA)** and **Quantization** (INT8/FP8) are used to shrink the KV cache footprint, enabling longer context windows on limited hardware like the **[[Gemma 4]]** models.

## Long-Term Storage & Retrieval
Efficient AI agents utilize a hybrid approach for persistence beyond the context window:

### 1. Relational Backends (Exact Retrieval)
- **[[SQLite]]**: Ideal for in-process agent state, conversation logs, and metadata.
- **[[PostgreSQL]]**: Used for production-scale deployments requiring high concurrency and complex data integrity.
- **[[PocketBase]]**: A single-binary solution for rapid backend development.

### 2. Vector Databases (Semantic Retrieval)
- **[[LanceDB]]**: An embedded, local-first vector store for fast RAG and embedding management.
- **[[Qdrant]]**: A high-performance similarity search engine written in Rust for production-grade retrieval.

### 3. Analytical Engines
- **[[DuckDB]]**: Utilized for calculating scalar metrics and analyzing long-term research logs.

## See Also
- **[[Quantization]]**: Model compression techniques.
- **[[MemGPT]]**: Virtual context management.
- **[[GraphRAG]]**: Relational memory structures.
- **[[SQLite]]**: Persistent storage layer.
- **[[LanceDB]]**: Local-first vector storage.
