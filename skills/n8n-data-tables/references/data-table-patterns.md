# Data Table Patterns

## Strong uses

- evaluation datasets
- lightweight workflow state
- temporary routing registries
- operator-visible control tables

## Weak uses

- high-contention transactional writes
- complex relational reporting
- heavy analytics that belong in a database or warehouse

## Design checklist

- primary lookup key
- update semantics
- cleanup interval
- role visibility

