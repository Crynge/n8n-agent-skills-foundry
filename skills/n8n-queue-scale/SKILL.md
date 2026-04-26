---
name: n8n-queue-scale
description: Use for queue mode, worker scaling, concurrency, webhook replicas, backpressure, latency analysis, and capacity-aware n8n workflow design.
---

# n8n Queue Scale

Use this skill when workflow reliability depends on throughput, concurrency, or deployment topology.

## Quick workflow

1. Identify whether the issue is latency, throughput, backlog, or unstable connections.
2. Map execution mode, worker topology, and webhook topology.
3. Separate trigger bottlenecks from worker bottlenecks.
4. Evaluate concurrency and queue side effects per workflow class.
5. Design for degraded behavior, not only peak success.

## Core rules

- Scaling n8n changes behavior, not just performance.
- Long-lived transports like SSE need topology-aware routing.
- Queue backlog can invalidate timing assumptions in downstream systems.
- High concurrency without idempotency magnifies bad writes.

## Deep references

- queue and capacity notes: [references/queue-and-capacity.md](references/queue-and-capacity.md)

