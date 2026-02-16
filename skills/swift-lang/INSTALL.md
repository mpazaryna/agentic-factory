# Installation

## Option 1: Copy to Project

Copy the entire `swift-lang/` folder to your project's `.claude/skills/` directory:

```bash
cp -r swift-lang/ /path/to/your-project/.claude/skills/
```

## Option 2: Copy to Global Skills

For availability across all projects, copy to your home directory:

```bash
cp -r swift-lang/ ~/.claude/skills/
```

## Option 3: Symlink (Development)

If you want to keep the skill updated from this repository:

```bash
ln -s /path/to/agentic-factory/skills/swift-lang ~/.claude/skills/swift-lang
```

## Verification

After installation, the skill should activate when you ask about Swift language features like macros, concurrency, or testing.

## Requirements

- Claude Code CLI
- No external dependencies (pure documentation skill)
