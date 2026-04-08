Gemma 4 is a versatile family of open-weight generative AI models from Google, designed for tasks ranging from reasoning and summarization to advanced coding. It features three distinct architectures—Small (2B/4B), Dense (31B), and Mixture-of-Experts (26B MoE)—to accommodate various hardware from mobile devices to servers. With context windows up to 256K and native support for multimodality and system prompts, Gemma 4 is highly optimized for agentic workflows and can be further refined through [[LLM-Fine-Tuning]] or compressed using [[Quantization]] for efficient local execution.

# Gemma 4 Model Overview

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

## Parameter Sizes and [[Quantization]]
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
- **[[LLM-Fine-Tuning]] Overhead:** Memory requirements for fine-tuning are drastically higher than for inference. Use Parameter-Efficient Fine-Tuning (PEFT) methods like LoRA (Low-Rank Adaptation) to reduce footprint.
