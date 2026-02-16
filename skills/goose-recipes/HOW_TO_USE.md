# How to Use the Goose Recipes Skill

## Quick Start

Ask Claude to help create or modify Goose recipes:

```
"Create a Goose recipe for code review"
"Help me add retry logic to this recipe"
"Fix the validation error in my recipe.yaml"
"Create a recipe that processes markdown files"
```

## What This Skill Does

The Goose Recipes skill helps you work with Goose recipes - reusable YAML/JSON configurations that define AI agent behaviors, tools, and workflows.

Claude will:
1. Create recipes from templates (basic, advanced, MCP server)
2. Configure parameters, extensions, and retry logic
3. Set up structured outputs with JSON schemas
4. Debug validation errors
5. Guide you through complex recipe features

## Core Concepts

### What is a Goose Recipe?

A Goose recipe is a configuration file (YAML or JSON) that packages:
- Task instructions or prompts
- Required parameters
- Extension tools (MCP servers)
- Retry logic and validation
- Output formatting

Think of it as a "script" for an AI agent.

### Recipe Structure

```yaml
version: "1.0.0"                    # Required: Recipe version
title: "Recipe Name"                # Required: Short title
description: "What it does"         # Required: Detailed description

parameters:                         # Optional: Input parameters
  - key: param_name
    input_type: string
    requirement: required
    description: "Parameter purpose"

instructions: "Step-by-step..."     # or "prompt:"
extensions: [...]                   # Optional: MCP servers/tools
retry: {...}                        # Optional: Retry configuration
response: {...}                     # Optional: Structured output
```

## Usage Examples

### Example 1: Create Simple Recipe

```
User: "Create a Goose recipe that analyzes Python code for bugs"

Claude: I'll create a basic recipe for Python code analysis.

[Loads assets/basic-recipe-template.yaml]
[Customizes for Python analysis]

Here's your recipe (save as code-analyzer.yaml):

```yaml
version: "1.0.0"
title: "Python Code Bug Analyzer"
description: "Analyzes Python code files for potential bugs, security issues, and code quality problems"

parameters:
  - key: python_file
    input_type: file
    requirement: required
    description: "Python source code file to analyze"

  - key: severity_level
    input_type: string
    requirement: optional
    description: "Minimum severity to report (low, medium, high)"
    default: "medium"

instructions: |
  Analyze the provided Python code for:
  1. Potential bugs (null checks, exception handling)
  2. Security vulnerabilities (SQL injection, XSS)
  3. Code quality issues (complexity, duplication)
  4. Best practice violations

  Focus on issues of {{ severity_level }} severity or higher.
  Provide specific line numbers and fix suggestions.

prompt: "Analyze this Python code:\n\n{{ python_file }}"

response:
  json_schema:
    type: object
    properties:
      issues:
        type: array
        items:
          type: object
          properties:
            line: { type: integer }
            severity: { type: string }
            category: { type: string }
            description: { type: string }
            suggestion: { type: string }
      summary: { type: string }
    required: [issues, summary]
```

**Usage:**
```bash
goose run --recipe code-analyzer.yaml --param python_file=app.py
```
```

### Example 2: Add Retry Logic

```
User: "Add retry logic to ensure the recipe creates an output.json file"

Claude: I'll add retry configuration with file validation.

Add this to your recipe:

```yaml
retry:
  max_retries: 3
  checks:
    - type: shell
      command: "test -f output.json && jq -e '.status' output.json"
  on_failure: "rm -f output.json"
```

This will:
- Retry up to 3 times if validation fails
- Check that output.json exists AND contains a "status" field
- Clean up the file before retrying

The shell command must exit with code 0 for success.
```

### Example 3: Configure MCP Server

```
User: "Create a recipe that uses a GitHub MCP server to create issues"

Claude: I'll create a recipe with MCP server configuration for GitHub.

```yaml
version: "1.0.0"
title: "GitHub Issue Creator"
description: "Creates GitHub issues from bug reports"

parameters:
  - key: bug_report
    input_type: file
    requirement: required
    description: "Bug report markdown file"

  - key: repo_name
    input_type: string
    requirement: required
    description: "GitHub repository (owner/repo)"

