---
name: n8n-expression-engine
description: Use for n8n expression authoring, debugging, and data mapping. Covers $json, $node, item linking, webhook payload access, array transforms, date math, and when not to use expressions.
---

# n8n Expression Engine

Use this skill when the task is primarily about mapping or transforming data with native n8n expressions.

## Quick workflow

1. Identify the data shape at the current node boundary.
2. Confirm whether the value should come from current input, a prior node, or linked items.
3. Write the smallest correct expression.
4. Re-check behavior with arrays, nulls, and missing keys.
5. Replace expressions with Code only when native expressions become unreadable or unsafe.

## Use this skill when

- the user asks for `{{ }}` syntax
- a mapping field returns `undefined`
- webhook payload paths are unclear
- a node needs date math, string cleanup, or conditional mapping

## Core rules

- Start from the actual node execution shape, not what the upstream API docs suggest.
- Distinguish `$json`, `$item()`, `$node`, and linked-item access patterns.
- Prefer explicit fallback behavior over assuming keys always exist.
- Use Code nodes only after native expression options become too brittle.

## Common traps

- forgetting webhook payloads often sit under `body`
- referencing a prior node without understanding item linking
- using expressions to implement multi-step control flow
- mixing stringified JSON and object access

## Escalation triggers

Move to `n8n-data-flow-ops` when:

- there are branching or merge semantics involved
- the issue is not just syntax, but item-cardinality mismatch

Move to `n8n-code-javascript` when:

- the transform needs loops, reducers, or complex object reconstruction

## Deep references

- expression patterns and pitfalls: [references/expression-patterns.md](references/expression-patterns.md)
