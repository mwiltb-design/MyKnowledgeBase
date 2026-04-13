# MemGPT

## Summary
An operating-system-inspired memory architecture (also known as Letta) that enables AI agents to manage virtually infinite context by "paging" information between a fixed-size window and long-term storage.

## Virtual Context Management
MemGPT treats the LLM's limited context window like a **CPU Cache**.
- **Working Context**: The immediate, "high-speed" memory (Persona, User Profile, recent chat).
- **Archival Memory**: Long-term storage for infinite history, searched via vector retrieval.
- **Recall Memory**: A structured database (SQL) for precise retrieval of specific past events.

## Self-Editing Memory
Unlike standard RAG, MemGPT agents are **proactive**. They use function calls to:
1. **Update Core Memory**: Modify their own persona or what they know about the user based on new information.
2. **Archival Search**: Manually trigger a search for old context when the current window is insufficient.

## See Also
- **[[AI Memory]]**: General memory constraints.
- **[[Second Brain Workflow]]**: Manual implementation of similar patterns.
- **[[Pi Coding Agent]]**: Integration target for autonomous memory.