extensions:
  - type: stdio
    name: github-mcp
    cmd: npx
    args: ["-y", "@modelcontextprotocol/server-github"]
    env_keys: [GITHUB_PERSONAL_ACCESS_TOKEN]
    description: "GitHub MCP server for issue management"

instructions: |
  1. Parse the bug report: {{ bug_report }}
  2. Extract title, description, and severity
  3. Use the github-mcp extension to create an issue in {{ repo_name }}
  4. Label based on severity (critical, major, minor)
  5. Return the created issue URL

prompt: "Create a GitHub issue from this bug report"

response:
  json_schema:
    type: object
    properties:
      issue_url: { type: string }
      issue_number: { type: integer }
      title: { type: string }
    required: [issue_url, issue_number, title]
```

**Setup:**
```bash
export GITHUB_PERSONAL_ACCESS_TOKEN="your_token_here"
goose run --recipe github-issue-creator.yaml \
  --param bug_report=bug.md \
  --param repo_name=owner/repo
```
```

### Example 4: Debug Validation Error

```
User: "I'm getting: 'Template variable without parameter: data_file'"

Claude: You're using {{ data_file }} in your template but haven't defined it as a parameter.

Add this to your parameters section:

```yaml
parameters:
  - key: data_file
    input_type: file          # Use "string" if not reading file contents
    requirement: required     # or "optional" or "user_prompt"
    description: "Input data file for processing"
```

If it's optional, also add:
```yaml
    default: "data/default.json"
```

Now {{ data_file }} will be properly substituted when the recipe runs.
```

### Example 5: Multi-Step Workflow

```
User: "Create a recipe for a documentation generation workflow"

Claude: I'll create a multi-step recipe with instructions and structured output.

```yaml
version: "1.0.0"
title: "API Documentation Generator"
description: "Generates comprehensive API documentation from source code"

parameters:
  - key: source_dir
    input_type: string
    requirement: required
    description: "Directory containing source code"

  - key: output_format
    input_type: string
    requirement: optional
    description: "Output format (markdown, html, openapi)"
    default: "markdown"

  - key: include_examples
    input_type: string
    requirement: optional
    description: "Include usage examples (true/false)"
    default: "true"

instructions: |
  **Documentation Generation Workflow**

  Phase 1: Discovery
  - Scan {{ source_dir }} for API endpoints
  - Identify request/response structures
  - Extract inline documentation

  Phase 2: Analysis
  - Group endpoints by resource
  - Document authentication requirements
  - List required/optional parameters

  Phase 3: Generation
  - Create {{ output_format }} documentation
  - Include examples: {{ include_examples }}
  - Add table of contents and navigation

  Phase 4: Validation
  - Verify all endpoints documented
  - Check for broken links
  - Validate code examples

  Save output to: api-docs/{{ output_format }}/

prompt: "Begin documentation generation for {{ source_dir }}"

retry:
  max_retries: 2
  checks:
    - type: shell
      command: "test -d api-docs/{{ output_format }}"

response:
  json_schema:
    type: object
    properties:
      endpoints_documented: { type: integer }
      output_location: { type: string }
      warnings: { type: array, items: { type: string } }
    required: [endpoints_documented, output_location]
```
```

## Common Patterns

### File Input Processing

Read and use file contents:

```yaml
parameters:
  - key: config
    input_type: file
    requirement: required
    description: "Configuration file"

prompt: "Process this config:\n{{ config }}"
```

### Optional Parameters with Defaults

```yaml
parameters:
  - key: verbose
    input_type: string
    requirement: optional
    description: "Enable verbose output"
    default: "false"
```

### Environment-Based Secrets

```yaml
extensions:
  - type: stdio
    name: api-client
    cmd: api-client-mcp
    env_keys: [API_KEY, API_SECRET]
```

### Subrecipe Composition

Combine multiple recipes:

```yaml
sub_recipes:
  - name: "validation"
    path: "./validate.yaml"
    values:
      strict: "true"

  - name: "processing"
    path: "./process.yaml"
```

### HTTP MCP Servers with Authentication

**Important:** For HTTP-based MCP servers requiring auth, use parameters instead of extensions:

