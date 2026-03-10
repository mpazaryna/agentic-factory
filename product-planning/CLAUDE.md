# Product Planning

End-to-end product planning practice: from raw tickets to executed specs.

## Components

### Skills
- **prd-template-guidance** — Expert knowledge for PRD structure, quality, and best practices

### Agents
- **ticket-refiner** — Converts project management tickets into formal PRDs by cross-referencing the codebase
- **prd-to-spec** — Translates PRDs into technical specs with implementation details (depends on ticket-refiner)
- **spec-executor** — Generic executor for any spec-based workflow

### Commands
- **prd** — Guided PRD creation through a structured Q&A workflow (~30 min, 10 questions)

## How They Work Together

The pipeline flows: raw ticket → `ticket-refiner` → PRD → `prd-to-spec` → technical spec → `spec-executor` → implementation. The `/prd` command is the interactive alternative — when there's no existing ticket, it guides the user through creating a PRD from scratch using `prd-template-guidance` for quality.

## Conventions
- PRDs follow the structure defined in prd-template-guidance (Problem, Goals, Non-Goals, User Stories, Requirements, Success Metrics, Acceptance Criteria)
- Specs include implementation phases, file-level changes, and acceptance tests
- Output locations are discovered from project structure, not hardcoded

## What's Missing
- Roadmap planning skill (prioritization frameworks, sequencing)
- Retrospective agent (post-implementation analysis)
