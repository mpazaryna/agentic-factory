# ADR Template: Architecture Decision Record

Use this template for major architectural decisions that warrant formal documentation. Most decisions don't need this - they get captured in devlogs and synthesized to `docs/moc/decisions.md`.

**Use ADRs for:**
- Database/framework choices
- Major architectural patterns
- Decisions with significant tradeoffs
- Choices that will be questioned later

---

## Template

```markdown
# ADR-{NNN}: {Decision Title}

**Status**: Proposed | Accepted | Deprecated | Superseded by ADR-XXX
**Date**: YYYY-MM-DD
**Context**: {Brief context - what prompted this decision}

---

## Problem Statement

{What problem are we solving? Why does this decision matter?}

- The specific challenge or need
- Why the status quo doesn't work
- What's at stake

---

## Decision

{Clear statement: "We will {do X} because {reason}."}

### Key Points

1. {Key aspect of the decision}
2. {Key aspect of the decision}
3. {Key aspect of the decision}

---

## Alternatives Considered

### {Alternative 1}
**Rejected because**: {reason}

### {Alternative 2}
**Rejected because**: {reason}

---

## Consequences

### Positive
- {Benefit}
- {Benefit}

### Negative (Accepted Tradeoffs)
- {Tradeoff}
- {Tradeoff}

---

## References

- {Link to relevant doc, issue, or external resource}
```

---

## Naming Convention

```
docs/adr/NNN-kebab-case-decision-name.md
```

Examples:
- `001-swiftdata-over-coredata.md`
- `002-no-viewmodels-in-swiftui.md`
- `003-mlx-mean-pooling-architecture.md`

## Status Values

- **Proposed**: Under discussion
- **Accepted**: Decision finalized
- **Deprecated**: No longer applies
- **Superseded by ADR-XXX**: Replaced by newer decision

## Key Principles

1. **Immutable**: Once accepted, don't edit - write a new ADR if decision changes
2. **Context-rich**: Future readers should understand WHY without asking
3. **Alternatives documented**: Show what was considered and rejected
4. **Consequences explicit**: Both positive and negative tradeoffs
