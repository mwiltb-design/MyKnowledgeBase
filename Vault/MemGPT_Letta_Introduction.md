# Letta (formerly MemGPT) Introduction

## Source
[letta.com](https://www.letta.com/docs/introduction)

## Summary
Introduction to the "Memory-First" architecture for AI agents, inspired by operating system memory management, enabling persistent states across sessions and virtually infinite context windows.

## Key Concepts
- **Memory-First Architecture**: Agents are designed with persistent memory that survives across sessions, unlike standard stateless LLM calls.
- **Virtual Context Management**: Inspired by OS hierarchical memory (RAM vs. Disk). It manages a "Working Context" (fixed size) and "Archival/Recall Memory" (infinite size).
- **Self-Editing Memory**: Agents use background subagents or specific function calls to update their own persona, human user profiles, and long-term experiences.

## Technical Specs
- **Environment**: Requires Node.js 18+ for CLI; supports Python SDK.
- **Storage**: Uses vector databases for archival memory and relational databases for conversation logs and metadata.
- **Portability**: Agents (including their full memory state) can be moved across different environments or models.

## Architectural Diagram
```text
[User Input] --> [Letta Server]
                     |
        [LLM Context Window (Working Memory)]
         /           |           \
[Core Persona]  [User Profile]  [Recent Chat]
         ^           |           ^
         |    [Memory Subagent]  |
         v           |           v
[Archival Memory (Vector DB)] [Recall Memory (SQL)]
```
