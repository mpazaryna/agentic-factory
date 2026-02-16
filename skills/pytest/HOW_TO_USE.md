# How to Use pytest

## Basic Usage

```
/test
"Run the tests"
"Run tests and show me what's failing"
```

## Selective Runs

```
"Run tests for the content cleaner"
"Run tests -k test_r11"
"Run only the integration tests"
```

## What to Provide

- Nothing required for a full test run
- A specific test file or directory to narrow scope
- A `-k` filter to run matching tests only
- Pytest markers (`-m slow`) for tagged tests

## What You'll Get

- Total tests, passed, failed, skipped, duration
- Failing test names with brief failure descriptions
- Report file path if the project uses a report plugin

## Project Setup

Before using this skill in a new project, customize the SKILL.md:

1. Set your package manager command (e.g., `uv run pytest`)
2. Set your test directory (e.g., `tests/`)
3. Set your report path if applicable (e.g., `docs/reports/test-report.md`)

## Tips

- Run after every feature or fix to catch regressions early
- Use `-k` filters to focus on the area you just changed
- If tests fail due to missing packages, run your package manager's install first
