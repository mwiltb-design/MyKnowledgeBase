# Metric Definition

## Summary
An explanation of scalar metrics, like val_bpb, that provide AI agents with a clear standard for evaluating and improving research results.

- Goal: **[[Metric Definition|Scalar metric]]** that allows an agent to decide if an experiment is an improvement.
- Primary Choice: **val_bpb (Validation Bits Per Byte)**.
- Why **val_bpb**:
    - **Vocab-Size-Independent**: Unlike standard loss, it allows for fair architectural comparisons even when tokenization changes.
- Direction: Lower is better.
- Alternative Metrics:
    - **Sharp Ratio** (**[[Scope Expansion|Trading]]**).
    - **Conversion Rate** (**[[Scope Expansion|Marketing]]**).
    - **Loading Time (ms)** (**[[Scope Expansion|Web Performance]]**).
