# Decision Log: Commands vs Skills vs Agents

**Date**: 2024-11-29
**Context**: Building `/plan-spec` command to convert specs into TDD plans
**Decision**: Pivot from command to skill; rethink command usage generally

---

## The Realization

While building a `/plan-spec` slash command, we recognized a fundamental mismatch between the artifact type and the task's nature.

**The task**: Read a spec file, decompose it into TDD-sequenced testable units, output a plan.

**The problem**: This requires *judgment*:
- What constitutes a "testable unit" varies by codebase
- Dependency ordering requires domain understanding
- Some specs need more decomposition, others less
- The "right" sequence is context-dependent

**Slash commands are deterministic**. They execute the same structured steps every time. But good TDD planning is inherently *non-deterministic* — it requires reasoning, adaptation, and expertise.

---

## The Paradigm Shift

### Old Mental Model (Script-Oriented)
```
User invokes command → Deterministic steps → Fixed output
```

Commands as "macros" — human triggers, predictable execution.

### New Mental Model (Agentic)
```
User intent
    ↓
Agent (autonomous, explores, reasons)
    ↓
Applies Skills (methodologies, expertise, judgment)
    ↓
Uses Tools (Read, Write, Bash, etc.)
    ↓
Produces work
```

**The goal is wide expanses of compute performing agentic actions**, not narrow deterministic scripts.

---

## Artifact Type Decision Framework

### Commands (Rare — Use Sparingly)

**Characteristics**:
- Highly deterministic
- Same input → same output
- Governance/enforcement ("must follow this format")
- Context injection ("fetch this data, inject it")

**Examples**:
- `/git:commit` — Enforce commit message format, signing, hooks
- `/git:issue 123` — Fetch issue data, inject into context
- Escape hatches when human wants to force a specific action

**Anti-pattern**: Using commands for tasks requiring judgment, exploration, or adaptation.

### Skills (Primary — Default Choice)

**Characteristics**:
- Methodology + mental model
- Claude applies judgment within the framework
- Output adapts to context and complexity
- Reference examples guide but don't constrain

**Examples**:
- `spike-driven-dev` — TDD spike methodology
- `tdd-planner` — Decomposing specs into test-first sequences (what `/plan-spec` should be)
- Domain expertise that requires situational application

**When to use**: Any task where "it depends" is part of the answer.

### Agents (Autonomous Specialists)

**Characteristics**:
- Autonomous exploration and reasoning
- Orchestrate multiple skills and tools
- Discover as they go
- Handle complex, multi-step work

**Examples**:
- `quality-control-enforcer` — Reviews code for issues
- `research-docs-fetcher` — Explores and organizes documentation
- Domain specialists that own a workflow end-to-end

**When to use**: Complex tasks requiring discovery, multi-step reasoning, or workflow ownership.

---

## Hierarchy

```
Agents (orchestrate, reason, explore)
   ↓ apply
Skills (methodologies, expertise, judgment)
   ↓ use
Tools (Read, Write, Bash, Glob, etc.)
```

Commands sit *outside* this hierarchy — they're escape hatches for human-triggered deterministic actions, not part of the agentic flow.

---

## Implications for Factory

1. **Bias toward skills and agents** — Commands should be the exception
2. **Question command requests** — "Does this require judgment?" If yes → skill
3. **Commands for governance only** — Git protocols, format enforcement, data injection
4. **Agents read skills** — The natural flow is agent applies methodology, not human invokes script

---

## Action Items

- [ ] Delete `/plan-spec` command
- [ ] Rebuild as `tdd-planner` skill
- [ ] Audit existing commands — which should be skills/agents?
- [ ] Update factory guides to reflect this decision framework

---

## Key Quote

> "We want to encourage wide expanses of compute to perform agentic actions."

Commands short-circuit agentic potential. Skills and agents embrace it.
