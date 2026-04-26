---
name: n8n-mcp-toolsmith
description: Master skill for using n8n MCP tooling safely and efficiently. Use before any n8n MCP call, node search, validation loop, workflow CRUD, credential management, data tables operation, or instance audit.
---

# n8n MCP Toolsmith

Use this skill as the first hop before any n8n MCP interaction.

## Quick workflow

1. Search the node, template, or credential type first.
2. Fetch only the node detail level needed for the task.
3. Validate config before mutating a live workflow.
4. Use workflow-level updates only after the node-level shape is correct.
5. Re-run validation after each structural edit.

## Use this skill when

- finding the correct node or operation
- converting between node type naming formats
- using workflow CRUD tools
- managing credentials or data tables
- auditing an n8n instance

## Core rules

- Treat `search -> inspect -> validate -> update -> validate` as the default control loop.
- Preserve a distinction between node-search formats and workflow-runtime formats if your MCP server uses both.
- Avoid loading full schemas unless a standard detail view is insufficient.
- Prefer targeted partial updates over rewriting entire workflows.

## High-risk mistakes

- using the wrong `nodeType` namespace between discovery tools and workflow mutation tools
- skipping validation because the node “looks right”
- assuming auto-fix will correct broken topology or semantic errors
- updating active workflows without checking published version behavior

## Operational guidance

- Use instance audit tools before recommending security posture changes.
- Inspect credential schema before creating credentials programmatically.
- For data tables, confirm column schema and write-path assumptions before bulk inserts.
- For AI workflows, search cluster root nodes and required sub-node relationships before suggesting a topology.

## What good looks like

- the tool call sequence is minimal
- every mutation is followed by validation
- the workflow is changed surgically instead of rebuilt blindly
- the assistant explains why a node or template was chosen

## Deep references

- MCP surfaces and operational notes: [references/mcp-surfaces.md](references/mcp-surfaces.md)
