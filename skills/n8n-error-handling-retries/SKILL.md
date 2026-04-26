---
name: n8n-error-handling-retries
description: Use for retry policy, error workflow design, compensating actions, dead-letter patterns, fallback handling, and side-effect-safe recovery in n8n.
---

# n8n Error Handling Retries

Use this skill when workflow resilience depends on how failures are handled.

## Quick workflow

1. Classify failures by recoverability.
2. Separate transient failures from semantic failures.
3. Place retries only where replay is safe.
4. Design compensation or dead-letter paths for unsafe repeats.
5. Make incident visibility part of the recovery design.

## Core rules

- Retrying writes is not automatically safe.
- A failed workflow needs a next state, not just a logged error.
- Error workflows should preserve enough context to repair the incident.
- Human review is often the right recovery path for ambiguous side effects.

## Deep references

- recovery and retry patterns: [references/recovery-patterns.md](references/recovery-patterns.md)

