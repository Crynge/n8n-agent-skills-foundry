---
name: n8n-code-python
description: Python Code node skill for n8n. Use when Python is specifically required, while accounting for environment limitations, standard-library-only expectations, return shape rules, and workflow-safe transformations.
---

# n8n Code Python

Use this skill only when Python is specifically requested or genuinely improves clarity.

## Quick workflow

1. Confirm Python is actually needed.
2. Check environment limitations before proposing imports.
3. Use the simplest data access pattern that matches node mode.
4. Return the correct n8n item structure.
5. Keep the logic deterministic and testable.

## Core rules

- Default to JavaScript unless Python is clearly better.
- Assume standard-library-first constraints.
- Avoid pseudocode that depends on unavailable third-party packages.
- Document workarounds when a missing library changes the approach.

## Strong use cases

- regex-heavy parsing
- hashing and signatures
- compact datetime and statistics tasks
- text normalization

## Weak use cases

- HTTP-heavy pipelines
- data science logic expecting pandas or numpy
- logic that relies on external package ecosystems

## Common traps

- assuming `requests` is available
- returning non-item structures
- mixing per-item and batch semantics
- losing linkage expectations downstream

## Deep references

- Python environment and limitation notes: [references/python-limits.md](references/python-limits.md)
