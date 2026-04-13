Source: [[Gemma_4_Technical_Analysis.md]]

## Summary
- **Unsloth** is a highly optimized framework for fine-tuning LLMs, offering significant speed and memory improvements (up to **2x faster**, **70% less VRAM**).
- Primary tool for fine-tuning **[[Gemma 4]]**, **Llama-3.1**, and Mistral models on consumer GPUs.
- Supports **QLoRA** (Quantized Low-Rank Adaptation) for 4-bit parameter-efficient training.

## Performance Features
- **Speed**: Optimized kernels for faster training iterations compared to standard Hugging Face implementations.
- **Memory**: Reduces VRAM requirements by ~60% while maintaining performance integrity.
- **Self-Healing**: Unsloth Studio includes a plugin to automatically repair malformed JSON in tool-calling outputs.

## Deployment
- Compatible with **Ollama** and **LM Studio** for exporting fine-tuned adapters.
- Hardware Requirements: Minimum **8GB VRAM** for **E2B**; **10-17GB** for **E4B**.

---
**See also:** [[LLM Fine Tuning]], [[Gemma 4]], [[RLVR]].
