# Orchestra

A methodology for agent-driven project execution. The metaphor is literal: every project is a performance, and every performance needs a score.

## The Metaphor

An orchestra doesn't improvise symphonies. Musicians read from a score, follow a conductor, and produce something greater than any individual could. Software projects work the same way when agents are involved.

**The Score** is the roadmap — a PRD that defines the vision and lists milestones. Milestones are PRDs that list deliverables. Deliverables are the actual files in your repo. PRDs all the way down.

**The Composer** is you. You write the score. You decide what gets built, in what order, and what "done" looks like. You evaluate inputs from stakeholders, research, and agents before anything enters the system. The composer is always human.

**The Conductor** interprets the score and keeps tempo. Today, that's you — reading the active milestone, identifying what's not done, and pointing agents at the next piece of work. Over time, as structure improves, this role shifts agentic. Clear done-conditions and machine-readable materials tables make the conductor role delegatable.

**The Orchestra** is your agents. They read the score for context, pick up tickets as contracts, execute the work, and update the score when they're done. An agent that completes work but doesn't update the PRD hasn't finished the job.

**The Audience** — co-founders, stakeholders, investors — experiences the output, never the machinery. The `.orchestra/` folder is backstage. Nobody asks to see the compiler; they ask to see what it built.

## The Score: PRDs All The Way Down

```
Roadmap PRD (the score)
└── Milestone PRD (a movement)
    └── Deliverables (the notes)
        └── Content files in your repo
```

The insight is that a PRD already contains the shape of a milestone: an objective, success criteria, a materials table, and references. A roadmap is just the top-level PRD whose materials table lists milestones instead of deliverables.

The **materials table** is the key structure at every level:

```markdown
| Material | Location | Status |
|----------|----------|--------|
| {name} | {path or link} | Done / In Progress / Not Started / Needs Refresh |
```

Roadmap rows are milestones. Milestone rows are deliverables. Tickets are generated from the gap — rows that aren't "Done" become work.

## The Workflow

1. **Compose** — Define a milestone as a PRD. Set the objective, write the done-conditions, fill the materials table with what needs to exist.

2. **Conduct** — Read the milestone PRD. Identify what's not done. Propose or generate tickets from the gaps. Today this is manual; tomorrow an agent reads `roadmap.md` and surfaces the day's work.

3. **Perform** — Each ticket becomes an agentic session. The agent reads the milestone PRD for context, executes the work, creates or updates the deliverable in the repo.

4. **Progress** — Status rolls up through the materials tables. Deliverable done → update milestone PRD. All deliverables done → update roadmap. The score always reflects reality.

## The Agent Session Loop

Every agent session follows the same pattern:

1. **Read the score** — roadmap → active milestone → materials table
2. **Perform** — execute the ticket
3. **Update the score** — mark the deliverable, update milestone progress

If the agent doesn't update the score, the performance isn't complete.

## The Folder

```
.orchestra/
├── README.md          ← Explains the system
├── roadmap.md         ← The score (top-level PRD)
├── adr/               ← Decision Records — standing constraints
├── work/              ← Per-ticket PRDs and specs
│   └── TEMPLATES/     ← PRD and spec templates
└── devlog/            ← What happened and why, by quarter
```

**ADRs** (Business/Architecture Decision Records) are long-lived decisions that constrain how the project evolves. They outlast any individual ticket. When an agent needs to know why something is the way it is, the answer is in a ADR.

**Work items** are per-ticket folders containing a PRD and optionally a spec. The PRD defines intent; the spec defines execution. Folder naming follows `{ticket-id}-{short-name}/`.

**Devlogs** are chronological entries capturing what happened, what was learned, and what changed. Not a changelog — context that helps agents understand the trajectory of the project.

## Why This Works

The system has no new artifact types. PRDs, specs, and decision records are well-understood formats. The innovation is using them recursively — the same materials-table structure at every level creates a machine-readable execution graph that agents can traverse.

The topology is the reference chain. Roadmap links to milestones, milestones link to deliverables, deliverables are files in the repo. No separate graph definition needed. The structure *is* the plan.

## Installation

```
/plugin marketplace add mpazaryna/agentic-factory
/plugin install orchestra@agentic-factory
```

Then scaffold your project:

```
/scaffold ./my-project
```

This creates the `.orchestra/` folder with the full structure, templates, and the founding ADR.
