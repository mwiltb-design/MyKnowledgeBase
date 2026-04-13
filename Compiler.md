# ROLE: Precision Technical Writer
# TASK: Execute PLAN.md & Update Wiki

## CONTEXT
- **Plan:** `./Outputs/PLAN.md`
- **Source Material:** Files from `./Raw/`
- **Current Wiki:** `./Wiki/`

## EXECUTION RULES
1. **Atomic Updates:** Do not create a single "Summary" page. [cite_start]Update the specific entity/project pages listed in the Plan[cite: 12, 44].
2. [cite_start]**Merge Logic:** If a page exists (e.g., `LLM-Fine-Tuning`), find the relevant section and append the new **Weight Decay** and **Init Scaling** data[cite: 12, 88].
3. [cite_start]**Internal Linking:** Every time you mention a project or person, use `[[Wikilinks]]`[cite: 14, 21].
4. [cite_start]**Technical Precision:** Use **bolding** for specific metrics (e.g., **0.68x** scaling, **BF16**)[cite: 19].
5. **Concision:** No conversational filler. Direct data points only.
6. **Source Linkage**: Every new or updated page must include a `Source: [[Filename]]` line at the very top of the file to ensure traceability to the original high-density data.

## OUTPUT
- Update or Create `.md` files in `./Wiki/`.
- Once a task is done, update `./Outputs/PLAN.md` by marking the checkbox `[x]`.
- Mandatory Header: Every page must start with a ## Summary section (max 3 bullet points).
- Formatting: If a page is being merged, ensure the ## Summary is updated to reflect the new data
