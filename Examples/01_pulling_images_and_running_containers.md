# Example 1: Pulling Images & Running Containers in CLI

## Overview

This guide covers essential Docker commands for pulling images from registries and running containers via the command line interface.

```
┌─────────────────────────────────────────────────────────────────┐
│                      Docker CLI Workflow                         │
│                                                                  │
│  docker pull nginx    │    docker run nginx    │    docker ps   │
│  ┌──────────┐         │    ┌──────────┐         │  ┌──────────┐ │
│  │ Registry │         │    │  Image  │         │  │Container │ │
│  │  (Hub)   │         │    │ ──────▶ │         │  │ ──────── │ │
│  └──────────┘         │    └──────────┘         │  └──────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

---

## Part 1: Pulling Images

### Basic Pull Commands

```bash
# Pull latest version (uses :latest tag)
docker pull nginx

# Pull specific tag
docker pull nginx:1.25.3
docker pull python:3.12-slim
docker pull redis:7-alpine

# Pull from different registries
docker pull ghcr.io/username/myapp:latest
docker pull gcr.io/my-project/myimage:v1
```

### Understanding Image Pull Layers

```bash
# Pull with verbose output
docker pull -v nginx:latest

# Example output:
# latest: Pulling from library/nginx
# a6bd71f48f68: Already exists
# 96b1e6d1461d: Downloading [=========>           ]  5.237MB/22.04MB
# 54d9e99e5071: Download complete
```

### Pull Commands Reference

| Command | Description |
|---------|-------------|
| `docker pull <image>` | Pull latest tag |
| `docker pull <image>:tag` | Pull specific tag |
| `docker pull -a <image>` | Pull all tags |
| `docker pull --quiet <image>` | Silent mode |

### Common Official Images

| Image | Description | Size |
|-------|-------------|------|
| `nginx` | Web server | ~140MB |
| `python:3.12` | Python runtime | ~1GB |
| `node:20` | Node.js runtime | ~1.1GB |
| `redis:7-alpine` | Redis database | ~30MB |
| `postgres:16` | PostgreSQL database | ~380MB |
| `ubuntu:22.04` | Ubuntu OS | ~80MB |
| `alpine:3.19` | Minimal Linux | ~7MB |

---

## Part 2: Running Containers

### Basic Run Commands

```bash
# Run simplest container
docker run hello-world

# Run nginx in background (detached)
docker run -d nginx:latest

# Run with port mapping (host:container)
docker run -d -p 8080:80 nginx:latest
```

### Interactive Containers

```bash
# Run with interactive terminal
docker run -it ubuntu bash

# Run Alpine Linux
docker run -it alpine sh

# Exit without stopping (detach)
# Press: Ctrl+P, Ctrl+Q
```

### Container with Environment Variables

```bash
# Single env variable
docker run -d -e NODE_ENV=production nginx

# Multiple env variables
docker run -d -e \
  -e APP_ENV=production \
  -e PORT=3000 \
  -e DATABASE_URL=postgres://... \
  myapp:latest
```

### Container with Volume Mounts

```bash
# Mount local directory
docker run -d -p 8080:80 -v $(pwd)/html:/usr/share/nginx/html nginx

# Mount with read-only
docker run -d -v $(pwd)/config:/etc/app:ro myapp

# Use named volume
docker run -d -v my-data:/var/lib/postgresql/data postgres
```

### Container with Custom Name

```bash
# Assign custom name
docker run -d --name my-nginx nginx

# List containers to verify
docker ps --filter "name=my-nginx"
```

---

## Part 3: Managing Containers

### Listing Containers

```bash
# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Show only container IDs
docker ps -q

# Format output
docker ps --format "table {{.ID}}\t{{.Names}}\t{{.Status}}"
```

### Starting, Stopping, Restarting

```bash
# Start a stopped container
docker start my-nginx

# Stop running container
docker stop my-nginx

# Stop with timeout (seconds)
docker stop -t 30 my-nginx

# Restart container
docker restart my-nginx

# Stop all running containers
docker stop $(docker ps -q)
```

### Removing Containers

```bash
# Remove stopped container
docker rm my-nginx

# Force remove running container
docker rm -f my-nginx

# Remove all stopped containers
docker container prune

# Remove containers by pattern
docker rm $(docker ps -a -f ancestor=nginx --format "{{.ID}}")
```

### Viewing Container Logs

```bash
# View logs
docker logs my-nginx

# Follow logs (real-time)
docker logs -f my-nginx

# Show last 50 lines
docker logs --tail 50 my-nginx

# Show logs since timestamp
docker logs --since "2024-01-15T10:00:00" my-nginx
```

### Executing Commands in Container

```bash
# Open bash shell
docker exec -it my-nginx bash

