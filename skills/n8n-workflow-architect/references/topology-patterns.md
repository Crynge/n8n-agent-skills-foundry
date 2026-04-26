# Topology Patterns

## Common shapes

- intake -> normalize -> route -> act -> observe
- schedule -> fetch delta -> process batch -> summarize
- chat -> classify -> tool path -> approval -> commit
- trigger -> sub-workflow -> reconcile -> publish

## Split criteria

- ownership boundary
- reuse need
- different retry semantics
- different deployment cadence

## Review questions

- where do side effects begin
- where is idempotency enforced
- how does the workflow recover mid-run