```yaml
parameters:
  - key: API_KEY
    input_type: string
    requirement: optional
    description: "API key for MCP server"
    default: "your-key"

instructions: |
  MCP Server: https://server.example.com/mcp
  Auth: Bearer {{ API_KEY }}

  Available tools:
  - tool_name: Description

  Make authenticated HTTP requests to access tools.
```

## Recipe Templates

The skill includes three ready-to-use templates:

### 1. Basic Recipe (`assets/basic-recipe-template.yaml`)

Simple structure with required fields:
- Version, title, description
- Single parameter
- Basic prompt

**When to use:** Simple, single-purpose tasks

### 2. Advanced Recipe (`assets/advanced-recipe-template.yaml`)

Complex features:
- Multiple parameters
- Retry logic with validation
- Structured JSON output
- Subrecipes

**When to use:** Multi-step workflows, validation needed

### 3. MCP Server Recipe (`assets/mcp-server-recipe-template.yaml`)

HTTP MCP server integration:
- Authentication via parameters
- Server URL documentation
- Tool usage guidance

**When to use:** Working with HTTP-based MCP servers

## Debugging Recipes

### Common Errors and Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| "Template variable without parameter" | Using `{{ var }}` without defining | Add parameter definition |
| "Optional parameter without default" | Optional param missing default value | Add `default: "value"` |
| "Invalid YAML syntax" | Indentation or quote issues | Check YAML formatting |
| "Shell command failed" | Retry check command error | Test command separately |
| "Extension not found" | MCP server not installed | Install extension or check cmd path |

### Validation Checklist

Before running a recipe, verify:
- [ ] Version, title, description present
- [ ] All template variables have parameters
- [ ] Optional parameters have defaults
- [ ] Shell commands are escaped properly
- [ ] JSON schemas are valid
- [ ] Extension commands are available

## Best Practices

### Do's ✅

- Start with templates, customize as needed
- Test shell commands separately before adding to retry logic
- Use descriptive parameter names and descriptions
- Validate JSON schemas before adding to response
- Document MCP server tools in instructions
- Keep recipes focused on one primary task

### Don'ts ❌

- Don't skip required fields (version, title, description)
- Don't use template variables without parameters
- Don't forget defaults for optional parameters
- Don't use complex shell commands without testing
- Don't mix CLI and Desktop formats in same file

## Integration with Workflow

### Development Workflow

```bash
# 1. Create recipe with Claude's help
# Ask: "Create a recipe for X"

# 2. Save to file
cat > my-recipe.yaml

# 3. Test locally
goose run --recipe my-recipe.yaml --param key=value

# 4. Iterate based on results
# Ask Claude: "The recipe failed with error X, how do I fix it?"

# 5. Share with team
git add my-recipe.yaml
git commit -m "Add recipe for X"
```

### Reusable Recipe Library

```
recipes/
├── code-review.yaml
├── docs-gen.yaml
├── test-gen.yaml
└── refactor.yaml
```

## Advanced Features

### Template Inheritance

```yaml
{% extends "base-recipe.yaml" %}
{% block instructions %}
Custom instructions here
{% endblock %}
```

### Template Filters

```yaml
prompt: "{{ content | indent(2) }}"
```

### Built-in Parameters

```yaml
# recipe_dir is automatically available
path: "{{ recipe_dir }}/data/input.json"
```

## Common Questions

**Q: YAML vs JSON?**
A: Both work. YAML is more human-readable. Ask Claude: "Convert this to JSON format"

**Q: Can recipes call other recipes?**
A: Yes, use `sub_recipes` to compose workflows.

**Q: How do I test recipes without running?**
A: Ask Claude: "Validate this recipe for errors"

**Q: Can I use environment variables?**
A: Yes, via `env_keys` in extensions or as parameters.

**Q: What's the difference between instructions and prompt?**
A: Instructions provide context/steps, prompt initiates action. You can use both.

## Related Skills

- **goose-recipe-analysis** - Analyze and optimize existing recipes
- **code-reviewer** - Review recipe YAML quality

## Reference Documentation

For complete field reference:
- **references/recipe-structure.md** - Comprehensive field documentation

---

Generated by Claude Code Skills Factory
