# orchestrator

Coordinate yoga class planning by routing queries to specialist skills and synthesizing responses.

## Quick Start

```
/orchestrator Create a complete 60-minute hip-opening class with teaching language
/orchestrator Build a backbend sequence for students with lower back issues
/orchestrator I want to teach about "letting go" — build me a class
/orchestrator Am I ready to teach this sequence?
/orchestrator Create a hip-opening class and make sure I'm ready to teach it
```

## What It Does

The orchestrator is the conductor, not the performer. It:

1. Understands what the teacher is asking for
2. Routes to the right specialist — or coordinates multiple specialists in sequence
3. Synthesizes outputs into a cohesive document
4. Proactively asks clarifying questions when needed (duration, level, population, focus, output format)

### Specialist Agents

| Specialist | Use for |
|---|---|
| **asana-strategist** | Sequence building, pose selection, class structure, timing |
| **anatomy-expert** | Contraindications, modifications, muscle engagement, safety |
| **theme-developer** | Teaching narratives, verbal cues, thematic arcs |
| **professor** | Readiness evaluation, knowledge probes, guided learning |

### Coordination Patterns

**Single-agent** — most requests route directly to one specialist.

**Full class plan** — Asana Strategist builds the sequence → Anatomy Expert validates safety → Theme Developer adds teaching language → Orchestrator synthesizes.

**Theme-first** — Theme Developer develops the framework → Asana Strategist structures the sequence.

**Readiness check** — Professor generates challenges based on sequence content, evaluates responses, and reports readiness score.

**Full preparation** — all four specialists run in sequence, producing a complete class plan plus teaching readiness assessment.

The orchestrator proactively suggests a Professor readiness check when a complex sequence is generated or when the teacher seems uncertain.

## See Also

- [asana-strategist](../asana-strategist/README.md)
- [anatomy-expert](../anatomy-expert/README.md)
- [theme-developer](../theme-developer/README.md)
- [professor](../professor/README.md)
