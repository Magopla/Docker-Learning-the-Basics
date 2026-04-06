# Lesson 1.2: Images, Containers, Registries, and Tags

These four terms are the basic vocabulary of Docker. If they are clear, the rest of Docker becomes much easier.

## Image

An image is a reusable template for creating containers.

You can think of it as:

- the packaged filesystem
- the runtime environment
- the default command and metadata

Examples:

- `nginx:alpine`
- `python:3.12-slim`
- `postgres:16-alpine`

Important properties of images:

- they are read-only once built
- they are versioned using tags
- they can be pulled from a registry

## Container

A container is a running or stopped instance of an image.

If an image is the template, the container is the actual thing created from it.

Examples:

- image: `nginx:alpine`
- container name: `web`

This command uses an image to create a container:

```bash
docker run -d --name web nginx:alpine
```

In that example:

- `nginx:alpine` is the image
- `web` is the container

## Registry

A registry stores and distributes images.

Common registries:

- Docker Hub
- GitHub Container Registry
- Amazon ECR
- Google Artifact Registry

When you run `docker pull nginx:alpine`, Docker fetches that image from a registry if it is not already present locally.

## Tag

A tag identifies a specific version or variant of an image.

Examples:

- `nginx:latest`
- `nginx:1.27`
- `python:3.12-slim`
- `postgres:16-alpine`

The part after the colon is the tag.

Why tags matter:

- they help reproducibility
- they communicate intent
- they reduce surprise when environments are rebuilt later

## Why `latest` Can Be Risky

`latest` is convenient for learning, but it is not a stable version pin.

For repeatable environments, prefer specific tags such as:

- `postgres:16-alpine`
- `python:3.12-slim`
- `nginx:1.27-alpine`

## How These Pieces Fit Together

Typical flow:

1. Pull an image from a registry.
2. Create and run a container from that image.
3. Inspect logs, ports, volumes, and environment.
4. Stop and remove the container when finished.

Example:

```bash
docker pull nginx:alpine
docker run -d --name web -p 8080:80 nginx:alpine
docker ps
docker stop web
docker rm web
```

## Summary Table

| Term | Meaning | Example |
| --- | --- | --- |
| Image | Reusable template | `nginx:alpine` |
| Container | Instance of an image | `web` |
| Registry | Place where images are stored | Docker Hub |
| Tag | Version or variant label | `alpine` |

## Next Step

Continue to [`03-architecture.md`](./03-architecture.md).
