# Module 6: Data Engineering Example

This module shows how Docker can support a realistic local setup for data work without becoming an overly large platform project.

## Learning Goal

By the end of this module, you should be able to explain how Docker helps create a reproducible local data environment with:

- a relational database
- object storage
- a lightweight UI for inspection
- a notebook-style workspace

## Why This Example

A lot of Docker tutorials stop at Nginx or Redis. Those are useful, but they do not always connect naturally to a data workflow.

This module gives you a more relevant example:

- `postgres`: structured data and metadata
- `minio`: S3-compatible object storage for files and datasets
- `adminer`: quick database inspection
- `notebook`: a workspace for experiments and analysis

## Sections

| Section | Focus |
| --- | --- |
| [`01-local-platform-overview.md`](./01-local-platform-overview.md) | Why this stack is useful |
| [`02-running-the-stack.md`](./02-running-the-stack.md) | How to start and inspect the example |

## Lab Location

```text
6-data-engineering-example/labs/local-data-platform/
├── .env.example
└── compose.yml
```

## Mini Quiz

1. Why is Docker helpful for local data setups with multiple services?
2. What role does object storage play in a data platform?
3. Why is a Compose file helpful for a stack like this?

## Next Step

Start with [`01-local-platform-overview.md`](./01-local-platform-overview.md).
