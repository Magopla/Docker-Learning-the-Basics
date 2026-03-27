# Docker vs Virtual Machines

## Overview

Containerization and virtualization are two fundamental technologies for running isolated environments. While they share similarities, they differ significantly in architecture, performance, and use cases.

---

## Architecture Comparison

### Virtual Machines (VMs)

```
┌─────────────────────────────────────────┐
│              Host Machine               │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐ │
│  │   VM1   │  │   VM2   │  │   VM3   │ │
│  │ ┌─────┐ │  │ ┌─────┐ │  │ ┌─────┐ │ │
│  │ │ OS  │ │  │ │ OS  │ │  │ │ OS  │ │ │
│  │ ├─────┤ │  │ ├─────┤ │  │ ├─────┤ │ │
│  │ │ App │ │  │ │ App │ │  │ │ App │ │ │
│  │ └─────┘ │  │ └─────┘ │  │ └─────┘ │ │
│  └─────────┘  └─────────┘  └─────────┘ │
│         ↑         ↑         ↑           │
│  ┌──────────────────────────────────┐   │
│  │           Hypervisor             │   │
│  └──────────────────────────────────┘   │
│  ┌──────────────────────────────────┐   │
│  │        Physical Hardware         │   │
│  │   CPU  │  Memory  │  Storage     │   │
│  └──────────────────────────────────┘   │
└─────────────────────────────────────────┘
```

### Docker Containers

```
┌─────────────────────────────────────────┐
│              Host Machine               │
│  ┌──────────────────────────────────┐   │
│  │         Docker Engine            │   │
│  │  ┌─────────┐  ┌─────────┐       │   │
│  │  │   C1    │  │   C2    │       │   │
│  │  │  App 1  │  │  App 2  │       │   │
│  │  ├─────────┤  ├─────────┤       │   │
│  │  │ Libs    │  │ Libs    │       │   │
│  │  ├─────────┤  ├─────────┤       │   │
│  │  │ Container│ │ Container│      │   │
│  │  │ Runtime │  │ Runtime │       │   │
│  │  └─────────┘  └─────────┘       │   │
│  └──────────────────────────────────┘   │
│  ┌──────────────────────────────────┐   │
│  │        Physical Hardware         │   │
│  │   CPU  │  Memory  │  Storage     │   │
│  └──────────────────────────────────┘   │
└─────────────────────────────────────────┘
```

---

## Quick Comparison Table

| Feature | Docker Containers | Virtual Machines |
|---------|------------------|------------------|
| **Isolation** | Process-level | Full OS isolation |
| **Startup Time** | Seconds | Minutes |
| **Size** | MBs | GBs |
| **Performance** | Near-native | Moderate overhead |
| **Resource Usage** | Lightweight | Heavy |
| **Portability** | Highly portable | Less portable |
| **Boot Required** | No | Yes |
| **System Calls** | Share host kernel | Full kernel |

---

## Detailed Comparison

### Resource Utilization

| Aspect | Docker | Virtual Machines |
|--------|--------|------------------|
| **Memory Overhead** | ~MB per container | ~GB per VM |
| **Disk Space** | Shared base images + diffs | Full OS per VM |
| **CPU Usage** | Minimal | Moderate |
| **Network Overhead** | Minimal (bridge) | Moderate (virtual switch) |

### Isolation & Security

| Aspect | Docker | Virtual Machines |
|--------|--------|------------------|
| **Kernel Sharing** | Shares host kernel | Separate kernel |
| **Security Boundary** | Process isolation | Hardware-level |
| **Attack Surface** | Smaller | Larger |
| **Container Escape** | Possible (misconfiguration) | Very rare |
| **Host Access** | Can access host filesystem | Fully isolated |

### Use Cases

| Use Case | Best Choice | Reason |
|----------|-------------|--------|
| Microservices | **Docker** | Lightweight, fast scaling |
| CI/CD Pipelines | **Docker** | Fast builds, reproducible |
| Legacy Apps | **VM** | Full OS compatibility |
| Development Environments | **Docker** | Consistency across team |
| Running Windows Apps | **VM** | Requires Windows kernel |
| Database Servers | **VM** | Predictable resources |
| Serverless Functions | **Docker** | Cold start matters |
| High Security Workloads | **VM** | Stronger isolation |

---

## Performance Comparison

### Startup Time

| Environment | Typical Startup |
|-------------|-----------------|
| Docker Container | 100ms - 2s |
| Virtual Machine | 30s - 5min |

### Memory Usage

| 4GB Host Machine Scenario | Docker | Virtual Machines |
|--------------------------|--------|------------------|
| Available for Apps | ~3.5GB | ~1GB (2 VMs) |
| Base Overhead | ~100MB | ~2GB |

### Density (Containers/VMs per Host)

| Host Specs | Docker Containers | Virtual Machines |
|------------|-------------------|------------------|
| 4GB RAM, 2 CPU | 50-100 | 2-4 |
| 16GB RAM, 4 CPU | 200-400 | 8-16 |
| 64GB RAM, 8 CPU | 800-1600 | 32-64 |

---

## When to Use What

### Choose Docker Containers When:
- Building cloud-native microservices
- Need fast scaling and deployment
- Working with CI/CD pipelines
- Want efficient resource utilization
- Need consistent development environments

