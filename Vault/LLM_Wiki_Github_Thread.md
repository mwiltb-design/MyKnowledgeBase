# LLM Wiki Github Thread

**Original Filename:** llm-wiki.png

## Visual Description
The image is a long, vertical composite screenshot of a GitHub Gist or repository discussion page. It features a dark theme. The top section contains a detailed proposal titled "LLM Wiki" in Markdown. Below the main proposal is a threaded conversation with several participants, including Andrej Karpathy (marked as "Maintainer"). The thread includes text blocks, code snippets (like the python script for generating reports), and summary tables of experiment results.

## Extracted Content: The LLM Wiki Proposal
(Note: This section matches the text in `LLM_Native_Wiki.md`, describing the three-layer architecture of Raw Sources, The Wiki, and The Schema, and the core operations of Ingest, Query, and Lint.)

## Discussion Highlights
**Andrej Karpathy (Mar 8, Maintainer):**
- Reported a fresh overnight run inspired by Issue #32.
- Applied "early wins" like batch halving, depth 9, SSSSL, and RoPE 200K.
- Discovered that weight decay on embeddings and value embeddings (VEs) is significant.
- Noted a "narrow optimum" for transformer initialization scale at 0.68x.
- **Top Wins Table:**
    - Halve batch 524K -> 262K (-0.0119)
    - Depth 9, aspect_ratio 57 (-0.0043)
    - Embedding LR 0.6 -> 0.8 (-0.0033)
    - RoPE base frequency 10K -> 200K (-0.0012)
- **Dead Ends:** Weight tying (shared embed/unembed) was "completely broken." Parallel attention + MLP was "much worse."

## Metadata & Infrastructure
- **GPU:** NVIDIA H100 80GB
- **Experiments:** 126 (23 kept, 102 discarded, 1 crash)
- **Wall time:** ~10.5 hours
- **Agent:** Claude (Anthropic)

## Analysis of the "Karpathy Loop"
The discussion emphasizes that AutoResearch is not just hyperparameter tuning but "orchestrating agents" where the human acts as a "research advisor." The shift is from writing code to writing "experimental protocols" in `program.md`.

---
*Reference to original file: llm-wiki.png*
