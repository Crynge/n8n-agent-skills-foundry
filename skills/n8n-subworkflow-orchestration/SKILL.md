---
name: n8n-subworkflow-orchestration
description: Use for Execute Sub-workflow patterns, modular workflow boundaries, reuse, orchestration, call semantics, handoff contracts, and nested workflow reliability in n8n.
---

# n8n Subworkflow Orchestration

Use this skill when workflows start becoming systems instead of single flows.

## Quick workflow

1. Decide whether logic deserves its own workflow boundary.
2. Define input and output contracts between parent and child workflows.
3. Decide sync, async, or event-driven invocation semantics.
4. Isolate retries and side effects per boundary.
5. Trace failures across workflow hops.

## Core rules

- A sub-workflow should encapsulate a stable capability.
- Workflow boundaries are also permission and ownership boundaries.
- Nested orchestration needs explicit contracts, not implied field names.
- Avoid distributing one transaction across many nested workflows.

## Deep references

- orchestration patterns: [references/orchestration-patterns.md](references/orchestration-patterns.md)

