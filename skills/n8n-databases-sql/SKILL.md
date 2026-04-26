---
name: n8n-databases-sql
description: Use for database nodes, SQL patterns, transactions, pagination, cursoring, bulk operations, and database-safe workflow design in n8n.
---

# n8n Databases SQL

Use this skill when workflows read from or write to relational databases.

## Quick workflow

1. Identify the database role: source, sink, lookup, queue, or state store.
2. Choose the safest query/write pattern.
3. Decide transaction and idempotency boundaries.
4. Handle pagination, chunking, and lock contention explicitly.
5. Validate output shape and error behavior under empty and high-volume cases.

## Core rules

- A database node is a contract with concurrency and state, not just a connector.
- Bulk writes need chunk size and retry policy decisions.
- Read consistency and write idempotency should be explicit.
- Avoid making SQL the hidden workflow control plane unless it is intentionally your state store.

## Deep references

- SQL and state patterns: [references/sql-patterns.md](references/sql-patterns.md)

