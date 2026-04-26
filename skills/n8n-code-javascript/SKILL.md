---
name: n8n-code-javascript
description: JavaScript Code node skill for n8n. Use for item access, transformation logic, loop state, $helpers usage, HTTP requests, DateTime handling, pairedItem preservation, and runtime-safe return shapes.
---

# n8n Code JavaScript

Use this skill for JavaScript in Code nodes.

## Quick workflow

1. Confirm whether the node runs once for all items or once per item.
2. Select the correct input accessor.
3. Preserve item linking if downstream nodes depend on it.
4. Return the exact structure n8n expects.
5. Keep side effects minimal inside Code nodes.

## Core rules

- Prefer JavaScript over Python for most n8n Code node work.
- Respect execution mode and return shape.
- Keep HTTP calls and retries explicit when using `$helpers`.
- Preserve `pairedItem` metadata when the workflow requires traceable lineage.

## What to watch closely

- array-vs-single-item confusion
- returning plain objects instead of `[{ json: ... }]`
- mutating shared objects across items
- losing binary payload references
- hidden timezone assumptions in date logic

## Good use cases

- structured transforms
- enrichment with lightweight helper calls
- custom reducers or aggregations
- cross-item summary generation

## Bad use cases

- replacing straightforward expression logic
- embedding large business-rule engines that deserve a service layer
- hiding credentials in code

