# Module 0: Prerequisites

This module helps you confirm that your machine is ready before you begin the actual Docker exercises.

## Learning Goal

Before continuing, you should be able to say:

- Docker is installed
- Docker Desktop or Docker Engine is running
- `docker run hello-world` works
- I know where to go if the daemon is not reachable

## System Requirements

These are practical beginner-friendly targets, not strict rules for every setup.

### macOS

| Item | Recommended |
| --- | --- |
| macOS | 13 or later |
| RAM | 8 GB or more |
| Free disk space | 15-20 GB |
| CPU | Apple Silicon or Intel |

### Linux

| Item | Recommended |
| --- | --- |
| Ubuntu | 22.04 LTS or similar modern distro |
| RAM | 4 GB or more |
| Free disk space | 15-20 GB |
| Architecture | 64-bit |

### Windows

| Item | Recommended |
| --- | --- |
| Windows | 11 with WSL2 |
| RAM | 8 GB or more |
| Free disk space | 15-20 GB |
| Virtualization | Enabled |

## Recommended Installation Path

For beginners:

- macOS: Docker Desktop
- Windows: Docker Desktop with WSL2
- Linux: Docker Engine or Docker Desktop, depending on preference

If you are on macOS, the easiest path is Docker Desktop:

1. Download it from [Docker Desktop](https://www.docker.com/products/docker-desktop/).
2. Install the correct build for your machine.
3. Launch the app and wait until Docker reports it is running.

## Verification Commands

Run these commands in a terminal:

```bash
docker --version
docker compose version
docker info | head -10
docker run hello-world
docker ps -a
```

What success looks like:

- the version commands print installed versions
- `docker info` shows client and server details
- `hello-world` prints a success message
- `docker ps -a` shows at least the completed `hello-world` container

## Common Problems

### Cannot connect to the Docker daemon

Usually Docker is installed, but not running yet.

On macOS:

```bash
open -a Docker
docker ps
```

### `docker compose` is missing

Your installation may be incomplete or outdated. Reinstall Docker Desktop or update Docker Engine and verify again with:

```bash
docker compose version
```

### Port conflict errors later in the course

This is common and not a sign that Docker is broken. It usually means another process is already using the host port you picked.

Example:

```bash
docker run -d -p 8081:80 nginx:alpine
```

## Checklist

- [ ] `docker --version` works
- [ ] `docker compose version` works
- [ ] `docker run hello-world` works
- [ ] `docker ps -a` shows the container history

## Mini Quiz

1. What does `docker info` tell you that `docker --version` does not?
2. If the CLI exists but cannot reach the daemon, what is the most likely issue?
3. Why is `hello-world` a good first test?

## Module Exercise

Before moving on, try this without checking earlier sections:

```bash
docker run -d --name prereq-nginx -p 8080:80 nginx:alpine
docker ps
docker stop prereq-nginx
docker rm prereq-nginx
```

If that works, your machine is ready for the rest of the course.

## Next Step

Continue to [`../1-docker-concepts/README.md`](../1-docker-concepts/README.md).
