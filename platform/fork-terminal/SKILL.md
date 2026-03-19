---
name: fork
description: "Fork a terminal session to a new terminal window with agentic coding tools (Claude Code, Codex CLI, Gemini CLI) or raw CLI commands. Use when the user requests 'fork terminal', 'new terminal', or 'fork session'."
---

# Fork Terminal

Fork a terminal session to a new terminal window using agentic coding tools or raw CLI commands.

## Variables

ENABLE_RAW_CLI_COMMANDS: true
ENABLE_GEMINI_CLI: true
ENABLE_CODEX_CLI: true
ENABLE_CLAUDE_CODE: true
AGENTIC_CODING_TOOLS: claude-code, codex-cli, gemini-cli

## Instructions

Based on the user's request, follow the Cookbook to determine which tool to use.

### Fork Summary User Prompts

- IF: The user requests a fork terminal with a summary. This ONLY works for agentic coding tools. The tool MUST BE enabled as well.
- THEN:
  - Read `${CLAUDE_SKILL_DIR}/prompts/fork_summary_user_prompt.md` as a template
  - Fill it out IN YOUR MEMORY with the conversation history and the next user request
  - Pass that prompt to the agentic coding tool
  - IMPORTANT: Do not update the file directly — use it as a template in memory
- EXAMPLES:
  - "fork terminal use claude code to <xyz> summarize work so far"
  - "spin up a new terminal request <xyz> using claude code include summary"

## Workflow

1. Understand the user's request
2. READ: `${CLAUDE_SKILL_DIR}/tools/fork_terminal.py` to understand the tooling
3. Follow the Cookbook to determine which tool to use
4. Execute `${CLAUDE_SKILL_DIR}/tools/fork_terminal.py: fork_terminal(command: str)`

## Cookbook

### Raw CLI Commands
- IF: Non-agentic tool AND `ENABLE_RAW_CLI_COMMANDS` is true
- THEN: Read and execute `${CLAUDE_SKILL_DIR}/cookbook/cli-command.md`
- EXAMPLES: "Create a new terminal to <xyz> with ffmpeg/curl/python"

### Claude Code
- IF: Claude Code agent AND `ENABLE_CLAUDE_CODE` is true
- THEN: Read and execute `${CLAUDE_SKILL_DIR}/cookbook/claude-code.md`
- EXAMPLES: "fork terminal use claude code to <xyz>"

### Codex CLI
- IF: Codex CLI agent AND `ENABLE_CODEX_CLI` is true
- THEN: Read and execute `${CLAUDE_SKILL_DIR}/cookbook/codex-cli.md`
- EXAMPLES: "fork terminal use codex to <xyz>"

### Gemini CLI
- IF: Gemini CLI agent AND `ENABLE_GEMINI_CLI` is true
- THEN: Read and execute `${CLAUDE_SKILL_DIR}/cookbook/gemini-cli.md`
- EXAMPLES: "fork terminal use gemini to <xyz>"
