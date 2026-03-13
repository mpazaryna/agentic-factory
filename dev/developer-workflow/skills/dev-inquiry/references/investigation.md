# Investigation Mode: Feynman-Style Exploration

## The Core Principle

> "I learned very early the difference between knowing the name of something and knowing something." — Richard Feynman

Most developers research by reading docs, copying tutorials, hoping it works. This is **knowing the name**.

Investigation mode flips this: experiment first, observe behavior, build mental model, then read docs. This is **knowing something**.

## The Investigation Protocol

### Step 1: State Your Ignorance (10 min)

Before touching code, write down:

```markdown
## What I Think I Know
- [Current assumptions]

## What I Don't Know
- [Honest gaps]

## What Would Surprise Me
- [Predictions that could be wrong]
```

This creates accountability. You'll revisit after experimenting.

**Example** — Investigating `@Observable`:
```markdown
## What I Think I Know
- It replaces @ObservedObject
- Uses macros
- More efficient somehow

## What I Don't Know
- How it tracks property changes
- Whether it works with structs
- What the macro generates

## What Would Surprise Me
- If computed properties triggered updates
- If nested objects just worked
```

### Step 2: Design the Simplest Experiment (15 min)

Find the **atomic unit** of what you're investigating.

**Bad experiments** (too complex):
- "Build a todo app with @Observable"
- "Implement MVVM with observation"

**Good experiments** (atomic):
- "Does changing a property update the view?"
- "What happens with nested objects?"

Write the experiment as a **question**, not a feature.

### Step 3: Build and Observe (30 min - 1 hour)

Create minimal code to answer your question:

```swift
// Question: Does @Observable track nested changes?
@Observable class Parent {
    var child = Child()
}
@Observable class Child {
    var value = 0
}
```

**Run it. Watch it. Don't assume—observe.**

Write exactly what happened:
- Did the view update?
- Any console warnings?
- What was the actual behavior?

### Step 4: Poke the Edges (1-2 hours)

Intentionally try to break it:

| Experiment | Question |
|------------|----------|
| Remove @Observable from Child | Does tracking still work? |
| Use struct instead of class | Does it compile? |
| Access in non-view code | Crash? Warning? |
| Mutate from background thread | What happens? |

Each "breakage" reveals constraints and mechanics.

### Step 5: Form a Mental Model (30 min)

Based on experiments, write a **simple explanation**:

```markdown
## My Mental Model of @Observable

The macro generates:
1. Getters/setters for each stored property
2. Setters broadcast "changed"
3. SwiftUI subscribes when reading in body
4. Only read properties trigger updates

Key constraints:
- Must be class (reference type)
- Nested objects need their own @Observable
- Computed properties work if they read tracked props
```

### Step 6: Validate Against Documentation

NOW read the docs. Compare:
- Did I miss anything?
- Was I wrong somewhere?
- Edge cases I didn't discover?

Update your mental model.

### Step 7: Test by Teaching

Can you:
- Explain this to a junior developer?
- Predict behavior in new scenarios?
- Debug when it breaks?
- Explain WHY it works that way?

If not, go back to Step 2 with a different angle.

## Investigation Template

```markdown
# Investigation: [Technology/Concept]

## Starting Point
- What I think I know: ...
- What I don't know: ...
- Why I'm investigating: ...

## Experiments

### Experiment 1: [Simplest case]
**Question**: [Single question]
**Code**: [Minimal code]
**Observation**: [What actually happened]

### Experiment 2: [Edge case]
**Question**: [What if X?]
**Code**: [Code that might break]
**Observation**: [What actually happened]

### Experiment 3: [Real-world scenario]
**Question**: [Does this work for my case?]
**Code**: [Closer to real usage]
**Observation**: [What actually happened]

## Mental Model
[Simple explanation of how this works]

## Key Findings
- [What I learned]
- [What surprised me]
- [What I still don't understand]
```

## Common Mistakes

### Starting with Docs
**Problem**: Primed to see what docs describe, not what happens.
**Fix**: Experiment first, docs second.

### Copy-Paste Tutorials
**Problem**: Know it works, not why or when it won't.
**Fix**: Type it yourself, change things, break things.

### Only Testing Happy Path
**Problem**: Don't know failure modes.
**Fix**: Intentionally try wrong inputs, missing data.

### Stopping at "It Works"
**Problem**: Can use it but can't debug it.
**Fix**: Ask "why does this work?" and "what would break it?"

## The Feynman Test

After investigation:

1. **Can I explain this to a junior?** — Not just how to use it, but how it works.
2. **Can I predict behavior?** — In scenarios I haven't tested?
3. **Can I debug when broken?** — Do I understand enough to find problems?
4. **Do I know the tradeoffs?** — What does this sacrifice?

All YES = understanding achieved. Any NO = investigate more.

## Next Steps

After investigation:
- **Confident in approach?** → Proceed to build or compare options
- **Need validation?** → Move to Spike mode (see `spike.md`)
- **Multiple options?** → Move to Compare mode (see `scoring.md`)
