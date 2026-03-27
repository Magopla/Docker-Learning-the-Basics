# Module 3: Hands-On Exercises
## Practice What You've Learned

---

## 🎯 Goal

Get hands-on experience with Docker through guided exercises. By the end of this module, you'll be able to:
- ✅ Use Docker CLI confidently
- ✅ Run and manage containers
- ✅ Work with volumes and networks
- ✅ Use Docker Compose for multi-container setups
- ✅ Manage containers via Portainer

---

## 📚 Exercise Order

Follow these exercises in order. Each builds on the previous one.

```
┌─────────────────────────────────────────────────────────────────┐
│                    EXERCISE ROADMAP                              │
│                                                                  │
│  ┌─────────────────┐                                           │
│  │   Exercise 1     │  CLI Essentials                           │
│  │   🖥️ basics     │  docker run, pull, ps, logs              │
│  └────────┬────────┘                                           │
│           │                                                     │
│           ▼                                                     │
│  ┌─────────────────┐                                           │
│  │   Exercise 2     │  Running Containers                       │
│  │   🚀 containers  │  Ports, volumes, env vars                 │
│  └────────┬────────┘                                           │
│           │                                                     │
│           ▼                                                     │
│  ┌─────────────────┐                                           │
│  │   Exercise 3     │  Managing Containers                      │
│  │   🔧 lifecycle   │  Start, stop, exec, inspect              │
│  └────────┬────────┘                                           │
│           │                                                     │
│           ▼                                                     │
│  ┌─────────────────┐                                           │
│  │   Exercise 4     │  Networks & Volumes                       │
│  │   🌐 storage     │  Data persistence, container comms        │
│  └────────┬────────┘                                           │
│           │                                                     │
│           ▼                                                     │
│  ┌─────────────────┐                                           │
│  │   Exercise 5     │  Docker Compose                           │
│  │   📝 compose     │  Multi-container apps                     │
│  └────────┬────────┘                                           │
│           │                                                     │
│           ▼                                                     │
│  ┌─────────────────┐                                           │
│  │   Exercise 6     │  Portainer                               │
│  │   🖥️ GUI        │  Visual container management              │
│  └─────────────────┘                                           │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📋 Exercise Summary

| # | Exercise | Time | Difficulty |
|---|----------|------|------------|
| 1 | [CLI Essentials](./01-cli-essentials.md) | 20 min | ⭐ Beginner |
| 2 | [Running Containers](./02-running-containers.md) | 25 min | ⭐ Beginner |
| 3 | [Managing Containers](./03-managing-containers.md) | 20 min | ⭐⭐ Intermediate |
| 4 | [Networks & Volumes](./04-networks-volumes.md) | 30 min | ⭐⭐ Intermediate |
| 5 | [Docker Compose](./05-docker-compose.md) | 40 min | ⭐⭐⭐ Advanced |
| 6 | [Portainer](./06-portainer.md) | 15 min | ⭐ Beginner |

---

## 🚀 Quick Start

### Exercise 1: CLI Essentials

Learn the essential Docker commands in 5 minutes:

```bash
# Pull an image
docker pull nginx:alpine

# Run a container
docker run -d --name my-nginx -p 8080:80 nginx:alpine

# Check it's running
docker ps

# View logs
docker logs my-nginx

# Stop and remove
docker stop my-nginx && docker rm my-nginx
```

**📄 Go to Exercise 1:** [CLI Essentials](./01-cli-essentials.md)

---

## 💡 Tips for Success

### 1. Type Commands, Don't Copy-Paste
Typing commands helps you remember them better.

### 2. Experiment!
Don't just follow the steps exactly. Try your own variations.

### 3. Check Your Work
After each step, use `docker ps` to verify the state.

### 4. Clean Up After Each Exercise
```bash
# Remove containers from the exercise
docker stop $(docker ps -aq) && docker rm $(docker ps -aq)

# Remove unused images
docker image prune -a
```

---

## 🆘 Need Help?

1. **Check the reference:** [Commands Cheatsheet](../4-reference/commands-cheatsheet.md)
2. **Read the logs:** `docker logs <container>`
3. **Ask questions:** Google the exact error message

---

## ✅ Before You Start

Make sure Docker is running:

```bash
docker info | head -5
```

If you see "Cannot connect to Docker daemon", start Docker Desktop:

```bash
open -a Docker
```

---

## 📁 Files in This Folder

```
3-hands-on/
├── README.md                    # ← You are here
├── 01-cli-essentials.md        # Exercise 1
├── 02-running-containers.md     # Exercise 2
├── 03-managing-containers.md    # Exercise 3
├── 04-networks-volumes.md       # Exercise 4
├── 05-docker-compose.md          # Exercise 5
└── 06-portainer.md              # Exercise 6
```

---

## 👨‍🏫 Tip from Your Mentor

> **"Break things on purpose!"**
>
> The best way to learn Docker is to experiment. Try:
> - What happens if I don't give a container a name?
> - What if I don't expose ports?
> - What if I delete a container with a volume?
>
> Breaking things teaches you how they work.

---

**Next: [Exercise 1: CLI Essentials](./01-cli-essentials.md)**
