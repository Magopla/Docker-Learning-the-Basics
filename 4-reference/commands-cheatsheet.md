# Docker Commands Cheatsheet
## Quick Reference for Common Commands

---

## 📦 Container Commands

### Create & Run

```bash
docker run nginx:alpine                          # Run container
docker run -d nginx:alpine                       # Detached mode
docker run -it ubuntu bash                      # Interactive
docker run --name my-app nginx:alpine           # Named
docker run -p 8080:80 nginx:alpine             # Port mapping
docker run -e NODE_ENV=prod nginx:alpine       # Environment var
docker run -v ~/data:/data nginx:alpine         # Volume mount
docker run --rm nginx:alpine                    # Auto-remove after stop
docker run -w /app node:20 npm start            # Working directory
```

### List & Inspect

```bash
docker ps                                 # Running containers
docker ps -a                             # All containers
docker ps -q                             # Only IDs
docker ps --format "table {{.Names}}\t{{.Status}}"  # Format
docker inspect my-container              # Full details
docker inspect --format '{{.NetworkSettings.IPAddress}}' my-container
docker port my-container                 # Port mappings
```

### Start, Stop, Restart

```bash
docker start my-container                # Start
docker stop my-container                 # Stop
docker restart my-container              # Restart
docker pause my-container                # Pause
docker unpause my-container              # Unpause
```

### Remove

```bash
docker rm my-container                  # Remove stopped
docker rm -f my-container               # Force remove
docker rm $(docker ps -aq)              # Remove all containers
docker container prune                   # Remove stopped containers
```

---

## 🖼️ Image Commands

```bash
docker images                           # List images
docker images -a                        # Include intermediate
docker pull nginx:alpine                # Pull image
docker rmi nginx:alpine                 # Remove image
docker rmi $(docker images -q)           # Remove all images
docker image prune                       # Remove unused
docker image prune -a                    # Remove all unused
docker build -t myapp:1.0 .             # Build image
docker tag myapp:latest myapp:1.0       # Tag image
docker tag myapp:latest user/myapp:latest  # Tag for registry
docker history nginx:alpine              # Image layers
```

---

## 🔍 Logs & Debug

```bash
docker logs my-container                 # View logs
docker logs -f my-container             # Follow logs
docker logs --tail 50 my-container      # Last 50 lines
docker logs --since "1h" my-container   # Last hour
docker exec -it my-container sh          # Shell access
docker exec my-container ls /app        # Run command
docker cp my-container:/file.txt .      # Copy from container
docker cp app.txt my-container:/tmp/     # Copy to container
docker diff my-container                 # Changes to container
docker top my-container                 # Running processes
docker stats                            # Resource usage
docker stats my-container               # Specific container
```

---

## 🌐 Network Commands

```bash
docker network ls                       # List networks
docker network create my-net            # Create network
docker network inspect my-net           # Inspect
docker network connect my-net container # Connect
docker network disconnect my-net container  # Disconnect
docker network rm my-net                # Remove
docker network prune                    # Remove unused
```

---

## 💾 Volume Commands

```bash
docker volume ls                        # List volumes
docker volume create my-data            # Create volume
docker volume inspect my-data          # Inspect
docker volume rm my-data                # Remove
docker volume prune                     # Remove unused
```

---

## 🐳 Docker Compose

```bash
docker compose up -d                    # Start services
docker compose up -d --build           # Build + start
docker compose down                     # Stop services
docker compose down -v                 # Also remove volumes
docker compose ps                       # List services
docker compose logs -f                 # Follow logs
docker compose logs -f web              # Specific service
docker compose exec web sh              # Shell into service
docker compose exec db psql -U postgres # Command in service
docker compose restart web              # Restart service
docker compose stop                     # Stop (keep containers)
docker compose start                    # Start stopped services
docker compose config                   # Validate file
docker compose build                    # Build images
docker compose pull                     # Pull images
docker compose top                      # Running processes
```

---

## 🔧 System Commands

```bash
docker info                            # System info
docker version                          # Version
docker system df                       # Disk usage
docker system prune                     # Clean up
docker system prune -a                  # Full cleanup
docker system prune --volumes          # Include volumes
docker builder prune                   # Build cache
```

---

## 📋 Common Flags Reference

| Flag | Description | Example |
|------|-------------|---------|
| `-d` | Detached mode | `docker run -d` |
| `-it` | Interactive + TTY | `docker run -it` |
| `-p 8080:80` | Port mapping | `docker run -p 8080:80` |
| `-e VAR=value` | Environment variable | `docker run -e NODE_ENV=prod` |
| `-v /path:/path` | Volume mount | `docker run -v ~/data:/data` |
| `--name` | Container name | `docker run --name web` |
| `--rm` | Auto-remove | `docker run --rm` |
| `-w` | Working directory | `docker run -w /app` |
| `--network` | Network | `docker run --network my-net` |
| `-f` | Force | `docker rm -f` |

---

## 🚨 Status Codes

| Exit Code | Meaning |
|-----------|---------|
| 0 | Clean exit |
| 1 | General error |
| 125 | Docker daemon error |
| 126 | Command cannot execute |
| 127 | Command not found |
| 137 | OOM (Out of Memory) killed |
| 143 | SIGTERM received |

---

## 📝 Common Workflows

### Run a Web Server
```bash
docker run -d -p 8080:80 --name web nginx:alpine
```

### Run a Database
```bash
docker run -d \
  --name db \
  -e POSTGRES_PASSWORD=secret \
  -v db-data:/var/lib/postgresql/data \
  postgres:16-alpine
```

### Full Cleanup
```bash
docker stop $(docker ps -aq) && docker rm $(docker ps -aq)
docker image prune -a
docker volume prune
```

### Update Container
```bash
docker pull nginx:alpine
docker stop my-nginx && docker rm my-nginx
docker run -d --name my-nginx -p 8080:80 nginx:alpine
```
