# How to Use dev-explore

## Basic Usage

Describe what you need:

```
"Help me understand this codebase"
"Export docs for NotebookLM"
"Generate a PROJECT.md for my portfolio"
```

## Modes

### Analyze Mode
For understanding new codebases:

```
"Analyze this codebase and help me understand the architecture"
"Create a codebase analysis focused on onboarding"
"Analyze this TypeScript project and highlight testing patterns"
```

**Output**: `codebase_analysis.md` with tech stack, architecture, file breakdowns, diagrams

### Export Mode
For consolidating docs for external LLM tools:

```
"Export docs for NotebookLM"
"Consolidate documentation for upload"
"Generate docs/exports/ with all project documentation"
```

**Output**: `docs/exports/` directory with numbered consolidated files ready for upload

### Portfolio Mode
For resume and interview preparation:

```
"Create a PROJECT.md for my portfolio"
"Generate portfolio documentation with interview talking points"
"Create a PROJECT.md - this project serves 500+ daily users"
```

**Output**: `PROJECT.md` with elevator pitch, challenges, resume bullets, talking points

## Combined Modes

```
"Generate both a codebase analysis and a PROJECT.md"
"Create complete documentation using all three modes"
```

## Tips for Best Results

1. **Run from project root** - Works best with full repository access
2. **Have a README** - Existing docs improve analysis quality
3. **Maintain devlog** - `docs/devlog/` entries enhance documentation
4. **Provide metrics** - Business outcomes make portfolio mode compelling
5. **Be specific** - Tell which mode and any focus areas
6. **Iterate** - Generated docs are starting points; enhance with your insights

## What to Provide

### For All Modes
- Access to the repository (run in project directory)
- Optional: Specific areas to focus on

### For Portfolio Mode
- Business metrics (user counts, performance improvements)
- Key challenges you want highlighted
- Target audience (recruiters, technical interviewers)

### For Export Mode
- Up-to-date documentation in `docs/` folder
- ADRs in `.orchestra/decisions/`
- Devlogs in `docs/devlog/`
