---
status: accepted
created_on: 2026-04-05
---

# ADR-001: Orchestra Artifact Frontmatter Contract

## Context

Bench indexes `.orchestra/` folders across all managed repos into SQLite for display and filtering. Initially, metadata like status and date was embedded as bold fields in markdown content (`**Status:** Accepted`, `**Date:** 2026-02-22`). This worked for human reading but required fragile regex extraction for agents and bench.

Separately, the question arose of how sub-agents should be kicked off from work items. The answer was a `ticket` field in frontmatter pointing to the originating ticket in the external ticketing system (ClickUp). This created a need to formalize which fields belong on which artifact types.

The five orchestra artifact types are: ADR, PRD, spec, devlog, UML.

## Decision

All orchestra artifacts carry YAML frontmatter. The fields are standardized per artifact type as follows:

| Field | ADR | PRD | spec | devlog | UML |
|-------|-----|-----|------|--------|-----|
| `created_on` | yes | yes | yes | yes | yes |
| `status` | yes | yes | yes | — | — |
| `ticket` | — | yes | yes | — | — |

### Status vocabularies

Each artifact type uses its own status vocabulary appropriate to its lifecycle:

**ADR:**
- `proposed` — decision under consideration
- `accepted` — active, this is how we do it
- `deprecated` — no longer applies
- `superseded` — replaced by a newer ADR

**PRD:**
- `draft` — being written
- `approved` — scoping complete, ready to hand off to spec
- `complete` — the work it described is done

**spec:**
- `draft` — being written
- `approved` — ready to implement
- `in-progress` — actively being worked
- `complete` — implemented

Devlog and UML carry no `status` — devlogs are journal entries (always done), UML diagrams are reference material without a meaningful lifecycle status.

### Ticket field

The `ticket` field appears only on PRDs and specs. It is a reference to the originating ticket in the external ticketing system and serves two purposes:

1. **Audit trail** — traceability from orchestra artifact back to the ticket that initiated the work
2. **Agent context** — a sub-agent can look up the ticket for additional context at kickoff

The ticket is not the source of truth for status. Status lives in the file. The ticket lifecycle is owned by humans in the ticketing system; the orchestra folder lifecycle is owned by agents and read by bench.

### Two audiences, two systems

This decision formalizes a clean separation:

- **Ticketing system** — human-facing. Managers read status there. Ticket lifecycle is closed by humans when work ships.
- **Orchestra folder** — agent-facing. Agents glob artifact types and read frontmatter to understand what is in flight, what decisions have been made, and what work remains. Bench reads the same frontmatter for filtering and display.

Agents should be able to answer "what's in flight?" from `.orchestra/` frontmatter alone, without querying the ticketing system.

### ADRs as ambient context

ADRs are not initiated by tickets. They are decisions that surface during the execution of ticketed work and are written by agents as that work proceeds. Future agents glob `.orchestra/adr/` before starting work to understand prior decisions — ADRs inform rather than initiate. The ticket → PRD → spec chain handles *what* is being built; the ADR folder handles *why we decided this*.

## Consequences

- The `orchestra:adr`, `orchestra:prd`, `orchestra:spec`, and `orchestra:devlog` skills should write conforming frontmatter when creating new files.
- Bench `lib/db.ts` indexes `status`, `created_on`, and `ticket` from frontmatter as the authoritative source, with no fallback to bold-field extraction for new artifacts.
- Status vocabularies are kept distinct per type — bench filters by artifact type before filtering by status.
