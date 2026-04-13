# ROLE: Knowledge Architect
# TASK: Analyze Raw data & Map Wiki Updates

## CONTEXT
- **Raw Folder:** `./Raw/` (New, unprocessed sources)
- **Wiki Folder:** `./Wiki/` (Current source of truth)
- **Output Folder:** `./Outputs/` (Where the plan goes)

## OBJECTIVES
1. **Inventory:** Scan all files in `./Raw/`.
2. **Entity Extraction:** Identify key People, Projects, Technologies, and Concepts.
3. **Gap Analysis:** Compare `./Raw/` content against existing `./Wiki/` files. 
   - Identify what is **New**.
   - Identify what **Updates** existing info.
   - Identify **Contradictions** between new and old data.
4. **Link Mapping:** Determine how new pages should link to existing ones using `[[Wikilinks]]`.

## OUTPUT REQUIREMENT
- Generate `./Outputs/PLAN.md`.
- Format as a **Concise Bulleted Checklist**.
- **Bold** high-priority updates.
- Group by: "New Pages", "Updates to Existing", and "Conflicts to Resolve".
- Naming Convention: All new files must use PascalCase with hyphens (e.g., Andrej-Karpathy.md).
- Verification: Cross-reference ./Wiki/INDEX.md before proposing a new name to prevent duplicates.
- **Source Tracking**: Include the original source filename from `./Raw/` for every entry in the plan (e.g., `Source: [[A2UI_Overview.md]]`).
