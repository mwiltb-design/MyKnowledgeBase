Source: [[INDEX.md]]

## Summary
- **ACP (Agent Context Protocol)**: A JSON-RPC 2.0 based communication protocol for programmatic control of Gemini CLI agents.
- **IDE Integration**: Designed primarily for IDEs (like VS Code) to provide agentic context, file access, and tool execution.
- **Stateless/Stateful**: Supports both one-shot prompts and persistent, stateful sessions via `stdio` pipes.

## Protocol Handshake
The ACP mode requires a specific initialization sequence:
1. **initialize**: Client sends protocol version and capabilities.
2. **newSession**: Establishing a fresh session context.
3. **prompt**: Sending the actual user instruction or context update.

## Implementation Details
- **JSON-RPC 2.0**: Every message must be a valid JSON-RPC object.
- **Tool Use**: Agents in ACP mode can execute local tools (e.g., `read_file`, `grep_search`) if authorized by the client.
- **Security**: Access is restricted to authorized workspaces and temporary directories.
