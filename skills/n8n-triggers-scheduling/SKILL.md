---
name: n8n-triggers-scheduling
description: Use for trigger design, schedules, polling strategy, cron correctness, webhook-vs-poll tradeoffs, trigger deduplication, and production-safe event intake in n8n.
---

# n8n Triggers Scheduling

Use this skill when the workflow’s reliability depends on how it starts.

## Quick workflow

1. Identify the event source and delivery guarantees.
2. Choose push, poll, cron, manual, chat, or file-based trigger mode.
3. Design dedupe and replay handling before downstream writes.
4. Confirm timezone, daylight saving, and missed-run behavior.
5. Validate production trigger behavior separately from editor test behavior.

## Use this skill when

- picking between Webhook, Schedule Trigger, Chat Trigger, Form Trigger, Local File Trigger, or polling nodes
- tuning cadence, backfill, or catch-up behavior
- handling duplicate or late events

## Core rules

- Trigger choice is a systems design decision.
- Fast polling is not a substitute for proper event delivery.
- Cron correctness is useless if idempotency is absent.
- Production and test trigger URLs can behave differently.

## Deep references

- scheduling patterns: [references/scheduling-patterns.md](references/scheduling-patterns.md)

