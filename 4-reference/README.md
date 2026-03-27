# Reference Guide
## Quick Lookups for Common Tasks

---

## 📚 In This Section

| File | Description |
|------|-------------|
| [Commands Cheatsheet](./commands-cheatsheet.md) | All Docker commands |
| [docker-compose-template.yml](./docker-compose-template.yml) | Template for compose files |

---

## 🚀 Quick Reference by Task

### Run a Container
```bash
docker run -d --name my-app -p 8080:80 nginx:alpine
```

### List Everything
```bash
docker ps                  # Running containers
docker ps -a              # All containers
docker images             # Images
docker volume ls          # Volumes
docker network ls         # Networks
```

### Stop & Remove
```bash
docker stop my-app                    # Stop
docker rm my-app                      # Remove
docker rm -f my-app                   # Force remove
docker system prune                    # Clean all unused
```

### View Logs
```bash
docker logs my-app            # All logs
docker logs -f my-app         # Follow
docker logs --tail 50 my-app  # Last 50 lines
```

### Execute Commands
```bash
docker exec -it my-app sh           # Shell
docker exec my-app ls /app           # Single command
```

### Docker Compose
```bash
docker compose up -d                 # Start
docker compose down                  # Stop
docker compose logs -f               # Logs
docker compose ps                    # Status
```

---

## 📖 Detailed Reference

### [Commands Cheatsheet](./commands-cheatsheet.md)

Comprehensive list of all Docker CLI commands organized by category:
- Container management
- Image management
- Network commands
- Volume commands
- Docker Compose commands

### [Compose Template](./docker-compose-template.yml)

Ready-to-use template for docker-compose.yml with comments.

---

## 🔗 Related Sections

- **Setup**: [2-setup/docker-compose.yml](../2-setup/docker-compose.yml)
- **Hands-on**: [3-hands-on](../3-hands-on/README.md)
- **Resources**: [resources/README.md](../resources/README.md)

---

## 👨‍🏫 Tip

Bookmark this page! You'll reference it often while working with Docker.
