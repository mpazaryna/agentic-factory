---
name: recipes
description: "Create, validate, and work with Goose recipes — reusable AI agent configurations with parameters, extensions, retry logic, and structured outputs. Use when creating recipe.yaml files, configuring Goose extensions, or debugging recipe validation errors."
---

# Goose Recipes

Create and work with Goose recipes — reusable configurations that package specific AI agent setups.

## Quick Start

Start with `${CLAUDE_SKILL_DIR}/assets/basic-recipe-template.yaml` and customize. For complex workflows, use `${CLAUDE_SKILL_DIR}/assets/advanced-recipe-template.yaml`.

## Core Recipe Creation Workflow

### 1. Define Required Fields

Every recipe MUST have:
- `version`: Use "1.0.0"
- `title`: Short, descriptive title
- `description`: Detailed explanation of purpose

### 2. Add Instructions or Prompt

- `instructions`: Multi-step guidance for complex tasks
- `prompt`: Direct task statement for simple tasks
- Both: Instructions provide context, prompt initiates action

### 3. Configure Parameters

```yaml
parameters:
  - key: param_name
    input_type: string  # or "file" to read file contents
    requirement: required  # or "optional" or "user_prompt"
    description: "What this parameter does"
    default: "value"  # Required for optional parameters
```

Use parameters in templates: `{{ param_name }}`

### 4. Add Extensions (if needed)

```yaml
extensions:
  - type: stdio
    name: extension_name
    cmd: command_to_run
    args: [arguments]
    timeout: 300
    description: "What this extension provides"
```

### 5. Configure Retry Logic (optional)

```yaml
retry:
  max_retries: 3
  checks:
    - type: shell
      command: "test -f output.json"
  on_failure: "rm -f output.json"
```

### 6. Define Structured Output (optional)

```yaml
response:
  json_schema:
    type: object
    properties:
      result:
        type: string
        description: "Main result"
    required: [result]
```

## Common Patterns

### MCP Server Access with Authentication

**IMPORTANT**: Do NOT use `sse` or `streamable_http` extension types for HTTP-based MCP servers with auth. Instead, pass credentials as parameters and document tools in instructions.

### File Input Processing

```yaml
parameters:
  - key: source_code
    input_type: file
    requirement: required
prompt: "Analyze this code:\n{{ source_code }}"
```

### Subrecipe Composition

```yaml
sub_recipes:
  - name: "validate"
    path: "./validation.yaml"
    values:
      strict_mode: "true"
```

## CLI vs Desktop Formats

**CLI Format** (root-level fields): `version`, `title`, `description` at root
**Desktop Format** (nested): Wrapped in `recipe:` object with `name:` at root

## Debug Common Issues

| Issue | Solution |
|-------|----------|
| Template variable without parameter | Add parameter definition for `{{ variable }}` |
| Optional parameter without default | Add `default: "value"` to parameter |
| Invalid YAML syntax | Check indentation and quotes |

## Reference

- [references/recipe-structure.md](references/recipe-structure.md) — Complete field reference
- Templates in `assets/`: basic, advanced, mcp-server
