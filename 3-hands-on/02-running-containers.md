# Exercise 2: Running Containers
## Advanced Container Options

---

## 🎯 Goal

Learn to run containers with:
- Port mapping
- Environment variables
- Volume mounts
- Container naming
- Interactive mode

**Time: ~25 minutes**

---

## 1️⃣ Port Mapping

Containers are isolated. To access them, map ports from host to container.

```bash
# Format: -p HOST_PORT:CONTAINER_PORT
docker run -d --name web -p 8080:80 nginx:alpine

# Check the port mapping
docker port web

# Visit http://localhost:8080
open http://localhost:8080
```

### Multiple Ports

```bash
docker run -d --name app -p 3000:3000 -p 9229:9229 node:20
```

### Clean up

```bash
docker stop web && docker rm web
```

---

## 2️⃣ Environment Variables

Pass configuration to containers via environment variables.

```bash
# Set env vars with -e
docker run -d --name db \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_DB=mydb \
  postgres:16-alpine

# Verify
docker exec db env | grep POSTGRES
```

### Multiple Variables

```bash
docker run -d --name app \
  -e NODE_ENV=production \
  -e PORT=3000 \
  -e DATABASE_URL=postgres://db:5432/mydb \
  node:20
```

### Clean up

```bash
docker stop db && docker rm db
```

---

## 3️⃣ Volume Mounts

Persist data or share files between host and container.

### Mount Local Directory

```bash
# Create a local directory
mkdir -p ~/docker-test/html

# Create a simple HTML file
echo "<h1>Hello from Docker!</h1>" > ~/docker-test/html/index.html

# Mount it to nginx
docker run -d --name web \
  -p 8080:80 \
  -v ~/docker-test/html:/usr/share/nginx/html:ro \
  nginx:alpine

# Visit http://localhost:8080
open http://localhost:8080

# Edit the file and refresh - changes appear!
echo "<h1>Updated!</h1>" > ~/docker-test/html/index.html
```

### Named Volumes

```bash
# Create a named volume
docker volume create my-data

# Use the volume
docker run -d --name db \
  -v my-data:/var/lib/postgresql/data \
  postgres:16-alpine

# Data persists even after container is removed
docker rm -f db
docker run -d --name db2 \
  -v my-data:/var/lib/postgresql/data \
  postgres:16-alpine
```

### Clean up

```bash
docker stop web db db2 && docker rm web db db2
docker volume rm my-data
```

---

## 4️⃣ Container Naming

Containers have random names by default. Give them meaningful names.

```bash
# With --name flag
docker run -d --name my-nginx nginx:alpine
docker run -d --name my-postgres postgres:16-alpine
docker run -d --name my-redis redis:7-alpine

# List by name
docker ps

# Remove by name
docker stop my-nginx my-postgres my-redis
docker rm my-nginx my-postgres my-redis
```

---

## 5️⃣ Interactive Mode

Run containers with a terminal for debugging.

```bash
# Run Ubuntu with interactive terminal
docker run -it --name my-ubuntu ubuntu:22.04 bash

# You're now inside the container!
# Try some commands:
ls
whoami
cat /etc/os-release
exit
```

### Alpine Linux (smaller)

```bash
docker run -it --name my-alpine alpine sh
```

---

## 6️⃣ Detached vs Interactive

| Mode | Flag | Use Case |
|------|------|----------|
| Detached | `-d` | Services that run in background |
| Interactive | `-it` | Debugging, shells, REPLs |
| One-off | (no flags) | Run single command |

```bash
# Detached - web server
docker run -d --name web nginx:alpine

# Interactive - Python REPL
docker run -it --name py python:3.12 python

# One-off command
docker run --rm python:3.12 python -c "print('Hello!')"
```

---

## 🧪 Challenge

Create a complete web application stack:

1. Run nginx on port 8080
2. Mount your current directory as web content
3. Set `NGINX_HOST=localhost` environment variable
4. Name it `challenge-web`

**Solution:**
```bash
docker run -d --name challenge-web \
  -p 8080:80 \
  -v $(pwd):/usr/share/nginx/html:ro \
  -e NGINX_HOST=localhost \
  nginx:alpine
```

---

## ✅ Checklist

- [ ] Run container with port mapping
- [ ] Run container with environment variables
- [ ] Mount a volume
- [ ] Name a container
- [ ] Run interactive container

---

## 🚀 Next Steps

**Go to Exercise 3:** [Managing Containers](./03-managing-containers.md)
