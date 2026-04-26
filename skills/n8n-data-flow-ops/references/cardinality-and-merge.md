# Cardinality and Merge

## Questions to answer

- does this node operate on one item or many
- when does an array become separate items
- what output cardinality will the next node expect

## Merge risk patterns

- asymmetric branches
- one branch empty, one branch many
- duplicate join keys
- manual Code node aggregation before merge

## Recommended checks

- trace sample counts after each branch
- validate branch outputs before merge
- preserve lineage if later audits matter

