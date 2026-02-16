# Installing web-design

## Quick Install

Copy the skill folder to your project's `.claude/skills/` directory:

```bash
cp -r web-design/ /path/to/your/project/.claude/skills/
```

## Global Install

For availability across all projects:

```bash
cp -r web-design/ ~/.claude/skills/
```

## Verify Installation

The structure should look like:

```
.claude/
└── skills/
    └── web-design/
        ├── SKILL.md              # Orchestrator
        ├── README.md             # Overview
        ├── HOW_TO_USE.md         # Usage guide
        ├── INSTALL.md            # This file
        └── references/
            ├── css-system.md     # Variables, theming
            ├── components.md     # UI components
            ├── backgrounds.md    # Gradients, patterns
            └── responsive.md     # Mobile-first layouts
```

## Related Skills

Platform-specific:
- `swift-ui` - SwiftUI/iOS implementation

Design theory:
- `design-principles` - Design theory and fundamentals
- `design-review` - Audit and submission prep

## Usage

Once installed, Claude will use this skill when you ask for web implementation:

```
"Set up CSS for my new project"
"Build me a card component"
"Add a gradient background"
"Make this layout responsive"
```
