---
status: approved
created_on: 2026-04-05
---

# Orchestra Plugin Roadmap

**Objective:** A complete, self-consistent methodology plugin that agents can use to manage any project — and that uses itself to manage its own development.

## Success Criteria

- [ ] Every skill produces artifacts with conforming frontmatter
- [ ] The plugin's own development is tracked in this `.orchestra/` folder
- [ ] An agent opening this folder cold can understand the plugin's state and history
- [ ] The methodology is stable enough that other plugins can adopt the per-plugin `.orchestra/` pattern

## Context

Orchestra started as a methodology for managing agentic projects via PRDs all the way down. It lives in a monorepo of Claude Code plugins (agentic-factory). The plugin is both the tool and a demonstration of the tool — its own development should model the methodology it teaches.

The per-plugin `.orchestra/` pattern means each installable plugin in the monorepo carries its own roadmap and decision history. Agents opening a plugin folder get full context without querying external systems.

## Milestones

| Material | Location | Status |
|----------|----------|--------|
| Core Loop | .orchestra/work/core-loop/prd.md | Done |
| Frontmatter Contract | .orchestra/work/frontmatter-contract/prd.md | Done |
| ADR Skill | .orchestra/work/adr-skill/prd.md | Not Started |
| Per-Plugin Convention | .orchestra/work/per-plugin-convention/prd.md | In Progress |

## References

- [ADR-000: The Score](adr/ADR-000-the-score.md)
- [ADR-001: Artifact Frontmatter Contract](adr/ADR-001-artifact-frontmatter-contract.md)
