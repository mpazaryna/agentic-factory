# dev-context (Lean)

Set up working context for GitHub issues. Create formal ADRs when needed.

## Quick Start

```
"Set up context for issue #115"     → Creates docs/specs/115-feature-name.md
"Create ADR for choosing X over Y"  → Creates docs/adr/NNN-*.md
```

## Two Modes

### 1. Issue Spec (Default)
Creates a spec file for multi-session tasks:
```
docs/specs/{num}-{short-name}.md
```

### 2. Architecture Decision Record
For major decisions that warrant formal documentation:
```
docs/adr/NNN-decision-name.md
```

## Philosophy

This is a **lean** context skill. Most work doesn't need formal documentation:

| Need | Solution |
|------|----------|
| Task definition | GitHub issue |
| Working notes | `docs/specs/` files |
| Decision history | Devlogs → ADRs |
| Major architecture decision | ADR (use sparingly) |

## Structure

```
dev-context/
├── skill.md                    # Main skill definition
├── README.md                   # This file
└── references/
    └── templates/
        └── adr.md              # ADR template
```

## Part of the dev-* Family

| Skill | Purpose |
|-------|---------|
| `dev-context` | Set up working space, create ADRs |
| `dev-explore` | Analyze codebases, export docs |
| `dev-reports` | Write devlogs |
| `dev-inquiry` | Technical investigation |

## See Also

- `docs/specs/README.md` - Working space conventions
- `docs/adr/ADR-003-documentation-maintenance-workflows.md` - Maintenance cycles
