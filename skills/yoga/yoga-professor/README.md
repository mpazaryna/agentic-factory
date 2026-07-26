# professor

Evaluate yoga teaching readiness through scenarios, knowledge probes, and guided learning exercises.

This is a background knowledge skill (`user-invocable: false`). It is loaded automatically by the orchestrator when readiness evaluation or knowledge development is needed.

## What It Does

The professor operates in two modes:

**Evaluative mode** — when asked "Am I ready?" or "Quiz me": generates challenges, scores responses across four dimensions, and delivers a clear readiness verdict.

**Developmental mode** — when asked "Help me understand" or "What should I study?": identifies knowledge gaps, explains what the teacher is missing, and provides practice scenarios.

### Challenge Types

- **Scenario challenges** — realistic classroom situations requiring judgment ("A student says their lower back hurts in Forward Fold. What do you do?")
- **Explain-back prompts** — articulate the reasoning behind sequence decisions
- **Knowledge probes** — specific technical questions on anatomy, contraindications, or modifications

### Scoring

| Dimension | What's Being Assessed |
|---|---|
| Anatomy | Muscles, joints, biomechanics |
| Sequencing | Why poses are ordered as they are |
| Safety | Recognizing and responding to contraindications |
| Cueing | Clear, helpful verbal guidance |

| Score | Verdict |
|---|---|
| 90-100 | Ready |
| 75-89 | Mostly Ready — review specific gaps |
| 60-74 | Developing — focused study recommended |
| Below 60 | Not Yet Ready — build understanding first |

## How It Gets Invoked

The orchestrator routes here when a teacher asks:

- "Am I ready to teach this sequence?"
- "Quiz me on this class"
- "Test my knowledge of hip openers"
- "What should I study before teaching backbends?"
- "I'm nervous about teaching inversions"
- "Challenge my understanding of this sequence"

The orchestrator also proactively suggests the professor after generating complex sequences.

## See Also

- [orchestrator](../orchestrator/README.md) — coordinates professor with other specialists
