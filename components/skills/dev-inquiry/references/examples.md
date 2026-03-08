# Dev Inquiry Examples

Real examples across all inquiry modes.

---

## Example 1: Investigation — Understanding @Observable

**Trigger**: "Let's explore the new Observation framework"

### Phase 1: State Ignorance

```markdown
## What I Think I Know
- Replaces @ObservedObject/@StateObject
- Uses macros
- More efficient somehow

## What I Don't Know
- How it tracks property changes
- Whether it works with structs
- How nested objects work
```

### Phase 2: Experiments

**Experiment 1**: Does changing a property update the view?
```swift
@Observable class Counter { var value = 0 }
// Tap button, increment value
```
**Observation**: View updates. Works without @State or @ObservedObject.

**Experiment 2**: Nested objects?
```swift
@Observable class Parent { var child = Child() }
@Observable class Child { var name = "test" }
```
**Observation**: Works! Both need @Observable.

**Experiment 3**: Struct instead of class?
```swift
@Observable struct Counter { } // Compile error!
```
**Observation**: Must be class.

### Phase 3: Mental Model

```markdown
The @Observable macro:
1. Generates getters/setters for stored properties
2. Setters broadcast "changed"
3. SwiftUI subscribes when reading in body
4. Only read properties trigger updates

Constraints:
- Must be class
- Nested objects need their own @Observable
- iOS 17+ only
```

### Outcome

Understanding achieved. Can explain, predict, debug.

---

## Example 2: Spike — SwiftData Integration

**Trigger**: "Spike SwiftData before we build the whole data layer"

### Spike Definition

```markdown
## Spike: SwiftData with Nested Codable

**Time budget**: 6 hours
**Scope**: ONE model with nested JSON structure

**What this proves**:
- SwiftData handles nested Codable
- Real JSON from API decodes correctly
- Query performance acceptable
```

### TDD Execution

**Step 1**: Write tests first
```swift
func testExerciseDecoding() {
    let json = loadRealJSON("exercise_sample.json")
    let exercise = try? JSONDecoder().decode(Exercise.self, from: json)
    XCTAssertNotNil(exercise)
    XCTAssertEqual(exercise?.steps.count, 5)
}
```
Tests fail (no code yet).

**Step 2**: Implement minimal model
```swift
@Model
class Exercise {
    var name: String
    var stepsData: Data // Store nested as Data

    var steps: [Step] {
        try? JSONDecoder().decode([Step].self, from: stepsData)
    }
}
```
Tests pass.

**Step 3**: Test with real data
- Loaded 649 exercises from production JSON
- All decoded successfully
- Query time: 45ms for full set

### Outcome

**Success**. Pattern documented:
- Use `Data` property for nested Codable
- Computed property for decoded access
- Ready to build remaining models

---

## Example 3: Comparison — SwiftData vs CoreData

**Trigger**: "Compare SwiftData vs CoreData for our app"

### Context

```markdown
**Building**: Fitness app with offline data
**Team**: Solo developer
**Target**: iOS 17+
**Must-haves**: Reliable persistence, relationships, good query performance
```

### Investigation Summary

Both options investigated. Key observations:
- SwiftData: Clean syntax, 45ms queries, limited community
- CoreData: Verbose, 38ms queries, extensive resources

### Scoring

```markdown
| Criteria | Weight | SwiftData | CoreData |
|----------|--------|-----------|----------|
| API simplicity | 30% | 5 (macros) | 3 (verbose) |
| Performance | 20% | 4 (45ms) | 4 (38ms) |
| Stability | 20% | 3 (new) | 5 (proven) |
| Community | 15% | 2 (limited) | 5 (extensive) |
| Future CloudKit | 15% | 3 (coming) | 5 (mature) |

**SwiftData**: 3.65
**CoreData**: 4.20
```

### Sanity Check

Numbers say CoreData, but:
- API simplicity matters a lot for solo dev
- iOS 17+ means SwiftData is viable
- CloudKit not in MVP

Reconsidering weights: If API simplicity is 40%, SwiftData wins.

### Decision

**Selected**: SwiftData

**Rationale**: DX improvement worth stability risk for MVP. iOS 17+ removes compatibility concern.

**Tradeoffs accepted**: May hit bugs (mitigate with testing), less community help (use Apple forums).

**Reversibility**: Medium — can wrap in repository pattern.

---

## Example 4: Full Flow — New Feature Architecture

**Trigger**: "How should we build the sync feature?"

### Phase 1: Investigation

Explored sync patterns:
- Optimistic (immediate local, async server)
- Pessimistic (wait for server confirmation)
- Hybrid (optimistic with conflict resolution)

Built minimal experiments for each. Observed:
- Optimistic: Great UX, conflict complexity
- Pessimistic: Simple, poor offline UX
- Hybrid: Best of both, more code

### Phase 2: Spike

Spiked hybrid approach:
- 6 hours
- One model with sync
- Real conflict scenarios

**Result**: Pattern works. Conflict resolution simpler than expected with last-write-wins for our data.

### Phase 3: Comparison

```markdown
| Criteria | Weight | Optimistic | Pessimistic | Hybrid |
|----------|--------|------------|-------------|--------|
| UX | 35% | 5 | 2 | 5 |
| Simplicity | 25% | 3 | 5 | 3 |
| Reliability | 25% | 3 | 5 | 4 |
| Offline | 15% | 5 | 1 | 5 |

**Optimistic**: 3.95
**Pessimistic**: 3.35
**Hybrid**: 4.25
```

### Phase 4: Decision

**Selected**: Hybrid with last-write-wins

**Rationale**: Spike proved feasibility. Best UX with acceptable complexity.

**Risks**: Edge cases in conflict resolution (mitigate with logging).

---

## Example 5: Failed Investigation → Pivot

**Trigger**: "Let's use Realm for cross-platform"

### Investigation

**Assumption**: Realm = shared code iOS/Android

**Experiments**:
- Realm Swift: Works, but `Object` base class feels dated
- SwiftUI integration: Own observation system, awkward
- "Cross-platform": Same file format, NOT shared code

### Mental Model Updated

Realm is cross-platform **database format**, not shared code. Still platform-specific implementation.

### Pivot Decision

**Don't use Realm.**

**Why**: Cross-platform isn't what we thought. SwiftData on iOS, Room on Android is cleaner.

**Lesson**: Investigate assumptions before committing.

---

## Anti-Pattern Examples

### Bad: Scoring Without Investigation

```markdown
| Criteria | PostgreSQL | MongoDB |
|----------|------------|---------|
| Performance | 4 | 5 |
```
**Problem**: Where did these numbers come from? No experiments.

### Bad: Skipping Spike for Unfamiliar Territory

"SwiftData should work for our nested models, let's build the whole layer."

**Result**: 2 weeks in, discovered it doesn't handle our structure. Rebuild.

**Fix**: 6-hour spike would have found this Day 1.

### Bad: Deciding Before Understanding

"React is popular, let's use React."

**Problem**: Popularity isn't a criterion. What about your team, your requirements?

### Bad: Analysis Paralysis

47-page framework comparison over 2 weeks.

**Problem**: Could have built MVP in any framework in that time.

**Fix**: Time-box decisions. If can't decide, pick most reversible and move.
