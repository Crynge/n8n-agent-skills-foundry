# Forms and Chat Patterns

## Good patterns

- short guided forms with validation before side effects
- chat intake followed by structured confirmation
- progressive disclosure for optional fields

## Common failures

- form accepts ambiguous free text where structured choices are needed
- chat trigger calls tools with no user confirmation
- error messages reveal internal workflow details instead of next steps

## Design questions

- what does the user see on success
- what happens if downstream systems are slow
- how does the workflow ask for missing information

