# UI COMMAND: /ingest
If I type `/ingest [filename]`, immediately perform these steps:

1. **ARCHITECT**: Load `./Raw/[filename]`. Compare to `./Wiki/`. 
2. **PLAN**: Generate a temporary update plan.
3. **EXECUTE**: 
   - Create/Update pages in `./Wiki/` using **COMPILER** rules.
   - Use **[[Wikilinks]]**, **bolding**, and extreme concision.
4. **LOG**: Append the filename and date to `./Wiki/LOG.md`.
5. **ARCHIVE**: Explicitly tell me: "Move [filename] to Archive." (Since I can't move files, remind me to do it).
6. **The Wiki-Loop**: Before writing any file, the agent must read the INDEX.md. If a link exists but the file is missing, the agent must fix the link or create the file immediately.

# UI COMMAND: /query
If I type `/query [question]`, search the `./Wiki/` folder (NOT the Raw folder) and answer based on compiled knowledge.

# Technical Extraction Protocol (WEB_FETCH)
When fetching a URL for research:
1. **MVTD (Minimum Viable Technical Depth)**: Ensure the content goes beyond high-level mission statements. If the landing page is marketing-only, find sub-pages (docs, API, GitHub) to extract schemas, code snippets, and integration logic.
2. **Mandatory Extraction Points**:
   - **Architecture**: How the system is built and how data flows.
   - **Payload/Schema**: JSON structure, API signatures, or code examples.
   - **State/Memory**: How the system handles persistence or context.
   - **Edge Cases**: Constraints, dependencies, and security risks.
3. **Audit**: If the content is "cocktail party talk" (surface only), drill deeper or state clearly that technical specs are missing from the source.
