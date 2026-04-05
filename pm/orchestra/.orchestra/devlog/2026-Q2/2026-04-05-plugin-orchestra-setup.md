---
created_on: 2026-04-05
---

# 2026-04-05: Orchestra Plugin — Dogfooding Session

## What Happened

- Added YAML frontmatter to generated PRD and spec files (v1.6.0)
- Wrote and accepted ADR-001: Artifact Frontmatter Contract (v1.7.0)
- Established per-plugin `.orchestra/` pattern — each installable plugin in the monorepo carries its own agent knowledge base
- Scaffolded `pm/orchestra/.orchestra/` as the first per-plugin instance

## Decisions

- Per-plugin `.orchestra/` folders are the right granularity for a monorepo. One root folder mixes concerns across unrelated plugins.
- The `.orchestra/` folder is not dev scaffolding — it's ambient context for any agent that opens the plugin folder. When you distribute an agentic team, they need it.
- Initial status on PRDs should be `draft`, not `in-progress`. Status vocabulary is now per-artifact-type per ADR-001.

## Next Steps

- Update scaffold and conventions skills to document the per-plugin pattern
- Build the `orchestra:adr` skill (flagged in ADR-001 consequences)
- Adopt per-plugin `.orchestra/` in at least one other plugin (kairos is the natural next candidate)
