---
name: n8n-webhooks-api
description: Skill for webhook, API, auth, and request-response design in n8n. Use for inbound webhooks, outbound HTTP calls, OAuth/API key patterns, HMAC verification, idempotency, and response shaping.
---

# n8n Webhooks API

Use this skill for workflows that ingest or call APIs.

## Quick workflow

1. Define the contract at the boundary.
2. Decide sync response vs async processing.
3. Validate auth, signatures, and replay protection.
4. Normalize payload shape immediately.
5. Apply idempotency before side effects.

## Core rules

- Webhook trust boundaries should be explicit.
- Signature verification belongs early.
- Async acknowledgement is safer for slow downstream work.
- HTTP Request nodes need predictable retry and pagination handling.

## Use this skill when

- designing webhook intake workflows
- using OAuth, API keys, or signed requests
- responding to callers with structured payloads
- debugging headers, body modes, or auth failures

## High-risk mistakes

- assuming test URLs and production URLs behave identically
- doing irreversible side effects before dedupe
- ignoring rate limits and pagination
- treating API auth as a node concern only, instead of a workflow concern

## Pairing guidance

- pair with `n8n-node-configurator` for exact node settings
- pair with `n8n-credentials-security` for auth posture

## Deep references

- boundary and auth patterns: [references/api-boundary-patterns.md](references/api-boundary-patterns.md)
