# Orchestration Patterns

## Good reasons to split

- reusable enrichment block
- shared approval workflow
- environment-specific side-effect wrapper
- complex AI capability reused across products

## Common traps

- parent and child both own retries
- hidden coupling through field names
- child workflows returning shapes the parent never validates
- no runbook for tracing nested failures

## Recommended contracts

- explicit input schema
- explicit output schema
- owner per workflow
- escalation rule for partial failures

