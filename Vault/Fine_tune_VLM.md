# Fine-Tune a Small Vision Language Model (VLM) Locally

## Introduction
This document is a transcript/guide for fine-tuning a small Vision Language Model (VLM) or Multimodal Language Model (MLLM) locally, specifically using tools like the Nvidia DGX Spark, the TRL library, and Smoldl-VLM-500M.

## Process Overview
1.  **Download the Model:** Use Smoldl-VLM-500M (under 1B parameters).
2.  **Download the Dataset:** FoodExtract-1k-Vision dataset.
3.  **Fine-tune the Model:** Use Supervised Fine-Tuning (SFT) via the TRL library.
4.  **Upload to Hugging Face:** Share the resulting model.
5.  **Create a Demo:** Build a Gradio interface.

## What is a VLM?
A VLM typically consists of:
- **Image Encoder:** (e.g., SigLIP) to process visual data.
- **Projection Layer (Connector):** Merges text and image embeddings.
- **Text Decoder (LLM):** Produces output tokens.

## Case Studies
- **Nutrify:** An app for recognizing whole foods from images (no barcodes) and outputting structured JSON via Gemini or local VLMs.
- **Invoice Extractor:** Extracting structured data (Title, Date, Amount) from business invoices to JSON/Excel.

## Technical Recipe (Based on SmolDocling Paper)
- **Model:** SmolVLM2-500M-Video-Instruct.
- **Dataset:** FoodExtract-1k-Vision (1,500 samples: 1,000 food, 500 non-food "hard negatives").
- **Hardware/Time:** The paper used 64x Nvidia A100 GPUs for 38 hours, but local fine-tuning on smaller datasets is feasible in ~1 hour.
- **Hyperparameters:**
    - **Optimizer:** AdamW.
    - **Learning Rate:** 2e-4.
    - **Gradient Clipping:** 1.0.
    - **Warm-up Ratio:** 0.03.
    - **Epochs:** 1 to 4.

## Key Technique: Freezing the Vision Encoder
As per section 5.1 of the SmolDocling paper, the **Vision Encoder is frozen** during the first stage of training.
- **Trainable Params:** ~420M.
- **Frozen Params:** ~86.5M.
- **Logic:** Align the LLM to the desired output format first. Unfreezing the vision encoder (Stage 2) requires a larger dataset to avoid performance degradation.

## Training Pipeline (SFT)
- **Data Collator:** Stacks samples into batches. Images are processed into pixel value tensors, while text is tokenized.
- **SFTTrainer:** Handles the training loop using the `SFTConfig` settings.
- **Loss Curves:** Success is measured by the training/validation loss decreasing over time.

## Deployment & Testing
- **Hugging Face Hub:** Use `HuggingFaceHub` API to upload the `model.safetensors` and config files.
- **Gradio Demo:** Create `app.py` to allow users to upload images and see the VLM's structured JSON output.

## Extensions & Future Work
1. **Formalize Evaluations:** Compare small VLM outputs against larger models (e.g., Qwen-VL-8B).
2. **Data Scaling:** Increase from 1.5k samples to 10k+ diverse, real-world images.
3. **Prompt Removal:** Fine-tune for direct image-to-JSON extraction to save on input tokens and latency.
4. **Fix Repetitive Generation:** Use RLVR (Reinforcement Learning for Verified Rewards) to penalize redundant JSON outputs.

---
**Source:** Google Doc: Fine tune VLM (ID: 1BzH7wq8aytmt_cMCQjqJ-6gsyzlBfnWyzRUy15AfEVI)
**Date Fetched:** 2026-04-12
