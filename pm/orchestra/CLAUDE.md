# Orchestra

The `.orchestra/` agent knowledge base methodology — PRDs all the way down.

## Skills

### Setup
- **scaffold** — Create the .orchestra/ folder structure, templates, and initial roadmap
- **ticket** — Capture a work ticket as the starting point, scaffold the work item folder

### Planning (the loop)
- **milestone** — Diff materials table against repo state, surface gaps, propose next work
- **prd** — Expand a ticket brief into a full PRD with objective, criteria, materials table
- **spec** — Derive an execution spec from an approved PRD

### Operations
- **roadmap** — Read and manage roadmap.md: status, next work, updates, add milestones
- **devlog** — Document work sessions: journals, devlogs, status updates
- **uml** — Generate Mermaid diagrams (sequence, class, deployment, component, state) into .orchestra/uml/

### Background
- **conventions** — The methodology, roles, folder structure, rules (Claude-only)

## The Loop

```
/ticket → /prd → /spec → implement → /devlog
```

The autonomous version of this loop is the **lenny** agent (`agents/lenny.md`).

**Document ownership:** PRDs are product-layer documents refined only with requestor input. Specs are execution-layer documents derived from PRDs and refined by the agent at runtime.

## References

- `references/adr-000-the-score.md` — Founding decision: the orchestra metaphor and PRD hierarchy
- `references/readme-template.md` — Template for .orchestra/README.md
- `references/prd-template.md` — PRD template (used at roadmap, milestone, and work-item level)
- `references/spec-template.md` — Spec template for execution detail
