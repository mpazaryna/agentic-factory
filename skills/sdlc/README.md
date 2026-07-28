# sdlc/

Orchestra — a software development lifecycle encoded for agents.

Eighteen skills that carry a piece of work from a ticket to a merge: scope it,
spec it, build it, review it, ship it, and leave a record of why. They are meant
to be used as a loop, not a menu — each stage produces the input the next one
expects, and the artifacts live in a `.orchestra/` folder in the consuming
project.

## The loop

| Stage | Skill | Produces |
|-------|-------|----------|
| Orient | `orchestra-usher` | a read of current project state, routed to the next skill |
| Set up | `orchestra-scaffold` | the `.orchestra/` knowledge base in a project |
| Frame | `orchestra-roadmap` | vision and milestones |
| Review | `orchestra-milestone` | gaps between the plan and the repo |
| Intake | `orchestra-ticket` | a work item folder from a brief |
| Scope | `orchestra-prd` | objective, success criteria, materials |
| Design | `orchestra-spec` | approach, steps, acceptance criteria, risks |
| Specify | `orchestra-gherkin` | executable BDD scenarios |
| Build | `orchestra-implement` | a branch, commits, a completed spec |
| Check | `orchestra-review` | gaps and shortcuts caught before merge |
| Ship | `orchestra-merge` | merged branch, closed work item |
| Record | `orchestra-devlog`, `orchestra-adr` | the story behind the commits, decisions and their consequences |

Four more sit outside the sequence:

- **`orchestra-plan`** — a conductor that runs PRD → Spec → Gherkin in one
  interactive session with approval gates, instead of three invocations.
- **`orchestra-afk`** — the same discipline with nobody at the keyboard. Gates
  become files, approval becomes a commit.
- **`orchestra-uml`** — Mermaid diagrams into `.orchestra/uml/`.
- **`orchestra-program`** — explains what Orchestra is and where to start.
- **`orchestra-eval`** — grades a skill run against the assertions in its
  `evals/` folder.

## Skills or MCP

The same playbooks are also served over MCP by
[mpazaryna/orchestra](https://github.com/mpazaryna/orchestra), a Cloudflare
Worker exposing `orchestra_get_skill`, `orchestra_get_prompt`, and friends.

Two delivery mechanisms, one body of content:

| | Installed skills (here) | MCP server |
|---|---|---|
| Requires | nothing beyond the install | a deployed Worker, an API key, network |
| Invocation | slash commands, auto-load on description | agent calls a tool |
| Updates | reinstall | redeploy, consumers get it immediately |

**This repo is the source of truth for skill content.** The orchestra repo holds
its own copies, adapted for MCP delivery; the two are intentionally allowed to
differ, and changes here do not propagate there.

## Evals

Most skills carry an `evals/evals.json` — assertions about what a correct run
produces. Run `orchestra-eval <skill-name>` in a project where the skill was just
executed to grade the output against them.
