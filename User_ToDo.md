# User To-Do List

## Formatting Instructions
- **Tasks**: Use `[ ]` for pending tasks and `[x]` for completed tasks.
- **Priority**: Use `(High)`, `(Medium)`, or `(Low)` tags if needed.
- **Notes**: Add any relevant context or sub-tasks as nested bullets.
- **Update Rule**: When a task is finished, change `[ ]` to `[x]` and move it to the "Completed" section if it gets too long.

## Active Tasks
- [ ] **A2UI Implementation: Subject Map** (High)
  - [ ] Define `A2UI_Catalog.json` for Wiki components (Card, Summary, Link).
  - [ ] Implement "Adjacency List" output format for Wiki navigation.
  - [ ] Test "Intent-based" navigation (instead of script-based loops).
- [ ] **Integrated Skill: Wiki Architect** (Medium)
  - [ ] Create `SKILL.md` for automated indexing and contradiction checking.
  - [ ] Replace `simple_agent.py` logic with integrated `read_file` and `grep_search` patterns.
- [ ] **Integrated Skill: Business Strategist** (Low)
  - [ ] Create `SKILL.md` focused on RV Park & Stone Masonry research synthesis.
- [ ] **Integrated Skill: Health Synthesis** (Low)
  - [ ] Create `SKILL.md` for factual health logging and study tracking.

## Completed Tasks
- [x] Pull latest changes from GitHub
- [x] Create `simple_agent.py` (Initial rule-based script)
  - *Note: Pivoted to Integrated Skills & A2UI for better "Brain" integration.*
- [x] Create `User_ToDo.md` and establish tracking workflow
- [x] add 'simple_agent_py'(librarian) to CLI skills
  - Notes: Set up as a 'Workspace Skill' in `.gemini/skills/wiki-librarian/`.
