Source: [[Ollama_Technical_Research.md]]

## Summary
- **Ollama** is a Go-based local LLM orchestrator that enables running, pulling, and creating large language models on personal hardware.
- It wraps **llama.cpp** for core tensor computations and provides a simple REST API (default port **11434**).
- Features automated **Hardware Acceleration** for NVIDIA (CUDA), AMD (ROCm), and Apple Silicon (Metal).

## API Protocols
- **`/api/chat`**: Standard conversational endpoint using message arrays.
- **`/api/generate`**: Raw completion endpoint for single-turn prompts.
- **`/api/pull`**: acquisition of models from the Ollama registry.
- **`/api/create`**: Build custom models using a **[[Modelfile]]**.

## Model Management
- **Modelfile**: Configuration blueprint for setting `temperature`, `num_ctx` (context window), and system prompts.
- **Quantization**: Primarily utilizes **[[Quantization|GGUF]]** for efficient 4-bit and 8-bit model compression.
- **Persistence**: Content-addressable storage (blobs/manifests) ensures efficient model versioning and shared layer management.

---
**See also:** [[Quantization]], [[Gemma 4]], [[Pi Coding Agent]].
