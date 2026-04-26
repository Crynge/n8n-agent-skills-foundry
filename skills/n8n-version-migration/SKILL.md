---
name: n8n-version-migration
description: Use for n8n upgrades, workflow migration risk review, node deprecations, editor/runtime behavior changes, and controlled rollout planning across versions and environments.
---

# n8n Version Migration

Use this skill when the challenge is change across versions, not just current configuration.

## Quick workflow

1. Identify the current and target version boundaries.
2. List affected nodes, enterprise features, and deployment assumptions.
3. Review deprecations, auth changes, and runtime behavior changes.
4. Test representative workflows before broad rollout.
5. Stage migration and rollback plans explicitly.

## Core rules

- n8n upgrades are operational events.
- A version bump can change node behavior, credential behavior, or infrastructure assumptions.
- High-value workflows deserve targeted migration checks, not only general smoke tests.
- Rollback should be designed before upgrade windows begin.

## Deep references

- migration and compatibility notes: [references/migration-playbook.md](references/migration-playbook.md)

