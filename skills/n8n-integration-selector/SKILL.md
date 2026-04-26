---
name: n8n-integration-selector
description: Integration strategy skill for choosing between built-in nodes, credential-only support, HTTP Request, MCP, or community nodes. Use for app selection, auth tradeoffs, fallback planning, and connector architecture.
---

# n8n Integration Selector

Use this skill when the question is “which integration approach should we use?”

## Quick workflow

1. Check for a built-in node first.
2. Decide whether the built-in node actually supports the needed operation.
3. Compare credential-only support, HTTP Request, and community node options.
4. Evaluate auth complexity, pagination, file handling, and long-term maintenance.
5. Pick the simplest reliable option.

## Core rules

- Built-in nodes are preferred, but not automatically best.
- HTTP Request is often the clean fallback when a native node is partial.
- Community nodes require trust and maintenance review.
- A connector decision is an operational decision, not just a coding decision.

## Decision lenses

- auth support
- operation completeness
- data-shape predictability
- pagination behavior
- maintenance burden
- observability
- portability across environments

## Pairing guidance

- pair with `n8n-webhooks-api` for HTTP-heavy integrations
- pair with `n8n-credentials-security` for auth tradeoffs
- pair with `n8n-community-node-author` if a custom node becomes justified

## Deep references

- connector decision matrix: [references/integration-decision-matrix.md](references/integration-decision-matrix.md)
