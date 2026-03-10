# [Project Name] Context

> Dynamic development context — Last updated: [date]
> See README.md for stable documentation
> Generate with: /context-rebuild or manually maintain

## Project Identity

- **Name:** [project-name]
- **Purpose:** [one-line description of what this project does]
- **Type:** [e.g., iOS app, web API, CLI tool, data pipeline]
- **Repo:** [public/private]

## Tech Stack

- **Runtime:** [e.g., Node.js 20, Python 3.12, Swift 5.9, Cloudflare Workers]
- **Languages:** [e.g., TypeScript, Swift, Python]
- **Framework:** [e.g., React, SwiftUI, FastAPI, Hono]
- **Database:** [e.g., PostgreSQL, SQLite, KV, none]
- **Tooling:** [e.g., Vite, Xcode, Docker, Turborepo]
- **Package Manager:** [e.g., npm, pip, SPM]
- **Testing:** [e.g., Jest, Swift Testing, pytest]
- **CI/CD:** [e.g., GitHub Actions, Vercel, Xcode Cloud]

## Directory Structure

```
[key directories and their purpose — not every file, just the architecture]
```

## Conventions

- **Naming:** [e.g., kebab-case files, PascalCase components]
- **Architecture:** [e.g., MVC, MVVM, hexagonal, serverless]
- **State management:** [e.g., SwiftData, Redux, Zustand]
- **API patterns:** [e.g., REST, GraphQL, tRPC]
- **Error handling:** [e.g., Result types, try/catch, error boundaries]
- **Key ADRs:** [list any architectural decision records and their locations]

## Key Files

| File | Purpose |
|------|---------|
| [entry point] | [description] |
| [config file] | [description] |
| [main module] | [description] |

## Agent Knowledge Base (.orchestra/)

> Remove this section if your project does not use the .orchestra/ pattern.

```
.orchestra/
├── adr/        Architecture Decision Records (long-lived constraints)
├── work/       Per-ticket work items (PRDs + specs)
│   ├── TEMPLATES/
│   │   ├── prd.md
│   │   └── spec.md
│   └── {ticket-id}-{name}/
│       ├── prd.md       Business intent (produced by ticket-refiner)
│       └── spec.md      Technical contract (produced by prd-to-spec)
├── devlog/     Chronological development journal (by quarter)
└── README.md
```

**Pipeline:** `/refine-ticket` → prd.md → validate → `/write-spec` → spec.md → `/tk-open` → implement

## External Integrations

- [e.g., ClickUp API — task management]
- [e.g., Salesforce — CRM data source]
- [e.g., Cloudflare R2 — object storage]

## Known Constraints

- [e.g., API rate limits, HIPAA compliance requirements, offline-first]
- [e.g., Must support iOS 17+, macOS 14+]
- [e.g., Max bundle size 500KB]
