---
name: n8n-data-flow-ops
description: Data-shaping and control-flow skill for n8n. Use for loops, merges, branching, split-out patterns, item linking, deduplication, batching, binary movement, and cross-branch state handling.
---

# n8n Data Flow Ops

Use this skill when the workflow’s challenge is how data moves, splits, rejoins, or accumulates.

## Quick workflow

1. Identify item cardinality at each step.
2. Decide where arrays stay arrays and where they become separate items.
3. Design loop boundaries and termination conditions.
4. Protect branch semantics through merges.
5. Re-check downstream assumptions after every shape change.

## Core rules

- Item cardinality is a first-class design decision.
- Merge semantics should be explicit, never assumed.
- Loop nodes need a clean stop condition and state boundary.
- Dedupe belongs before expensive or irreversible work.

## Common trouble spots

- Split Out followed by nodes expecting a single aggregate object
- Merge operations that silently drop or duplicate data
- Code nodes that destroy item linkage
- branch execution assumptions that differ from actual n8n behavior

## Useful mental models

- shape normalization early
- expansion in the middle
- side effects late
- reconsolidation before reporting or storage

## Deep references

- item cardinality and merge patterns: [references/cardinality-and-merge.md](references/cardinality-and-merge.md)
