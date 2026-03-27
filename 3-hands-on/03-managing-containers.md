# Exercise 3: Managing Containers
## Container Lifecycle & Inspection

---

## 🎯 Goal

Learn to:
- Start, stop, restart containers
- Execute commands in running containers
- Inspect container details
- View and follow logs
- Copy files to/from containers

**Time: ~20 minutes**

---

## 1️⃣ Container Lifecycle

```bash
# Create container (don't start)
docker create --name my-app nginx:alpine

# Start container
docker start my-app

# Stop container
docker stop my-app

# Restart container
docker restart my-app

# Or use run (create + start)
docker run -d --name my-app nginx:alpine
```

### Pause/Unpause

```bash
docker pause my-app    # Freeze container
docker unpause my-app  # Resume container
```

---

## 2️⃣ Execute Commands

Run commands inside a running container:

```bash
# Run single command
docker exec my-app ls /usr/share/nginx/html

# Run with output
docker exec my-app cat /etc/alpine-release

# Interactive shell
docker exec -it my-app sh
```

### Practical Examples

```bash
# Check nginx config
docker exec my-app cat /etc/nginx/nginx.conf

# List running processes
docker exec my-app ps aux

# Check environment
docker exec my-app env

# Exit shell
exit
```

---

## 3️⃣ Inspect Containers

Get detailed information about a container:

```bash
# Full inspection
docker inspect my-app

# Get specific fields (JSON)
docker inspect --format '{{.NetworkSettings.IPAddress}}' my-app
docker inspect --format '{{.Config.Image}}' my-app
docker inspect --format '{{.State.Status}}' my-app
```

### Useful Format Options

| Field | Command |
|-------|---------|
| IP Address | `{{.NetworkSettings.IPAddress}}` |
| Image | `{{.Config.Image}}` |
| Status | `{{.State.Status}}` |
| Ports | `{{.NetworkSettings.Ports}}` |

---

## 4️⃣ View Logs

```bash
# View logs
docker logs my-app

# Follow logs (real-time)
docker logs -f my-app

# Last 20 lines
docker logs --tail 20 my-app

# Logs since timestamp
docker logs --since "2024-01-01" my-app
```

---

## 5️⃣ Copy Files

```bash
# Copy FROM container TO host
docker cp my-app:/etc/nginx/nginx.conf ./nginx.conf

# Copy FROM host TO container
echo "test" > test.txt
docker cp test.txt my-app:/tmp/test.txt

# Verify
docker exec my-app cat /tmp/test.txt
```

---

## 6️⃣ Resource Stats

```bash
# Live stats for all containers
docker stats

# Stats for specific container
docker stats my-app

# One-time stats
docker stats --no-stream my-app
```

---

## 🧪 Challenge

Debug a container step by step:

1. Run a container
2. Execute `ps aux` inside it
3. Copy its config file to your host
4. View its logs
5. Stop and clean up

```bash
# 1. Run
docker run -d --name debug-test nginx:alpine

# 2. Execute
docker exec debug-test ps aux

# 3. Copy
docker cp debug-test:/etc/nginx/nginx.conf ./debug-nginx.conf

# 4. View logs
docker logs debug-test

# 5. Clean up
docker stop debug-test && docker rm debug-test
```

---

## ✅ Checklist

- [ ] Start/stop/restart containers
- [ ] Execute commands with `docker exec`
- [ ] Inspect container details
- [ ] View container logs
- [ ] Copy files to/from containers

---

## 🚀 Next Steps

**Go to Exercise 4:** [Networks & Volumes](./04-networks-volumes.md)
