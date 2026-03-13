---
name: rebuild-readme
description: "Generate a developer-focused README.md for a project or module — overview, getting started, architecture, development, deployment. Use when the user wants to regenerate their README."
argument-hint: "<folder-path>"
allowed-tools: Bash, Read, Write
disable-model-invocation: true
---

# Rebuild README

Follow the Workflow for the `FOLDER_PATH` then Report the completed work.

## Variables

FOLDER_PATH: $ARGUMENTS

## Workflow

If no `FOLDER_PATH` is provided, STOP immediately and ask the user to provide it.

Analyze the target directory and create a README.md that includes:

1. **Project Overview** — What it does, key technologies, license
2. **Getting Started** — Prerequisites, installation, environment setup, quick start
3. **Architecture** — High-level overview, key components, data flow
4. **Development** — Available scripts, testing, linting, build process
5. **Deployment** — Environments, CI/CD, production considerations
6. **API/Interface Documentation** — Endpoints, component props, CLI commands
7. **Contributing** — Link to CONTEXT.md, code style, PR process
8. **Troubleshooting** — Common issues, debug commands, logs

The generated README should be professional, focused on onboarding developers, and avoid duplicating dynamic context from CONTEXT.md.
