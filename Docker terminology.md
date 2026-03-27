# Docker Terminology: Images, Containers, Registries, and Tags

## Core Concepts Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                      Docker Ecosystem                            │
│                                                                  │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐        │
│  │  Registry   │────▶│   Image     │────▶│  Container  │        │
│  │ (Docker Hub)│     │ (Template)  │     │ (Running)   │        │
│  └─────────────┘     └─────────────┘     └─────────────┘        │
│         │                  │                                      │
│         │                  │ Tag                                  │
│         │                  ▼                                      │
│         │           ┌─────────────┐                               │
│         │           │ nginx:1.25  │                               │
│         │           │ nginx:1.25-alpine│                          │
│         │           └─────────────┘                               │
│         │                                                        │
└─────────────────────────────────────────────────────────────────┘
```

---

## 1. Images

### What is a Docker Image?

An image is a read-only template with instructions for creating a container. It contains the application code, runtime, libraries, environment variables, and configuration files.

### Image Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Immutable** | Cannot be modified once created |
| **Layered** | Composed of multiple read-only layers |
| **Versioned** | Each change creates a new layer |
| **Portable** | Can be shared and run anywhere |

### Image Structure

```
┌─────────────────────────────────┐
│         Container Layer         │  (Writable)
├─────────────────────────────────┤
│         Application Layer       │  (e.g., Node.js app)
├─────────────────────────────────┤
│         Dependencies Layer      │  (e.g., node_modules)
├─────────────────────────────────┤
│         Runtime Layer           │  (e.g., Node.js runtime)
├─────────────────────────────────┤
│         Base Image Layer        │  (e.g., Ubuntu, Alpine)
└─────────────────────────────────┘
```

### Image Commands

```bash
# List local images
docker images
docker image ls

# Pull an image from registry
docker pull nginx:latest

# Build image from Dockerfile
docker build -t my-app:1.0 .

# Tag an image
docker tag my-app:1.0 username/my-app:1.0

# Remove an image
docker rmi nginx:latest

# Inspect image details
docker image inspect nginx:latest

# History of image layers
docker history nginx:latest

# Remove unused images
docker image prune

# Remove all unused images
docker image prune -a
```

---

## 2. Containers

### What is a Docker Container?

A container is a runnable instance of an image. It's a lightweight, standalone, executable package that includes everything needed to run the software.

### Container vs Image

| Aspect | Image | Container |
|--------|-------|-----------|
| **State** | Read-only | Read-write |
| **Purpose** | Template | Running instance |
| **Lifecycle** | Persistent | Ephemeral by default |
| **Changes** | Layers stack | Writable layer on top |

### Container Lifecycle

```
    ┌──────────┐
    │ Created  │
    └────┬─────┘
         │ docker create
         ▼
    ┌──────────┐
    │ Running  │◀─────────┐
    └────┬─────┘          │
         │                │ docker start
         │ docker run     │
         ▼                │
    ┌──────────┐          │
    │  Paused  │──────────┘
    └────┬─────┘ docker unpause
         │ docker pause
         ▼
    ┌──────────┐
    │ Stopped  │──────────┐
    └────┬─────┘          │
         │                │ docker start
         │ docker stop    │
         ▼                │
    ┌──────────┐          │
    │  Killed  │──────────┘
    └──────────┘ docker start
```

### Container Commands

```bash
# Run a container
docker run nginx:latest
docker run -d --name my-nginx -p 8080:80 nginx:latest

# Interactive container
docker run -it ubuntu bash

# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Start/Stop/Restart container
docker start my-nginx
docker stop my-nginx
docker restart my-nginx

# Remove container
docker rm my-nginx
docker rm -f my-nginx  # Force remove running container

# Inspect container
docker inspect my-nginx

# View container logs
docker logs my-nginx
docker logs -f my-nginx  # Follow logs

# Execute command in running container
docker exec -it my-nginx bash

# Pause/Unpause container
docker pause my-nginx
docker unpause my-nginx

# View container stats
docker stats

# Container resource limits
docker run -d --name small-nginx \
  --memory="256m" \
  --cpus="0.5" \
  nginx:latest
```

### Common Container Flags

| Flag | Short | Description | Example |
|------|-------|-------------|---------|
| `--name` | - | Assign container name | `--name my-app` |
| `-d` | `--detach` | Run in background | `-d` |
| `-it` | `--interactive --tty` | Interactive mode | `-it bash` |
| `-p` | `--publish` | Port mapping | `-p 8080:80` |
| `-v` | `--volume` | Volume mount | `-v /host:/container` |
| `--env` | `-e` | Environment variable | `-e NODE_ENV=prod` |
| `--network` | - | Network to join | `--network my-net` |
| `--rm` | - | Remove after exit | `--rm` |

---

## 3. Registries

### What is a Registry?

A registry is a storage and distribution system for Docker images. It hosts images and provides retrieval mechanisms.

### Registry Types

| Type | Description | Examples |
|------|-------------|----------|
| **Public Registry** | Free, open to everyone | Docker Hub, GitHub Container Registry |
| **Private Registry** | Restricted access | AWS ECR, Google GCR, self-hosted |
| **Self-hosted** | Run your own registry | Harbor, Registry |

### Popular Registries

| Registry | Provider | URL |
|----------|----------|-----|
| Docker Hub | Docker | hub.docker.com |
| GitHub Container Registry | GitHub | ghcr.io |
| Amazon ECR | AWS | aws.amazon.com/ecr |
| Google Artifact Registry | Google Cloud | cloud.google.com |
| Azure Container Registry | Microsoft Azure | azure.microsoft.com |

### Registry Commands

```bash
# Login to registry
docker login
docker login ghcr.io
docker login -u username registry.example.com

