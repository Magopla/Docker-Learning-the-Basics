# Lesson 1.2: Images, Containers, Registries & Tags
## The Building Blocks of Docker

---

## 🎯 Goal

Understand the four fundamental concepts of Docker:
- **Images** - The blueprints
- **Containers** - The running instances
- **Registries** - The storage locations
- **Tags** - The version labels

---

## 🏗️ The Docker Ecosystem

```
┌─────────────────────────────────────────────────────────────────┐
│                    DOCKER ECOSYSTEM                              │
│                                                                  │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐      │
│  │  REGISTRY  │────▶│   IMAGE     │────▶│  CONTAINER  │      │
│  │  (Storage) │     │  (Template) │     │  (Running)  │      │
│  │             │     │             │     │             │      │
│  │ Docker Hub  │     │ nginx:1.25  │     │ my-web-server│     │
│  │ ghcr.io     │     │ redis:7     │     │ db-prod     │      │
│  │ ECR         │     │ python:3.12 │     │ cache       │      │
│  └─────────────┘     └─────────────┘     └─────────────┘      │
│         │                    │                                      │
│         │                    │ Tag                                  │
│         │                    ▼                                      │
│         │           ┌─────────────┐                               │
│         │           │ nginx:1.25  │                               │
│         │           │ nginx:alpine│                               │
│         │           └─────────────┘                               │
│         │                                                        │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📦 What is a Docker Image?

An image is a **read-only template** with instructions for creating a container.

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
│         Container Layer         │  ← Writable (creates when container runs)
├─────────────────────────────────┤
│         Application Layer       │  ← Your app code
├─────────────────────────────────┤
│         Dependencies Layer      │  ← node_modules, pip packages, etc.
├─────────────────────────────────┤
│         Runtime Layer           │  ← Python, Node.js, Java, etc.
├─────────────────────────────────┤
│         Base Image Layer        │  ← Ubuntu, Alpine, Debian
└─────────────────────────────────┘
```

### Example: What nginx Image Contains

```
nginx:latest
│
├── Ubuntu (Base Layer)
│   └── Linux kernel, system libraries
├── Python/Perl (Runtime)
│   └── Package managers
├── nginx Binary
│   └── Web server software
└── Configuration
    └── Default configs
```

---

## 🐳 What is a Container?

A container is a **runnable instance** of an image.

### Container vs Image

| Aspect | Image | Container |
|--------|-------|-----------|
| **State** | Read-only | Read-write |
| **Purpose** | Template | Running instance |
| **Lifecycle** | Persistent | Can be started/stopped/deleted |
| **Changes** | Never changes | Writable layer on top |

### Container Lifecycle

```
    ┌──────────┐
    │ Created   │
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
    │ Stopped  │
    └────┬─────┘
         │ docker stop
         ▼
    ┌──────────┐
    │  Killed  │
    └──────────┘
```

---

## 🏪 What is a Registry?

A registry is a **storage and distribution system** for Docker images.

### Registry Types

| Type | Description | Examples |
|------|-------------|----------|
| **Public** | Free, open to everyone | Docker Hub, GitHub GHCR |
| **Private** | Restricted access | AWS ECR, Google GCR |
| **Self-hosted** | Run your own | Harbor, Registry |

### Popular Registries

| Registry | Provider | URL |
|----------|----------|-----|
| Docker Hub | Docker | hub.docker.com |
| GitHub Container Registry | GitHub | ghcr.io |
| Amazon ECR | AWS | aws.amazon.com/ecr |
| Google Artifact Registry | Google Cloud | cloud.google.com |
| Azure Container Registry | Microsoft Azure | azure.microsoft.com |

### How Registries Work

```
┌─────────────────────────────────────────────────────────────────┐
│                    PUSH & PULL WORKFLOW                          │
│                                                                  │
│  LOCAL MACHINE              REGISTRY              CLOUD           │
│  ┌───────────┐            ┌───────────┐          ┌───────────┐ │
│  │ nginx:1.25│───push───▶│ nginx:1.25│──────────▶│ S3/Cloud  │ │
│  │  (local)  │            │ (storage) │          │  Storage  │ │
│  └───────────┘            └───────────┘          └───────────┘ │
│         │                      ▲                               │
│         │                      │                               │
│         │◀─────pull───────────┘                               │
│         │                                                     │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🏷️ What is a Tag?

A tag is a **label** applied to a specific version of an image.

### Tag Format

```
registry.example.com:5000/namespace/image:tag
│                        │       │       │    │
│                        │       │       │    └── Tag (version)
│                        │       │       └─────── Image name
│                        │       └─────────────── Namespace
│                        └────────────────────── Registry (optional)
```

### Common Tag Patterns

| Tag Pattern | Meaning | Example |
|-------------|---------|---------|
| `:latest` | Default, most recent | `nginx:latest` |
| `:1.25.3` | Specific version | `node:20.11.0` |
| `:-alpine` | Lightweight base | `python:3.12-alpine` |
| `:-slim` | Minimal installation | `node:20-slim` |
| `:-bookworm` | Debian release | `debian:bookworm` |
| `:-jammy` | Ubuntu 22.04 LTS | `ubuntu:22.04` |

### Tag Best Practices

| Practice | Why |
|----------|-----|
| **Use specific versions** | Reproducibility |
| **Avoid :latest in production** | Unpredictable changes |
| **Semantic versioning** | Clear upgrade path |
| **Date-based tags** | Reproducible builds |

---

## 🔄 How They Work Together

### Example: Running a Web Server

```bash
# 1. PULL image from registry
docker pull nginx:1.25-alpine
```
```
┌─────────┐     ┌─────────────┐     ┌─────────────┐
│ Registry │────▶│   IMAGE     │────▶│   (stored   │
│  (Hub)   │     │ nginx:1.25 │     │  locally)   │
└─────────┘     └─────────────┘     └─────────────┘
```

```bash
# 2. CREATE container from image
docker run -d -p 8080:80 --name my-server nginx:1.25-alpine
```
```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   IMAGE     │────▶│  CONTAINER  │────▶│  RUNNING!   │
│ nginx:1.25  │     │ my-server   │     │   :8080     │
│ (template)  │     │ (instance)  │     │   :80       │
└─────────────┘     └─────────────┘     └─────────────┘
```

---

## 📝 Summary Table

| Concept | What it is | Example |
|---------|------------|---------|
| **Image** | Read-only blueprint | `nginx:1.25-alpine` |
| **Container** | Running instance of image | `my-web-server` |
| **Registry** | Storage for images | Docker Hub |
| **Tag** | Version of image | `:1.25-alpine` |

---

## 💻 Hands-On Commands

### Images

```bash
# List local images
docker images

# Pull an image
docker pull nginx:1.25-alpine

# Remove an image
docker rmi nginx:1.25-alpine
```

### Containers

```bash
# Run a container
docker run -d --name web nginx:1.25-alpine

# List running containers
docker ps

# Stop container
docker stop web

# Remove container
docker rm web
```

### Registries

```bash
# Login to Docker Hub
docker login

# Push image
docker push username/myapp:1.0
```

### Tags

```bash
# Tag an image
docker tag myapp:latest username/myapp:1.0

# Push with tag
docker push username/myapp:1.0
```

---

## ✅ Key Takeaways

1. **Image** = Recipe (read-only blueprint)
2. **Container** = Cookie (running instance)
3. **Registry** = Shelf/Library (storage)
4. **Tag** = Version number (e.g., v1.2.3)

---

## 🚀 Next Steps

**Continue to:** [Lesson 1.3: Docker Architecture](./03-architecture.md)
