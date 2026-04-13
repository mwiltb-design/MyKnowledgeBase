Source: [[Hermes_Agent_Technical_Research.md]], [[Ollama_Technical_Research.md]]

# Hermes Agent

## Summary
- Platform-agnostic agent featuring a **Unified Messaging Gateway** and multi-backend execution.
- Acts as an **MCP Host**, dynamically connecting to external tool servers.
- Capable of **Automatic Skill Creation** (Procedural Memory) and cross-session persistence via **[[SQLite]] FTS5**.

## Architecture (Execution Backends)
- **Environments**: Supports 6 isolated backends: **Local**, **Docker**, **SSH**, **Daytona**, **Singularity**, and **Modal**.
- **Hibernation**: Backends like Daytona/Modal allow environments to hibernate and wake on demand.
- **Orchestration**: Spawns isolated subagents via **RPC** for zero-context-cost parallel execution.

## Unified Messaging Gateway
- **Protocol Abstraction**: Unifies Telegram, Discord, Slack, WhatsApp, and CLI into a common internal format.
- **Messaging Loop**: Supports real-time "Interrupt-and-Redirect" and built-in voice-to-text transcription.

## Memory & Learning
- **Search**: Uses **[[SQLite]] FTS5** for high-speed full-text search over conversation history.
- **Dialectic Modeling**: Builds a deepening profile of user preferences and identity (via **[[Honcho]]**).
- **Procedural Memory**: Autonomously stores and retrieves new "skills" (tool-calling sequences) after task completion.

## Model Integration
- **Providers**: Native support for **[[OpenRouter]]**, Nous Portal, and **[[Ollama]]**.
- **Hot-Swapping**: `hermes model` command allows for mid-session model switching.

---
**See also:** [[Agent Skills]], [[OpenRouter]], [[Ollama]], [[Gemma 4]].
