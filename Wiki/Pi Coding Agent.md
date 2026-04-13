Source: [[Pi_Coding_Agent_Technical_Research.md]], [[OpenRouter_GitHub_Research.md]], [[Ollama_Technical_Research.md]], [[Vercel_AI_SDK_Technical_Research.md]]

# Pi Coding Agent

## Summary
- Lean, extensible CLI agent designed for autonomous research, model optimization, and **bash-driven** workflows.
- Features a **Message Queue** architecture with **Compaction** to manage context window overflows.
- Utilizes a **Tree-based Session** model (JSONL) allowing for non-destructive branching and forking.

## Architecture & Loop
- **Message Queue**: Operations are driven by steering messages (post-turn) and follow-up messages (post-completion).
- **Compaction Mechanism**: Summarizes older history to maintain the session's tree structure without losing high-level context.
- **Entry Points**: Primarily CLI (`pi` command) or programmatic SDK (`AgentSessionRuntime`).

## Core Toolset
- **Filesystem**: `read` (view), `write` (create), and `edit` (surgical/diff-based modification).
- **Shell**: `bash` (direct command execution).
- **Navigation**: `grep` (search), `find` (locate), and `ls` (list).

## Inference & Models
- **[[Ollama]] Integration**: `ollama launch pi` for local hosting.
- **Cloud Inference**: Native integration with **[[OpenRouter]]** for accessing **[[Claude 3.7]]**, **[[Llama 3.1]]**, and **[[Gemma 4]]**.
- **Unified SDK**: Leverages **[[Vercel AI SDK]]** patterns for provider abstraction.

## Extension Pattern (Skills)
- **[[Agent Skills|Skills]]**: Markdown-based capability packages (`SKILL.md`) providing specific logic and instructions.
- **Extensions**: TypeScript modules using `pi: ExtensionAPI` to register new tools, commands, and shortcuts.

---
**See also:** [[Agent Skills]], [[AutoResearch]], [[OpenRouter]].
