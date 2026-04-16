Source: [[Subagents_Announcement_April2026.md]]

# Subagents

## Summary
An overview of the Subagents feature in Gemini CLI (released April 15, 2026), enabling the delegation of complex, high-volume tasks to specialized expert agents with isolated context windows and toolsets.

## Core Concepts
- **Strategic Orchestrator**: The primary agent acts as a manager, identifying sub-tasks and routing them to the most relevant **[[Subagents]]**.
- **Context Isolation**: Each subagent operates in its own separate context window, preventing context rot and pollution in the main session.
- **Atomic Execution**: Subagent tool calls and research cycles are consolidated into a single response back to the main agent.

## Built-in Subagents
- **generalist**: High-intensity batch processing and command execution.
- **cli_help**: Expert on Gemini CLI documentation and configuration.
- **codebase_investigator**: Specialized for architectural mapping and root-cause analysis.

## Custom Subagents
- **Definition**: Markdown files (`.md`) with YAML frontmatter.
- **Storage**:
    - **Global**: `~/.gemini/agents/`
    - **Project**: `.gemini/agents/`
- **Mandatory Fields**: `name` and `description` (used for routing).

## Usage
- **Automatic Routing**: Based on agent descriptions.
- **Explicit Delegation**: Using the `@agent-name` syntax (e.g., `@generalist`).
- **Parallel Execution**: Multiple subagents can run simultaneously for independent research or analysis tasks.

---
**See also:** [[Agent Skills]], [[Pi Coding Agent]], [[A2UI]].