# Logout from registry
docker logout
docker logout ghcr.io

# Pull from registry
docker pull nginx:latest
docker pull redis:7-alpine

# Push to registry
docker push username/my-app:latest

# Search registry
docker search nginx
docker search --filter stars=1000 nginx
```

### Docker Hub Commands

```bash
# Official image (no namespace)
docker pull nginx
docker pull ubuntu
docker pull python:3.12

# User/Organization image
docker pull username/my-app:latest

# Pull with specific tag
docker pull nginx:1.25.3-alpine

# Pull all tags of an image (manifest list)
docker pull --all-tags nginx
```

---

## 4. Tags

### What is a Tag?

A tag is a label applied to a specific version (version number, variant) of an image. Tags are mutable and can be reassigned to different image IDs.

### Tag Format

```
registry.example.com:5000/namespace/image:tag
│                        │       │       │    │
│                        │       │       │    └── Tag (version/variant)
│                        │       │       └─────── Image name
│                        │       └─────────────── Namespace (user/org)
│                        └────────────────────── Registry host (optional)
```

### Common Tag Patterns

| Tag Pattern | Meaning | Example |
|-------------|---------|---------|
| `:latest` | Default tag, most recent | `nginx:latest` |
| `:1.25.3` | Specific version | `node:20.11.0` |
| `:-alpine` | Lightweight base image | `python:3.12-alpine` |
| `:-slim` | Minimal installation | `node:20-slim` |
| `:-bookworm` | Debian release codename | `debian:bookworm` |
| `:-buster` | Old Debian release | `debian:buster` |
| `:-focal` | Ubuntu 20.04 LTS | `ubuntu:20.04` |
| `:-jammy` | Ubuntu 22.04 LTS | `ubuntu:22.04` |

### Tagging Commands

```bash
# Tag an image
docker tag my-app:latest my-app:1.0.0
docker tag my-app:latest registry.example.com/my-app:v1

# Multiple tags at once
docker build -t my-app:latest -t my-app:1.0.0 -t my-app:v1 .

# Push with multiple tags
docker push my-app:latest
docker push my-app:1.0.0
docker push my-app:v1

# List all tags for an image (Docker Hub)
curl -s https://hub.docker.com/v2/repositories/library/nginx/tags | jq '.results[].name'

# Remove a tag
docker rmi my-app:old-tag
```

### Tag Best Practices

| Practice | Description |
|----------|-------------|
| **Use specific versions** | Avoid `:latest` in production |
| **Semantic versioning** | `app:1.2.3` for major.minor.patch |
| **Date-based tags** | `app:20240115` for reproducible builds |
| **Commit SHA tags** | `app:a1b2c3d` for exact commits |
| **Immutable tags** | Once tagged, don't reassign |

---

## 5. Practical Examples

### Complete Workflow Example

```bash
# 1. Pull a base image
docker pull ubuntu:22.04

# 2. Run a container and install software
docker run -it --name my-container ubuntu:22.04 bash
# Inside container:
apt update && apt install -y nginx
exit

# 3. Commit changes to create new image
docker commit my-container my-nginx:latest

# 4. Tag for distribution
docker tag my-nginx:latest username/my-nginx:1.0

# 5. Push to registry
docker login
docker push username/my-nginx:1.0

# 6. On another machine, pull and run
docker pull username/my-nginx:1.0
docker run -d -p 8080:80 username/my-nginx:1.0
```

### Dockerfile to Image to Container

```dockerfile
# Dockerfile
FROM nginx:alpine
COPY ./index.html /usr/share/nginx/html/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

```bash
# Build image
docker build -t my-webapp:latest .

# Run container
docker run -d -p 8080:80 my-webapp:latest
```

### Environment Variables and Tags

```bash
# Build with build args
docker build -t my-app:1.0 --build-arg VERSION=1.0 .

# Run with environment variables
docker run -d \
  --name my-app \
  -e NODE_ENV=production \
  -e PORT=3000 \
  my-app:1.0
```

---

## Quick Reference Cheat Sheet

### Images
```bash
docker images              # List local images
docker pull <image>        # Pull image from registry
docker build -t <name> .   # Build image from Dockerfile
docker rmi <image>         # Remove image
docker image prune         # Remove unused images
```

### Containers
```bash
docker ps                  # List running containers
docker ps -a               # List all containers
docker run <image>         # Run container
docker stop <container>    # Stop container
docker rm <container>      # Remove container
docker logs <container>    # View logs
docker exec -it <container> bash  # Shell into container
```

### Registries
```bash
docker login               # Login to registry
docker push <image>        # Push to registry
docker search <term>       # Search Docker Hub
```

### Tags
```bash
docker tag <source> <target>   # Create a tag
docker push <image>:<tag>      # Push specific tag
docker pull <image>:<tag>      # Pull specific tag
```

---

## Common Patterns

### Pattern 1: Development Environment
```bash
docker run -v $(pwd):/app -p 3000:3000 -it node:20 bash
```

### Pattern 2: Production Deployment
```bash
docker build -t myapp:1.0.0 --build-arg ENV=production .
docker tag myapp:1.0.0 registry.example.com/myapp:v1.0.0
docker push registry.example.com/myapp:v1.0.0
```

### Pattern 3: Database Container
```bash
docker run -d \
  --name postgres-db \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_DB=myapp \
  -v postgres-data:/var/lib/postgresql/data \
  postgres:16-alpine
```

### Pattern 4: Multi-container Setup
```bash
# docker-compose.yml approach
docker-compose up -d
docker-compose logs -f app
docker-compose down
```
