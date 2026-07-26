# Installing feynman-inquiry

Skills install **per project** — the repo that consumes the skill declares it.
There is no global install.

## Editable copy

Pull the skill into the current project with the [`skills`](https://www.skills.sh)
CLI. It lands in the project's agent dir, editable and committed with the repo:

```bash
npx skills@latest add mpazaryna/agentic-factory --skill feynman-inquiry
```

## Read-only, versioned

To take the skill as part of a managed bundle that can't drift in place, install
the marketplace plugin instead:

```
/plugin marketplace add mpazaryna/agentic-factory
/plugin install skills@agentic-factory
```

## Verification

After installation, the skill should appear when Claude Code starts. Test with:

```
"Let's explore async/await"
```

Claude should engage investigation mode.

## Structure

```
.claude/skills/feynman-inquiry/
├── SKILL.md              # Main orchestrator
├── README.md
├── HOW_TO_USE.md
├── INSTALL.md
└── references/
    ├── investigation.md
    ├── spike.md
    ├── scoring.md
    └── examples.md
```

## Requirements

- Claude Code with skills support
- No external dependencies

## Updating

Re-sync from source:

```bash
npx skills@latest update
```
