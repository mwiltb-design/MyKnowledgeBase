Source: [[Vercel_AI_SDK_Technical_Research.md]]

## Summary
- **Vercel AI SDK** is a provider-agnostic TypeScript toolkit for building AI-powered applications and agentic workflows.
- Standardizes interactions across OpenAI, Anthropic, Google, and **[[OpenRouter]]** via a unified provider interface.
- Core focus on **Generative UI** and type-safe structured data generation using **Zod**.

## Primary Functions
- **`generateText` / `streamText`**: High-level functions for text generation with integrated token tracking.
- **`generateObject` / `streamObject`**: Specialized for creating type-safe JSON payloads conforming to a specific schema.

## Agentic Capabilities
- **Tool Calling**: Native support for defining and executing tools with Zod parameters.
- **`ToolLoopAgent`**: Automated orchestrator for multi-step model-tool interaction cycles.
- **Generative UI**: Real-time mapping of tool-call results to React/UI components.

---
**See also:** [[OpenRouter]], [[TypeScript]], [[Pi Coding Agent]].
