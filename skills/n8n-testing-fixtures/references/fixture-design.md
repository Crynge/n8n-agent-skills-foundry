# Fixture Design

## Include

- nominal case
- missing field case
- duplicate event case
- stale data case
- partial downstream outage case

## Avoid

- fabricated payloads that ignore real nesting
- secrets left in headers or bodies
- “one record only” test sets for workflows that normally process batches

## Best use

- store small canonical fixtures
- add one fixture whenever an incident reveals a new shape

