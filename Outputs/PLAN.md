# Knowledge Architect Plan: Database Ecosystem Update

## Overview
This plan integrates foundational database technologies into the Wiki to support both **AI Agent Memory** and the upcoming **RV Park Management** project.

## New Pages
- [x] **[[PostgreSQL]]**: Comprehensive guide on the "Object-Relational" standard, focusing on extensibility (JSONB) and GIS.
  - Source: [[PostgreSQL_Official_About.md]]
- [x] **[[PocketBase]]**: Detailed overview of the "All-in-One" backend solution for rapid development.
  - **High Priority** for RV Park Website.
  - Source: [[PocketBase_Official_Intro.md]]
- [x] **[[DuckDB]]**: Introduction to "In-process Analytical SQL" for fast data processing and local-first analytics.
  - Source: [[DuckDB_Official_Why.md]]
- [x] **[[LanceDB]]**: Guide to the embedded vector database for AI agents and RAG.
  - Source: [[LanceDB_Official_Overview.md]]
- [x] **[[Qdrant]]**: Overview of the Rust-based vector similarity search engine for production-grade AI.
  - Source: [[Qdrant_Official_Overview.md]]

## Updates to Existing
- [x] **[[SQLite]]**: Expand from a "lightweight layer" to a "Full-featured SQL engine," including its role as a serverless application file format.
  - Source: [[SQLite_Official_About.md]]
- [x] **[[AI Memory]]**: Add sections on **Vector Databases** (LanceDB, Qdrant) and **Relational Backends** (PostgreSQL) for long-term agent state.
- [x] **[[RV Park Digital Strategy]]**: Link to **[[PocketBase]]** as the recommended technical stack for the 2026 website implementation.
- [x] **[[INDEX.md]]**:
  - Create a new category: **## Database & Storage Systems**.
  - Move [[SQLite]] under this category.
  - Add links to [[PostgreSQL]], [[PocketBase]], [[DuckDB]], [[LanceDB]], and [[Qdrant]].

## Link Mapping (Cross-Pollination)
- [x] **[[PostgreSQL]]** <-> **[[LanceDB]]**: Compare "Embedded" vs. "Server-side" for vector storage.
- [x] **[[PocketBase]]** <-> **[[SQLite]]**: Explain how PocketBase leverages SQLite for its portable backend.
- [x] **[[DuckDB]]** <-> **[[Metric Definition]]**: How DuckDB can be used to calculate scalar metrics from raw research logs.
- [x] **[[AI Memory]]** <-> **[[Vector Databases]]**: Deep dive into semantic similarity vs. exact SQL retrieval.

## Conflicts to Resolve
- **None Identified**: The new data complements existing notes without contradiction.

---
**Next Step**: Task Complete.
