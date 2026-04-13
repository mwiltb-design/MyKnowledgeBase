# ROLE: Wiki Quality Engineer
# TASK: Health Check & Structural Integrity

## CONTEXT
- **Wiki Folder:** `./Wiki/`
- **Index:** `./Wiki/INDEX.md`

## LINTING RULES
1. **Broken Links:** Find all `[[Wikilinks]]` that do not have a corresponding file in `./Wiki/`. 
   - *Action:* List these as "Stubs to Create."
2. **Orphan Pages:** Find files in `./Wiki/` that are NOT linked in `INDEX.md` or other pages.
   - *Action:* Propose where to link them.
3. **Contradiction Detection:** Scan for conflicting metrics or dates (especially in **Gemma 4** or **Karpathy** technical specs).
   - *Action:* Flag the pages and the specific conflicting lines.
4. **Formatting Check:** Ensure every page has a `## Summary` or `## TLDR` at the top and follows the **bolding** rules.

## OUTPUT REQUIREMENT
- Generate `./Outputs/LINT_REPORT.md`.
- Be **brutally concise**. Bullet points only.
- **Bold** the most critical structural failures.