# Portainer Setup Guide

## Overview

Portainer is a lightweight web-based container management UI that simplifies Docker management through an intuitive graphical interface. It complements CLI operations and is especially useful for visualizing container relationships and managing resources.

```
┌─────────────────────────────────────────────────────────────────┐
│                    Portainer Architecture                         │
│                                                                  │
│  ┌──────────────┐         ┌──────────────────────────────┐     │
│  │   Browser    │◀───────▶│        Portainer            │     │
│  │   (HTTP)     │         │        Container             │     │
│  └──────────────┘         │  ┌────────────────────────┐  │     │
│                            │  │   Web Server (Nginx)  │  │     │
│                            │  │   Port: 9000, 8000    │  │     │
│                            │  ├────────────────────────┤  │     │
│                            │  │   Portainer Backend    │  │     │
│                            │  │   API & Business Logic │  │     │
│  ┌──────────────┐         │  └────────────────────────┘  │     │
│  │   Docker     │◀────────│         │                    │     │
│  │   Daemon     │         └─────────┼────────────────────┘     │
│  │   (API)      │                   │                          │
│  └──────────────┘                   │ /var/run/docker.sock    │
└─────────────────────────────────────┼──────────────────────────┘
                                      │
                            ┌─────────▼──────────┐
                            │   Portainer Data    │
                            │   (Named Volume)    │
                            │   /data             │
                            └─────────────────────┘
```

---

## Installation Methods

### Method 1: Docker CLI (Recommended)

#### Prerequisites

- Docker Engine installed and running
- Ports 9000 and 8000 available
- Access to Docker socket

#### Installation Steps

**Step 1: Create Portainer Data Volume**

```bash
docker volume create portainer_data
```

**Step 2: Run Portainer Container**

```bash
docker run -d \
  --name portainer \
  --restart=always \
  -p 9000:9000 \
  -p 8000:8000 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v portainer_data:/data \
  portainer/portainer-ce:latest
```

#### Docker Compose Method

Create `docker-compose.yml`:

```yaml
version: "3.8"

services:
  portainer:
    image: portainer/portainer-ce:latest
    container_name: portainer
    restart: unless-stopped
    security_opts:
      - no-new-privileges:true
    volumes:
      - /etc/localtime:/etc/localtime:ro
      - /var/run/docker.sock:/var/run/docker.sock
      - ./portainer-data:/data
    ports:
      - 9000:9000
      - 8000:8000
```

Run with:

```bash
docker-compose up -d
```

---

### Method 2: Portainer Agent (Remote Management)

For managing remote Docker hosts or Swarms:

#### Install on Remote Host

```bash
docker run -d \
  --name portainer-agent \
  --restart=always \
  -p 9001:9001 \
  -p 9002:9002 \
  -e AGENT_CLUSTER_ADDR=192.168.1.100 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /var/lib/portainer-agent/data:/var/lib/portainer-agent/data \
  portainer/agent:latest
```

#### Connect from Portainer

1. Go to Home > Environments > Add environment
2. Select "Agent"
3. Enter remote host IP and port 9001
4. Click "Connect"

---

### Method 3: Portainer Business Edition (Trial)

For production environments with advanced features:

```bash
docker volume create portainer_data

docker run -d \
  --name portainer \
  --restart=always \
  -p 9000:9000 \
  -p 8000:8000 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v portainer_data:/data \
  portainer/portainer-ee:latest
```

> Note: Portainer Business requires a license key after 14-day trial.

---

## Initial Setup

### Step-by-Step Guide

1. **Open Portainer**
   - Navigate to: http://localhost:9000
   - First-time setup wizard appears

2. **Create Admin User**
   ```
   ┌─────────────────────────────────────────┐
   │       Create Admin User                │
   │                                         │
   │  Username: admin                       │
   │  Password: ************                 │
   │  Confirm:  ************                 │
   │                                         │
   │  ☑ Use a random 32-byte secret         │
   │                                         │
   │         [Create User]                   │
   └─────────────────────────────────────────┘
   ```

3. **Select Environment**
   ```
   ┌─────────────────────────────────────────┐
   │       Get Started                       │
   │                                         │
   │  Which environment do you want to       │
   │  manage?                                │
   │                                         │
   │  ┌─────────────────────────────────┐   │
   │  │ 🐳 Docker                       │   │
   │  │   Manage a local Docker         │   │
   │  │   environment                   │   │
   │  └─────────────────────────────────┘   │
   │                                         │
   │  ┌─────────────────────────────────┐   │
   │  │ ☁ Kubernetes                    │   │
   │  │   Connect to a K8s environment  │   │
   │  └─────────────────────────────────┘   │
   │                                         │
   │  ┌─────────────────────────────────┐   │
   │  │ 📦 Nomad                        │   │
   │  │   Connect to a Nomad environment│   │
   │  └─────────────────────────────────┘   │
   └─────────────────────────────────────────┘
   ```

4. **Click "Connect"** for local Docker

5. **Dashboard Overview**
   ```
   ┌─────────────────────────────────────────────────────┐
   │  Home > Docker                                      │
   │  ┌───────────────┐ ┌───────────────┐              │
   │  │ Containers: 5 │ │ Images: 12   │              │
   │  └───────────────┘ └───────────────┘              │
   │  ┌───────────────┐ ┌───────────────┐              │
   │  │ Volumes: 3   │ │ Networks: 4   │              │
   │  └───────────────┘ └───────────────┘              │
   └─────────────────────────────────────────────────────┘
   ```

---

## Features Overview

### Container Management

