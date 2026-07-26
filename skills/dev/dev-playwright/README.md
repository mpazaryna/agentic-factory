# playwright

Generate Playwright E2E tests by exploring a live website and automating browser interactions.

## Quick Start

```
generate playwright tests for https://myapp.com/login
explore the checkout flow at https://shop.example.com and write tests
write playwright tests for the dashboard at localhost:3000
```

## What It Does

Does not generate tests from a description alone — it actually navigates the site first:

1. Opens the specified URL using the Playwright MCP browser
2. Explores one key functionality (navigates, clicks, fills forms)
3. Closes the browser
4. Writes a TypeScript test using `@playwright/test` based on what it observed — role-based locators, auto-retrying assertions, no unnecessary `waitForTimeout` calls
5. Saves the test file to the `tests/` directory
6. Runs the test and iterates until it passes

Tests follow Playwright best practices: semantic locators (`getByRole`, `getByLabel`), built-in auto-waiting, and descriptive test titles with comments.
