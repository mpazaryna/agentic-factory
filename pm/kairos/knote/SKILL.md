---
name: knote
description: "Capture a quick timestamped thought as a knote. Use when logging a thought, observation, decision, or anything worth capturing mid-day."
allowed-tools: Read, Write, Bash
disable-model-invocation: false
---

# Knote

Fast capture for thoughts, notes, and observations throughout the day.

## Two Modes

### 1. Explicit Invocation (`/kairos:knote`)
When the user types `/kairos:knote` with no content:
- Prompt: "What's on your mind?"
- Wait for response, then save

### 2. Natural Language Capture
When the user dictates something that's clearly meant to be captured, save it immediately. Don't ask for clarification.

**Recognition patterns:**
- "knote that"
- "log that"
- "capture that"
- "quick note:"
- Any statement followed by a capture instruction

**Example:**
> "We figured out that the sync issue was caused by a race condition in the file watcher. Knote that."

Just save it. Don't ask "what would you like to capture?"

## Create the Knote

- Filename: `kairos/knotes/YYYY/MM/YYYY-MM-DD-HHMMSS.md`
- Frontmatter:
  ```yaml
  ---
  tags: [knote]
  date: YYYY-MM-DD
  time: HH:MM
  ---
  ```
- Body: The captured text (extracted from what user said, minus the capture instruction)

## Confirm

Show: "Captured to `kairos/knotes/YYYY/MM/YYYY-MM-DD-HHMMSS.md`"

Done - no follow-up needed.

## Notes

- No title needed - the timestamp is the identifier
- Tag with `knote` for easy filtering
- These are raw captures - process later or let them accumulate
- Can be reviewed during `/shutdown` or weekly review
- Works great with voice dictation (Wispr)
