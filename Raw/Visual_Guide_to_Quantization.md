# Visual_Guide_to_Quantization

> **Metadata**
> Original Filename: A Visual Guide to Quantization - Maarten.png

This guide provides a comprehensive visual overview of Large Language Model (LLM) quantization, explaining how to run massive models on consumer hardware.

## Visual Diagrams Description
The original PNG contains a series of visual diagrams illustrating:
- **Normal Distribution:** A bell curve graph comparing the high precision of FP32 (many values) versus the discrete, limited steps of INT4 (only 16 ticks).
- **Weight Matrices:** Grids and arrays demonstrating how numbers are compressed from full floats to shorter representations.
- **Memory Comparison:** A visual scale showing 16-bit vs 4-bit sizes, showing a ~4x reduction in required space.

## Numerical Precision
Quantization is the process of reducing the precision of the model's weights to save memory.
- **FP32 (32-bit):** Highest precision, 4 bytes per weight.
- **FP16 (16-bit):** Standard for training, 2 bytes per weight.
- **INT8 (8-bit):** 1 byte per weight.
- **INT4 (4-bit):** 0.5 bytes per weight.

## Memory Formula
Memory (GB) = (Parameters × Bits per weight) / (8 × 1024³)

## Quantization Formats
### GGUF (llama.cpp)
A portable container format for weights and metadata.
- **K-Quants:** Layer-aware quantization (e.g., Q4_K_M).
- **IQ-Quants:** Importance-matrix guided quantization for better quality at low bit depths.

### GPU Optimized (NVIDIA)
- **GPTQ:** Calibration-based quantization.
- **AWQ:** Activation-aware weight quantization, protects high-impact weights.
- **EXL2:** Mixed-precision specialist for NVIDIA GPUs.

## Hardware Guide (VRAM Requirements)
| VRAM | Models That Fit Fully |
| :--- | :--- |
| 6 GB | 7-8B (Q4_K_M) |
| 8 GB | 7-8B (Q5/Q8) |
| 12 GB | 13-14B (Q4_K_M) |
| 24 GB | 34B (Q4_K_M), 70B (Q2_K - tight) |
| 48 GB | 70-72B (Q4_K_M) |

## The 1-Bit Frontier
**BitNet b1.58:** A model natively trained with ternary weights {-1, 0, 1}, requiring only ~1.58 bits per weight. Offers massive speedups on CPUs.

## When Not to Quantize
- **Legal/Medical/Compliance:** Where every clause matters.
- **Embedding Generation:** Sensitive to precision loss.
- **Inference on Fine-Tuned Models:** If tuned in FP16, run in FP16 to avoid quality drop.
