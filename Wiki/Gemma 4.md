Source: [[Gemma_4_Technical_Analysis.md]]

# Gemma 4

## Summary
An overview of Google's Gemma 4 generative AI model family, featuring native multimodality, advanced reasoning depth, and a commercially permissive **Apache 2.0** license.

- Models: **[[Gemma 4]]** is a family of open-weight models (released April 2, 2026) derived from the **Gemini 3** ecosystem.
- Architecture Variants:
    - **E2B & E4B (Effective)**: Edge-scale models optimized for mobile, IoT, and real-time transcription.
    - **31B (Dense)**: Server-grade performance for complex reasoning.
    - **26B A4B (MoE)**: High-throughput Mixture-of-Experts architecture.
- Capabilities:
    - **Thinking Mode**: Native step-by-step reasoning outputs (e.g., `<|channel>thought`).
    - **Multimodality**: Integrated processing of text, image, audio, and video.
    - **Context Window**: 128K to **256K** tokens.

## Architectural Innovations
- **[[MatFormer]]**: Nested sub-models allowing dynamic scaling from a single checkpoint.
- **Per-Layer Embeddings (PLE)**: Layer-specific lookup tables that sharpen reasoning depth per stage.
- **Hybrid Attention**: 4:1 ratio of local (sliding-window 512) to global attention layers using **p-RoPE**.

## VRAM Inference Requirements (4-bit)
- **Gemma 4 E2B**: **4 GB - 5 GB** (Effective Params: **2.3B**)
- **Gemma 4 E4B**: **5.5 GB - 6 GB** (Effective Params: **4.5B**)
- **Gemma 4 31B**: **17.4 GB**
- **Gemma 4 26B A4B**: **15.6 GB**

## Local Deployment
- **Ollama**: `ollama pull gemma4:e4b`; requires `num_ctx 131072` for full window.
- **LM Studio**: Supports GGUF with full GPU offloading for all 35-42 layers.
- **AI Edge Gallery**: Native offline inference for Android and iOS (iPhone 15 Pro+).

---
**See also:** [[MatFormer]], [[Unsloth]], [[Quantization]].
