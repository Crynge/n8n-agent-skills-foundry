---
name: n8n-evals-guardrails
description: Evaluation and guardrail skill for n8n AI workflows. Use for light evaluations, metric design, approval gates, output checking, risk segmentation, fallback strategy, and safe tool execution.
---

# n8n Evals Guardrails

Use this skill when an AI workflow needs to be trustworthy, not merely impressive.

## Quick workflow

1. Define failure classes.
2. Build a small but representative evaluation dataset.
3. Wire evaluation triggers and output capture.
4. Add approval or block conditions for unsafe actions.
5. Review outputs and convert repeated failures into workflow changes.

## Core rules

- A working demo without evals is not production evidence.
- Separate factual quality, format quality, and action safety.
- Add human approval before side effects that change external systems.
- Make fallback behavior a first-class output path.

## Recommended controls

- light evaluations for quick iteration
- metric-based evaluation when examples scale
- schema validation for structured outputs
- allowlist and denylist checks for tool parameters
- “safe to execute” gates before external writes

## Pairing guidance

- pair with `n8n-ai-builder` for overall design
- pair with `n8n-observability-debug` for execution-level debugging

