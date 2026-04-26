---
name: n8n-data-tables
description: Use for Data Table design, row operations, schema choices, evaluation datasets, lightweight workflow state, and internal data products built on n8n data tables.
---

# n8n Data Tables

Use this skill when Data Table is the right storage primitive.

## Quick workflow

1. Decide whether Data Table is state, dataset, cache, or reporting surface.
2. Design row keys and schema intentionally.
3. Plan read/write patterns and cardinality.
4. Review concurrency, cleanup, and table lifecycle.
5. Validate whether a database or sheet would be a better fit.

## Core rules

- Data Tables are useful, but they are not a free replacement for databases.
- Row identity and update semantics should be explicit.
- Evaluation datasets benefit from deliberate column design.
- Table lifecycle and cleanup matter in long-running automations.

## Deep references

- Data Table design notes: [references/data-table-patterns.md](references/data-table-patterns.md)

