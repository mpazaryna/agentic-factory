# How to Use the Rebuild Context Command

## Quick Start

Run the command with a project path:

```
/rebuild-context /path/to/project
/rebuild-context .
/rebuild-context ~/workspace/my-app
```

## What This Command Does

Analyzes your project and creates `CONTEXT.md` with:
- Active work areas (recently modified files)
- Current integration points
- Known issues and blockers
- Testing focus areas
- Environment-specific notes

## When to Use

Run this command when:
- Starting work on a project after time away
- Switching between features
- Onboarding team members
- Before planning next sprint
- After major refactoring
- When context feels stale

## Usage Examples

### Example 1: Update Project Context

```
User: "/rebuild-context ."

Command: Analyzing current project...

Checking recent activity:
- Found 10 recently modified files
- Identified 3 active directories
- Detected 2 pending issues in code comments

Generating CONTEXT.md...

✅ CONTEXT.md updated successfully!

Summary:
- Active work areas: authentication, API endpoints
- Recent files: src/auth/login.ts, src/api/users.ts
- Known issues: Rate limiting needs implementation
- Testing focus: Missing tests for auth flow
- Last updated: 2024-11-14T14:00:00Z
```

Generated CONTEXT.md:
```markdown
# My App Context

> Dynamic development context - Last updated: 2024-11-14T14:00:00Z
> See README.md for stable documentation

## Active Work Areas

### Recently Modified Files
1. src/auth/login.ts (2 hours ago)
2. src/api/users.ts (4 hours ago)
3. tests/auth.test.ts (5 hours ago)
4. src/middleware/auth.ts (1 day ago)
5. src/models/User.ts (1 day ago)

### Active Directories
- `src/auth/` - Authentication system refactor
- `src/api/` - New user endpoints
- `tests/` - Auth test coverage

## Quick Reference

### Primary Entry Points
- `src/auth/login.ts` - Main authentication logic
- `src/api/users.ts` - User management endpoints
- `src/middleware/auth.ts` - Auth middleware

### Key Integration Files
- `src/auth/jwt.ts` - Token generation/validation
- `src/db/users.ts` - User database queries
- `src/api/routes.ts` - Route configuration

### Common Patterns
- JWT-based authentication
- Async/await for all DB operations
- Error handling via middleware

## Known Issues & Blockers

### Current Bugs
- Rate limiting not yet implemented (TODO in auth.ts:45)
- Password reset emails not sending (blocked on SMTP config)

### Workarounds in Place
- Using in-memory session store (needs Redis in production)

### Dependencies Needing Updates
- express-jwt v7 → v9 (breaking changes to review)

## Testing Focus

### Recently Updated Tests
- tests/auth.test.ts - Login flow tests
- tests/api/users.test.ts - User CRUD operations

### Areas Needing Coverage
- Password reset flow (0% coverage)
- Token refresh logic (partial coverage)
- Error handling edge cases

### Failing/Flaky Tests
- None currently

## Environment Status

### Local Development Setup
- PostgreSQL running on localhost:5432
- Redis not configured (using memory store)
- SMTP disabled (emails logged to console)

### Environment Variables in Use
```
DATABASE_URL=postgresql://localhost:5432/myapp
JWT_SECRET=dev-secret-key
NODE_ENV=development
```

### Debug Flags
- `DEBUG=auth:*` - Auth module debugging
- `LOG_LEVEL=debug` - Verbose logging
```

### Example 2: After Time Away

```
User: "I haven't worked on this project in 2 weeks. What's the current state?"

Command: "/rebuild-context ."

Agent: Let me rebuild the context to show current project state...

✅ CONTEXT.md updated with recent activity:

**Active Work:**
- Payment integration (last modified yesterday)
- Database migration (last week)

**Known Issues:**
- Stripe webhook endpoint timing out
- Migration rollback script missing

**Testing Focus:**
- Payment flow tests added
- Need integration tests for webhooks

Check CONTEXT.md for full details.
```

### Example 3: Team Onboarding

