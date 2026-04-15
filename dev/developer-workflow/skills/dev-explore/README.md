# dev-explore

Codebase exploration and documentation generation.

## What This Skill Does

Systematically explores codebases and generates documentation with three modes:

| Mode | Output | Best For |
|------|--------|----------|
| **analyze** | `codebase_analysis.md` | Understanding new codebases, onboarding |
| **export** | `docs/exports/` | Consolidating docs for external LLM tools |
| **portfolio** | `PROJECT.md` | Resumes, interviews, showcasing work |

## When to Use

- Onboarding to an unfamiliar codebase
- Exporting docs for NotebookLM or other external LLM tools
- Preparing portfolio artifacts for job hunting
- Generating onboarding materials for new team members

## Related Skills

This skill is part of the `dev-*` family:

- **dev-inquiry** - Investigation and technical decisions
- **dev-explore** (this skill) - Codebase understanding
- **dev-reports** - Journals and status reports
- **dev-context** - ADR/Design/Spec/Plan scaffolding

## Quick Example

```
"Help me understand this codebase"
→ Analyze mode
→ Generates codebase_analysis.md with architecture diagrams

"Export docs for NotebookLM"
→ Export mode
→ Generates docs/exports/ with consolidated files

"I need a PROJECT.md for my portfolio"
→ Portfolio mode
→ Generates resume-ready documentation
```

## Technology Support

Auto-detects and loads specialized templates for:
- iOS/Swift
- Android/Kotlin
- Cloudflare Workers
- MCP Servers
- TypeScript
- Jest Testing

## Folder Structure

```
dev-explore/
├── SKILL.md              # Orchestrator
├── README.md             # This file
├── HOW_TO_USE.md         # Usage examples
├── templates/            # Output templates
│   ├── analyze-base.md
│   ├── export.md
│   ├── portfolio.md
│   └── tech/             # Technology-specific
└── examples/             # Full output examples
```
