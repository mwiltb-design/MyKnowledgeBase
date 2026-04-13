Source: [[Fine_tune_VLM.md]]

## Summary
- **Vision Language Models** (VLM/MLLM) combine image and text inputs to produce structured outputs.
- Architecture consists of an **Image Encoder**, **Projection Layer**, and **Text Decoder**.
- Optimized for specific tasks like **Nutrify** (food extraction) and **Invoice Extraction** via fine-tuning.

## Components
- **Image Encoder:** (e.g., **SigLIP**) processes visual data.
- **Projection Layer:** The "connector" merging visual and text embeddings.
- **Text Decoder:** LLM generating the final output tokens.

## Applications
- **Structured Extraction:** Converting visual documents/images into JSON/Excel formats.
- **Edge Inference:** Local execution for privacy, scalability, and offline use.
- **Examples:** **Nutrify** (whole food recognition), **Invoice Extractor**, and **Visual Intelligence** for calendar events.
