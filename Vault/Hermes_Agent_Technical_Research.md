# Hermes Agent: Technical Research & Architecture

## 1. Core Architecture (Multi-Backend)
Hermes Agent is a platform-agnostic agent featuring a **Unified Messaging Gateway** and isolated execution environments.

### Execution Backends
Supports six isolated environments: **local, Docker, SSH, Daytona, Singularity, and Modal**. Enables environments to hibernate and wake on demand.

### Unified Messaging Gateway
Abstracts multiple protocols (Telegram, Discord, Slack, WhatsApp) into a common internal format, ensuring cross-platform conversation continuity.

## 2. Tools & MCP Integration
- **Model Context Protocol (MCP)**: Acts as an MCP host, dynamically connecting to external servers for tool discovery and execution.
- **Built-in Tools**: 40+ native tools for filesystem, terminal, and web search.
- **Subagent Orchestration**: Spawns isolated subagents via RPC for zero-context-cost parallel turns.

## 3. Model & Inference
- **Providers**: Natively supports **OpenRouter** and Nous Portal.
- **Local Models**: Connects to local servers (Ollama, vLLM) via OpenAI-compatible endpoints.
- **Dynamic Hot-Swapping**: `hermes model` command allows mid-session model switching.

## 4. Memory & Learning
- **Trajectory Compression**: Compresses conversation histories to train future model versions.
- **FTS5 Session Search**: Uses SQLite full-text search for high-speed historical retrieval.
- **Dialectic User Modeling**: Uses **Honcho** to build a profile of user preferences and identity.
- **Procedural Memory (Skills)**: Autonomously creates and stores new "skills" (tool-calling sequences) after task completion.

## 5. Messaging Loop Features
- **Shared Command Interface**: Slash commands (e.g., `/new`, `/model`) are unified across platforms.
- **Interrupt-and-Redirect**: Supports real-time redirection of agent work via new messages.
- **Voice-to-Text**: Built-in transcription for voice memo inputs.

---
**Source:** [nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent)
**Date Fetched:** 2026-04-12
