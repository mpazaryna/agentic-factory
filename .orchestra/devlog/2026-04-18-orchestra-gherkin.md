---
created_on: 2026-04-18
commits: 94c4fdd, bc8ca52
---

# New Skill: orchestra-gherkin

## Overview

Added `orchestra-gherkin` to the orchestra methodology pipeline. It reads a PRD or spec from `.orchestra/work/` and produces BDD scenarios in Gherkin format, written to a fenced `gherkin` code block inside a markdown file.

## Motivation

The orchestra pipeline already covers PRD → spec. Gherkin closes the loop: acceptance criteria from the spec become executable BDD scenarios that QA and developers can use directly. Without this step, acceptance criteria stay buried in markdown prose.

## Usage

```
/orchestra-gherkin .orchestra/work/my-feature/spec.md
/orchestra-gherkin .orchestra/work/my-feature/prd.md
/orchestra-gherkin my-feature
```

## Output

Writes alongside the source file:
- `spec.md` → `gherkin-spec.md`
- `prd.md` → `gherkin-prd.md`

Output format:

````markdown
```gherkin
Feature: User Authentication
  Users can sign in with email and password

  Background:
    Given the authentication service is running

  Scenario: Successful login
    Given a registered user with email "user@example.com"
    When they submit valid credentials
    Then they receive an access token
```
````

## Rules Baked In

- 3–7 scenarios per feature — more than that, split features
- `Background:` only when 3+ scenarios share preconditions
- `@wip` tags on out-of-scope items from the source
- Prefers `spec.md` over `prd.md` if both exist — spec has more concrete detail
- Every scenario: at least one `Given`, `When`, `Then`
- `And` for chaining — never repeat `Given`/`When`/`Then` back to back

## Source Type Handling

**From a PRD:** user goals → happy path scenarios, success criteria → `Then` clauses.

**From a spec:** deliverables → Feature description, implementation steps → Scenario steps, acceptance criteria → `Then` clauses, risks → negative/error scenarios.

## Fix: Output Filename

Initial version wrote `gherkin.md` regardless of source. Fixed in `bc8ca52` to use `gherkin-spec.md` or `gherkin-prd.md` so both outputs can coexist in the same directory.
