# Recovery Patterns

## Retry only when

- the upstream operation is transient
- the action is idempotent or deduped
- repeated delay is acceptable

## Prefer alternate handling when

- external writes may already have succeeded
- partial downstream state is unknown
- legal or financial operations need review

## Useful recovery designs

- dead-letter tables
- operator review queues
- compensating actions
- delayed reprocessing with dedupe keys

