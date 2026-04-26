---
name: n8n-node-configurator
description: Operation-aware node configuration skill for n8n. Use for selecting the correct operation, field dependencies, hidden options, pagination, binary handling, AI sub-node wiring, and credential expectations.
---

# n8n Node Configurator

Use this skill when the hard part is not the workflow shape, but the exact node configuration.

## Quick workflow

1. Confirm the node and operation.
2. Identify required fields and dependent fields.
3. Check auth mode, body mode, response mode, and pagination behavior.
4. Validate against realistic sample input.
5. Confirm output shape for the next node.

## Core rules

- Choose operation before filling fields.
- Dependent parameters often hide behind booleans or mode switches.
- Paginated APIs need explicit continuation handling, not optimistic assumptions.
- Binary, file, and HTML nodes deserve output-shape checks before downstream mapping.

## Use this skill when

- HTTP Request setup is confusing
- an AI cluster node needs sub-node attachments
- a node has several operations with different schemas
- a trigger works in test mode but not in production mode

## High-risk areas

- body serialization mode
- pagination termination
- binary property naming
- file path behavior
- tool sub-node placement for AI agents
- credential type mismatch

## Pairing guidance

- pair with `n8n-webhooks-api` for API-facing nodes
- pair with `n8n-ai-builder` for agent clusters
- pair with `n8n-credentials-security` when auth setup is involved

