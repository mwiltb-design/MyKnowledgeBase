Source: [[OpenRouter_GitHub_Research.md]], [[Vercel_AI_SDK_Technical_Research.md]]

## Summary
- **OpenRouter** is a **Unified API Gateway** for LLMs, standardizing access to 300+ models from multiple providers (OpenAI, Anthropic, Google, Meta, etc.) via a single OpenAI-compatible interface.
- Core benefit: Abstracting the fragmented AI landscape through a single point of access with integrated **Routing** and **Reliability** features.
- Primary repositories include `ai-sdk-provider` (for **[[Vercel AI SDK]]**) and `typescript-agent` for autonomous workflows.

## Architecture & Ecosystem
- **Unified Interface**: Standardizes request/response formats (OpenAI-compatible) across disparate models.
- **Routing & Reliability**:
    - **Provider Fallbacks**: Setting `route: "fallback"` automatically cycles through providers if the primary one fails.
    - **Response Healing**: A dedicated plugin to repair malformed JSON from models, ensuring structural integrity for structured outputs.
- **Agent-Centric Infrastructure**: Includes frameworks like **`spawn`** (deploying agents on any cloud) and **`typescript-agent`** for dynamic model switching.

## Integration Patterns
- **[[Vercel AI SDK]]**: Using `@openrouter/ai-sdk-provider` for seamless model initialization in TypeScript applications.
- **Security & Headers**: Mandatory `HTTP-Referer` (for site rankings) and `X-Title` (for app visibility) headers.
- **Authentication**: `Authorization: Bearer <OPENROUTER_API_KEY>`.

## Error Handling
- **Rate Limits (429)**: Returns `retry-after` data.
- **Insufficient Credits (402)**: Returns error when user balance is exhausted.
- **Provider Failures (502/503)**: Triggers fallback if configured.

---
**See also:** [[Agent Skills]], [[Pi Coding Agent]], [[Claude 3.7]], [[Llama 3.1]].
