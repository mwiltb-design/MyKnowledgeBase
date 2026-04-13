# Microsoft GraphRAG Overview

## Source
[Microsoft Research](https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/)

## Summary
A technical overview of Microsoft's GraphRAG framework, which uses knowledge graphs and hierarchical community summarization to enable global reasoning over private datasets.

## Key Concepts
- **Knowledge Graph Augmentation**: Unlike baseline RAG (vector search on text chunks), GraphRAG uses LLMs to extract entities and relationships into a structured graph.
- **Community Summarization**: The graph is partitioned into hierarchical semantic clusters (communities). LLMs pre-summarize these communities to enable "whole dataset reasoning."
- **Provenance**: Every assertion in the generated answer is linked back to specific nodes/edges in the graph and original source text.

## Technical Specs
- **Indexing**: Two-stage process: 1) Entity/Relationship extraction, 2) Hierarchical community clustering.
- **Query Types**: 
    - **Global Search**: Aggregates information across the entire dataset (e.g., "What are the main themes?").
    - **Local Search**: Reasons about specific entities and their immediate neighbors.

## Architectural Diagram
```text
[Private Dataset] 
      |
[LLM Extraction] --> [Entities & Relationships]
      |                      |
[Graph Clustering] <--- [Knowledge Graph]
      |
[Community Summaries]
      |
[User Query] --> [Graph-Based Retrieval] --> [Augmented Prompt] --> [LLM Response]
```
