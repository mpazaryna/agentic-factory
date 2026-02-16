# Installation: /plan-spec

## Quick Install

### For This Project Only

```bash
cp commands/plan-spec/plan-spec.md .claude/commands/
```

### For All Projects (Global)

```bash
cp commands/plan-spec/plan-spec.md ~/.claude/commands/
```

## Verify Installation

After copying, test the command:

```
/plan-spec --help
```

Or try with a test spec file:

```
/plan-spec test-spec.md
```

## Requirements

- Claude Code CLI
- No additional dependencies

## File Structure

```
commands/plan-spec/
├── plan-spec.md      # Main command file (copy this)
├── HOW_TO_USE.md     # Usage documentation
├── INSTALL.md        # This file
└── README.md         # Overview
```

## Uninstall

### Project-level

```bash
rm .claude/commands/plan-spec.md
```

### Global

```bash
rm ~/.claude/commands/plan-spec.md
```

## Troubleshooting

### Command Not Found

Ensure the file was copied to the correct location:
- Project: `.claude/commands/plan-spec.md`
- Global: `~/.claude/commands/plan-spec.md`

### Permission Denied

Check file permissions:
```bash
chmod 644 ~/.claude/commands/plan-spec.md
```

### Spec File Not Found

Ensure you're providing the correct path to your spec file:
```
/plan-spec ./specs/my-spec.md
```
