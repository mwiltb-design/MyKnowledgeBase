# AutoResearch (The Karpathy Loop)

Source: [[Karpathy_Autoresearch_Explained.md]], [[Auto_Research_Tutorial.md]]

## Summary
- **Auto-Research** is a general paradigm for **autonomous knowledge discovery** that uses a recursive experimental loop.
- **The Karpathy Loop** is a specific 3-file implementation designed for high-throughput, autonomous model optimization.
- Shift from writing code to writing **experimental protocols** in **`program.md`** to remove the human bottleneck.

## The 3-File Architecture
- **`prepare.py`**: Fixed constants, data prep, and runtime utilities. **Immutable** for the agent.
- **`train.py`**: The full GPT model and training loop. **Editable** by the agent.
- **`program.md`**: Baseline instructions and **experimental protocols**. **Editable** by the human researcher.

## The Ratchet Loop (Experimental Protocol)
1. **Hypothesis**: Propose a theory for improvement.
2. **Execution**: Agent modifies **`train.py`** and runs experiment.
3. **Evaluation**: Compare result to baseline using **[[Metric Definition|scalar metric]]** (e.g., **[[Metric Definition|val_bpb]]**).
4. **Decision**: Keep (commit to git) or discard (git reset).

## Core Primitives
- **Editable Asset**: Single file (**`train.py`**) the agent is permitted to modify.
- **Scalar Metric**: Single number that determines success.
- **Time-Boxed Cycle**: Fixed **5-minute training budget** per experiment to ensure direct comparability.
- **Throughput**: ~12 experiments per hour; ~100 experiments overnight.

## Implementation & Hardware
- **Hardware**: Tested on **NVIDIA H100 80GB**.
- **Cross-Platform**: Supports smaller GPUs via forks for **[[Quantization|MacOS (MLX)]]** and **Windows (RTX)**.

---
**See also:** [[Andrej Karpathy]], [[Metric Definition]], [[Agent Skills]].
