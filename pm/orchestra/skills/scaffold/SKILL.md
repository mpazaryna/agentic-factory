---
name: scaffold
description: "Scaffold the .orchestra/ agent knowledge base in a project — creates folder structure, templates, README, and initial roadmap. Use when setting up a new project or adding .orchestra/ to an existing one."
argument-hint: "<project-path>"
disable-model-invocation: true
---

# Scaffold .orchestra/

Create the `.orchestra/` agent knowledge base structure in the target project.

## What It Creates

```
.orchestra/
├── README.md                          ← Explains the folder to agents and humans
├── roadmap.md                         ← The score — top-level PRD
├── bdr/                               ← Business/Architecture Decision Records
│   └── BDR-000-the-score.md           ← Founding decision: PRDs all the way down
├── work/                              ← Per-ticket work items
│   └── TEMPLATES/
│       ├── prd.md                     ← PRD template
│       └── spec.md                    ← Spec template
└── devlog/                            ← Chronological journal
    └── {YYYY}-Q{N}/                   ← Current quarter folder
```

## Steps

1. Determine target path from $ARGUMENTS (default: current working directory)
2. Check if `.orchestra/` already exists — if so, STOP and report what's there
3. Create the directory structure above
4. Generate `README.md` from [references/readme-template.md](${CLAUDE_SKILL_DIR}/../../references/readme-template.md)
5. Generate `roadmap.md` as an empty top-level PRD with the project name
6. Generate `BDR-000-the-score.md` from [references/bdr-000-the-score.md](${CLAUDE_SKILL_DIR}/../../references/bdr-000-the-score.md)
7. Generate PRD and spec templates in `work/TEMPLATES/`
8. Create the current quarter devlog folder

## Roadmap PRD (roadmap.md)

The roadmap is the top-level PRD. Ask the user for:
- **Project name**
- **Vision** (1-2 sentences — what does "done" look like at the highest level?)
- **Initial milestones** (if known)

Generate the roadmap using the PRD template with milestones as materials table rows:

```markdown
| Material | Location | Status |
|----------|----------|--------|
| {milestone name} | .orchestra/work/{id}-{name}/prd.md | Not Started |
```

## After Scaffolding

Report what was created and remind the user:
- Add `.orchestra/` references to the project's `CLAUDE.md`
- The roadmap is the score — define milestones as PRDs
- BDRs capture standing decisions agents must follow
- Devlogs capture what happened and why
