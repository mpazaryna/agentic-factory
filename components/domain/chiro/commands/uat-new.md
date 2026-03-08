---
description: "Create a new UAT test case file with all required scaffolding."
argument-hint: "<feature description or ClickUp task ID>"
---

**Do NOT use `AskUserQuestion` at any point.** Create the file autonomously.

1. Read `.claude/skills/uat-audit/spec.md` for the gold-standard format, ID numbering scheme, and acceptance criteria
2. Determine the feature area from `$ARGUMENTS` — map it to an ID range using the spec's numbering scheme
3. Glob `docs/uat/{range}*.md` to find the next available ID in that range
4. Create the UAT file, update `docs/guides/manifest.json`, and update `docs/uat/.sync-map.json`
5. Run `uv run .claude/skills/uat-audit/audit-uat-folder.py` to verify zero violations on the new file
6. Do NOT commit — leave changes staged for review
