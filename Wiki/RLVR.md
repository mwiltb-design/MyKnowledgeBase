Source: [[Fine_tune_VLM.md]]

## Summary
- **Reinforcement Learning for Verified Rewards** (RLVR) is a technique used to optimize model outputs against specific, verifiable criteria.
- **Verification Rule:** A reward function that assigns a binary score (+1 for success, 0 for failure) based on the output format.
- **Use Case:** Used in **[[SmolVLM2]]** to penalize and eliminate **repetitive generation** in JSON payloads.

## Logic
1. **Reward Function:** Define the desired behavior (e.g., "JSON must not contain redundant keys").
2. **Training:** The model receives feedback for each output generated.
3. **Policy Update:** The model's behavior shifts towards higher reward (correctly structured, non-repetitive) outputs.

---
**See also:** [[VLM]], [[SmolVLM2]], [[LLM Fine Tuning]].
