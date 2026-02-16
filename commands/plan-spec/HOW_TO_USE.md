# How to Use: /plan-spec

## Purpose

Convert a specification file into a TDD (Test-Driven Development) implementation plan. The command reads your spec, decomposes it into testable units, and generates a sequenced plan that a coding agent can follow test-first.

## Invocation

```
/plan-spec [spec-file-path]
```

## Examples

### Basic Usage

```
/plan-spec spec-01.md
```
Output: Creates `plan-01.md` in the same directory

### Named Spec Files

```
/plan-spec authentication-spec.md
```
Output: Creates `authentication-plan.md` in the same directory

### Specs in Subdirectories

```
/plan-spec docs/api-spec.md
```
Output: Creates `docs/api-plan.md` (same directory as spec)

### Feature Specs

```
/plan-spec features/user-registration-spec.md
```
Output: Creates `features/user-registration-plan.md`

## What It Does

1. **Reads** your spec file
2. **Extracts** requirements, features, and technical details
3. **Decomposes** into testable units
4. **Sequences** in dependency order (foundational first)
5. **Generates** a plan with explicit TDD steps for each unit
6. **Writes** the plan file with matching naming convention

## Output Structure

The generated plan includes:

- **Overview**: Summary and key deliverables from spec
- **Test-First Implementation Sequence**: Numbered steps, each with:
  - What failing tests to write
  - What to implement to pass
  - What to refactor after green
- **Dependencies & Order** (only if helpful)
- **Completion Criteria**: Test coverage checklist

## Naming Convention

| Input Spec | Output Plan |
|------------|-------------|
| `spec-01.md` | `plan-01.md` |
| `spec-02.md` | `plan-02.md` |
| `authentication-spec.md` | `authentication-plan.md` |
| `api-spec.md` | `api-plan.md` |
| `user-profile-spec.md` | `user-profile-plan.md` |

## Workflow Integration

1. Write your spec file (e.g., `spec-01.md`)
2. Run `/plan-spec spec-01.md`
3. Review generated `plan-01.md`
4. Follow the TDD sequence to implement

## Tips

- Keep specs focused on one feature/component
- Include acceptance criteria in your spec for better test guidance
- The plan is a roadmap - adjust as you learn during implementation
- Use with spike-driven-dev methodology for unfamiliar territory
