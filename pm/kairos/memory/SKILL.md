---
name: memory
description: "Capture a quick timestamped thought to memory. Use when logging a thought, observation, decision, or anything worth remembering mid-day."
allowed-tools: Read, Write, Bash
disable-model-invocation: false
---

# Memory

Fast capture for thoughts, notes, and observations throughout the day.

## Two Modes

### 1. Explicit Invocation (`/kairos:memory`)
When the user types `/kairos:memory` with no content:
- Prompt: "What would you like to remember?"
- Wait for response, then save

### 2. Natural Language Capture
When the user dictates something that's clearly meant to be captured, save it immediately. Don't ask for clarification.

**Recognition patterns:**
- "remember that"
- "log that"
- "capture that as a note"
- "quick note:"
- "memory:"
- Any statement followed by a capture instruction

**Example:**
> "We figured out that the sync issue was caused by a race condition in the file watcher. Remember that."

Just save it. Don't ask "what would you like to capture?"

## Create the Note

- Filename: `kairos/memory/YYYY-MM-DD-HHMMSS.md`
- Frontmatter:
  ```yaml
  ---
  tags: [memory]
  date: YYYY-MM-DD
  time: HH:MM
  ---
  ```
- Body: The captured text (extracted from what user said, minus the capture instruction)

## Confirm

Show: "Logged to `kairos/memory/YYYY-MM-DD-HHMMSS.md`"

Done - no follow-up needed.

## Notes

- No title needed - the timestamp is the identifier
- Tag with `memory` for easy filtering
- These are raw captures - process later or let them accumulate
- Can be reviewed during `/shutdown` or weekly review
- Works great with voice dictation (Wispr)
