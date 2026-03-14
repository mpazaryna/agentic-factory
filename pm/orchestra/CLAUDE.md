# Orchestra

The `.orchestra/` agent knowledge base methodology — PRDs all the way down.

## Skills

### Setup
- **scaffold** — Create the .orchestra/ folder structure, templates, and initial roadmap

### Conductor (the planning loop)
- **milestone-review** — Diff materials table against repo state, surface gaps, propose next work
- **write-prd** — Generate a PRD from a milestone gap
- **write-spec** — Generate an execution spec from an approved PRD
- **create-ticket** — Push an approved spec to ClickUp as an executable ticket

### Operations
- **roadmap** — Read and manage roadmap.md: status, next work, updates, add milestones

### Background
- **conventions** — The methodology, roles, folder structure, rules (Claude-only)

## The Loop

```
/milestone-review → /write-prd → /write-spec → /create-ticket → /open → implement → /close → update materials table
```

## References

- `references/adr-000-the-score.md` — Founding decision: the orchestra metaphor and PRD hierarchy
- `references/readme-template.md` — Template for .orchestra/README.md
- `references/prd-template.md` — PRD template (used at roadmap, milestone, and work-item level)
- `references/spec-template.md` — Spec template for execution detail
