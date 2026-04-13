# Mem0 Overview

## Source
[docs.mem0.ai](https://docs.mem0.ai/overview)

## Summary
Overview of Mem0, a "Memory-as-a-Service" layer that provides persistent, personalized, and hybrid (vector + graph) memory for AI agents.

## Key Concepts
- **Managed Memory Layer**: A production-ready, fully managed service for AI agent memory.
- **Hybrid Memory**: Combines vector-based semantic memory with graph-based relational memory.
- **Continuity**: Ensures agents remember user preferences and past interactions across different platforms and sessions without "prompt bloat."

## Technical Specs
- **Features**: Rerankers, async-by-default behavior, and multi-modal support.
- **Compliance**: SOC 2 Type II and GDPR compliant.
- **Integrations**: Native support for LangChain, CrewAI, and Vercel AI SDK.

## Architectural Diagram
```text
[AI Agent] <--> [Mem0 API / SDK]
                     |
        [Managed Infrastructure]
         /           |           \
[Vector Store] [Graph Services] [Rerankers]
         \           |           /
        [Persistent Memory Layer]
```
