# anatomy-expert

Provide yoga anatomy expertise — biomechanics, contraindications, modifications, and anatomical rationale behind postures.

This is a background knowledge skill (`user-invocable: false`). It is loaded automatically by the orchestrator when anatomical depth is needed — not invoked directly.

## What It Does

For any asana, the anatomy expert analyzes:

- **Primary actions** — what the body is fundamentally doing (flexion, extension, rotation)
- **Muscle engagement** — which muscles are working concentrically, eccentrically, or isometrically, named specifically
- **Joint mechanics** — what each joint is doing and its safe range
- **Contraindications** — who should avoid or modify the pose, and why, distinguishing absolute from relative
- **Common compensation patterns** — how bodies cheat and why it matters
- **Anatomical cues** — teaching language grounded in accurate anatomy

Safety is always first: contraindications before benefits, modifications before full expression, anatomical why before instructional how.

## How It Gets Invoked

The orchestrator routes here when a teacher asks:

- "What muscles are engaged in [pose]?"
- "What are the contraindications for [pose]?"
- "How do I modify [pose] for tight hamstrings / a knee injury / pregnancy?"
- "Is this sequence safe for someone with lower back issues?"
- "Why does [pose] feel like [sensation]?"

## See Also

- [asana-strategist](../asana-strategist/README.md) — sequence design and pose selection
- [orchestrator](../orchestrator/README.md) — routes queries to the right specialist
