# Integration Decision Matrix

## Prefer built-in nodes when

- the required operation is supported
- auth is straightforward
- payload shape is predictable

## Prefer HTTP Request when

- native node lacks the needed operation
- custom headers or undocumented endpoints are required
- rollout speed matters more than node convenience

## Prefer community or custom nodes when

- the integration is strategic and repeatedly reused
- workflow-only HTTP wrappers are creating too much repeated complexity

