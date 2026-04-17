# asana-strategist

Design yoga sequences — class structures, pose progressions, and balanced practices.

This is a background knowledge skill (`user-invocable: false`). It is loaded automatically by the orchestrator when sequence design is needed — not invoked directly.

## What It Does

The asana strategist builds anatomically sound yoga sequences following a mandatory six-phase structure:

1. **Opening** — seated centering and breath awareness
2. **Warming** — gentle movement preparing the body
3. **Building** — standing poses for strength and stability
4. **Peak** — the sequence's most demanding postures
5. **Counter-poses** — balancing movements
6. **Closing** — restorative postures and Savasana

For each pose it provides Sanskrit name, English translation, category, primary anatomical focus, key contraindications, and suggested hold time. For full sequences it includes phase labels, transition notes, time estimates, and level alternatives.

Before finalizing any recommendation it checks anatomical soundness, contraindication conflicts, counter-pose balance, thematic coherence, and timing fit.

## How It Gets Invoked

The orchestrator routes here when a teacher asks:

- "Build me a 60-minute hip-opening sequence for beginners"
- "What poses should I include for a backbend-focused class?"
- "What comes before/after Warrior III?"
- "Create a class for mixed levels with no inversions"

## See Also

- [anatomy-expert](../anatomy-expert/README.md) — safety validation and anatomical depth
- [orchestrator](../orchestrator/README.md) — routes queries and coordinates multi-agent workflows
