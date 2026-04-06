# Section 5.2: Local, Dev, and Production Environments

This section explains how Docker can support the same product across multiple environments without making them identical in every detail.

## The Three Environments In This Example

### Local Development

This is where a developer works during the sprint.

Typical characteristics:

- bind mounts for fast iteration
- hot reload if the framework supports it
- developer-friendly ports
- more direct inspection and experimentation

### Shared Dev Environment

This environment is closer to an integration or QA area.

Typical characteristics:

- built image is deployed, not bind-mounted source code
- environment variables are set for the dev area
- teammates can validate the sprint work together
- image tag comes from CI

### Production

This is the stable environment used by real consumers.

Typical characteristics:

- same tested image, promoted from earlier stages
- production-specific config and secrets
- restart behavior and healthchecks matter more
- fewer exposed ports and less debugging access

## What Should Stay Consistent

Across dev and prod, the most important thing to keep stable is the image itself.

That way:

- code does not drift between environments
- tested dependencies stay the same
- rollbacks are easier

## What Should Differ

It is normal for these values to change by environment:

- `APP_ENV`
- database hostnames
- external API endpoints
- secrets
- public ports
- resource settings

## How Docker Helps

Docker and Compose make this easier by separating:

- the built image
- the runtime configuration

That is why this module includes:

- `compose.local.yml`
- `compose.dev.yml`
- `compose.prod.yml`

Each file is for a different stage in the product lifecycle.

## Mini Quiz

1. Why are bind mounts more common in local development than in production?
2. Why should production usually avoid relying on source-code mounts?
3. What is the main benefit of deploying the same image tag to dev and prod?

## Next Step

Continue to [`03-jenkins-pipeline.md`](./03-jenkins-pipeline.md).
