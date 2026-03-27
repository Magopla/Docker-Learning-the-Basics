# Exercise 4: Networks & Volumes
## Data Persistence & Container Communication

---

## 🎯 Goal

Learn to:
- Create and manage Docker networks
- Connect containers to networks
- Use volumes for data persistence
- Enable container-to-container communication

**Time: ~30 minutes**

---

## 1️⃣ Docker Networks

### Network Drivers

| Driver | Description | Use Case |
|--------|-------------|----------|
| `bridge` | Default, single host | Most common |
| `host` | Remove network isolation | Performance critical |
| `overlay` | Multi-host | Swarm clusters |
| `none` | No networking | Isolated containers |

### Default Bridge Network

```bash
# All containers connect to default bridge
docker run -d --name app1 nginx:alpine
docker run -d --name app2 nginx:alpine

# Check they're on same network
docker inspect app1 --format '{{.NetworkSettings.Networks}}'
```

### Custom Bridge Network

```bash
# Create a custom network
docker network create my-network

# Run containers on this network
docker run -d --name web --network my-network nginx:alpine
docker run -d --name api --network my-network redis:7-alpine

# Containers can reach each other by name!
docker exec web ping -c 1 api

# List networks
docker network ls
```

### Inspect Network

```bash
docker network inspect my-network
```

### Remove Network

```bash
docker network rm my-network
```

---

## 2️⃣ Container Communication

Containers on the same network can communicate:

```bash
# Create network
docker network create demo-net

# Run nginx (will respond to ping)
docker run -d --name web --network demo-net nginx:alpine

# Run alpine with ping
docker run -d --name client --network demo-net alpine sleep infinity

# Ping from client to web
docker exec client ping -c 3 web

# Containers use service names as hostnames
docker exec client wget -O- http://web
```

### Clean up

```bash
docker stop web client
docker rm web client
docker network rm demo-net
```

---

## 3️⃣ Volumes for Persistence

### Volume Types

| Type | Syntax | Use Case |
|------|--------|----------|
| Named volume | `-v my-volume:/path` | Persistent data |
| Bind mount | `-v /host/path:/container/path` | Development |
| tmpfs | `--tmpfs /path` | Sensitive data (RAM) |

### Named Volumes

```bash
# Create volume
docker volume create my-data

# Use volume with container
docker run -d --name db \
  -v my-data:/var/lib/postgresql/data \
  postgres:16-alpine

# Write some data (simulate)
docker exec db psql -U postgres -c "CREATE TABLE test (id int);"

# Data persists after container removal!
docker rm -f db

# Start new container with same volume
docker run -d --name db2 \
  -v my-data:/var/lib/postgresql/data \
  postgres:16-alpine

# Data is still there!
docker exec db2 psql -U postgres -c "\dt"

# Clean up
docker rm -f db2
docker volume rm my-data
```

### Bind Mounts (Host Directory)

```bash
# Create host directory
mkdir -p ~/docker-data/app

# Mount to container
docker run -d --name dev \
  -v ~/docker-data/app:/app \
  -w /app \
  node:20 node -e "require('fs').writeFileSync('/app/test.txt', 'Hello')"

# Check on host
cat ~/docker-data/app/test.txt
```

---

## 4️⃣ Practical Example: Database Stack

```bash
# Create network
docker network create app-net

# Run PostgreSQL
docker run -d \
  --name postgres \
  --network app-net \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_DB=mydb \
  -v postgres-data:/var/lib/postgresql/data \
  postgres:16-alpine

# Run pgAdmin (web UI for PostgreSQL)
docker run -d \
  --name pgadmin \
  --network app-net \
  -p 8080:80 \
  -e PGADMIN_DEFAULT_EMAIL=admin@admin.com \
  -e PGADMIN_DEFAULT_PASSWORD=admin \
  dpage/pgadmin4:latest

# In pgAdmin, connect to: postgres:5432
# (container name as hostname works!)

# Clean up
docker stop postgres pgadmin
docker rm postgres pgadmin
docker network rm app-net
docker volume rm postgres-data
```

---

## 🧪 Challenge

Create a two-container setup:
1. Redis cache (port 6379)
2. A script that writes to Redis

```bash
# 1. Create network
docker network create redis-net

# 2. Run Redis
docker run -d --name redis --network redis-net redis:7-alpine

# 3. Run a client that writes to Redis
docker run --rm --network redis-net \
  redis:7-alpine redis-cli -h redis SET test "Hello Redis!"

# 4. Read from Redis
docker run --rm --network redis-net \
  redis:7-alpine redis-cli -h redis GET test

# 5. Clean up
docker rm -f redis
docker network rm redis-net
```

---

## ✅ Checklist

- [ ] Create a custom bridge network
- [ ] Connect containers to network
- [ ] Use container names for DNS
- [ ] Create and use named volumes
- [ ] Persist data across container restarts

---

## 🚀 Next Steps

**Go to Exercise 5:** [Docker Compose](./05-docker-compose.md)
