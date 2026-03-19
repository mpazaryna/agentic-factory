---
name: technical-decision
description: "Analyze technical options with structured comparison matrices, scoring, and ADR draft generation. Use when the user needs help choosing between technologies, architectures, or implementation approaches."
context: fork
agent: general-purpose
allowed-tools: WebFetch, WebSearch, Read, Bash
argument-hint: "<decision to analyze>"
---

# Technical Decision Analysis

Analyze the technical decision: $ARGUMENTS

## Workflow

### Step 1: Understand Decision Context

- What's being decided
- What options exist
- Why it matters
- What's at stake

### Step 2: Define Evaluation Criteria

Infer criteria based on decision type:

**Technology Selection**: Maturity, performance, developer experience, documentation, future-proofing, migration path

**Architecture Decision**: Complexity, maintainability, scalability, user experience, cost

**Implementation Approach**: Time to implement, code quality, testability, flexibility

### Step 3: Research Each Option

For each option gather facts from official documentation, benchmarks, real-world usage, known issues. Analyze pros, cons, tradeoffs, and risks.

### Step 4: Score Options

Create comparison matrix:

| Criterion | Weight | Option A | Option B |
|-----------|--------|----------|----------|
| {Criterion} | H/M/L | score/5 | score/5 |

### Step 5: Generate Recommendation

- **Selected Option**: Which one to choose
- **Rationale**: Why (based on criteria + context)
- **Tradeoffs**: What we're accepting
- **Risks**: What to watch out for
- **Validation**: How to verify it was right

### Step 6: Create ADR Draft

```markdown
# ADR-{N}: {Decision Title}

**Status**: Proposed
**Date**: {DATE}
**Context**: {WHY_NEEDED}
**Decision**: We will {SELECTED_OPTION}
**Rationale**: {WHY_THIS_CHOICE}
**Consequences**: Positive, Negative, Neutral
**Alternatives Considered**: {REJECTED_OPTIONS}
```

## Decision Quality Principles

1. **Evidence-based**: Backed by research and data
2. **Context-aware**: Consider project constraints
3. **Explicit about tradeoffs**: No option is perfect
4. **Reversible-aware**: Note if/how decision can change
5. **Validated**: Include how to verify correctness
