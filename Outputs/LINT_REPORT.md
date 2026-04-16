# Wiki Audit Report (LINT)

## Summary
- **Total Articles**: 50
- **Status**: **STRUCTURAL FAILURE** (Formatting and link issues detected)

## Broken / Missing Links (Stubs)
- **[[TypeScript]]**: Linked in `Vercel AI SDK.md` but file is missing.
- **[[Modelfile]]**: Linked in `Ollama.md` but file is missing.
- **[[RV-Park-Infrastructure]]**: Formatting error in `RV Park Operations 2026.md`.
- **[[RV-Park-Operations-2026]]**: Formatting error in `RV Park Infrastructure.md`.
- **[[Ollama.md]]**, **[[Vercel AI SDK.md]]**, etc.: Invalid links in `LOG.md` (extension included).

## Orphaned Files
The following files are present in `./Wiki/` but are NOT linked in `INDEX.md`:
1. **[[ACP Mode]]**
2. **[[DuckDB]]**
3. **[[LanceDB]]**
4. **[[PocketBase]]** (Linked from other pages, but missing from Index)
5. **[[PostgreSQL]]** (Linked from other pages, but missing from Index)
6. **[[Qdrant]]** (Linked from other pages, but missing from Index)
7. **[[SQLite]]** (Linked from other pages, but missing from Index)

## Formatting & Synthesis Issues
- **[[Subagents]]**: Page is a raw dump of an announcement. Missing `## Summary` and proper Wiki structure.
- **Source Links**: Multiple pages use `[[Vault_File.md]]` style links. These should be clarified as sources or converted to Wiki links if relevant.

## Contradiction Detection
- **Gemma 4**: Released date (April 2, 2026) confirmed across Vault and Wiki. No metric conflicts found.

## Critical Actions
- **Bold** formatting check: Most pages follow rules, but `Subagents.md` is non-compliant.
- **Index Update**: Add missing Technical Domains (Databases).
- **Link Repair**: Fix hyphenated wikilinks and remove extensions from `LOG.md`.
