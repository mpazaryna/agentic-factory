# .orchestra — Orchestra Plugin Knowledge Base

This folder is the agent knowledge base for the **orchestra plugin** itself.

Any agent working on this plugin should read this folder before making changes:
- `roadmap.md` — plugin vision and milestone status
- `adr/` — decisions that shaped the methodology; read before proposing changes
- `work/` — active and completed work items
- `devlog/` — session journals

## The Plugin

Orchestra is a methodology plugin for Claude Code. It provides the `.orchestra/` agent knowledge base pattern — PRDs all the way down, materials tables as executable contracts, and a clear separation between product and execution layers.

Skills: scaffold, ticket, milestone, prd, spec, roadmap, devlog, conventions  
Agent: lenny (autonomous conductor)

## The Loop

```
/orchestra:ticket → /orchestra:prd → /orchestra:spec → implement → /orchestra:devlog
```

Lenny runs the full loop autonomously when given a milestone.
