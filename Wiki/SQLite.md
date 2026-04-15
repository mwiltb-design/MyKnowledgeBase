Source: [[SQLite_Official_About.md]]

## Summary
- **SQLite** is a full-featured, zero-configuration, transactional SQL database engine.
- Unlike most SQL databases, it is **serverless** and reads/writes directly to ordinary disk files.
- The most used database engine globally, serving as the standard for mobile, desktop, and AI agent state.

## Core Characteristics
- **Serverless**: No separate server process. A complete database is contained in a single disk file.
- **Zero-Configuration**: No setup or administration is needed. 
- **Transactional**: Fully ACID-compliant, ensuring data integrity even during system crashes or power failures.
- **FTS5 Extension**: Utilized for high-speed full-text search over conversation histories and Wiki files.

## Role in AI Memory
Provides a reliable, local-first storage layer for **[[AI Memory]]** and **[[Hermes Agent]]** state. It is an ideal "application file format" for persistent agent logs.

---
**See also:** [[PostgreSQL]], [[PocketBase]], [[AI Memory]].
