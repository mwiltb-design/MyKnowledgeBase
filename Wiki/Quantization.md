Quantization is a critical technique for running massive Large Language Models on consumer-grade hardware by reducing the numerical precision of the model's weights. By compressing full 32-bit floats into formats like 8-bit or 4-bit integers, quantization drastically lowers VRAM requirements, often by a factor of four, without significantly compromising the model's reasoning capabilities. This process is essential for local execution of state-of-the-art models like [[Gemma-4]] and is a key component in efficient [[LLM-Fine-Tuning]] workflows, enabling advanced AI to run on everything from mobile devices to desktop GPUs.

# Visual Guide to Quantization

Quantization allows for the compression of weight matrices by mapping high-precision floating-point numbers to a smaller set of discrete values, significantly reducing the memory footprint.

## Numerical Precision Levels
- **FP32 (32-bit):** 4 bytes per weight (highest precision).
- **FP16 (16-bit):** 2 bytes per weight (standard for training).
- **INT8 (8-bit):** 1 byte per weight.
- **INT4 (4-bit):** 0.5 bytes per weight.

## Memory Formula
Memory (GB) = (Parameters × Bits per weight) / (8 × 1024³)

## Popular Quantization Formats
### GGUF (llama.cpp)
A portable container format supporting metadata and diverse quantization methods:
- **K-Quants:** Layer-aware quantization (e.g., Q4_K_M).
- **IQ-Quants:** Importance-matrix guided quantization.

### GPU-Optimized Formats
- **GPTQ:** Calibration-based for NVIDIA GPUs.
- **AWQ:** Activation-aware weight quantization.
- **EXL2:** High-performance mixed-precision specialist.

## Hardware VRAM Requirements
| VRAM | Models That Fit Fully |
| :--- | :--- |
| 6 GB | 7-8B (Q4_K_M) |
| 12 GB | 13-14B (Q4_K_M) |
| 24 GB | 34B (Q4_K_M), 70B (Q2_K) |
| 48 GB | 70-72B (Q4_K_M) |

## Important Considerations
While quantization is highly effective for inference, it should be avoided for:
- **Legal/Medical/Compliance Tasks:** Where precision is critical.
- **Embedding Generation:** Sensitive to precision loss.
- **[[LLM-Fine-Tuning]] Workflows:** For best results, run inference at the same precision used during fine-tuning.
