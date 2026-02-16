---
name: pytest
description: Run a Python test suite with pytest and report results. Use when the user wants to run tests, check test status, or generate a test report.
---

# Pytest

Run a project's Python test suite and report structured results.

## When to Use

- User says "run tests", "check tests", or `/test`
- After implementing a feature or fix, to verify nothing broke
- When the user wants a summary of test health

## Capabilities

- **Run Tests**: Execute pytest with verbose output
- **Summarize Results**: Total, passed, failed, skipped, duration
- **Report Failures**: Show failing test names with brief failure descriptions
- **Report Generation**: Confirm test report written (if project uses a report plugin)
- **Selective Runs**: Pass through `-k` filters, specific test files, or markers

## Input Requirements

- **Optional**: specific test file or directory (defaults to project test directory)
- **Optional**: `-k` filter expression for selective test runs
- **Optional**: pytest markers (`-m slow`, `-m integration`)

## Output

- Console summary: total tests, passed, failed, skipped, duration
- Failure details: test name + brief description of each failure
- Report file path (if the project generates a markdown report)

## How to Use

Customize these fields for your project before use:

| Field | Default | Example |
|-------|---------|---------|
| Package manager | `uv` | `uv`, `poetry`, `pip` |
| Test directory | `tests/` | `tests/`, `test/`, `src/tests/` |
| Report path | *(none)* | `docs/reports/test-report.md` |

### Steps

1. Run: `{package_manager} run pytest {test_directory} -v`
2. If a report path is configured, confirm the report was written
3. Summarize results: total tests, passed, failed, skipped, duration
4. If there are failures, show the failing test names and a brief description of each failure
5. If a report path is configured, mention it is ready to commit

If the user passes arguments (e.g., a specific test file or `-k` filter), append them to the pytest command.

## Best Practices

1. Always run with `-v` for verbose output unless the user specifies otherwise
2. Show failures first — that's what the user cares about
3. Don't re-run tests automatically on failure; let the user decide next steps
4. If all tests pass, keep the summary brief

## Limitations

- Requires pytest to be installed in the project's environment
- Report generation depends on the project having a pytest report plugin configured
- Does not install dependencies — if tests fail due to missing packages, tell the user to run their package manager's install command
