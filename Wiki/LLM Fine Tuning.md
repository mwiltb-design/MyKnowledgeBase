Source: [[Fine_tune_VLM.md]], [[Gemma_4_Technical_Analysis.md]]

# LLM Fine-Tuning

## Summary
An exploration of LLM fine-tuning techniques, highlighting Andrej Karpathy's research and modern VLM/Gemma-4 fine-tuning strategies.

- Specialization: Specialized models using **PEFT (LoRA/QLoRA)** on **[[Gemma 4]]** or **[[Llama-3.1]]**.
- **[[Gemma 4]] / [[VLM]] Recipe:**
    - **Framework**: **[[Unsloth]]** (Optimized kernels, 2x faster, 60% less VRAM).
    - **Strategy**: **QLoRA** (4-bit quantization with trainable adapters).
    - **Hyperparameters**:
        - **Learning Rate**: **2e-4**.
        - **Max Seq Length**: **4096**.
        - **Batch Size**: **2** (Accumulation steps: **4**).
    - **Stage 1**: Freeze encoders (`finetune_vision_layers = False`) to align language model to application style.
- **[[Andrej Karpathy|Karpathy]]'s Research:**
    - **Weight Decay (WD)**: Embeddings (**0.001**), VEs (**0.003**), lm_head (**0.01**).
    - **Init Scaling**: Transformer Init Scale (**0.68x**).
    - **Learning Rate**: **FINAL_LR_FRAC: 0.05**.

---
**See also:** [[Unsloth]], [[MatFormer]], [[RLVR]].
