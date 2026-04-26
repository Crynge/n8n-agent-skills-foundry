# Binary Handling

## Core checks

- binary property name
- MIME type
- file size
- temporary storage behavior
- retention or cleanup path

## Common issues

- downstream node expects `data` but upstream used a custom property
- AI or parser nodes receive text when they expected binary
- large file loops exhaust worker memory
- local path assumptions fail in containerized deployments

## Recommended patterns

- upload early when files are large
- transform metadata separately from file content
- avoid repeated binary duplication across branches

