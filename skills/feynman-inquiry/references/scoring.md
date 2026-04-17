# Compare & Decide: Evidence-Based Scoring

## Prerequisites

Scoring comes **after** investigation. If you haven't experimented with each option, you're scoring opinions, not evidence.

**Before scoring**:
- [ ] Investigated each option (see `investigation.md`)
- [ ] Have concrete observations, not doc summaries
- [ ] Understand tradeoffs from experience
- [ ] Know your specific context

## The Comparison Process

### Step 1: Define Your Context

Before comparing, be explicit about your situation:

```markdown
## Decision Context

**What I'm building**: [specific feature/system]
**Timeline**: [constraints]
**Team**: [size, experience]
**Existing stack**: [what's in place]
**Must-haves**: [non-negotiable requirements]
**Nice-to-haves**: [preferences]
**Anti-requirements**: [things to avoid]
```

Context determines which criteria matter. "Best database" doesn't exist—only "best for X situation."

### Step 2: Choose Criteria (4-6 max)

Select criteria relevant to YOUR context:

**Technology Selection**:
- Learning curve, Performance, Documentation
- Community/ecosystem, Maturity, Migration path

**Architecture Decision**:
- Complexity, Maintainability, Scalability
- Flexibility, Reversibility, Coupling

**Implementation Approach**:
- Time to implement, Code quality, Testability
- Extensibility, Risk level, Maintenance burden

**Pick 4-6 criteria max.** More dilutes the comparison.

### Step 3: Weight by Importance

Assign weights that sum to 100%:

```markdown
| Criteria | Weight | Why |
|----------|--------|-----|
| Performance | 30% | Core requirement |
| Maintainability | 25% | Long-term project |
| Learning curve | 20% | Small team |
| Community | 15% | Need help |
| Migration path | 10% | Nice to have |
```

**Forcing weights makes you confront priorities.** If everything is "important," nothing is.

### Step 4: Score Each Option (1-5)

| Score | Meaning |
|-------|---------|
| 5 | Excellent — exceeds needs |
| 4 | Good — meets needs well |
| 3 | Adequate — meets needs |
| 2 | Poor — barely acceptable |
| 1 | Bad — doesn't meet needs |

**Every score needs evidence from investigation.**

```markdown
## Option A: SwiftData

| Criteria | Score | Evidence |
|----------|-------|----------|
| Performance | 4 | 50ms for 10k records in experiment |
| Maintainability | 5 | Macro-generated, minimal boilerplate |
| Learning curve | 3 | 2 days to understand macro behavior |
| Community | 2 | Few SO answers, limited examples |
| Migration | 4 | Clear CoreData migration docs |
```

### Step 5: Calculate Weighted Scores

```markdown
| Criteria | Weight | Option A | Option B |
|----------|--------|----------|----------|
| Performance | 30% | 4 (1.2) | 5 (1.5) |
| Maintainability | 25% | 5 (1.25) | 3 (0.75) |
| Learning curve | 20% | 3 (0.6) | 4 (0.8) |
| Community | 15% | 2 (0.3) | 5 (0.75) |
| Migration | 10% | 4 (0.4) | 2 (0.2) |
| **Total** | 100% | **3.75** | **4.00** |
```

### Step 6: Sanity Check

Numbers are a tool, not the answer:

1. **Does the winner feel right?** If not, examine weights.
2. **Knockout factors?** A 1 in critical area might disqualify regardless.
3. **Margin?** Within 0.3 points = effectively tied.
4. **Optimizing for what?** Short-term vs long-term can flip answers.

## Making the Decision

### Decision Template

```markdown
## Decision: [What you're deciding]

### Context
[Your specific situation]

### Options Considered
1. [Option A]
2. [Option B]
3. [Option C if applicable]

### Comparison

| Criteria | Weight | A | B | C |
|----------|--------|---|---|---|
| [Criteria 1] | X% | Score | Score | Score |
| ... | | | | |
| **Total** | 100% | X.XX | X.XX | X.XX |

### Recommendation

**Selected**: [Option]

**Rationale** (key differentiators):
- [Primary reason with evidence]
- [Secondary reason]

**Tradeoffs accepted**:
- [What you're giving up]
- [Why it's acceptable]

**Risks**:
- [Risk 1]: [Mitigation]
- [Risk 2]: [Mitigation]

**Reversibility**: [Easy/Medium/Hard]
- [How to change later if needed]

**Validation**:
- [How you'll know if decision was right]
- [When to revisit]
```

## Quick Comparison (2 Options)

For simple A vs B:

```markdown
# [Option A] vs [Option B]

## Context
What I need: ...

## Head-to-Head

| Aspect | A | B | Winner |
|--------|---|---|--------|
| [Criteria 1] | [Evidence] | [Evidence] | A/B/Tie |
| [Criteria 2] | [Evidence] | [Evidence] | A/B/Tie |
| [Criteria 3] | [Evidence] | [Evidence] | A/B/Tie |

## Verdict

**Choose [Option]** because [1-2 sentence rationale].

**Accept tradeoff**: [what you're giving up].
```

## Common Pitfalls

### Scoring Without Evidence

**Bad**: "Performance: 5 (heard it's fast)"
**Good**: "Performance: 4 (measured 50ms in experiment)"

### Too Many Criteria

**Bad**: 12 criteria at 8% each
**Good**: 5 criteria that actually matter

### Equal Weights

**Bad**: Everything is 20%
**Good**: Force prioritization

### Ignoring Context

**Bad**: "Option A is objectively better"
**Good**: "Option A is better for our context because..."

### Numbers Override Judgment

**Bad**: "Spreadsheet says B, so B"
**Good**: "B scores highest, but the 2 in security is a knockout"

## When Numbers Don't Help

Some decisions can't be scored:

- **Taste decisions**: UI aesthetics, code style
- **Bet decisions**: Emerging tech, no track record
- **Political decisions**: Team buy-in matters more
- **Already constrained**: Requirements limit to one option

Acknowledge it and document reasoning without forcing scores.

## Time-Boxing Decisions

| Decision Impact | Investigation + Comparison Time |
|-----------------|--------------------------------|
| Easily reversible | 2 hours max |
| Moderate impact | 1 day max |
| Hard to reverse | 3 days max |

If you can't decide in the time budget, pick the most reversible option and move on.

## Next Steps

After decision:
- **Ready to build?** → Proceed with confidence
- **Need validation first?** → Spike the chosen approach (see `spike.md`)
- **Want to document formally?** → Use an ADR skill
