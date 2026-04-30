---
created_on: 2026-04-30
---

# Own Your Code, Rent Your Services

## Overview

A design philosophy for managing software dependencies: write your own utilities and libraries rather than taking on open source code dependencies, while freely using external services consumed over an API. The agentic-factory skills setup is a direct expression of this principle.

## The Distinction

Two kinds of dependencies, treated very differently:

**Code dependencies** — you pull in someone else's library or utility. You now own the maintenance surface. It can go stale, break on updates, diverge from what you need, or simply disappear. Every open source dependency is a bet that someone else will keep it working.

**Service dependencies** — you call an API. The service provider maintains the implementation. You own only the interface contract. If ClickUp changes their internals, that's their problem. Your code stays clean.

## Where This Shows Up

The skills symlink in `~/.claude/skills` is a concrete instance of this principle. Rather than installing third-party skills from the marketplace and taking on their update cadence, every skill that lives under that symlink goes through agentic-factory. It earns its place, matches the project's standards, and doesn't drift because someone upstream changed something.

The Bench/ClickUp integration is the service side of the same coin. Bench needed a ticketing system. The options were: build one, use an open source one, or use ClickUp as a service. Building a ticketing system is not the business. Using an open source ticketing library means owning that code. ClickUp as a service means Atlassian (or whoever) handles it — Bench just calls the API.

## The Threshold

The principle isn't "write everything." Linux is the obvious exception — no one writes an operating system. The threshold is roughly: if it's infrastructure you'd never meaningfully own (OS, cloud platform, database engine), use it. If it's a utility, library, or web app at a scale you could realistically build, build it.

Below that threshold, the cost of dependency management — version conflicts, stale packages, upstream breaking changes, reading someone else's source to debug your problem — usually exceeds the cost of writing it yourself.

## Why This Matters for Agentic Factory

Skills are code. Pulling in someone else's skill means taking on their design decisions, their update schedule, and their potential abandonment. The value of this repo is that every skill in it works the same way, earns its place, and doesn't require watching a third-party repo for changes.

When a skill from an external source is genuinely useful, the right move is to read it, understand it, and write a version that fits here — not copy-paste it in as a dependency.
