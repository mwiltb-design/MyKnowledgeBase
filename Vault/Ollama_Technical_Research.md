# Ollama: Technical Research & Architecture

## 1. Core Architecture
Ollama is a Go-based client-server orchestrator that manages the lifecycle of local LLMs. It wraps **llama.cpp** for core tensor computations and model inference.

## 2. API Protocols (Port 11434)
- **`/api/chat`**: Manages conversational state via message arrays.
- **`/api/generate`**: Standard completion endpoint for raw prompts.
- **`/api/pull` / `/api/create`**: Handles model acquisition and building from custom `Modelfile` definitions.

## 3. Modelfile Syntax
The `Modelfile` defines the model's configuration:
- **`PARAMETER`**: Controls behavior like `temperature`, `num_ctx` (context window), and `top_k`.
- **`SYSTEM`**: Sets the persona or operational constraints.
- **`TEMPLATE`**: Formats the `SYSTEM` and user `PROMPT` for specific architectures.

## 4. Hardware Acceleration & Performance
- **Discovery**: Automatically identifies and utilizes available hardware:
    - **NVIDIA (CUDA)** / **AMD (ROCm)** / **Apple Silicon (Metal)**.
- **CPU Fallback**: Uses optimized AVX/AVX2/AVX-512 instructions if no GPU is present.

## 5. Model Management
- **GGUF Quantization**: Primary format for efficient 4-bit/8-bit weight compression.
- **Content-Addressable Storage**: Stores models as shared "blobs" and manifests (similar to Docker), reducing storage redundancy.

---
**Source:** [ollama/ollama (GitHub)](https://github.com/ollama/ollama)
**Date Fetched:** 2026-04-12
