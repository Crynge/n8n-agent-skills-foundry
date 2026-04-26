---
name: n8n-credentials-security
description: Security skill for n8n credentials, secrets, access, and trust boundaries. Use for auth strategy, external secrets, least privilege, webhook trust, community node risk, and secret-handling patterns.
---

# n8n Credentials Security

Use this skill whenever a workflow touches authentication, sensitive data, or external trust boundaries.

## Quick workflow

1. Identify all secrets and external trust boundaries.
2. Prefer managed credentials over inline secrets.
3. Scope privileges narrowly.
4. Decide secret storage, rotation, and environment promotion strategy.
5. Re-check logs, execution data, and outputs for leakage risk.

## Core rules

- Secrets should not live in expressions or Code nodes unless there is no safer option.
- Least privilege beats convenience.
- Test credentials and production credentials should be isolated.
- Community nodes deserve explicit trust review.

## Current areas this skill covers

- credential management
- external secrets
- webhook auth and signing
- token rotation planning
- credential sharing risk
- instance audit posture

## High-risk mistakes

- hardcoding API keys in code
- using owner-level credentials for editor convenience
- promoting workflows across environments without secret remapping
- leaking secrets through execution logs or AI context

## Deep references

- secrets and auth patterns: [references/secrets-and-auth.md](references/secrets-and-auth.md)
