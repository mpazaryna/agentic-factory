# Installing design-principles

## Quick Install

Copy the skill folder to your project's `.claude/skills/` directory:

```bash
cp -r design-principles/ /path/to/your/project/.claude/skills/
```

## Manual Install

1. Create the skills directory if it doesn't exist:
   ```bash
   mkdir -p .claude/skills
   ```

2. Copy the entire `design-principles` folder:
   ```bash
   cp -r /path/to/design-principles .claude/skills/
   ```

## Verify Installation

The structure should look like:

```
.claude/
└── skills/
    └── design-principles/
        ├── SKILL.md              # Orchestrator
        ├── README.md             # Overview
        ├── HOW_TO_USE.md         # Usage guide
        ├── INSTALL.md            # This file
        └── references/
            ├── typography.md     # Font principles
            ├── color.md          # Color systems
            ├── hierarchy.md      # Visual hierarchy
            ├── motion.md         # Animation
            └── accessibility.md  # A11y guidelines
```

## Related Skills

For complete design coverage, also install:

- `web-design` - Web/CSS implementation patterns
- `swift-ui` - SwiftUI/iOS implementation patterns
- `design-review` - Audit checklists and submission prep

## Usage

Once installed, Claude will automatically use this skill when you ask design-related questions:

```
"Help me choose typography for my app"
"What color palette should I use?"
"How do I create better visual hierarchy?"
```
