Source: [[Gemma_4_Technical_Analysis.md]]

# Quantization

## Summary
A guide to quantization techniques that reduce AI model precision to save VRAM, with specific standards for 2026 local deployment.

- Definition: Reducing bit-precision of model weights to lower memory requirements with minimal accuracy loss.
- Precision Levels:
    - **BF16**: 2 bytes/weight (Mac Studio/Workstation baseline).
    - **INT8 (Q8_0)**: 1 byte/weight.
    - **INT4 (Q4_K_M)**: **0.5 bytes/weight** (Standard for mobile/IoT).
- Memory Formula: **GB = (Parameters × Bits) / 8**.

## Gemma 4 Requirements (4-bit Q4)
- **E2B**: **4 GB - 5 GB** (Target: Mid-range Android, Pi 5).
- **E4B**: **5.5 GB - 6 GB** (Target: Flagship Phones, Laptops).
- **31B**: **17.4 GB**.
- **26B A4B (MoE)**: **15.6 GB**.

## Industry Standards (2026)
- **GGUF**: The universal standard for CPU/GPU inference (Ollama, LM Studio).
- **MLX**: Optimized format for Apple Silicon unified memory.
- **SFP8**: High-throughput inference for data-center scale.
- **BitNet b1.58**: Ternary weight frontier.

---
**See also:** [[MatFormer]], [[Gemma 4]].
