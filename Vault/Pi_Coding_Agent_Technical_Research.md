# Pi Coding Agent: Technical Research & Architecture

## 1. Core Architecture
Pi Coding Agent is a minimal terminal coding harness built for extensibility. It operates on a **Message Queue** system with a focus on non-destructive branching and compaction.

### Entry Points
- **CLI**: Primary interactive interface (`pi` command).
- **SDK**: Accessible via `createAgentSession` and `AgentSessionRuntime`.

### The Agent Loop
- Supports **Steering Messages** (delivered after the current turn) and **Follow-up Messages** (delivered after completion).
- **Compaction Mechanism**: Automatically summarizes older history to preserve context window while maintaining the session's tree structure.

## 2. Built-in Toolset
Standard tools used by the LLM for filesystem and shell interaction:
- **`read` / `write` / `edit`**: Filesystem operations (including surgical modifications).
- **`bash`**: Direct shell execution.
- **`grep` / `find` / `ls`**: Codebase exploration and navigation.

## 3. State & Configuration
- **Session Persistence**: Stored as **JSONL files** in a tree structure (`id`/`parentId`), allowing for branching (via `/tree` or `/fork`). Sessions reside in `~/.pi/agent/sessions/`.
- **Inference**: Primarily cloud-based (Anthropic, OpenAI, Google, etc.). Supports custom/local endpoints via `models.json` if they follow standard API schemas.
- **Configuration Hierarchy**:
    - Global: `~/.pi/agent/settings.json`
    - Project: `.pi/settings.json`

## 4. Extension Pattern (Skills & Extensions)
- **Skills**: Markdown-based capability packages (`SKILL.md`) providing instructions/steps.
- **Extensions**: TypeScript modules using `pi: ExtensionAPI` to register new tools, commands, and shortcuts.
- **Pi Packages**: Distribution format bundled via `npm` or `git`.

## 5. Tech Stack
- **Language**: TypeScript.
- **Runtime**: Node.js.
- **Core Libs**: `@mariozechner/pi-ai`, `@mariozechner/pi-agent`.
- **Testing**: Vitest.

---
**Source:** [badlogic/pi-mono (packages/coding-agent)](https://github.com/badlogic/pi-mono/tree/main/packages/coding-agent)
**Date Fetched:** 2026-04-12
