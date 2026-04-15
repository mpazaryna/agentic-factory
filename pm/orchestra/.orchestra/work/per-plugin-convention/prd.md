---
status: in progress
created_on: 2026-04-05
---

# Per-Plugin Orchestra Convention

**Objective:** Each installable plugin in the agentic-factory monorepo carries its own `.orchestra/` folder, making the plugin self-describing for both agents and human contributors.

## Success Criteria

- [x] orchestra plugin has `.orchestra/` at `pm/orchestra/.orchestra/`
- [ ] scaffold skill documents the per-plugin pattern
- [ ] conventions skill references the per-plugin pattern
- [ ] CLAUDE.md at repo root documents the expectation
- [ ] At least one other plugin adopts the pattern

## Context

The insight driving this: `.orchestra/` isn't dev scaffolding — it's ambient context for any agent that opens the plugin folder. When you distribute an agentic team, they need to know the project's decisions, roadmap, and what's in flight. The `.orchestra/` folder is how you tell them.

In a monorepo of plugins, one root `.orchestra/` mixes concerns across unrelated plugins. Per-plugin folders keep context scoped and make each plugin independently navigable by agents.

## Materials

| Material | Location | Status |
|----------|----------|--------|
| orchestra plugin .orchestra/ | pm/orchestra/.orchestra/ | In Progress |
| scaffold skill update | pm/orchestra/scaffold/SKILL.md | Not Started |
| conventions skill update | pm/orchestra/conventions/SKILL.md | Not Started |
| repo CLAUDE.md update | CLAUDE.md | Not Started |

## References

- ADR-000: The Score (.orchestra/adr/ADR-000-the-score.md)
- ADR-001: Artifact Frontmatter Contract (.orchestra/adr/ADR-001-artifact-frontmatter-contract.md)
