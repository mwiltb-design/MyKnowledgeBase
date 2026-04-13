# A2UI (Agentic AI User Interface) Technical Overview

## 1. Architecture & Data Flow
A2UI uses a **declarative, component-based architecture** that separates the "brain" (AI Agent) from the "body" (Client Renderer).

*   **Interaction Flow:**
    1.  **User Input:** User sends a message to the AI agent.
    2.  **Agent Generation:** The agent generates **A2UI messages** (JSON) describing the UI structure and data.
    3.  **Streaming:** These messages are streamed to the client application in real-time.
    4.  **Native Rendering:** The client (Angular, Flutter, React, etc.) interprets the JSON and renders it using **native widgets** from a pre-defined catalog.
    5.  **Action Loop:** User interactions (clicks, form submissions) trigger **Actions** that are sent back to the agent, which then responds with updated UI states.
*   **Adjacency List Model:** The UI is represented as a flat list of components rather than a deep tree, making it easier for LLMs to generate and stream incrementally.

## 2. JSON Schema / Protocol (v0.8 Stable)
The protocol is designed to be **LLM-friendly**, using a flat, streaming-capable JSON structure. It avoids complex nesting to prevent "JSON hallucination" by the model.

### Payload Example (Conceptual):
```json
{
  "type": "surface",
  "id": "main-view",
  "components": [
    {
      "id": "header-1",
      "type": "Text",
      "props": {
        "content": "Restaurant Finder",
        "style": "h1"
      }
    },
    {
      "id": "map-view",
      "type": "GoogleMap",
      "props": {
        "lat": 37.7749,
        "lng": -122.4194,
        "zoom": 12
      }
    },
    {
      "id": "submit-btn",
      "type": "Button",
      "props": {
        "label": "Book Now"
      },
      "events": {
        "onPress": {
          "action": "book_reservation",
          "params": { "id": "rest_123" }
        }
      }
    }
  ]
}
```

## 3. Integration Patterns
Agents do not "write code"; they **describe intent** using a shared vocabulary (the **Component Catalog**).
*   **Catalogs:** The client defines a "Catalog" of allowed components (e.g., `Button`, `Chart`, `Map`). The agent is instructed (via system prompt) on which components are available and their required properties.
*   **Transports:** A2UI can be delivered over various transports, including **MCP (Model Context Protocol)**, WebSockets, or standard HTTP streams.
*   **Data Binding:** The protocol supports binding UI elements to dynamic data states, allowing the agent to update specific values without re-sending the entire UI.

## 4. Security: Avoiding Arbitrary Code Execution
A2UI is **Secure by Design** because it strictly forbids the execution of code sent from the agent.
*   **Declarative Only:** The agent sends *data* (JSON), not *logic* (JavaScript/Python). The client renderer contains all the actual executable code.
*   **Pre-approved Components:** The client only renders components that exist in its local catalog. If an agent tries to inject a `<script>` tag or an unknown component, the renderer simply ignores it.
*   **Trust Boundaries:** Because the UI is rendered natively, it inherits the security sandbox of the host application (e.g., a mobile app's permissions or a web app's CSP).

## 5. Protocol Versions
*   **v0.8 (Stable):** Focuses on surfaces, components, and the adjacency list model.
*   **v0.9 (Draft):** Introduces `createSurface`, client-side functions, and custom catalogs for more complex state management.

---
**Source:** [A2UI (https://a2ui.org/)](https://a2ui.org/)
**Date Fetched:** 2026-04-12