### Choose Virtual Machines When:
- Running different operating systems
- Need maximum security isolation
- Running legacy applications
- Require specific kernel configurations
- Compliance requires full isolation

---

# Installing Docker on macOS

## System Requirements

| Requirement | Intel Mac | Apple Silicon (M1/M2/M3) |
|-------------|-----------|--------------------------|
| **OS Version** | macOS 11+ | macOS 11+ |
| **RAM** | 4 GB minimum | 4 GB minimum |
| **Virtualization** | VT-x enabled | Rosetta 2 or native |
| **Disk Space** | 8 GB minimum | 8 GB minimum |

## Installation Methods

### Method 1: Docker Desktop (Recommended)

#### Step 1: Download Docker Desktop

Visit the official Docker website:

```
https://www.docker.com/products/docker-desktop
```

Click the "Download for Mac" button and select the appropriate version:
- **Apple Silicon**: `Docker-Desktop-*-aarch64.dmg`
- **Intel**: `Docker-Desktop-*-x86_64.dmg`

#### Step 2: Install Docker Desktop

1. Double-click the `.dmg` file you downloaded
2. Drag the Docker icon to the Applications folder
3. Launch Docker Desktop from Applications

#### Step 3: Verify Installation

Open Terminal and run:

```bash
docker --version
docker-compose --version
docker ps
```

Expected output:
```
Docker version 24.x.x, build xxxxxxx
Docker Compose version v2.x.x
CONTAINER ID   IMAGE   COMMAND   CREATED   STATUS   PORTS   NAMES
```

#### Step 4: Configure Docker Desktop

1. Open Docker Desktop from the menu bar
2. Go to Settings (gear icon)
3. Configure resources as needed:
   - **Memory**: 4GB minimum, 8GB+ recommended
   - **CPUs**: 2 minimum
   - **Disk image size**: 60GB+ recommended

### Method 2: Homebrew Installation

#### Prerequisites

Install Homebrew if not already installed:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### Installation

```bash
# Update Homebrew
brew update

# Install Docker
brew install --cask docker

# Alternative: Install Docker Desktop with GUI
brew install --cask docker
```

#### Launch Docker

1. Open Docker Desktop application from Applications
2. Accept the license agreement
3. Wait for Docker daemon to start

#### Verify with Homebrew

```bash
brew info docker
docker info
```

### Method 3: Manual Installation (Colima + Docker CLI)

For a lightweight alternative without Docker Desktop:

#### Install Colima

```bash
# Install Colima (lightweight Linux VM)
brew install colima

# Install Docker CLI
brew install docker
```

#### Start Colima

```bash
# Start with default settings
colima start

# Start with custom resources
colima start --arch aarch64 --vm-type=vz --vz-rosetta --cpu 4 --memory 8

# Stop Colima when not needed
colima stop
```

#### Configure Docker

```bash
# Set up Docker context
export DOCKER_HOST="unix:///Users/$USER/.colima/default/docker.sock"

# Or use docker context
docker context create colima --docker "host=unix://$HOME/.colima/default/docker.sock"
docker context use colima
```

#### Verify Installation

```bash
docker version
docker run hello-world
```

---

## Troubleshooting Common Issues

### Permission Denied Error

```bash
# Add your user to the docker group
sudo usermod -aG docker $USER

# Or on macOS, grant permissions in Docker Desktop > Settings > Advanced
```

### Docker Daemon Not Running

```bash
# Check Docker Desktop is running
open -a Docker

# Or start from terminal
/Applications/Docker.app/Contents/MacOS/Docker &
```

### Apple Silicon (M1/M2/M3) Issues

```bash
# Check architecture
uname -m
# Should output: arm64 for Apple Silicon

# Build for specific architecture
docker buildx build --platform linux/arm64 .
```

### Clean Uninstall (if needed)

```bash
# Remove Docker Desktop
rm -rf ~/Library/Application\ Support/Docker
rm -rf ~/Library/Containers/com.docker.*
rm -rf ~/Library/Preferences/com.docker.*
brew uninstall --cask docker
```

---

## Quick Reference Commands

```bash
# Check Docker version
docker --version

# View running containers
docker ps

# View all containers (including stopped)
docker ps -a

# Pull an image
docker pull nginx:latest

# Run a container
docker run -d -p 8080:80 nginx:latest

# Stop a container
docker stop <container_id>

# Remove a container
docker rm <container_id>

# List images
docker images

# Remove unused images
docker image prune -a

# View Docker logs
docker logs <container_id>

# Execute command in running container
docker exec -it <container_id> /bin/bash

# Docker Compose
docker-compose up -d
docker-compose down
```

---

## Next Steps

1. Run your first container: `docker run hello-world`
2. Create a Dockerfile for your application
3. Learn Docker Compose for multi-container applications
4. Explore Docker Hub for ready-to-use images
5. Practice with real-world scenarios

---

## Additional Resources

- Docker Official Documentation: https://docs.docker.com/
- Docker Hub: https://hub.docker.com/
- Docker Desktop: https://www.docker.com/products/docker-desktop/
- Awesome Docker: https://github.com/veggiemonk/awesome-docker
