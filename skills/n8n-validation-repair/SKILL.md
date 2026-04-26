---
name: n8n-validation-repair
description: Use when n8n validation fails or workflows break at runtime. Covers node validation loops, false positives, topology repair, runtime-vs-editor differences, and safe remediation sequencing.
---

# n8n Validation Repair

Use this skill when a workflow is broken, suspicious, or inconsistent across environments.

## Quick workflow

1. Reproduce the exact error surface.
2. Separate node-config errors from topology errors.
3. Fix required-field and type failures first.
4. Then fix cardinality, branch, or merge issues.
5. Re-run validation and confirm execution behavior, not just schema acceptance.

## What this skill optimizes for

- faster root cause isolation
- fewer invalid trial-and-error edits
- cleaner distinction between editor issues and production issues

## Core rules

- Always preserve the latest failing state before aggressive repairs.
- A passing validator does not guarantee a correct runtime result.
- Fix one class of failure at a time.
- Re-check published workflow state after editor fixes.

## Common failure families

- missing required parameters
- wrong field type or enum value
- operator metadata mismatch in IF or Switch-like nodes
- merge misalignment and empty-branch behavior
- broken item linking after a Code node
- credential mismatch that looks like a node failure

## Repair strategy

- use node-level validation before full workflow validation
- use auto-fix only for known structural cleanup, not semantic repair
- if runtime still fails, inspect execution data and branch behavior next

## When to escalate

- move to `n8n-observability-debug` if the schema is clean but executions diverge
- move to `n8n-source-control-release` if the issue appears only after promotion

