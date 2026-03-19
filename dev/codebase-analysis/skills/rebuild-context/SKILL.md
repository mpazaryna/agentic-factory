---
name: rebuild-context
description: "Update CONTEXT.md with current project state — active work areas, quick references, known issues, testing focus, environment status. Use when the user wants to regenerate their CONTEXT.md."
argument-hint: "<folder-path>"
allowed-tools: Bash, Read, Write
disable-model-invocation: false
---

# Rebuild Context

Follow the Workflow for the `FOLDER_PATH` then Report the completed work.

## Variables

FOLDER_PATH: $ARGUMENTS

## Workflow

If no `FOLDER_PATH` is provided, STOP immediately and ask the user to provide it.

Analyze the target directory and create a CONTEXT.md that includes:

1. **Active Work Areas**
   - Files recently modified (last 10 files)
   - Directories with recent activity
   - Current feature flags or experiments

2. **Quick Reference**
   - Primary entry points for current work
   - Key integration files being modified
   - Common code patterns in use

3. **Known Issues & Blockers**
   - Current bugs or limitations
   - Workarounds in place
   - Dependencies needing updates

4. **Testing Focus**
   - Test files recently updated
   - Areas needing test coverage
   - Failing or flaky tests

5. **Environment Status**
   - Local development setup notes
   - Environment-specific configurations
   - Debug flags or settings in use
