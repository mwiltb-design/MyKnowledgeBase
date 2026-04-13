# Transformer Inference Arithmetic

## Source
[kipply.github.io](https://kipp.ly/transformer-inference-arithmetic/)

## Summary
A deep dive into the mathematical constraints of running Transformers, focusing on memory bandwidth, KV caching, and the "memory wall" that limits performance for small batch sizes.

## Key Concepts
- **KV Cache (Past Cache)**: Caches Key and Value vectors during autoregressive sampling to avoid redundant calculations. Without it, sampling complexity is quadratic ($O(T^2)$); with it, it is linear ($O(T)$).
- **Memory vs. Compute Bound**: 
    - **Memory Bound**: Latency is limited by how fast weights can be loaded from VRAM (common for small batch sizes).
    - **Compute (FLOPs) Bound**: Latency is limited by the GPU's mathematical throughput (common for large batch sizes).
- **Model Parallelism**: Sharding model weights across multiple GPUs (Tensor Parallelism) to fit large models and parallelize computation.

## Technical Specs (Example: 52B Parameter Model)
- **Weight Storage**: ~104 GB (at 16-bit precision).
- **KV Cache Size**: ~2 MB per token (for $d_{model}=8192$, 64 layers).
- **A100 Ratio**: For an NVIDIA A100, the "math bandwidth" ratio is ~208. If batch size < 208, the system is typically memory bound.
- **FLOPs Calculation**: Total FLOPs per token is approximately $2 \times \text{Parameters}$.

## Architectural Diagram
```text
[Input Token] 
      |
[Embedding Layer]
      |
[Transformer Layer 1...N]
   |-- [Self-Attention] <--> [KV Cache Storage]
   |-- [Layer Norm]
   |-- [MLP / Feed-Forward]
      |
[Output Projection / Logits]
      |
[Sampling (Top-K/P)] --> [Next Token]
```
