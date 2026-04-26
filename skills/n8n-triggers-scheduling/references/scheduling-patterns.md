# Scheduling Patterns

## Trigger classes

- Push: Webhook, MCP Server Trigger, app-specific triggers
- Pull: polling app nodes, HTTP Request plus schedule, database delta scans
- Human-driven: Form Trigger, Chat Trigger, Manual Trigger
- File-driven: Local File Trigger or storage event patterns

## Design checklist

- exact-once is unavailable unless you design for it
- dedupe key source
- retry window
- replay path
- timezone source of truth
- backfill strategy

## Common failure modes

- cron runs in the wrong timezone
- queue backlog makes a “5 minute” trigger effectively much slower
- test trigger success hides production auth or ingress problems
- polling without cursor state causes duplicates