```
Team Member: "I'm new to this codebase. Where should I start?"

Developer: "/rebuild-context ."

Output: CONTEXT.md updated with:
- Current active work areas (what team is focused on)
- Primary entry points (where to start reading code)
- Known issues to be aware of
- Testing gaps that need help

New team member reads CONTEXT.md to understand:
- What's being actively developed
- What problems exist
- Where they can contribute
- What tests are needed
```

### Example 4: Before Sprint Planning

```
User: "/rebuild-context . "

Command: Analyzing project for sprint planning...

Generated CONTEXT.md shows:
- Completed work from last sprint
- Unresolved issues to carry forward
- Technical debt accumulated
- Testing gaps to address

Team uses CONTEXT.md to:
- Prioritize bug fixes
- Plan test coverage improvements
- Schedule tech debt cleanup
- Identify blockers for next sprint
```

## Command Workflow

### Step 1: Analyze Recent Activity

```bash
# Checks git log for recent commits
git log --pretty=format:"%h %an %ar %s" -10

# Lists recently modified files
find . -type f -mtime -7 -name "*.ts" -o -name "*.js"
```

### Step 2: Scan for Issues

```bash
# Looks for TODO, FIXME, HACK comments
grep -r "TODO\|FIXME\|HACK" src/
```

### Step 3: Identify Testing Needs

```bash
# Finds test files
find tests/ -name "*.test.*"

# Checks test coverage reports
cat coverage/coverage-summary.json
```

### Step 4: Generate CONTEXT.md

Creates structured markdown with all findings.

## Best Practices

### Do's ✅

- Run before starting work each day
- Update after completing major features
- Review before team meetings
- Share with new team members
- Commit to version control
- Reference in pull requests

### Don'ts ❌

- Don't manually edit CONTEXT.md (regenerate instead)
- Don't duplicate README.md content
- Don't include sensitive information
- Don't let it get stale (regenerate regularly)

## Integration with Workflow

### Morning Routine

```bash
# Start of day
/rebuild-context .

# Review current state
cat CONTEXT.md

# Plan work based on context
# Focus on known issues or testing gaps
```

### After Feature Completion

```bash
# Complete feature
git commit -m "feat: add payment integration"

# Update context
/rebuild-context .

# Review what changed
git diff CONTEXT.md

# Commit context update
git add CONTEXT.md
git commit -m "docs: update context after payment feature"
```

### Team Standup

```bash
# Before standup
/rebuild-context .

# Reference during standup:
# - Active work areas
# - Known blockers
# - Testing needs
```

## File Location

CONTEXT.md is created in the project root:

```
project/
├── CONTEXT.md        ← Dynamic context (frequently updated)
├── README.md         ← Stable documentation
├── src/
└── tests/
```

## Git Integration

Recommended `.gitignore` approach:

**Option 1: Track CONTEXT.md**
```bash
# Commit CONTEXT.md for team visibility
git add CONTEXT.md
git commit -m "docs: update project context"
```

**Option 2: Ignore CONTEXT.md**
```bash
# Add to .gitignore if context is developer-specific
echo "CONTEXT.md" >> .gitignore

# Each developer maintains their own context
```

**Recommended:** Track in version control for team alignment.

## Common Questions

**Q: How often should I run this?**
A: Daily or after significant changes. Whenever context feels stale.

**Q: Does it overwrite existing CONTEXT.md?**
A: Yes, it regenerates from current state. Don't manually edit.

**Q: Can I customize the sections?**
A: Not directly, but you can edit the command definition.

**Q: What if project has no git history?**
A: Still works - uses file modification times instead.

**Q: Does it work with monorepos?**
A: Yes, run for each package: `/rebuild-context packages/api`

## Related Commands

- **/rebuild-readme** - Generate/update stable README.md
- **learn-project** (skill) - Comprehensive codebase analysis

## Tips for Effective Context

1. **Run Regularly** - Daily or when switching context
2. **Review Before Work** - Understand current state
3. **Share with Team** - Commit for team visibility
4. **Reference in PRs** - Link to relevant context sections
5. **Update After Milestones** - Keep it current

---

Generated by Claude Code Skills Factory
