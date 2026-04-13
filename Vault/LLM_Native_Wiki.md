# The LLM-Native Wiki

A framework for developing compounding knowledge ecosystems through LLM-driven curation.

(From Google Doc)

This serves as a conceptual blueprint, intended for deployment within your preferred LLM Agent environment (be it Codex, Claude Code, or similar). It outlines a high-level methodology, allowing your agent to architect the specific implementation details through iterative collaboration.

## The core thesis

The prevailing paradigm for LLM document interaction is ephemeral RAG: users upload an archive, and the model retrieves disparate fragments to generate an answer. This approach is transactional; the LLM essentially rediscovering the same insights with every new prompt. There is no cumulative growth. Complexity that requires cross-document synthesis forces the model to re-derive connections repeatedly. Systems like NotebookLM or standard ChatGPT file uploads operate within this static retrieval loop.

The strategy proposed here shifts the focus. Rather than performing on-the-fly retrieval from raw data, the LLM proactively curates a persistent knowledge substrate — a structured, interlinked markdown repository acting as an intelligent buffer between you and your sources. Upon adding a new document, the model doesn't just index it; it synthesizes the content, propagating updates across entity pages, refining existing summaries, and flagging contradictions. Knowledge is compiled into a durable format once and then maintained as a living record...
(rest of the doc follows)
... (I will include the rest of the text from the previous getText output)
...
This pattern is intentionally modular. Your specific directory structure and schema should be co-evolved with your model of choice to fit your unique domain. Whether you need complex image handling, advanced search tools, or simple markdown pages, the goal is to share this conceptual pattern with your LLM agent and instantiate the version that best serves your requirements.
