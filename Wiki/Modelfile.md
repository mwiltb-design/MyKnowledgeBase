# Modelfile

## Summary
The configuration file format used by **[[Ollama]]** to define and create custom LLM instances, including system prompts, parameters, and template definitions.

- **BASE**: Specifies the foundation model (e.g., `FROM gemma4:e4b`).
- **SYSTEM**: Defines the behavior and persona of the agent.
- **PARAMETER**: Configures model-specific settings like `num_ctx` or `temperature`.
- **TEMPLATE**: Sets the specific prompt structure for the model.

---
**See also:** [[Ollama]], [[Quantization]], [[Gemma 4]].
