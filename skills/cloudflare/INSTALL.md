# Installing cloudflare Skill

## Option 1: Copy to Project

Copy the entire `cloudflare/` directory to your project's `.claude/skills/` folder:

```bash
cp -r cloudflare/ /path/to/your-project/.claude/skills/
```

## Option 2: Copy to Global Skills

For access across all projects, copy to your global Claude skills directory:

```bash
cp -r cloudflare/ ~/.claude/skills/
```

## Option 3: Symlink (Development)

If you're actively developing this skill:

```bash
ln -s /path/to/cloudflare ~/.claude/skills/cloudflare
```

## Verification

After installation, verify the skill is available:

```
List available skills
```

Or load it directly:

```
Load the cloudflare skill
```

## Directory Structure

Ensure this structure exists after installation:

```
.claude/skills/cloudflare/
  SKILL.md              # Required - router file
  README.md             # Overview
  HOW_TO_USE.md         # Usage guide
  INSTALL.md            # This file
  references/
    workers.md          # Worker fundamentals
    workers-ai.md       # AI integration
    durable-objects.md  # Stateful services
    kv.md               # KV caching
    hono.md             # Routing framework
```

## Prerequisites

For using patterns in this skill, you'll need:

1. **Cloudflare Account** - Sign up at cloudflare.com
2. **Wrangler CLI** - `npm install -g wrangler`
3. **Node.js** - v18+ recommended

## Related Skills

Consider also installing:
- **swift-ui** - If building iOS clients for your Workers
- **swift-lang** - Swift networking patterns for API consumption
