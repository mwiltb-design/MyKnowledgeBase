# LLM-Native Wiki

## Summary
A definition of the LLM-Native Wiki framework, which aims to create a persistent, structured, and interlinked knowledge repository for AI-driven synthesis.

**LLM-Native Wiki** is a framework for developing **compounding knowledge ecosystems** through **[[AutoResearch|AI-driven curation]]**.

## The Core Thesis
The prevailing paradigm for LLM interaction is **ephemeral RAG** (on-the-fly retrieval from raw data), which is transactional and lacks cumulative growth. The **LLM-Native Wiki** shifts the focus to a **persistent knowledge substrate** — a structured, interlinked markdown repository acting as an intelligent buffer between the user and their sources.

## Three-Layer Architecture
1. **Raw Sources**: The immutable source of truth (articles, links, PDFs, screenshots).
2. **The Wiki**: The living synthesis of knowledge. A structured, interlinked markdown repository.
3. **The Schema**: The governing conventions for the AI agent (e.g., **[[Second Brain Workflow|Agent.md]]**).

## Core Operations
- **Ingest**: The AI agent scans raw documents, synthesizes content, and propagates updates across **[[Auto Research|entity pages]]**.
- **Query**: The user interacts with the Wiki for cross-document synthesis.
- **Lint**: The AI agent identifies gaps, summarizes topics, and flags contradictions in the **[[Second Brain Workflow|monthly health check]]**.

## Implementation
This pattern is modular and can be deployed with any **[[Pi Coding Agent|CLI agent]]** (Codex, Claude Code). The goal is to share this conceptual pattern with your agent to instantiate a version that fits your unique domain.
