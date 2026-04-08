# Gemma4_Guide

> **Metadata**
> Original Filename: Gemma 4 model overview 1.png, Gemma 4 model overview 2.png

Gemma 4 is a family of generative artificial intelligence models designed for a wide variety of tasks including question answering, summarization, and reasoning. These models are provided with open weights and permit commercial use.

## Model Architectures
Gemma 4 spans three distinct architectures tailored for specific hardware requirements:
- **Small Sizes (2B and 4B):** Built for ultra-mobile, edge, and browser deployment (e.g., Pixel, Chrome).
- **Dense (31B):** A powerful dense model bridging the gap between server-grade performance and local execution.
- **Mixture-of-Experts (26B MoE):** Highly efficient model designed for high-throughput, advanced reasoning.

## Key Capabilities
- **Reasoning:** Highly capable reasoners with configurable thinking modes.
- **Extended Multimodalities:** Processes Text, Image (variable aspect ratio/resolution), Video, and Audio.
- **Context Window:** 128K context window for small models; 256K for medium models.
- **Enhanced Coding & Agentic Capabilities:** Improvements in coding benchmarks and built-in function-calling support.
- **Native System Prompt Support:** Built-in support for the `system` role for structured and controllable conversations.

## Parameter Sizes and Quantization
The following table details the approximate GPU or TPU memory requirements for running inference:

| Model | BF16 (16-bit) | SFP8 (8-bit) | Q4_0 (4-bit) |
| :--- | :--- | :--- | :--- |
| Gemma 4 E2B | 9.6 GB | 4.6 GB | 3.2 GB |
| Gemma 4 E4B | 15 GB | 7.5 GB | 5 GB |
| Gemma 4 31B | 58.3 GB | 30.4 GB | 17.4 GB |
| Gemma 4 26B A4B | 48 GB | 25 GB | 15.6 GB |

## Key Considerations for Memory Planning
- **Efficient Architecture (E2B and E4B):** Incorporates Per-Layer Embeddings (PLE) for efficiency on-device.
- **MoE Architecture (26B A4B):** Activates only 4 billion parameters per token, making memory requirements closer to a 26B model than a 4B model while maintaining high performance.
- **Base Weights Only:** Estimates above account for static model weights only; additional VRAM is needed for KV cache and context.
- **Context Window (KV Cache):** Memory consumption increases dynamically based on the number of tokens in the prompt and response.
- **Fine-Tuning Overhead:** Memory requirements for fine-tuning are drastically higher than for inference. Use Parameter-Efficient Fine-Tuning (PEFT) methods like LoRA (Low-Rank Adaptation) to reduce footprint.
