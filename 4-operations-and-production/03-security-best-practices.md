# Section 4.3: Security Best Practices

This section focuses on the most important Docker safety habits for beginners. The goal is not perfect security. The goal is avoiding the most common preventable mistakes.

## 1. Do Not Use `latest` Blindly

Security and reliability both improve when you know exactly what you are running.

Prefer explicit versions:

- `postgres:16-alpine`
- `python:3.12-slim`
- `nginx:1.27-alpine`

## 2. Keep Secrets Out Of The Repository

Avoid committing:

- passwords
- tokens
- cloud credentials
- database URLs with real secrets

For learning repos, use:

- `.env.example` with placeholder values
- a local `.env` file that is not committed

## 3. Publish Only The Ports You Need

Every published port is part of your attack surface.

Ask:

- does this service really need to be reachable from the host?
- does it need to be reachable publicly, or only internally?

## 4. Be Careful With Host Mounts

Bind mounts are powerful, but they also expose host files to containers.

Use read-only mounts where possible:

```yaml
volumes:
  - ./site:/usr/share/nginx/html:ro
```

## 5. Treat The Docker Socket As Privileged Access

Mounting:

```text
/var/run/docker.sock
```

into a container can effectively give that container broad control over Docker on the host.

That is why Portainer works well with it, and also why it should be used intentionally.

## 6. Use Minimal Images When Reasonable

Smaller images can reduce unnecessary packages and make downloads faster.

Examples:

- `python:3.12-slim`
- `postgres:16-alpine`
- `nginx:alpine`

This is not a magic security fix, but it is often a good habit.

## 7. Make Containers Replaceable

If a service depends on manual changes inside a running container, recovery becomes harder and riskier.

Safer pattern:

- configuration comes from code or env vars
- persistent data lives in volumes or external systems
- containers can be recreated consistently

## Beginner Security Checklist

- [ ] I avoid `latest` for important services
- [ ] real secrets are not committed to the repo
- [ ] published ports are intentional
- [ ] bind mounts are limited and read-only when possible
- [ ] I understand the sensitivity of the Docker socket
- [ ] I prefer smaller, purpose-fit images when practical

## Mini Quiz

1. Why is an unnecessary published port a security concern?
2. Why is a read-only bind mount safer than a writable one in many cases?
3. Why is the Docker socket considered sensitive?

## Next Step

Continue to [`../5-cicd-and-environments/README.md`](../5-cicd-and-environments/README.md).
