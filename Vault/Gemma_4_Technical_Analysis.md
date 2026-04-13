# Google Gemma 4: Technical Architecture & Deployment Optimization

## 1. Evolution & Mission
Gemma 4 (released April 2, 2026) shifts from raw parameter scaling to **intelligence-per-parameter**. It introduces native multimodality (Text, Image, Audio, Video) and a commercially permissive **Apache 2.0 license**.

## 2. Architectural Innovations
- **Matryoshka Transformer (MatFormer):** Nested sub-models within a single checkpoint. Weights of E2B are a subset of E4B, allowing dynamic scaling based on hardware/battery constraints.
- **Per-Layer Embeddings (PLE):** Layer-specific identity lookup tables that sharpen reasoning depth at each stage.
- **Hybrid Attention:** 4:1 ratio of local (sliding-window 512 tokens) to global attention layers. Global layers use Proportional RoPE (p-RoPE) and unified KV states to halve cache size.

## 3. Edge Variant Specifications
| Property | Gemma 4 E2B | Gemma 4 E4B |
| :--- | :--- | :--- |
| **Effective Params** | 2.3B | 4.5B |
| **Total Params (PLE)** | 5.1B | 8.0B |
| **Context Window** | 128K | 128K |
| **Modality Support** | Text, Image, Audio | Text, Image, Audio |
| **VRAM (4-bit)** | 4-5 GB | 5.5-6 GB |

## 4. Local Deployment Methodology
### Methodology 1: Ollama
- **Pull:** `ollama pull gemma4:e4b`
- **Context Window:** Requires a custom `Modelfile` with `PARAMETER num_ctx 131072`.

### Methodology 2: LM Studio
- **Quantization:** Supports GGUF.
- **Offloading:** Set "GPU Offload" to Max for 8GB+ VRAM devices to load all 35-42 layers.

### Methodology 3: AI Edge Gallery
- Native mobile deployment for Android (APK) and iOS (iPhone 15 Pro+).

## 5. Fine-Tuning Recipe (QLoRA)
- **Framework:** **Unsloth** (most optimized for Gemma 4).
- **Hardware:** E2B requires 8GB VRAM; E4B requires 10GB-17GB.
- **Hyperparameters:**
    - **Learning Rate:** 2e-4.
    - **Max Seq Length:** 4096.
    - **Batch Size:** 2 (Accumulation steps: 4).
- **Strategy:** Freeze encoders (`finetune_vision_layers = False`) initially to align the language model to descriptive styles.

## 6. Advanced Capabilities
- **Native Thinking Mode:** Enclosed in `<|channel>thought\n... <channel|>`. Note: Thought blocks should not be re-injected into context for subsequent turns.
- **Native Function Calling:** Edge variants act as system controllers via structured JSON payloads.
- **Self-Healing:** Unsloth Studio supports automatic correction of malformed tool-call JSON.

---
**Source:** Google Doc: Gemma Model Download, Test, Train (ID: 1A5FBmqtWlHxJHiFmN2U9nVwkRUGapeMb1EM9AGOSBxI)
**Date Fetched:** 2026-04-12
