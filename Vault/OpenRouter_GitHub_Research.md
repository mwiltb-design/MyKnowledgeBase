# OpenRouter GitHub Technical Research

## 1. Architecture & Ecosystem Overview
OpenRouter functions as a **Unified API Gateway** for LLMs, standardizing access to 300+ models from multiple providers (OpenAI, Anthropic, Google, Meta, etc.) via a single OpenAI-compatible interface.

### Key Repositories
- **`ai-sdk-provider`**: The OpenRouter provider for the **Vercel AI SDK**.
- **`typescript-sdk` / `python-sdk` / `go-sdk`**: Official SDKs for core backend stacks.
- **`spawn`**: A framework for deploying autonomous agents on any cloud.
- **`typescript-agent`**: Dedicated SDK for agentic workflows.

## 2. API Payload Schema (v1.0)
OpenRouter uses an OpenAI-compatible schema with extended fields in `extraBody` for routing and provider-specific controls.

### Request Payload Example:
```json
{
  "model": "anthropic/claude-3.7-sonnet",
  "messages": [
    { "role": "user", "content": "Explain the 'Grunt Test' for RV websites." }
  ],
  "extraBody": {
    "route": "fallback",
    "provider": {
      "allow_fallbacks": true,
      "require_parameters": true
    },
    "transforms": ["middle-out"]
  },
  "stream": true
}
```

### Response Payload Example:
```json
{
  "id": "gen-123",
  "model": "anthropic/claude-3.7-sonnet",
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "The Grunt Test is a UX principle..."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 15,
    "completion_tokens": 45,
    "total_tokens": 60
  }
}
```

## 3. Integration Patterns (Vercel AI SDK)
The `@openrouter/ai-sdk-provider` is the primary integration path for modern TypeScript applications.

### Implementation Snippet:
```typescript
import { createOpenRouter } from '@openrouter/ai-sdk-provider';
import { generateText } from 'ai';

const openrouter = createOpenRouter({
  apiKey: process.env.OPENROUTER_API_KEY,
  headers: {
    "HTTP-Referer": "https://your-site.com", // Used for OpenRouter rankings
    "X-Title": "My RV Park App",             // App name visibility
  }
});

const { text } = await generateText({
  model: openrouter('anthropic/claude-3-7-sonnet'),
  prompt: '...',
});
```

## 4. Routing & Reliability
- **Model IDs**: Uses `provider/model-name` (e.g., `openai/gpt-4o`).
- **Provider Fallbacks**: Setting `route: "fallback"` allows OpenRouter to cycle through available providers automatically.
- **Response Healing**: Includes a plugin to repair malformed JSON from models, ensuring structural integrity for agentic outputs.

## 5. Security & Error Handling
- **Authentication**: `Authorization: Bearer <KEY>`.
- **Headers**: Mandatory `HTTP-Referer` and `X-Title` for application identification.
- **Error Codes**:
  - `429`: Rate limit (includes `retry-after`).
  - `402`: Insufficient credits.
  - `502/503`: Provider failure (triggers fallback if enabled).

---
**Source:** [OpenRouter GitHub Organization](https://github.com/OpenRouterTeam)
**Date Fetched:** 2026-04-12
