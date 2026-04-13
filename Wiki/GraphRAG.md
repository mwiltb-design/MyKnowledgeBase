# GraphRAG

## Summary
A Microsoft-developed framework that enhances standard Retrieval-Augmented Generation (RAG) by using Knowledge Graphs to capture complex relationships and enable global reasoning over entire datasets.

## Relational Memory
While baseline RAG focuses on semantic similarity (vector search), **GraphRAG** focuses on **Structure**.
- **Entity Extraction**: Uses LLMs to identify people, places, and concepts and the relationships between them.
- **Knowledge Graph**: Builds a web of nodes and edges representing the "truth" of a dataset.

## Community Summarization
GraphRAG solves the "Global Query" problem (e.g., "What are the main themes?") by:
1. **Clustering**: Grouping related nodes into "communities."
2. **Summarization**: Generating summaries for these communities at multiple levels of abstraction.
3. **Global Search**: Reasoning over these summaries rather than raw text chunks.

## Provenance
Every claim made by a GraphRAG system is linked to specific nodes in the graph and the original source text, ensuring **high-fidelity citations**.

## See Also
- **[[AI Memory]]**: General architecture.
- **[[Metric Definition]]**: Using scalar metrics to evaluate graph density.
