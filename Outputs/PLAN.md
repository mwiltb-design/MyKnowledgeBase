# Knowledge Architecture Plan: Infrastructure & Stubs Ingestion

## Inventory
- `Raw/Vercel_AI_SDK_Technical_Research.md`: Unified provider architecture and agentic loops.
- `Raw/Ollama_Technical_Research.md`: Go-based local inference, API protocols, and Modelfiles.

## New Pages
- [x] **Ollama.md**: Local LLM orchestrator, API (11434), and hardware acceleration (Source: [[Ollama_Technical_Research.md]]).
- [x] **Vercel AI SDK.md**: Provider-agnostic abstraction, Generative UI, and Zod-based object generation (Source: [[Vercel_AI_SDK_Technical_Research.md]]).
- [x] **Claude 3.7.md**: (Stub) Frontier "thinking" model for agentic workflows.
- [x] **SQLite.md**: (Stub) Persistent storage for agent memory (FTS5).
- [x] **Honcho.md**: (Stub) User modeling and profile persistence.

## Updates to Existing
- [x] **Wiki/INDEX.md**:
    - Add **Ollama** and **Vercel AI SDK** to "Agentic Tools".
    - Add **Claude 3.7** to "Technical Domains".
- [x] **OpenRouter.md**: Link directly to [[Vercel AI SDK]].
- [x] **Pi Coding Agent.md**: Link to [[Ollama]] and [[Vercel AI SDK]].
- [x] **Hermes Agent.md**: Link to [[Ollama]], [[SQLite]], and [[Honcho]].
- [x] **Wiki/LOG.md**: Log the ingestion.

## Conflicts to Resolve
- None.

## Link Mapping
- `Ollama.md` -> [[Quantization]], [[Gemma 4]].
- `Vercel AI SDK.md` -> [[OpenRouter]], [[TypeScript]].
- `Claude 3.7.md` -> [[OpenRouter]], [[LLM Fine Tuning]].

## ARCHIVE
- **Move Vercel_AI_SDK_Technical_Research.md and Ollama_Technical_Research.md from Raw/ to Vault/.**
