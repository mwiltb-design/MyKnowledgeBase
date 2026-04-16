Source: [[Pi_Coding_Agent_Technical_Research.md]], [[Hermes_Agent_Technical_Research.md]], [[OpenRouter_GitHub_Research.md]]

# Agent Skills

## Summary
- Modular capabilities that extend the functionality of autonomous agents for research and data processing.
- Can be activated within a primary session or delegated to specialized **[[Subagents]]** for isolated, expert execution.
- Combines **Declarative Skills** (pre-written instructions) with **Procedural Skills** (autonomously learned sequences).

## Implementation Patterns
- **Markdown-based (Pi)**: Capability packages defined in `SKILL.md` files that provide structured logic and tool-use instructions.
- **Procedural (Hermes)**: Autonomously generated tool-calling sequences stored in a local skills repository after task completion.
- **Native Extensions**: TypeScript modules (Pi) or Python toolsets (Hermes) that register new commands and UI components.

## Core Capabilities
- **Web Scraping**: Integration via **[[OxyLabs MCP]]**.
- **Inference**: High-reliability access to 300+ models via **[[OpenRouter]]**.
- **Experimental Loop**: Execution of the **[[AutoResearch|Karpathy Loop]]** protocol.
- **Synthesis**: Automated data extraction and Wiki propagation.

## Management
- **Persistence**: Skills reside in `~/.pi/agent/skills/` or `~/.gemini/skills/`.
- **Orchestration**: Agents can dynamically select skills or delegate tasks to **[[Subagents]]** using the `@agent` syntax.

---
**See also:** [[Pi Coding Agent]], [[Hermes Agent]], [[MCP]].
