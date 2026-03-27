# Docker Learning the Basics

A comprehensive guide to understanding Docker fundamentals, containerization concepts, and practical Docker usage.

## 📚 Contents

### Core Concepts
| File | Description |
|------|-------------|
| [Docker vs Virtual Machines.md](./Docker%20vs%20Virtual%20Machines.md) | Compare containers vs VMs, architecture differences, and Docker installation for macOS |
| [Docker terminology.md](./Docker%20terminology.md) | Core concepts: Images, Containers, Registries, and Tags |

### Examples
| File | Description |
|------|-------------|
| [Examples/01_pulling_images_and_running_containers.md](./Examples/01_pulling_images_and_running_containers.md) | Essential CLI commands for images and containers |
| [Examples/Portainer_Setup.md](./Examples/Portainer_Setup.md) | Web-based container management UI setup |
| [Examples/Docker_Cheat_Sheet.md](./Examples/Docker_Cheat_Sheet.md) | Comprehensive command reference guide |

## 🚀 Quick Start

### Run Your First Container

```bash
# Pull and run a container
docker run hello-world

# Run nginx web server
docker run -d -p 8080:80 nginx:latest

# Open browser to http://localhost:8080
```

### Essential Commands

```bash
# Check Docker version
docker --version

# List running containers
docker ps

# List all containers
docker ps -a

# Stop a container
docker stop <container_id>

# Remove a container
docker rm <container_id>

# List images
docker images

# Pull an image
docker pull nginx:latest
```

## 📖 What You'll Learn

### 1. Docker vs Virtual Machines
- Understanding the architecture differences
- Resource utilization comparison
- Security and isolation differences
- When to use containers vs VMs
- How to install Docker on macOS

### 2. Docker Terminology
- **Images**: Read-only templates for creating containers
- **Containers**: Runnable instances of images
- **Registries**: Storage and distribution for images
- **Tags**: Version labels for images

## 🛠️ Prerequisites

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| macOS Version | 11 (Big Sur) | 13 (Ventura) or later |
| RAM | 4 GB | 8 GB |
| Disk Space | 8 GB | 20 GB |
| Processor | Intel or Apple Silicon | Apple Silicon (M1/M2/M3) |

## 📦 Installation

### macOS (Docker Desktop)

```bash
# Using Homebrew
brew install --cask docker

# Or download from:
# https://www.docker.com/products/docker-desktop
```

### Verify Installation

```bash
docker --version
docker run hello-world
```

---

## 🔗 Additional Resources

### Official Documentation
- [Docker Documentation](https://docs.docker.com/) - Official Docker docs
- [Docker Hub](https://hub.docker.com/) - Public image registry
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) - Desktop application

### Learning Platforms
- [Docker Curriculum](https://docker-curriculum.com/) - Interactive Docker tutorial
- [Play with Docker](https://labs.play-with-docker.com/) - Free online Docker playground
- [Docker Labs](https://github.com/docker/labs) - Official Docker labs and workshops

### Community & Support
- [Docker Community Forums](https://forums.docker.com/)
- [r/docker](https://reddit.com/r/docker) - Docker subreddit
- [Docker Slack](https://docker-community.slack.com/) - Community Slack channel

### Tools & Utilities
- [Docker Compose](https://docs.docker.com/compose/) - Multi-container applications
- [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/) - Dockerfile syntax
- [Docker Scout](https://docs.docker.com/scout/) - Container analysis
- [BuildKit](https://github.com/moby/buildkit) - Fast builds

### Books
- [Docker in Action](https://www.manning.com/books/docker-in-action) - Jeff Nickoloff
- [The Docker Book](https://dockerbook.com/) - James Turnbull
- [Container Security](https://nostarch.com/container-security) - Liz Rice

### Video Tutorials
- [Docker Official YouTube](https://www.youtube.com/@Docker)
- [Techworld with Nana](https://www.youtube.com/c/TechWorldwithNana) - Docker tutorials

### Related Technologies
- [Kubernetes](https://kubernetes.io/) - Container orchestration
- [Helm](https://helm.sh/) - Kubernetes package manager
- [Docker Swarm](https://docs.docker.com/engine/swarm/) - Container orchestration
- [Podman](https://podman.io/) - Docker alternative (daemonless)
- [Kaniko](https://github.com/GoogleContainerTools/kaniko) - Container builds in Kubernetes

---

## 🆕 Extra Resources

### Official Cheat Sheets
| Resource | Description |
|----------|-------------|
| [Docker Official Cheat Sheet (PDF)](https://docs.docker.com/get-started/docker_cheatsheet.pdf) | Official Docker quick reference PDF |
| [Collabnix Docker Cheat Sheet](https://dockerlabs.collabnix.com/docker/cheatsheet/) | Comprehensive community cheat sheet |
| [Docker Compose Cheat Sheet](https://collabnix.com/docker-compose-cheatsheet/) | Docker Compose commands reference |
| [Kubectl Cheat Sheet](https://collabnix.com/kubectl-cheatsheet/) | Kubernetes CLI reference |

### Interactive Learning
| Resource | Description |
|----------|-------------|
| [Play with Docker](https://labs.play-with-docker.com/) | Free online Docker playground |
| [Play with Docker Classroom](https://training.play-with-docker.com/) | Official Docker training labs |
| [Docker Curriculum](https://docker-curriculum.com/) | Step-by-step Docker tutorial |
