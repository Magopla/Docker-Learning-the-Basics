# Exercise 6: Portainer
## Visual Container Management

---

## 🎯 Goal

Learn to:
- Access and use Portainer web interface
- Manage containers visually
- View logs and inspect containers
- Manage images and volumes

**Time: ~15 minutes**

---

## 1️⃣ What is Portainer?

Portainer is a **web-based GUI** for managing Docker containers.

```
┌─────────────────────────────────────────────────────────────────┐
│                    PORTAINER INTERFACE                           │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  🐳 Portainer                    [Admin ▼]              │   │
│  ├─────────────────────────────────────────────────────────┤   │
│  │                                                         │   │
│  │  Dashboard                                              │   │
│  │  ┌────────────┐ ┌────────────┐ ┌────────────┐          │   │
│  │  │Containers │ │   Images   │ │  Volumes   │          │   │
│  │  │     5     │ │     12    │ │     3     │          │   │
│  │  └────────────┘ └────────────┘ └────────────┘          │   │
│  │                                                         │   │
│  │  Quick Actions                                          │   │
│  │  ┌─────────────────────────────────────────────────┐  │   │
│  │  │ [+ Create Container]  [Pull Image]  [Networks] │  │   │
│  │  └─────────────────────────────────────────────────┘  │   │
│  │                                                         │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2️⃣ Access Portainer

If you haven't installed Portainer yet:

```bash
# From the setup folder
cd 2-setup
docker compose up -d
```

**Open your browser:**
- http://localhost:9000 (HTTP)
- https://localhost:9443 (HTTPS)

**First-time setup:**
1. Create admin password
2. Click "Create User"
3. Select "Docker" environment
4. Click "Connect"

---

## 3️⃣ Dashboard Overview

The dashboard shows:
- **Containers**: Running/Stopped count
- **Images**: Downloaded images
- **Volumes**: Persistent storage
- **Networks**: Docker networks

---

## 4️⃣ Manage Containers

### View Containers
1. Click **"Containers"** in the sidebar
2. See all containers with status

### Start/Stop Container
1. Click the container name
2. Click **"Stop"** or **"Start"** button

### Create New Container
1. Click **"+ Add container"**
2. Fill in:
   - Name: `test-container`
   - Image: `nginx:alpine`
   - Port mapping: `8080:80`
3. Click **"Deploy the container"**

### View Logs
1. Click container name
2. Select **"Logs"** tab
3. Toggle **"Stream"** for real-time logs

### Access Console
1. Click container name
2. Select **"Console"** tab
3. Choose shell (bash/sh)
4. Click **"Connect"**

---

## 5️⃣ Manage Images

1. Click **"Images"** in sidebar
2. View all downloaded images
3. **Pull image**: Click **"Pull image"**, enter name
4. **Remove image**: Click the trash icon

---

## 6️⃣ Manage Volumes

1. Click **"Volumes"** in sidebar
2. See all volumes with size
3. **Create volume**: Click **"+ Add volume"**
4. **Remove volume**: Click the trash icon

---

## 7️⃣ Quick Actions

| Action | Where | How |
|--------|-------|-----|
| Start container | Containers | Click play button |
| Stop container | Containers | Click stop button |
| View logs | Container detail | Logs tab |
| Shell access | Container detail | Console tab |
| Inspect JSON | Container detail | Inspect tab |
| Remove container | Container detail | Actions → Delete |

---

## 🧪 Try This in Portainer

1. **Pull an image**: `redis:7-alpine`
2. **Create container**: `my-redis` with port `6379:6379`
3. **View logs**: See Redis startup
4. **Access console**: Run `redis-cli ping`
5. **Stop & remove**: Clean up

---

## ✅ Checklist

- [ ] Access Portainer at http://localhost:9000
- [ ] View containers list
- [ ] Create a new container via GUI
- [ ] View container logs
- [ ] Access container console
- [ ] Pull an image
- [ ] Stop and remove a container

---

## 🚀 Next Steps

**Congratulations! You've completed all exercises!**

Go to: [Commands Cheatsheet](../4-reference/commands-cheatsheet.md) for a quick reference.
