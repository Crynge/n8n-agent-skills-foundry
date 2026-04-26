---
name: n8n-ai-builder
description: Advanced AI workflow skill for n8n. Use for agent and chain design, Chat Trigger flows, memory, vector retrieval, MCP-enabled tools, tool routing, human fallback, and cluster-node composition.
---

# n8n AI Builder

Use this skill for modern AI workflows in n8n.

## Quick workflow

1. Decide chain vs agent.
2. Decide whether memory is needed and how it should persist.
3. Define tool boundaries and tool-call risk.
4. Add retrieval, evaluation, and fallback strategy before calling the workflow done.
5. Make approval points explicit for side-effecting tools.

## Core rules

- Not every AI workflow should be an agent.
- Memory is a product choice, not a default.
- Retrieval quality and prompt routing matter more than prompt verbosity.
- Human fallback is part of system design, not an optional polish step.

## Current n8n surfaces this skill covers

- Chat Trigger
- AI Transform
- Evaluation and Evaluation Trigger
- Guardrails
- MCP Client
- MCP Server Trigger
- cluster-node based agent composition

## Strong patterns

- classify -> retrieve -> answer -> evaluate
- chat -> tool selection -> approval -> tool execution -> summarize
- ingest docs -> chunk -> embed -> store -> retrieve -> cite

## Failure patterns

- agent used where a deterministic chain is enough
- no evaluation dataset
- no memory truncation or cleanup plan
- unsafe tool calls without approval boundaries

