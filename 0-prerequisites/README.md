# Module 0: Prerequisites
## What You Need Before Starting

---

## 🎯 Goal

By the end of this module, you will have:
- ✅ A running Docker installation
- ✅ Verified that Docker works correctly
- ✅ Understood the basic requirements

---

## 📋 System Requirements

### For macOS

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| macOS Version | 11 (Big Sur) | 13 (Ventura) or later |
| RAM | 4 GB | 8 GB |
| Disk Space | 8 GB free | 20 GB free |
| Processor | Intel or Apple Silicon | Apple Silicon (M1/M2/M3) |

### For Linux (Reference)

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| Ubuntu | 20.04 LTS | 22.04 LTS |
| RAM | 2 GB | 4 GB |
| Disk Space | 10 GB | 20 GB |
| 64-bit architecture | ✅ Required | ✅ Required |

### For Windows (Reference)

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| Windows | 10/11 Pro | 11 Pro |
| WSL2 | Required | Required |
| RAM | 4 GB | 8 GB |
| Disk Space | 8 GB | 15 GB |

---

## 🖥️ Which Platform Are You Using?

```
┌─────────────────────────────────────────────────────────────────┐
│                      SELECT YOUR PLATFORM                         │
│                                                                  │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐           │
│  │   macOS     │  │   Linux     │  │   Windows   │           │
│  │   🍎        │  │   🐧        │  │   🪟        │           │
│  │             │  │             │  │             │           │
│  │ Go to:      │  │ Go to:      │  │ Use WSL2    │           │
│  │ Setup Guide │  │ Linux Docs  │  │ + Docker    │           │
│  └─────────────┘  └─────────────┘  └─────────────┘           │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📦 Installing Docker on macOS (Recommended)

### Method 1: Docker Desktop (Easiest)

**Step 1: Download Docker Desktop**

Visit: https://www.docker.com/products/docker-desktop/

Click "Download for Mac" and choose:
- **Apple Silicon (M1/M2/M3)**: `Docker-Desktop-*-aarch64.dmg`
- **Intel Mac**: `Docker-Desktop-*-x86_64.dmg`

**Step 2: Install**

1. Double-click the `.dmg` file
2. Drag Docker icon to Applications folder
3. Launch Docker Desktop from Applications

**Step 3: Wait for Setup**

First launch takes 1-2 minutes. You'll see:
```
┌─────────────────────────────────────┐
│  Docker Desktop is starting...       │
│  ████████████████░░░░░ 80%          │
└─────────────────────────────────────┘
```

**Step 4: Verify Installation**

Open Terminal and run:

```bash
docker --version
```

Expected output:
```
Docker version 26.0.0, build xxxxxxx
```

### Method 2: Homebrew

```bash
# Install Docker Desktop via Homebrew
brew install --cask docker

# Launch Docker Desktop
open -a Docker
```

---

## ✅ Verify Your Installation

### Test 1: Docker Daemon

```bash
docker info 2>&1 | head -5
```

Expected output:
```
Client:
 Version:    26.0.0
 OS/Arch:    darwin/arm64
```

### Test 2: Run Hello World

```bash
docker run hello-world
```

Expected output:
```
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

### Test 3: Check Docker Status

```bash
docker ps
```

Expected output:
```
CONTAINER ID   IMAGE   COMMAND   CREATED   STATUS   PORTS   NAMES
```

(Empty list is correct - no containers running)

---

## 🐛 Troubleshooting Installation

### Issue: "Cannot connect to Docker daemon"

**Error:**
```
Cannot connect to the Docker daemon at unix:///Users/.../docker.sock
```

**Solution:**
```bash
# Docker Desktop isn't running
open -a Docker

# Wait 30 seconds, then verify
docker ps
```

---

### Issue: "Docker Desktop is not running"

**Solution:**
1. Open Applications folder
2. Double-click Docker icon
3. Wait for "Docker Desktop is running" in menu bar

---

### Issue: Apple Silicon (M1/M2/M3) Warnings

**Don't panic!** Apple Silicon Macs work great with Docker. You may see:
- "Running on Apple Silicon" - ✅ Normal
- Rosetta messages - ✅ Normal, for compatibility

---

## 🚀 Next Steps

Great! Docker is installed. Now let's continue:

### Option A: Jump to Concepts
Learn WHY Docker exists before using it.

📄 [Go to Module 1: Docker Concepts](../1-docker-concepts/README.md)

### Option B: Jump to Hands-On
Skip theory and start running containers.

📄 [Go to Module 3: CLI Essentials](../3-hands-on/01-cli-essentials.md)

---

## 📝 Quick Reference

### Docker Desktop Locations

| Item | Location |
|------|----------|
| Docker Desktop App | `/Applications/Docker.app` |
| Settings | Menu bar → Docker icon → Settings |
| Data | `~/Library/Containers/com.docker.docker` |

### Useful Commands

```bash
docker --version              # Check version
docker info                   # System info
open -a Docker               # Open Docker Desktop
```

---

## ✅ Module 0 Checklist

Before moving on, confirm you can do this:

- [ ] `docker --version` shows a version number
- [ ] `docker run hello-world` works
- [ ] `docker ps` shows an empty list

---

## 👨‍🏫 Tip from Your Mentor

> **"Don't skip the setup!"**
> 
> I know you're excited to start running containers. But spending 5 extra minutes to ensure Docker is correctly installed will save you hours of frustration later.
>
> If `hello-world` doesn't work, Google the exact error message. Someone else has had your problem and posted a solution.

---

**Next: [Module 1: Docker Concepts](../1-docker-concepts/README.md)**
