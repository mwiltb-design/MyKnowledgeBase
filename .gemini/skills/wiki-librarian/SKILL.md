---
name: wiki-librarian
description: A specialized agent skill for mapping and navigating the Wiki. It can list topics, extract summaries, and deep-dive into linked articles.
---

# Wiki Librarian Instructions
You are an expert at navigating this specific knowledge base. Use this skill when the user wants to:
- Map out a specific topic to see its connections.
- See summaries of related articles within a subject.
- Deep-dive into the full content of a wiki page.

## Available Resources
- `scripts/librarian.py`: The core Python engine for mapping and navigation.

## Workflow
1. **Activate:** When the user asks to "map" or "explore" a wiki topic, activate this skill.
2. **Execute:** Use `run_shell_command` to execute the librarian script: `python .gemini/skills/wiki-librarian/scripts/librarian.py`.
3. **Interact:** The script is interactive. You may need to help the user by typing their choices (numbers or topic names) into the terminal if they ask you to do it for them, or just let them interact with the script directly.
4. **Context:** If the script finds a link to a file that is missing or has no summary, offer to use your own `google_web_search` or `read_file` tools to help fill in the gaps.
