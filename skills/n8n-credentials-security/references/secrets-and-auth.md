# Secrets and Auth

## Secret providers in current official docs

- 1Password via Connect Server
- AWS Secrets Manager
- Azure Key Vault
- GCP Secrets Manager
- HashiCorp Vault

## Auth review lenses

- credential scope
- token refresh model
- project-level access
- production vs non-production separation
- log exposure risk

## Common leak paths

- inline headers in expressions
- debug logging or execution replay
- AI prompt context built from credential-bearing payloads

