# Spike Mode: TDD Validation

## The Railroad Spike Principle

When building a railroad, the **first spike** establishes direction, validates the foundation, proves feasibility. In software, a spike proves the approach works with ONE component before building everything.

**Before building anything complex**:
1. Drive one spike (build one minimal component with TDD)
2. Make sure it holds (test with real data)
3. Then build the railroad (replicate pattern)

## When to Spike

### Always Spike When

- Using a new architecture pattern for the first time
- Integrating with unfamiliar APIs or frameworks
- Making assumptions about data structures
- Building something you've never built before
- The failure cost is high (would require complete redesign)
- Multiple approaches seem equally valid
- The main ticket has >10 subtasks

### Red Flags That Demand a Spike

1. **"This should work..."** — Unvalidated assumptions
2. **"We'll deal with that later"** — Deferred architecture decisions
3. **"It's probably fine"** — Unvalidated data assumptions
4. **"How hard could it be?"** — Unfamiliar territory
5. **"Just start coding"** — No validation plan

## Spike Characteristics

### Good Spike

- **Time-boxed**: 4-8 hours maximum
- **Scope-limited**: ONE file, ONE component, ONE feature
- **Test-driven**: Write tests FIRST
- **Real data**: Production-like data, not mocks
- **Platform-tested**: All target platforms
- **Disposable**: OK to throw away
- **Proof-oriented**: Proves feasibility, not perfection

### Bad Spike

- **Open-ended**: "Explore options" without success criteria
- **Too broad**: Multiple components
- **No tests**: Code-first without validation
- **Mock data only**: Doesn't catch real issues
- **Perfectionist**: Trying to build production code

## The TDD Spike Workflow

### Step 1: Define Scope (30 min)

```markdown
## Spike: [What you're validating]

**Time budget**: [4-8 hours]
**Scope**: ONE [model/view/endpoint/integration]

**What this proves**:
- [ ] [Technical feasibility point 1]
- [ ] [Data structure validity]
- [ ] [Architecture pattern works]

**Success criteria**:
- [ ] Tests pass with real data
- [ ] Pattern documented
- [ ] Ready to replicate
```

### Step 2: Write Tests FIRST (1 hour)

```swift
func testModelCreation() { /* ... */ }
func testJSONDecoding() { /* ... */ }
func testRealDataLoading() { /* ... */ }
```

Run tests → **FAIL** (expected—code doesn't exist)

This is critical. Tests define success before implementation.

### Step 3: Implement Minimal Code (1-2 hours)

- Write **minimum code** to pass tests
- Focus on architecture, not features
- Don't add extra functionality

Run tests → **PASS**

### Step 4: Test with Real Data (1 hour)

- Load actual production/external data
- Test edge cases found in real data
- Verify platform compatibility

Document any data issues discovered.

### Step 5: Document Pattern (30 min)

```markdown
## Spike Results

**What worked**:
- [Pattern that succeeded]

**What didn't**:
- [Issues discovered]

**Pattern for main ticket**:
- [How to replicate this for remaining work]

**Effort adjustment**:
- Original estimate: X
- Revised estimate: Y (because Z)
```

## Spike Outcomes

### Success (Most Common)

- Tests pass with real data
- Pattern proven viable
- Architecture validated

**Action**: Close spike, proceed with main work using proven pattern.

### Partial Success

- Tests pass but adjustments needed
- Approach works but inefficient
- Edge cases discovered

**Action**: Document findings, adjust approach, possibly follow-up spike.

### Failure (Rare but Valuable)

- Tests fail consistently
- Approach fundamentally flawed
- Technical limitation discovered

**Action**: Research alternatives, spike different approach.

**All outcomes are wins** — better to fail on Day 1 than Day 5.

## Spike Template

```markdown
## Spike: [Feature/Pattern Name]

**Context**: [Why this spike is needed]

**Scope** (4-8 hours):
- [ ] Write tests FIRST
- [ ] Implement minimal code
- [ ] Test with real data
- [ ] Verify on target platforms
- [ ] Document findings

**What this proves**:
- [ ] Technical feasibility
- [ ] Data structure validity
- [ ] Architecture pattern works

**Success criteria**:
- [ ] All tests pass
- [ ] Real data loads correctly
- [ ] Pattern documented
- [ ] No architectural blockers

**Next steps**:
- If successful → Proceed with [main ticket]
- If issues → Document, adjust, possibly re-spike
```

## Common Pitfalls

### Scope Creep

**Problem**: Building more than ONE component
**Fix**: Ruthlessly limit scope. Prove ONE thing.

### Skipping Tests

**Problem**: No validation, just exploration
**Fix**: Tests define success. Write them first.

### Mock Data Only

**Problem**: Doesn't catch real-world issues
**Fix**: Use production-like data immediately.

### Fear of Throwing Away

**Problem**: Treating spike as production code
**Fix**: Spikes are proofs. Throw away freely.

### Open-Ended Exploration

**Problem**: No clear success criteria
**Fix**: Define what "done" looks like before starting.

## The Cost-Benefit

### Skip the Spike

**Week 1**: Build based on assumptions
**Week 2**: Discover architecture doesn't work
**Week 3**: Rebuild with new approach
**Week 4**: Still debugging

**Total**: 4+ weeks, high stress, fragile code

### Start with Spike

**Day 1**: TDD spike discovers issues in 4-6 hours
**Days 2-5**: Build using proven pattern

**Total**: 5 days, low stress, high confidence

**The spike saves 2+ weeks.**

## Next Steps

After spike:
- **Success?** → Build main feature with proven pattern
- **Partial success?** → Adjust and proceed, or spike alternative
- **Need to compare approaches?** → Move to Compare mode (see `scoring.md`)
