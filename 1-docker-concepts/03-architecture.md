# Lesson 1.3: Docker Architecture

This lesson explains what happens between the command you type and the container you see running.

## The Main Pieces

At a high level, Docker has four pieces worth remembering:

| Piece | Role |
| --- | --- |
| Docker client | The `docker` CLI you type into |
| Docker daemon | The background service that does the work |
| Docker objects | Images, containers, networks, and volumes |
| Registry | External storage for images |

## Client vs Daemon

When you run a command like:

```bash
docker run nginx:alpine
```

the CLI does not run the container by itself.

Instead:

1. the Docker client sends a request
2. the Docker daemon receives it
3. the daemon checks whether the image exists locally
4. if needed, it pulls the image from a registry
5. the daemon creates and starts the container

That client/daemon split explains many common beginner issues, especially:

- the daemon is not running
- the client exists but cannot connect
- permissions around the Docker socket

## Docker Objects

The daemon manages the objects you work with every day:

- images
- containers
- networks
- volumes

You can think of them like this:

- image: what to run
- container: the running instance
- network: how containers talk
- volume: where persistent data lives

## Registry In The Architecture

Registries sit outside your machine and store images.

Common example:

```bash
docker pull postgres:16-alpine
```

If that image is not cached locally, the daemon downloads it from a registry such as Docker Hub.

## The Docker Socket

On many systems, the client talks to the daemon through the Docker socket:

```text
/var/run/docker.sock
```

This matters because anything with access to that socket can often control Docker on the host.

That is why tools like Portainer can manage containers when they mount the socket, and also why that access should be treated carefully.

## Docker Desktop Note

On macOS and Windows, Docker Desktop provides a local Docker environment and hides some Linux-specific details behind the scenes.

For learning, that means:

- you can use normal Docker commands
- images, containers, and volumes are managed by Docker Desktop
- the conceptual model stays the same even if the implementation is slightly different from Linux

## Summary

- The CLI sends requests.
- The daemon performs the work.
- Registries store images.
- Images, containers, networks, and volumes are the main Docker objects.
- Socket access is powerful and should be treated as privileged access.

## Next Step

Continue to [`../2-setup/README.md`](../2-setup/README.md).
