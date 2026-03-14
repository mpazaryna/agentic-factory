# Orchestra

The `.orchestra/` agent knowledge base methodology — PRDs all the way down.

## Skills

### Setup
- **scaffold** — Create the .orchestra/ folder structure, templates, and initial roadmap

### Conductor (the planning loop)
- **milestone** — Diff materials table against repo state, surface gaps, propose next work
- **prd** — Generate a PRD from a milestone gap
- **spec** — Generate an execution spec from an approved PRD
- **ticket** — Push an approved spec to ClickUp as an executable ticket
- **conduct** — Run the entire loop autonomously (forked context, no human checkpoints)

### Operations
- **roadmap** — Read and manage roadmap.md: status, next work, updates, add milestones

### Background
- **conventions** — The methodology, roles, folder structure, rules (Claude-only)

## The Loop

```
/conduct (autonomous)
  or step-by-step:
/milestone → /prd → /spec → /ticket → /open → implement → /close → update score
```

## References

- `references/adr-000-the-score.md` — Founding decision: the orchestra metaphor and PRD hierarchy
- `references/readme-template.md` — Template for .orchestra/README.md
- `references/prd-template.md` — PRD template (used at roadmap, milestone, and work-item level)
- `references/spec-template.md` — Spec template for execution detail
