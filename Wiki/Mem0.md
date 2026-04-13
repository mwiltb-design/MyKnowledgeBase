# Mem0

## Summary
A specialized "Memory-as-a-Service" layer designed for personalized AI agents, combining vector and graph memory to maintain user preferences across sessions and platforms.

## Hybrid Memory Model
Mem0 integrates two distinct memory types to balance "vibes" and "facts":
- **Vector Memory**: For semantic similarity and "fuzzy" recall of past conversations.
- **Graph Memory**: For hard facts and structured relationships (e.g., "The user has an i5-8400T CPU").

## Key Features
- **Personalization**: Automatically extracts and remembers user-specific traits, avoiding "prompt bloat" from repeating instructions.
- **Continuity**: Maintains memory across different LLMs or agent sessions.
- **Async Processing**: Handles memory updates in the background to minimize user-facing latency.

## See Also
- **[[AI Memory]]**: Hardware foundations.
- **[[Hermes Agent]]**: Potential application for self-improving memory.
- **[[OxyLabs MCP]]**: Data sourcing for memory layers.
