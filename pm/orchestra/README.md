# Orchestra

A methodology for agent-driven project execution. The metaphor is literal: every project is a performance, and every performance needs a score.

## The Metaphor

An orchestra doesn't improvise symphonies. Musicians read from a score, follow a conductor, and produce something greater than any individual could. Software projects work the same way when agents are involved.

**The Score** is the roadmap — a PRD that defines the vision and lists milestones. Milestones are PRDs that list deliverables. Deliverables are the actual files in your repo. PRDs all the way down.

**The Composer** is you. You write the score. You decide what gets built, in what order, and what "done" looks like. You evaluate inputs from stakeholders, research, and agents before anything enters the system. The composer is always human.

**The Conductor** interprets the score and keeps tempo. Today, that's you — reading the active milestone, identifying what's not done, and pointing agents at the next piece of work. Over time, as structure improves, this role shifts agentic. Clear done-conditions and machine-readable materials tables make the conductor role delegatable.

**The Orchestra** is your agents. They read the score for context, pick up tickets as contracts, execute the work, and update the score when they're done. An agent that completes work but doesn't update the PRD hasn't finished the job.

**The Audience** — co-founders, stakeholders, investors — experiences the output, never the machinery. The `.orchestra/` folder is backstage. Nobody reads the score during intermission; they ask what's coming next.

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

## The Document Hierarchy

The system has two distinct layers with different owners:

**Product layer** (owned by the composer/requestor):
- **Roadmap** — The vision. Why this project exists, what milestones matter.
- **PRD** — The intent. What needs to be built, why it matters, what success looks like.

**Execution layer** (owned by the agent):
- **Spec** — The implementation plan. Derived from the PRD, but written in terms the agent can execute. The spec is the bridge between product intent and code.

This separation is deliberate. The requestor defines *what* and *why*. The agent derives *how* from the PRD and writes it into a spec. The requestor should never need to engage with implementation details at the code level. If the agent has questions about purpose or delivery requirements, it goes back to the PRD. If the agent needs to refine its approach, it updates the spec — no human approval needed.

PRDs are refined only with input from the requestor or product team. Specs can be refined by the agent at runtime.

## The Workflow

1. **Compose** — Define a milestone as a PRD. Set the objective, write the done-conditions, fill the materials table with what needs to exist.

2. **Conduct** — Read the milestone PRD. Identify what's not done. Propose or generate tickets from the gaps.

3. **Spec** — Derive an implementation plan from the PRD. The agent reads the PRD and produces a spec it can execute against. This is the last step before code.

4. **Perform** — The agent reads the spec, executes the work, and creates or updates deliverables in the repo. If the spec needs adjustment during implementation, the agent updates it.

5. **Close** — Update the score. Mark deliverables done in the milestone PRD. Write a devlog entry capturing what happened and what was learned.

## The Agent Session Loop

Every agent session follows the same pattern:

1. **Read the score** — roadmap → active milestone → materials table
2. **Read the PRD** — understand the intent, success criteria, and deliverables
3. **Write the spec** — derive an implementation plan from the PRD
4. **Perform** — execute against the spec
5. **Update the score** — mark the deliverable, update milestone progress
6. **Devlog** — capture what happened, decisions made, lessons learned

If the agent doesn't update the score, the performance isn't complete.

## The Folder

```
.orchestra/
├── README.md          ← Explains the system
├── roadmap.md         ← The score (top-level PRD)
├── adr/               ← Decision Records — standing constraints
├── work/              ← Per-ticket PRDs and specs
│   ├── TEMPLATES/     ← PRD and spec templates
│   └── {ticket-id}-{name}/
│       ├── prd.md     ← Intent — what and why (product layer)
│       └── spec.md    ← Implementation plan (execution layer)
└── devlog/            ← What happened and why, by quarter
```

**ADRs** (Business/Architecture Decision Records) are long-lived decisions that constrain how the project evolves. They outlast any individual ticket. When an agent needs to know why something is the way it is, the answer is in an ADR.

**PRDs** define intent — the objective, success criteria, and deliverables. They are product-layer documents, refined only with input from the requestor or product team. An agent with questions about "why" or fundamental delivery requirements goes to the PRD.

**Specs** define the implementation plan — derived from the PRD by the agent. The spec is what the agent reads to code. It can be refined by the agent at runtime as the approach evolves. No human approval needed for spec changes; the PRD's success criteria are the contract.

**Work items** are per-ticket folders containing a PRD and a spec. Folder naming follows `{ticket-id}-{short-name}/`.

**Devlogs** are chronological entries capturing what happened, what was learned, and what changed. Not a changelog — context that helps agents understand the trajectory of the project.

## Why This Works

The system has no new artifact types. PRDs, specs, and decision records are well-understood formats. The innovation is using them recursively — the same materials-table structure at every level creates a machine-readable execution graph that agents can traverse.

The clean separation between product layer (PRDs) and execution layer (specs) means requestors define intent without touching implementation, and agents derive implementation without needing to ask about intent. The PRD answers "why" and "what done looks like." The spec answers "how to build it." This boundary is what makes autonomous agent execution practical.

The topology is the reference chain. Roadmap links to milestones, milestones link to deliverables, deliverables are files in the repo. No separate graph definition needed. The structure *is* the plan.

## Getting Started

Orchestra is distributed as a plugin via [agentic-factory](https://github.com/mpazaryna/agentic-factory). Once installed, scaffold your project:

```
/scaffold .
```

This creates the `.orchestra/` folder with the full structure, templates, and the founding ADR.