# Run single command
docker exec my-nginx ls -la /var/log

# Run as different user
docker exec -u postgres my-nginx psql
```

### Inspecting Containers

```bash
# View all details
docker inspect my-nginx

# Get specific info (JSON)
docker inspect --format '{{.NetworkSettings.IPAddress}}' my-nginx
docker inspect --format '{{.Config.Image}}' my-nginx
```

### Container Stats

```bash
# View resource usage
docker stats

# View specific container
docker stats my-nginx

# Stream stats
docker stats --no-stream

# All containers with format
docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}"
```

---

## Part 4: Practical Examples

### Example 1: Running a Web Server

```bash
# Step 1: Pull nginx image
docker pull nginx:alpine

# Step 2: Run container
docker run -d \
  --name web-server \
  -p 8080:80 \
  nginx:alpine

# Step 3: Verify
curl http://localhost:8080

# Step 4: Check logs
docker logs web-server
```

### Example 2: Running a Database

```bash
# Run PostgreSQL
docker run -d \
  --name postgres-db \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -e POSTGRES_DB=mydb \
  -p 5432:5432 \
  -v postgres-data:/var/lib/postgresql/data \
  postgres:16-alpine

# Connect to database
docker exec -it postgres-db psql -U postgres mydb
```

### Example 3: Running Redis Cache

```bash
# Run Redis
docker run -d \
  --name redis-cache \
  -p 6379:6379 \
  redis:7-alpine

# Test connection
docker exec -it redis-cache redis-cli ping
# Expected: PONG
```

### Example 4: Running Python Application

```bash
# Run Python REPL
docker run -it python:3.12-slim python

# Run Python script
docker run -v $(pwd):/app python:3.12-slim python /app/script.py
```

### Example 5: Development Environment

```bash
# Run with current directory mounted
docker run -d \
  --name dev-server \
  -p 3000:3000 \
  -v $(pwd):/app \
  -w /app \
  node:20 \
  npm start

# View running processes
docker exec dev-server ps aux
```

### Example 6: Running cURL in Container

```bash
# Test API endpoint
docker run --rm \
  curlimages/curl:latest \
  https://api.example.com/health

# With headers
docker run --rm \
  curlimages/curl:latest \
  curl -H "Authorization: Bearer token" \
  https://api.example.com/data
```

---

## Part 5: Portainer Integration

For a graphical web-based container management interface, see the dedicated guide:

📄 **[Portainer Setup Guide](./Portainer_Setup.md)**

This guide covers:
- Installation methods (CLI, Docker Compose, Agent)
- Initial setup wizard
- Container, image, network, and volume management
- Advanced configuration and troubleshooting

Quick start:

```bash
# Install Portainer
docker volume create portainer_data
docker run -d --name portainer \
  -p 9000:9000 -p 8000:8000 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v portainer_data:/data \
  portainer/portainer-ce:latest

# Access at: http://localhost:9000
```

---

## Common Issues & Solutions

### Issue: Port Already in Use

```bash
# Find what's using port 80
lsof -i :80

# Or use different port
docker run -d -p 8080:80 nginx
```

### Issue: Container Exits Immediately

```bash
# Check logs
docker logs <container_id>

# Run interactively to debug
docker run -it <image> /bin/sh
```

### Issue: Permission Denied

```bash
# Check container user permissions
docker exec <container> id

# Fix volume permissions
docker run -v $(pwd):/data --privileged <image>
```

### Issue: Image Not Found

```bash
# Check image exists
docker search nginx

# Or pull with full path
docker pull library/nginx:latest
```

---

## Quick Reference

```bash
# Pull & Run
docker pull nginx
docker run -d -p 8080:80 nginx

# List
docker ps
docker ps -a

# Logs
docker logs -f <name>

# Execute
docker exec -it <name> bash

# Stop & Remove
docker stop <name>
docker rm <name>
```

---

## Related Documentation

- [Docker Run Reference](https://docs.docker.com/engine/reference/run/)
- [Docker CLI Reference](https://docs.docker.com/engine/reference/commandline/cli/)
- [Portainer Documentation](https://docs.portainer.io/)

---

## Additional Resources

| Resource | Description |
|----------|-------------|
| [Docker Official Docs](https://docs.docker.com/) | Complete Docker documentation |
| [Docker CLI Reference](https://docs.docker.com/engine/reference/commandline/) | All Docker commands |
| [Portainer Setup Guide](./Portainer_Setup.md) | Web-based container management |
| [Play with Docker](https://labs.play-with-docker.com/) | Free online Docker playground |
| [Docker Hub](https://hub.docker.com/) | Public image registry |
