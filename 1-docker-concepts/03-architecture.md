# Lesson 1.3: Docker Architecture
## How All the Pieces Fit Together

---

## 🎯 Goal

Understand how Docker's components work together to build, run, and manage containers.

---

## 🏗️ Docker Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                      DOCKER ARCHITECTURE                         │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    DOCKER CLIENT                         │   │
│  │                     (Your CLI)                          │   │
│  │         docker build, docker run, docker pull           │   │
│  └────────────────────────┬────────────────────────────────┘   │
│                           │                                      │
│                           ▼                                      │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    DOCKER DAEMON                        │   │
│  │                   (dockerd)                             │   │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ │   │
│  │  │ Builder  │ │  Packager │ │ Runner   │ │Registry  │ │   │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘ │   │
│  └────────────────────────┬────────────────────────────────┘   │
│                           │                                      │
│                           ▼                                      │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                 CONTAINERS & IMAGES                      │   │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐                │   │
│  │  │Cont 1   │  │Cont 2   │  │Cont 3   │                │   │
│  │  │nginx    │  │postgres │  │redis    │                │   │
│  │  └─────────┘  └─────────┘  └─────────┘                │   │
│  └────────────────────────┬────────────────────────────────┘   │
│                           │                                      │
│                           ▼                                      │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                 LINUX KERNEL                            │   │
│  │          (cgroups, namespaces, overlayfs)               │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔧 Components

### 1. Docker Client (CLI)

The **command-line tool** you interact with.

```bash
docker run nginx                    # You type this
     ↑
     └── Docker Client sends to Daemon
```

**Location:** Installed on your machine  
**Commands:** `docker build`, `docker run`, `docker pull`, etc.

---

### 2. Docker Daemon (dockerd)

The **background service** that manages containers.

```
┌─────────────────────────────────────────────────────────────────┐
│                        DAEMON RESPONSIBILITIES                   │
│                                                                  │
│  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐       │
│  │   Building    │  │    Image      │  │   Container   │       │
│  │   Images     │  │   Management   │  │   Lifecycle   │       │
│  │              │  │               │  │               │       │
│  │ docker build │  │ docker images │  │ docker run    │       │
│  │              │  │ docker pull   │  │ docker start  │       │
│  └───────────────┘  └───────────────┘  └───────────────┘       │
│                                                                  │
│  ┌───────────────┐  ┌───────────────┐                          │
│  │   Networks   │  │   Volumes     │                          │
│  │              │  │               │                          │
│  │ docker network│  │ docker volume │                          │
│  └───────────────┘  └───────────────┘                          │
└─────────────────────────────────────────────────────────────────┘
```

**Location:** Runs in background (system service)  
**Socket:** `/var/run/docker.sock`

---

### 3. Docker Registry

**Storage** for Docker images.

```
┌─────────────────────────────────────────────────────────────────┐
│                      DOCKER HUB                                  │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ 🔍 Search: "nginx"                                       │   │
│  ├─────────────────────────────────────────────────────────┤   │
│  │                                                         │   │
│  │ OFFICIAL REPOSITORIES                                    │   │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐                │   │
│  │  │  nginx  │  │ python  │  │  redis  │  ...           │   │
│  │  │ 500M+   │  │ 300M+   │  │  10M+   │                │   │
│  │  │ downloads│  │ downloads│  │ downloads │              │   │
│  │  └─────────┘  └─────────┘  └─────────┘                │   │
│  │                                                         │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

**Default:** Docker Hub (hub.docker.com)  
**Private:** AWS ECR, Google GCR, self-hosted

---

### 4. Docker Objects

#### Images (Templates)

```bash
# Images are built from Dockerfile
docker build -t myapp:1.0 .
```

#### Containers (Instances)

```bash
# Containers run from images
docker run -d myapp:1.0
```

#### Networks (Communication)

```bash
# Containers communicate via networks
docker network create my-network
docker run --network my-network nginx
```

#### Volumes (Persistence)

```bash
# Data persists in volumes
docker run -v my-volume:/data postgres
```

---

## 🔄 Request Flow

### When You Run `docker run nginx`:

```
┌─────────┐         ┌─────────┐         ┌─────────┐         ┌─────────┐
│  YOU   │         │ CLIENT  │         │ DAEMON  │         │REGISTRY │
└────┬────┘         └────┬────┘         └────┬────┘         └────┬────┘
     │                   │                   │                   │
     │ 1. docker run    │                   │                   │
     │ nginx            │                   │                   │
     │─────────────────▶│                   │                   │
     │                   │ 2. Pull nginx    │                   │
     │                   │─────────────────▶│                   │
     │                   │                   │    3. Check      │
     │                   │                   │    local cache   │
     │                   │                   │◀──────┐           │
     │                   │                   │       │ Found!   │
     │                   │ 4. Already exists │───────┘           │
     │                   │◀─────────────────│                   │
     │                   │                   │                   │
     │                   │ 5. Create & Start│                   │
     │                   │     Container    │                   │
     │                   │─────────────────▶│                   │
     │                   │                   │                   │
     │ 6. Running!       │                   │                   │
     │◀─────────────────│                   │                   │
     │                   │                   │                   │
     │                   │                   │                   │
     │                   │                   │                   │
     ▼                   ▼                   ▼                   ▼
