# SQL Patterns

## Strong workflow uses

- delta ingestion with watermark columns
- lookup enrichment by primary or natural key
- durable queue tables with lease semantics
- audit-log append tables

## Risks

- non-deterministic pagination
- long transactions inside workflow loops
- duplicate writes after retries
- schema drift breaking mappings

## Practical guidance

- paginate on stable cursors
- separate fetch and write phases
- upsert only when the target semantics are clear
- prefer explicit conflict behavior over silent overwrite

