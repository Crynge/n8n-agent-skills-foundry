---
name: n8n-observability-debug
description: Observability and debugging skill for n8n. Use for executions, workflow history, execution data, published-version drift, log streaming, insights, alerting, and production incident diagnosis.
---

# n8n Observability Debug

Use this skill when the workflow passed construction but fails under real load or in production.

## Quick workflow

1. Identify the exact execution surface that failed.
2. Compare editor state, published state, and workflow history.
3. Inspect execution data at the branch or node boundary where divergence begins.
4. Correlate with logs, concurrency, and trigger timing.
5. Add instrumentation or alerts before closing the incident.

## Core rules

- Manual success is not equivalent to production success.
- Published-version drift is a common hidden cause.
- Observability should exist before incidents, not only after them.
- Treat empty output, duplicate output, and delayed output as separate failure classes.

## Current n8n surfaces this skill covers

- executions
- workflow history
- execution data
- log streaming
- insights
- save and publish behavior

## Pairing guidance

- pair with `n8n-validation-repair` for schema or topology issues
- pair with `n8n-source-control-release` for environment-specific divergence

## Deep references

- incident taxonomy and instrumentation: [references/incident-taxonomy.md](references/incident-taxonomy.md)
