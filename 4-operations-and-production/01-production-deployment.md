# Section 4.1: Deploying Containers in Production

Production deployment is not just "run the same container somewhere else." It adds reliability, repeatability, observability, and recovery requirements.

## Core Mindset Shift

In learning mode, success often means:

- the container starts
- the app responds
- you can inspect it manually

In production, success also means:

- deployments are repeatable
- versions are controlled
- logs and metrics are visible
- secrets are handled safely
- failures are expected and recoverable

## Practices To Adopt Early

### Pin Image Versions

Prefer:

```yaml
image: postgres:16-alpine
```

Instead of:

```yaml
image: postgres:latest
```

Version pinning makes rollbacks and debugging much easier.

### Separate Configuration From The Image

Use environment variables, env files, or a proper secret manager depending on the environment.

Do not bake environment-specific values into the image.

### Use Healthchecks

Healthchecks help systems know whether a container is actually ready.

Example:

```yaml
healthcheck:
  test: ["CMD-SHELL", "pg_isready -U appuser -d appdb"]
  interval: 10s
  timeout: 5s
  retries: 5
```

### Think In Replaceable Containers

A production container should ideally be disposable:

- stop it
- replace it
- run the same image again

If important data disappears when the container is replaced, that data probably belongs in a volume, database, or object store.

### Plan Logging and Monitoring

At minimum, know:

- where logs go
- how to inspect a failing container
- how to tell whether a service is healthy

### Minimize Public Exposure

Only publish the ports that truly need external access.

For example:

- a web app may need a public port
- a database often should not be publicly exposed

## Practical Checklist For Small Production Setups

- [ ] images use explicit versions
- [ ] secrets are not hard-coded in the repo
- [ ] persistent data uses volumes or managed services
- [ ] healthchecks exist where appropriate
- [ ] logs are accessible
- [ ] unnecessary ports are not published
- [ ] restart behavior is defined intentionally

## Mini Quiz

1. Why is `latest` a poor production tag?
2. Why is a healthcheck different from "the container is running"?
3. Which kinds of data should live outside a replaceable container?

## Next Step

Continue to [`02-portainer-operations.md`](./02-portainer-operations.md).
