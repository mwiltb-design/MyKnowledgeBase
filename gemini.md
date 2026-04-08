# Project: LLM-Managed Knowledge Base

## Philosophy: Beyond RAG
This project is an implementation of a "persistent, compounding artifact" pattern for knowledge management. Unlike traditional Retrieval-Augmented Generation (RAG) which rediscovers knowledge from scratch with every query, this system focuses on **incremental synthesis**.

The goal is to move from a collection of "raw chunks" to a structured, interlinked **Wiki** that evolves over time. Every new piece of information is not just indexed, but integrated—updating summaries, noting contradictions, and strengthening the overall network of knowledge.

## The Three-Layer Architecture
The project is structured around three distinct logical layers:
1.  **Raw Sources:** The immutable source of truth. This contains original articles, papers, images, and data files that the system reads but never modifies.
2.  **The Wiki:** The living synthesis. A collection of interlinked Markdown files maintained by the LLM. This includes entity pages, concept summaries, and a central index.
3.  **The Schema:** The governing conventions. The "code" that defines how the wiki is structured and how the LLM should behave as a maintainer.

## Knowledge Domains
The knowledge base is currently focused on a diverse set of specialized interests, providing a unique "lens" for synthesis:
*   **AI Engineering:** Personal assistants, training local LLMs, agents, workflows, and AI memory.
*   **Space & Science:** Space travel mechanics, commercial space industry, and fundamental sciences (physics, biology, math).
*   **Personal Management:** Health (factual tracking, longevity tech), Wealth (investing, RV park ownership), and History.
*   **Professional Expertise:** Stone Masonry (architectural stone fabrication and management).

## Role and Intent
In this ecosystem:
*   **The User** acts as the Curator and Explorer—sourcing high-quality material and directing the lines of inquiry.
*   **The LLM** acts as the Programmer and Maintainer—handling the "bookkeeping" of knowledge (summarizing, cross-referencing, and filing).
*   **The Wiki** is the "Codebase"—a persistent record of understanding that becomes more valuable the longer it is maintained.

This document serves as the high-level conceptual framework for the project, allowing the agent to understand the "why" behind the structure and offer suggestions for improvement, usability, and scale.
