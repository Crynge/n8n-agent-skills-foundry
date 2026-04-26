# Queue and Capacity

## What to inspect

- execution latency
- queue wait time
- worker CPU and memory pressure
- webhook ingress fan-in
- long-lived connection routing

## MCP-specific note

Official docs warn that MCP Server Trigger traffic should be routed to a single dedicated webhook replica when using multiple webhook replicas, otherwise SSE and streamable HTTP connections can break.

## Scaling traps

- batching too late
- retry storms after upstream outages
- one noisy workflow starving others
- sticky long-lived transports routed incorrectly