```

---

## 📁 Key Locations (macOS)

| Component | Location |
|-----------|----------|
| Docker.sock | `/var/run/docker.sock` |
| Images | Inside Docker VM |
| Volumes | Inside Docker VM |
| Config | `~/Library/Containers/com.docker.docker` |

### Where Are Volumes Stored?

```
┌─────────────────────────────────────────────────────────────────┐
│                     macOS DOCKER DESKTOP                        │
│                                                                  │
│  Your Mac                                              Docker VM  │
│  ┌───────────────┐                              ┌─────────────┐│
│  │ docker CLI   │                              │ Images      ││
│  │              │                              │ Containers  ││
│  │ docker.sock │═════════════════════════════▶│ Volumes     ││
│  │ (socket)    │                              │             ││
│  └───────────────┘                              │ /var/lib/   ││
│                                                  │   docker/   ││
│                                                  └─────────────┘│
└─────────────────────────────────────────────────────────────────┘
```

---

## ⚙️ Docker Desktop vs Docker Engine

| Component | Docker Desktop | Docker Engine |
|-----------|----------------|---------------|
| **Includes** | Docker Engine + GUI + Kubernetes | CLI only |
| **Platform** | macOS, Windows | Linux |
| **GUI** | ✅ Included | ❌ Not included |
| **Kubernetes** | ✅ Built-in | ❌ Manual install |
| **Cost** | Free (personal use) | Free (open source) |

---

## 🔒 The Docker Socket

The socket file that allows communication with the Docker daemon.

```bash
# Socket location
/var/run/docker.sock
```

### What Needs Socket Access?

| Tool | Why |
|------|-----|
| Portainer | To manage containers |
| Docker CLI | To run commands |
| CI/CD tools | To build/deploy |

### Security Note

> ⚠️ **The socket gives root access!**
> 
> Anyone with access to the socket can control Docker, which means access to the host system.

```bash
# Bind mounting the socket (used by Portainer)
-v /var/run/docker.sock:/var/run/docker.sock
```

---

## 📊 Summary

```
┌─────────────────────────────────────────────────────────────────┐
│                      SUMMARY                                     │
│                                                                  │
│  ┌────────────┐    ┌────────────┐    ┌────────────┐            │
│  │   Client   │───▶│   Daemon   │───▶│ Containers │            │
│  │   (CLI)    │    │  (dockerd) │    │            │            │
│  └────────────┘    └─────┬──────┘    └────────────┘            │
│                          │                                      │
│                          ▼                                      │
│                   ┌────────────┐                                │
│                   │  Registry  │                                │
│                   │ (Docker Hub)│                               │
│                   └────────────┘                                │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## ✅ Key Takeaways

1. **Client** = You (CLI commands)
2. **Daemon** = Background service (does the work)
3. **Registry** = Image storage (like GitHub for code)
4. **Socket** = Communication channel between client and daemon

---

## 🚀 Next Steps

**Continue to:** [Module 2: Setup](../2-setup/README.md)
