---
name: n8n-source-control-release
description: Deployment and change-management skill for n8n. Use for source control, environments, workflow promotion, publish strategy, rollback posture, release checklists, and Git-backed collaboration.
---

# n8n Source Control Release

Use this skill when workflows move from local editing into shared or production environments.

## Quick workflow

1. Determine draft vs published behavior.
2. Confirm environment mapping and secret mapping.
3. Review source-control boundaries and promotion path.
4. Validate rollout and rollback procedures.
5. Publish only after operational checks are complete.

## Core rules

- Draft edits are not production changes until published.
- Promotion should be reproducible, not artisanal.
- Rollback paths should exist before high-risk deployments.
- Git state and workflow history solve different problems.

## Key topics

- source control and environments
- compare workflow changes
- copy work between environments
- workflow history vs execution history
- promotion checklists
- release notes for workflow changes

## Common mistakes

- assuming autosave means live
- promoting without environment-specific credential review
- ignoring version naming and change traceability