| Feature | Description | Access Path |
|---------|-------------|-------------|
| List Containers | View all containers with status | Containers > List |
| Start/Stop | Control container state | Containers > Actions |
| Create | Launch new containers | Containers > Add container |
| Inspect | View container details | Containers > Inspect |
| Logs | Real-time log viewer | Containers > Logs |
| Console | Terminal access | Containers > Console |
| Duplicate | Clone container config | Containers > Duplicate |
| Remove | Delete containers | Containers > Remove |

### Image Management

| Feature | Description | Access Path |
|---------|-------------|-------------|
| List Images | View downloaded images | Images > List |
| Pull Image | Download from registry | Images > Pull image |
| Build Image | Build from Dockerfile | Images > Build image |
| Tag Image | Add version tags | Images > Tag |
| Remove Image | Delete images | Images > Remove |
| Prune Images | Clean unused images | Images > Prune |

### Network Management

| Feature | Description |
|---------|-------------|
| List Networks | View all Docker networks |
| Create Network | Create new bridge/overlay networks |
| Inspect Network | View network configuration |
| Remove Network | Delete unused networks |

### Volume Management

| Feature | Description |
|---------|-------------|
| List Volumes | View all named volumes |
| Create Volume | Create new persistent volumes |
| Inspect Volume | View volume details and mounts |
| Remove Volume | Delete unused volumes |

---

## Advanced Configuration

### Enabling Edge Agent

For remote edge environments:

1. Go to **Settings > Edge**
2. Enable "Edge Agent async mode"
3. Configure polling interval
4. Save settings

### SSL/TLS Configuration

For secure HTTPS access:

```bash
docker stop portainer

docker run -d \
  --name portainer \
  --restart=always \
  -p 9443:9443 \
  -p 8000:8000 \
  -v portainer_data:/data \
  -v /path/to/certs:/certs \
  -v /var/run/docker.sock:/var/run/docker.sock \
  portainer/portainer-ce:latest \
  --ssl \
  --sslcert /certs/cert.pem \
  --sslkey /certs/key.pem
```

### Resource Limits

```bash
docker run -d \
  --name portainer \
  --restart=always \
  -p 9000:9000 \
  -p 8000:8000 \
  --memory="1g" \
  --cpus="1" \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v portainer_data:/data \
  portainer/portainer-ce:latest
```

### User Management

| Role | Permissions |
|------|-------------|
| **Administrator** | Full access to all features |
| **Operator** | Control containers, cannot modify settings |
| **User** | Read-only access |
| **Read-Only User** | View-only access |

---

## Troubleshooting

### Port Already in Use

```bash
# Check what's using port 9000
lsof -i :9000

# Use alternative port
docker run -d \
  --name portainer \
  -p 9100:9000 \
  -p 8001:8000 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v portainer_data:/data \
  portainer/portainer-ce:latest
```

### Permission Denied (Docker Socket)

```bash
# Check socket permissions
ls -la /var/run/docker.sock

# On Linux, add user to docker group
sudo usermod -aG docker $USER

# On macOS, ensure Docker Desktop has permissions
# System Settings > Privacy & Security > Docker
```

### Cannot Connect to Docker Daemon

```bash
# Verify Docker is running
docker info

# Restart Docker service
# macOS: Docker Desktop > Restart
# Linux: sudo systemctl restart docker
```

### Data Persistence Issues

```bash
# Verify volume exists
docker volume ls | grep portainer

# Inspect volume
docker volume inspect portainer_data

# Recreate if needed
docker volume create portainer_data
```

### Reset Portainer

```bash
# Stop and remove container
docker stop portainer
docker rm portainer

# Remove data volume (loses all data!)
docker volume rm portainer_data

# Recreate
docker volume create portainer_data
docker run -d \
  --name portainer \
  -p 9000:9000 \
  -p 8000:8000 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v portainer_data:/data \
  portainer/portainer-ce:latest
```

---

## Common Tasks via Portainer

### Create a Container

1. Go to **Containers** > **Add container**
2. Fill in:
   - Name: `my-nginx`
   - Image: `nginx:alpine`
   - Port mapping: `8080` → `80`
3. Click **Deploy the container**

### Pull an Image

1. Go to **Images** > **Pull image**
2. Enter image name: `redis:7-alpine`
3. Click **Pull**

### View Container Logs

1. Go to **Containers**
2. Click on container name
3. Select **Logs** tab
4. Enable "Stream" for real-time

### Access Container Console

1. Go to **Containers**
2. Click on container name
3. Select **Console** tab
4. Choose shell (bash/sh) and click **Connect**

---

## Quick Commands Reference

```bash
# Install Portainer
docker volume create portainer_data
docker run -d --name portainer \
  -p 9000:9000 -p 8000:8000 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v portainer_data:/data \
  portainer/portainer-ce:latest

# Stop Portainer
docker stop portainer

# Start Portainer
docker start portainer

# Restart Portainer
docker restart portainer

# Update Portainer
docker pull portainer/portainer-ce:latest
docker stop portainer
docker rm portainer
docker run -d --name portainer \
  -p 9000:9000 -p 8000:8000 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v portainer_data:/data \
  portainer/portainer-ce:latest

# Remove Portainer
docker stop portainer
docker rm portainer
docker volume rm portainer_data

# View logs
docker logs portainer

# Check status
docker ps | grep portainer
```

---

## Access URLs

| Service | URL |
|---------|-----|
| Portainer HTTP | http://localhost:9000 |
| Portainer HTTPS | https://localhost:9443 |
| Agent Port | http://localhost:9001 |

---

## Related Documentation

- [Portainer Official Documentation](https://docs.portainer.io/)
- [Portainer Installation Guide](https://docs.portainer.io/v/ce-2.11/start/install/server/docker/wsl)
- [Portainer Agent](https://docs.portainer.io/agent)
- [Portainer Business Edition](https://www.portainer.io/business)
