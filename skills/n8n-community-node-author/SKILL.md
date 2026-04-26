---
name: n8n-community-node-author
description: Use for building, packaging, testing, and publishing n8n community nodes. Covers node scaffolding, verification constraints, provenance-aware publishing, UX expectations, and safe dependency choices.
---

# n8n Community Node Author

Use this skill when the right solution is a custom or community node instead of a workflow-only pattern.

## Quick workflow

1. Confirm a workflow-level solution is insufficient.
2. Scope node capabilities and credential model.
3. Scaffold the node cleanly.
4. Lint, test, and document it.
5. Publish using the current verified-node process.

## Core rules

- Prefer workflow composition over node authoring unless reuse or UX clearly justifies a node.
- Follow n8n verification guidelines from the start.
- Keep the dependency graph conservative.
- Publish from GitHub Actions with provenance when targeting verification.

## Current publishing requirement

For verified community nodes, official docs state that from May 1, 2026 publishing must use GitHub Actions with a provenance statement.

## Strong deliverables

- clear node operations
- predictable credential UX
- minimal permissions
- tests and examples
- provenance-aware release workflow

