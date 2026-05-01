---
name: orchestra-program
description: "Explain what the orchestra methodology is — the pipeline, roles, file structure, status vocabulary, and skill index. Use when someone asks what orchestra is, how it works, or where to start."
allowed-tools: Read, Glob
---

# The Program

Present the orchestra methodology as a complete orientation. This is the program handed to every person who walks into the venue — human or agent, new collaborator or returning contributor.

## What to Present

### The Metaphor

Orchestra is a methodology for structured software development using AI agents. The name comes from the roles:

- **Composer** — the human who sets the vision and approves the work
- **Conductor** — the agent (Lenny) who interprets the score and leads execution
- **Musicians** — the skills, each playing their part in sequence
- **Score** — the spec: the agreed contract before performance begins

No musician improvises. No step is skipped. The program tells you what will be played, in what order, before the lights go dark.

---

### The Pipeline

Every piece of work moves through the same pipeline:

| Stage | Skill | What Happens |
|---|---|---|
| Capture | `/orchestra-ticket` | A work item is captured and scaffolded |
| Define | `/orchestra-prd` | Q&A with the composer produces the PRD — the *what* and *why* |
| Plan | `/orchestra-spec` | Q&A with the composer produces the spec — the *how* |
| Validate | `/orchestra-gherkin` | Acceptance criteria written as testable Gherkin scenarios |
| **Approve** | *(human gate)* | Composer signs off — the score is locked |
| Implement | `/orchestra-implement` | A branch is created, spec steps executed, commits made |
| Review | `/orchestra-review` | Every acceptance criterion checked with evidence — PASS or FAIL |
| Merge | `/orchestra-merge` | Reviewed branch merged to main, work item closed |

The Q&A before the spec is what makes the rest possible. A tight spec is a spec the implementer can execute without asking questions.

---

### Status Vocabulary

Work items carry a status that tracks exactly where they are in the pipeline:

```
draft → approved → in-progress → complete → reviewed → closed
```

| Status | Meaning |
|---|---|
| `draft` | PRD or spec written, not yet approved |
| `approved` | Composer has signed off — ready for next stage |
| `in-progress` | Implementation underway |
| `complete` | Implementation done, awaiting review |
| `reviewed` | Review passed — ready to merge |
| `closed` | Merged and done |

---

### File Structure

Everything lives under `.orchestra/` in the project root:

```
.orchestra/
├── roadmap.md              — Vision, milestones, active work
├── work/
│   └── {id}-{name}/
│       ├── prd.md          — The what and why
│       ├── spec.md         — The how
│       └── gherkin-spec.md — Acceptance criteria
├── adr/
│   └── 001-*.md            — Architectural decisions, numbered
└── devlog/
    └── YYYY-MM-DD-*.md     — Developer journals
```

Work item folders are named `{ticket-id}-{short-name}`. The ticket ID comes from ClickUp. If no ticket exists yet, use a descriptive slug.

---

### Skill Index

**Planning skills** — left side of the pipeline:

| Skill | Purpose |
|---|---|
| `orchestra-ticket` | Capture a work item and scaffold its folder |
| `orchestra-prd` | Generate a PRD from a milestone gap |
| `orchestra-spec` | Generate an execution spec from an approved PRD |
| `orchestra-gherkin` | Generate Gherkin scenarios from a spec |
| `orchestra-roadmap` | Read and manage the roadmap |
| `orchestra-milestone` | Review milestone progress, surface gaps |
| `orchestra-adr` | Capture an architectural decision |
| `orchestra-devlog` | Write developer journals |
| `orchestra-scaffold` | Bootstrap the `.orchestra/` structure in a new project |
| `orchestra-uml` | Generate UML diagrams as Mermaid code |

**Execution skills** — right side of the pipeline:

| Skill | Purpose |
|---|---|
| `orchestra-implement` | Execute an approved spec on a branch |
| `orchestra-review` | Review a completed implementation against its spec |
| `orchestra-merge` | Merge a reviewed branch to main and close the work item |

---

### Where to Start

**New to this repo?** Run `/orchestra-roadmap` to see the vision, active milestones, and current work items.

**Starting new work?** Run `/orchestra-ticket` to capture it, then follow the pipeline.

**Picking up existing work?** Find the work item folder under `.orchestra/work/`, read the spec, check the status, and invoke the skill that matches.

**Coming back after a break?** Run `/orchestra-milestone`. It reads `roadmap.md`, finds the first milestone that isn't Done, checks what's missing from its materials table, and tells you exactly what to do next. One command gets you oriented regardless of where you left off — no need to remember where you were.

---

## Reading the Repo

If the user wants a live picture of the current project alongside the program, read:
- `.orchestra/roadmap.md` — for the current vision and milestones
- `.orchestra/work/*/prd.md` — to list active work items and their statuses

Present the live state after the program overview if it adds useful context.
