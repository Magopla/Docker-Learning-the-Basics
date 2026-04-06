# Section 5.1: Local Data Platform Overview

This example is not meant to be a full production platform. It is meant to show how Docker can create a useful, repeatable local environment for data work.

## Services In The Example

### PostgreSQL

PostgreSQL is included to represent:

- warehouse-like structured data
- metadata storage
- SQL experimentation

### MinIO

MinIO is included to represent:

- object storage
- data lake style file storage
- S3-compatible local development workflows

### Adminer

Adminer gives you a quick way to inspect the PostgreSQL service in a browser.

### Notebook

The notebook service represents a workspace for:

- data exploration
- quick transformations
- testing connectivity to local services

## Why This Is A Good Docker Example

This stack brings together several important Docker ideas:

- multiple services in one Compose file
- published ports for selected tools
- named volumes for persistence
- environment-driven configuration
- service-to-service communication on a shared network

## What To Notice

As you work through the stack, pay attention to:

- which services need published ports
- which services need persistent data
- which service names become hostnames on the network
- which values belong in `.env`

## Next Step

Continue to [`02-running-the-stack.md`](./02-running-the-stack.md).
