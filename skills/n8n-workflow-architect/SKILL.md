---
name: n8n-workflow-architect
description: Architecture skill for designing robust n8n workflows. Use for choosing triggers, branching models, merge strategy, retries, sub-workflows, event choreography, and business-process topology.
---

# n8n Workflow Architect

Use this skill before building any non-trivial workflow.

## Quick workflow

1. Clarify trigger mode and production execution path.
2. Decide item granularity and side-effect boundaries.
3. Choose branch, loop, merge, and wait semantics.
4. Define failure domains and recovery behavior.
5. Decide whether sub-workflows or separate workflows are cleaner.

## Preferred architecture lenses

- trigger design
- idempotency
- side-effect isolation
- backpressure and batching
- resumability
- human intervention points

## Core rules

- A workflow that only succeeds manually is not production-ready.
- Keep side effects late and derived data early.
- Use sub-workflows when a capability deserves independent reuse, testing, or permission boundaries.
- Treat retries differently for read operations and write operations.

## Strong patterns

- webhook intake -> normalize -> dedupe -> route -> side effect -> notify
- schedule trigger -> fetch delta -> chunk -> process -> aggregate -> publish summary
- chat or form intake -> classify -> tool branch -> approval -> commit action

## Anti-patterns

- mixing ingestion, business logic, and irreversible writes in the first nodes
- giant “god workflows” with repeated logic instead of sub-workflows
- hidden operational state spread across expressions instead of explicit data

## Pairing guidance

- pair with `n8n-node-configurator` for node specifics
- pair with `n8n-validation-repair` once the topology exists
- pair with `n8n-source-control-release` before promotion

