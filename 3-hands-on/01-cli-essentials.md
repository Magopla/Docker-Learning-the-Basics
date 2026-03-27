# Exercise 1: Docker CLI Essentials
## Learn the Basic Commands

---

## 🎯 Goal

Learn the essential Docker CLI commands. By the end, you'll be able to:
- Pull images from Docker Hub
- Run basic containers
- List containers and images
- Stop and remove containers

**Time: ~20 minutes**

---

## 📝 Prerequisites

- Docker Desktop is running
- Terminal is open

---

## 1️⃣ Check Docker Installation

Let's verify Docker is working:

```bash
# Check Docker version
docker --version

# Check Docker Compose version
docker compose version

# Get Docker system info
docker info | head -10
```

**Expected output:**
```
Docker version 26.0.0, build xxxxxxx
Docker Compose version v2.x.x
Client:
 Version:    26.0.0
 ...
```

---

## 2️⃣ Run Your First Container

```bash
docker run hello-world
```

**What happened?**
1. Docker checked for `hello-world` image locally
2. Not found, so it pulled from Docker Hub
3. Created a container from the image
4. Container ran and printed the message
5. Container exited

**Check the container:**
```bash
docker ps -a
```

You'll see the `hello-world` container with status "Exited".

---

## 3️⃣ Pull Images

Images are downloaded from registries. Let's pull some:

```bash
# Pull nginx (web server)
docker pull nginx:alpine

# Pull Ubuntu
docker pull ubuntu:22.04

# Pull Python
docker pull python:3.12-slim
```

**List your images:**
```bash
docker images
```

**Output:**
```
REPOSITORY   TAG        IMAGE ID       SIZE
nginx        alpine     a6bd71f48f68   142MB
ubuntu       22.04      8a3cdc4b8d9c   77.8MB
python       3.12-slim  4aeca2f7d4b8    143MB
hello-world  latest     9c7a54a9a43c   9.14kB
```

---

## 4️⃣ Run Containers

### Run nginx (Web Server)

```bash
# Run nginx in background (detached)
docker run -d --name web-server nginx:alpine

# Check it's running
docker ps

# Should see:
# CONTAINER ID   IMAGE          STATUS       PORTS     NAMES
# xxxxxxxx        nginx:alpine   Up 2 mins   80/tcp    web-server
```

### Access nginx

Since we're in a container, let's just verify it's running:

```bash
# Check nginx logs
docker logs web-server

# Get container info
docker inspect web-server | head -20
```

---

## 5️⃣ List Containers

```bash
# List running containers
docker ps

# List ALL containers (including stopped)
docker ps -a

# List only container IDs
docker ps -q
```

---

## 6️⃣ Stop and Remove Containers

```bash
# Stop a container
docker stop web-server

# Check status
docker ps

# Container is stopped but still exists
docker ps -a

# Remove the container
docker rm web-server

# Verify it's gone
docker ps -a
```

---

## 7️⃣ Quick Reference Commands

| Command | What it does |
|---------|-------------|
| `docker images` | List downloaded images |
| `docker ps` | List running containers |
| `docker ps -a` | List all containers |
| `docker run <image>` | Create & start container |
| `docker stop <name>` | Stop container |
| `docker rm <name>` | Remove container |
| `docker logs <name>` | View container logs |

---

## 🧪 Challenge

Try this on your own:

1. Pull the `redis:alpine` image
2. Run a container named `my-redis`
3. Check it's running
4. Stop and remove it

**Solution:**
```bash
# 1. Pull
docker pull redis:alpine

# 2. Run
docker run -d --name my-redis redis:alpine

# 3. Check
docker ps

# 4. Stop & Remove
docker stop my-redis && docker rm my-redis
```

---

## ✅ Checklist

Before moving on, make sure you can:

- [ ] `docker run hello-world` works
- [ ] `docker pull nginx:alpine` works
- [ ] `docker images` shows downloaded images
- [ ] `docker ps` shows running containers
- [ ] `docker stop` and `docker rm` work

---

## 🚀 Next Steps

**Go to Exercise 2:** [Running Containers](./02-running-containers.md)
