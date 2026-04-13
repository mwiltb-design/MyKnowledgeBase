Source: [[Fine_tune_VLM.md]]

## Summary
- A family of small, efficient vision language models under **1B parameters**.
- Designed for **edge devices** and specific, repetitive extraction tasks.
- Successfully fine-tuned on **FoodExtract-1k-Vision** for structured JSON output.

## Training Recipe (Stage 1)
- **Base Model:** **SmolVLM2-500M-Video-Instruct**.
- **Technique:** **Frozen Vision Encoder** (~86.5M params) during initial alignment.
- **Hyperparameters:**
    - **Optimizer:** **AdamW**.
    - **Learning Rate:** **2e-4**.
    - **Grad Clipping:** **1.0**.
    - **Warm-up Ratio:** **0.03**.

## Evaluation
- Successfully predicts food items and attributes (broth, chicken, etc.) from images.
- Prone to **repetitive generation**; requires **[[RLVR]]** (Reinforcement Learning for Verified Rewards) for optimization.

---
**See also:** [[VLM]], [[LLM Fine Tuning]].
