# technical-decision

Analyze technical options with structured comparison matrices, scoring, and an ADR draft — for technology, architecture, or implementation choices.

## Quick Start

```
/technical-decision should we use Hono or Express for our Cloudflare Worker API
/technical-decision REST vs GraphQL for this mobile app backend
/technical-decision Zustand vs Jotai vs Redux Toolkit for state management
/technical-decision should we use SSR or static generation for this marketing site
```

## What It Does

Runs in a forked subagent. Produces a structured analysis with a clear recommendation.

1. **Understands context** — what's being decided, what options exist, what's at stake
2. **Defines evaluation criteria** — inferred from decision type:
   - Technology selection: maturity, performance, DX, docs, future-proofing
   - Architecture: complexity, maintainability, scalability, UX, cost
   - Implementation: time to implement, testability, flexibility
3. **Researches each option** — official docs, benchmarks, real-world usage, known issues
4. **Scores options** — weighted comparison matrix (High/Medium/Low criteria, score/5 per option)
5. **Recommends** — selected option, rationale, tradeoffs, risks, and how to validate the choice
6. **Drafts an ADR** — ready to save as `ADR-N: Decision Title` with status Proposed

## See Also

- `research-task` — for general technical research without the decision framework
- `spike-driven-dev` — validate the chosen approach before full implementation
