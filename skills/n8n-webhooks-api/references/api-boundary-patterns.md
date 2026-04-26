# API Boundary Patterns

## Intake sequence

- authenticate or verify signature
- normalize payload
- dedupe
- enqueue or continue
- respond

## Outbound sequence

- build request deterministically
- handle pagination or cursors
- classify errors
- retry only when safe

## Boundary mistakes

- synchronous responses with long downstream work
- dedupe after side effects
- response bodies that leak internal system state

