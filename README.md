# Docker Learning the Basics
## A Practical Guide for Junior Data Engineers

---

## 🎯 Welcome!

The repository has been created using Opencode to test the agent habilities to generate a guide as a "learning tutor".Use the repository as reference and how-to and not as a source of truth.

This repository is your **step-by-step journey** to mastering Docker from zero. Whether you're a junior Data Engineer or just getting started with containers, you've come to the right place.


### What You'll Learn

| Module | Topic | Time |
|--------|-------|------|
| 0 | Prerequisites & Setup | 15 min |
| 1 | Docker Fundamentals | 30 min |
| 2 | Your First Container | 20 min |
| 3 | Managing Containers | 25 min |
| 4 | Docker Compose | 30 min |
| 5 | Portainer (GUI) | 15 min |

**Total estimated time: ~2 hours**

---

## 📚 Learning Path

Follow this order - each module builds on the previous one:

```
┌─────────────────────────────────────────────────────────────────┐
│                     YOUR LEARNING JOURNEY                         │
│                                                                  │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐     │
│  │   0.    │───▶│   1.    │───▶│   2.    │───▶│   3.    │     │
│  │ SETUP   │    │CONCEPTS │    │  FIRST  │    │MANAGING │     │
│  │ ⭐      │    │  📖     │    │CONTAINER│    │   🔧   │     │
│  └─────────┘    └─────────┘    └─────────┘    └─────────┘     │
│                                                   │             │
│                                                   ▼             │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐     │
│  │   6.    │◀───│   5.    │◀───│   4.    │◀───│ REFERENCE│    │
│  │PORTTAINER│    │ COMPOSE │    │ NETWORKS│    │   📋    │     │
│  │   🖥️   │    │   🚀    │    │ & VOLS │    │         │     │
│  └─────────┘    └─────────┘    └─────────┘    └─────────┘     │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📁 Repository Structure

```
Docker Learning the Basics/
│
├── README.md                    # 📍 You are here - Start here!
│
├── 0-prerequisites/            # Module 0: What you need
│   └── README.md
│
├── 1-docker-concepts/          # Module 1: Theory
│   ├── README.md
│   ├── 01-virtualization-vs-containers.md
│   ├── 02-images-containers.md
│   └── 03-registries-tags.md
│
├── 2-setup/                    # Module 2: Installation
│   ├── README.md
│   └── docker-compose.yml      # Your first working compose file!
│
├── 3-hands-on/                 # Module 3+: Practice
│   ├── 01-cli-essentials.md
│   ├── 02-running-containers.md
│   ├── 03-managing-containers.md
│   ├── 04-networks-volumes.md
│   ├── 05-docker-compose.md
│   └── 06-portainer.md
│
├── 4-reference/                # Quick lookups
│   ├── README.md
│   ├── commands-cheatsheet.md
│   └── docker-compose-template.yml
│
└── resources/                  # External links
    └── README.md
```

---

## 🚀 Quick Start (5 minutes)

Already have Docker installed? Jump straight to action:

```bash
# 1. Run your first container
docker run hello-world

# 2. Run a web server
docker run -d -p 8080:80 nginx
# Open: http://localhost:8080

# 3. List running containers
docker ps

# 4. Stop it
docker stop $(docker ps -q)
```

---

## 📖 Module-by-Module Guide

### Module 0: Prerequisites
**→ Start here if you haven't installed Docker**

📄 [Go to Prerequisites](./0-prerequisites/README.md)

Learn: System requirements, how to install Docker Desktop on macOS

---

### Module 1: Core Concepts
**→ Understand the "why" before the "how"**

📄 [Go to Docker Concepts](./1-docker-concepts/README.md)

Learn:
- What is containerization?
- Docker vs Virtual Machines
- Images, Containers, Registries, Tags
- The Docker architecture

---

### Module 2: Setup
**→ Get your environment ready**

📄 [Go to Setup](./2-setup/README.md)

Do:
- Install Docker Desktop
- Verify installation
- Start Portainer (optional but recommended)

---

### Module 3: CLI Essentials
**→ Your first Docker commands**

📄 [Go to CLI Essentials](./3-hands-on/01-cli-essentials.md)

Commands you'll learn:
```bash
docker --version    # Check Docker
docker pull          # Download images
docker run           # Create & start containers
docker ps            # List containers
docker stop          # Stop containers
```

---

### Module 4: Running Containers
**→ Advanced container management**

📄 [Go to Running Containers](./3-hands-on/02-running-containers.md)

Learn:
- Interactive containers
- Environment variables
- Volume mounts
- Port mapping
- Container naming

---

### Module 5: Docker Compose
**→ Multi-container applications made easy**

📄 [Go to Docker Compose](./3-hands-on/05-docker-compose.md)

Learn:
- YAML syntax
- Service definition
- Networking between containers
- Volumes
- Real examples (Kafka, Spark, MongoDB)

---

### Module 6: Portainer
**→ Manage containers with a GUI**

📄 [Go to Portainer](./3-hands-on/06-portainer.md)

Learn:
- Install Portainer
- Web interface overview
- Container management via GUI

---

## 🔧 Common Commands Reference

| Command | What it does |
|---------|-------------|
| `docker run hello-world` | Run test container |
| `docker ps` | List running containers |
| `docker ps -a` | List ALL containers |
| `docker images` | List downloaded images |
| `docker stop <name>` | Stop a container |
| `docker rm <name>` | Remove a container |
| `docker logs <name>` | View container logs |
| `docker exec -it <name> bash` | Shell into container |

See full reference: [Commands Cheatsheet](./4-reference/commands-cheatsheet.md)

---

## 💡 Tips for Success

### 1. Type, Don't Copy-Paste
You'll learn faster by typing commands. Copy-paste skips muscle memory.

### 2. Break Things
The best way to learn is to intentionally break things and fix them.

### 3. Use Portainer Early
Don't wait - install Portainer early. It helps visualize what you're doing with the CLI.

### 4. Run the Examples
Each module has hands-on exercises. **Do them** - not just read them.

### 5. Ask Questions
If something doesn't work:
1. Check the troubleshooting section
2. Run `docker logs <container>`
3. Google the error message
4. Check the resources section

---

## 🆘 Troubleshooting

### "Cannot connect to Docker daemon"
```bash
# Docker Desktop isn't running
open -a Docker
```

### "Port already in use"
```bash
# Find what's using the port
lsof -i :8080
# Then either stop that service or use a different port
```

### "Container exits immediately"
```bash
# Check logs
docker logs <container_name>
# Run interactively to debug
docker run -it <image> /bin/sh
```

---

## 📞 Resources

| Resource | Description |
|----------|-------------|
| [Docker Docs](https://docs.docker.com/) | Official documentation |
| [Docker Hub](https://hub.docker.com/) | Image registry |
| [Play with Docker](https://labs.play-with-docker.com/) | Free online playground |
| [Docker Curriculum](https://docker-curriculum.com/) | Interactive tutorial |

📄 [All Resources](./resources/README.md)

---

## 👨‍🏫 About This Guide

This repository was created by a **Senior Data Engineer** to train junior team members. The goal is simple:

> **Get you from zero to productive with Docker in 2 hours.**

Each module is designed to be:
- ✅ **Short** - Focus on one concept at a time
- ✅ **Practical** - Learn by doing
- ✅ **Complete** - No skipping important details
- ✅ **Repeatable** - Works on any machine

---

## 📝 License

This is a learning resource. Feel free to use it, share it, and contribute!


