# Module 2: Setup
## Install Docker & Start Your First Container

---

## 🎯 Goal

By the end of this module, you will have:
- ✅ Docker Desktop installed and running
- ✅ Portainer installed (optional but recommended)
- ✅ Verified that everything works

---

## 📋 Prerequisites

Before starting, check your system:

```bash
# Check macOS version (should be 11+)
sw_vers

# Check chip (Intel or Apple Silicon)
uname -m
# arm64 = Apple Silicon
# x86_64 = Intel
```

---

## 🐳 Step 1: Install Docker Desktop

### Download Docker Desktop

1. Go to: https://www.docker.com/products/docker-desktop/
2. Click **"Download for Mac"**
3. Choose the correct version:
   - **Apple Silicon (M1/M2/M3)**: `Docker-Desktop-*-aarch64.dmg`
   - **Intel**: `Docker-Desktop-*-x86_64.dmg`

### Install

1. Double-click the `.dmg` file
2. Drag Docker to Applications
3. Launch Docker Desktop

**First launch takes 1-2 minutes.** You'll see a whale icon in the menu bar when ready.

---

## ✅ Step 2: Verify Installation

Open Terminal and run:

```bash
# 1. Check Docker version
docker --version

# 2. Check Docker Compose version
docker compose version

# 3. Run a test container
docker run hello-world

# 4. List containers (should be empty)
docker ps -a
```

Expected output for `docker run hello-world`:
```
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

---

## 🖥️ Step 3: Install Portainer (Recommended)

Portainer gives you a **web-based GUI** to manage containers. Highly recommended for beginners!

### Quick Install

```bash
# Create a volume for Portainer data
docker volume create portainer_data

# Run Portainer
docker run -d \
  --name portainer \
  --restart unless-stopped \
  -p 9000:9000 \
  -p 9443:9443 \
  -p 8000:8000 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v portainer_data:/data \
  portainer/portainer-ce:latest
```

Or use our **pre-configured docker-compose.yml**:

```bash
# From the setup folder
cd setup
docker compose up -d
```

### Access Portainer

| URL | Description |
|-----|-------------|
| http://localhost:9000 | HTTP (non-secure) |
| https://localhost:9443 | HTTPS (secure) |

### Portainer Setup Wizard

1. Open http://localhost:9000
2. Create admin password (min 8 characters)
3. Click "Create User"
4. Select "Docker" environment
5. Click "Connect"

**Congratulations!** You now have a visual Docker management interface.

---

## 🧪 Step 4: Test Your Setup

### Test 1: Run a Web Server

```bash
# Run nginx web server
docker run -d --name my-nginx -p 8080:80 nginx:alpine

# Check it's running
docker ps

# Open in browser
open http://localhost:8080

# Stop it
docker stop my-nginx

# Clean up
docker rm my-nginx
```

### Test 2: Run a Database

```bash
# Run PostgreSQL
docker run -d \
  --name my-postgres \
  -e POSTGRES_PASSWORD=secret \
  -p 5432:5432 \
  postgres:16-alpine

# Check logs
docker logs my-postgres

# Connect (optional)
docker exec -it my-postgres psql -U postgres

# Clean up
docker stop my-postgres && docker rm my-postgres
```

### Test 3: Run Redis Cache

```bash
# Run Redis
docker run -d \
  --name my-redis \
  -p 6379:6379 \
  redis:7-alpine

# Test connection
docker exec -it my-redis redis-cli ping
# Should return: PONG

# Clean up
docker stop my-redis && docker rm my-redis
```

---

## 🔧 Useful Commands

### Check Docker Status

```bash
docker info                    # Full system info
docker version               # Version info
docker ps                    # Running containers
docker ps -a                 # All containers
```

### Clean Up

```bash
# Remove all stopped containers
docker container prune

# Remove all unused images
docker image prune -a

# Remove all unused data
docker system prune -a
```

### View Logs

```bash
docker logs portainer         # View logs
docker logs -f portainer      # Follow logs
docker logs --tail 50 portainer  # Last 50 lines
```

---

## 🐛 Troubleshooting

### "Cannot connect to Docker daemon"

```bash
# Docker Desktop isn't running
open -a Docker

# Wait 30 seconds, then try again
docker ps
```

### "Port already in use"

```bash
# Find what's using the port
lsof -i :8080

# Stop that service or use a different port
```

### "Container exits immediately"

```bash
# Check logs
docker logs <container_name>

# Run interactively to debug
docker run -it nginx:alpine /bin/sh
```

---

## ✅ Setup Checklist

Before moving on, confirm:

- [ ] `docker --version` works
- [ ] `docker run hello-world` works
- [ ] Portainer is accessible at http://localhost:9000
- [ ] You can start and stop containers

---

## 🚀 Next Steps

**You're ready to start hands-on learning!**

Go to: [Module 3: CLI Essentials](../3-hands-on/01-cli-essentials.md)

Or if you prefer learning by doing, skip to:
- [Running Containers](../3-hands-on/02-running-containers.md)
- [Docker Compose](../3-hands-on/05-docker-compose.md)

---

## 📁 Files in This Folder

```
setup/
├── README.md                 # ← You are here
└── docker-compose.yml        # Portainer setup file
```

### The docker-compose.yml

This file sets up Portainer with a single command:

```bash
docker compose up -d
```

---

## 👨‍🏫 Tip from Your Mentor

> **"Master the basics first."**
>
> Before diving into complex setups, make sure you can:
> 1. Start/stop containers
> 2. View logs
> 3. Clean up
>
> These basics will save you hours of debugging later.

---

**Next: [Module 3: CLI Essentials](../3-hands-on/01-cli-essentials.md)**
