---
name: n8n-files-binary
description: Use for binary data, file ingestion, local and remote file movement, MIME handling, document pipelines, image/audio flows, and storage-safe binary patterns in n8n.
---

# n8n Files Binary

Use this skill when file payloads are part of the workflow.

## Quick workflow

1. Identify where binary data enters the workflow.
2. Confirm binary property naming and downstream expectations.
3. Decide whether content stays binary, becomes text, or is uploaded to storage.
4. Validate memory footprint and persistence implications.
5. Protect cleanup, retention, and data-loss edges.

## Core rules

- Binary payload handling should be explicit at each boundary.
- Large files change workflow performance characteristics.
- Text extraction and storage uploads are separate concerns.
- File paths and local disk behavior need environment-aware assumptions.

## Deep references

- binary and file patterns: [references/binary-handling.md](references/binary-handling.md)

