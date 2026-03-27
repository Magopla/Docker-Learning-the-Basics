# Module 1: Docker Core Concepts
## Understanding Containerization

---

## 🎯 Goal

By the end of this module, you will understand:
- ✅ What Docker is and why it exists
- ✅ How Docker differs from Virtual Machines
- ✅ Core Docker concepts: Images, Containers, Registries, Tags
- ✅ The Docker architecture

---

## 📚 Table of Contents

| Lesson | Topic | Time |
|--------|-------|------|
| 1.1 | [Virtualization vs Containers](./01-virtualization-vs-containers.md) | 15 min |
| 1.2 | [Images, Containers, Registries & Tags](./02-images-containers.md) | 15 min |
| 1.3 | [Docker Architecture](./03-architecture.md) | 10 min |

---

## 🚀 Quick Introduction

### What is Docker?

**Docker** is a platform for building, running, and shipping applications in **containers**.

Think of it like a **shipping container** for software:

```
┌─────────────────────────────────────────────────────────────────┐
│              REAL WORLD EXAMPLE                                  │
│                                                                  │
│   🚢 Shipping Container                                          │
│   ┌─────────────────────────────────┐                          │
│   │  ┌─────┐ ┌─────┐ ┌─────┐      │                          │
│   │  │Chair│ │Table│ │Shelf│      │  All the same container  │
│   │  └─────┘ └─────┘ └─────┘      │  Same truck, same ship    │
│   └─────────────────────────────────┘                          │
│                                                                  │
│   🐳 Docker Container                                            │
│   ┌─────────────────────────────────┐                          │
│   │  ┌─────┐ ┌─────┐ ┌─────┐      │                          │
│   │  │ App │ │ DB  │ │ Cache│     │  Same container           │
│   │  │ Code│ │ Data│ │ Logs │     │  Same host, same kernel   │
│   │  └─────┘ └─────┘ └─────┘      │                          │
│   └─────────────────────────────────┘                          │
└─────────────────────────────────────────────────────────────────┘
```

### Why Do Data Engineers Need Docker?

| Use Case | How Docker Helps |
|----------|-----------------|
| **Data Pipelines** | Package Spark, Kafka, Airflow in one container |
| **Database Testing** | Spin up PostgreSQL, MongoDB instantly |
| **Reproducibility** | Same environment across dev, test, prod |
| **Isolation** | Dependencies don't conflict |
| **Scaling** | Scale containers up or down easily |

---

## 📖 The Problem Docker Solves

### "It works on my machine!"

```
┌─────────────────────────────────────────────────────────────────┐
│                    THE CLASSIC PROBLEM                           │
│                                                                  │
│  Developer:  "Works on my machine!" 💻                          │
│                      ↓                                           │
│  Production: "It's broken!" 🚨                                   │
│                                                                  │
│  Why?                                                           │
│  • Different OS versions                                         │
│  • Different Python versions                                     │
│  • Missing dependencies                                         │
│  • Different configuration                                       │
└─────────────────────────────────────────────────────────────────┘
```

### Docker's Solution

```
┌─────────────────────────────────────────────────────────────────┐
│                    THE DOCKER SOLUTION                           │
│                                                                  │
│  ┌─────────────────┐                                            │
│  │   DEVELOPER     │                                            │
│  │   Machine        │                                            │
│  │                 │                                            │
│  │  ┌───────────┐  │                                            │
│  │  │ Container │  │  ←─── "It works EVERYWHERE!"               │
│  │  │ Python 3.11│  │                                           │
│  │  │ + packages │  │                                           │
│  │  └───────────┘  │                                           │
│  └─────────────────┘                                            │
│           ↓ same container ↓                                     │
│  ┌─────────────────┐                                            │
│  │   PRODUCTION     │                                            │
│  │   Server         │                                            │
│  │                 │                                            │
│  │  ┌───────────┐  │                                            │
│  │  │ Container │  │  ←─── Identical!                           │
│  │  │ Python 3.11│  │                                           │
│  │  │ + packages │  │                                           │
│  │  └───────────┘  │                                           │
│  └─────────────────┘                                            │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🎓 Key Concepts Preview

Before diving deep, here's a quick overview:

| Concept | Simple Explanation | Analogy |
|---------|-------------------|---------|
| **Image** | Blueprint for a container | Recipe |
| **Container** | Running instance of an image | Cookie |
| **Registry** | Where images are stored | Library |
| **Tag** | Version of an image | ISBN number |

---

## 📝 Lessons

### Lesson 1.1: Virtualization vs Containers
📄 [Read: Virtualization vs Containers](./01-virtualization-vs-containers.md)

Learn the architectural differences between VMs and containers.

---

### Lesson 1.2: Images, Containers, Registries & Tags
📄 [Read: Images, Containers, Registries & Tags](./02-images-containers.md)

Understand the building blocks of Docker.

---

### Lesson 1.3: Docker Architecture
📄 [Read: Docker Architecture](./03-architecture.md)

See how all the pieces fit together.

---

## 🧪 Quick Quiz

Test your understanding before moving on:

### Question 1
What is the difference between an image and a container?

<details>
<summary>Click for answer</summary>

An **image** is a read-only template with instructions for creating a container. A **container** is a runnable instance of that image.

</details>

### Question 2
Name three popular Docker registries.

<details>
<summary>Click for answer</summary>

- Docker Hub
- Amazon ECR
- Google Container Registry (GCR)
- GitHub Container Registry (GHCR)
- Azure Container Registry

</details>

### Question 3
What does a tag represent?

<details>
<summary>Click for answer</summary>

A **tag** represents a specific version of an image, like `nginx:1.25` or `python:3.12-slim`.

</details>

---

## ✅ Module 1 Checklist

Before moving on, confirm you understand:

- [ ] Why we use containers (not VMs for everything)
- [ ] What is an image vs container
- [ ] What is a registry
- [ ] What is a tag

---

## 🚀 Next Steps

**Option A: Install Docker**
Ready to get hands-on? Install Docker and start practicing.

📄 [Go to Setup](../2-setup/README.md)

**Option B: Jump to Hands-On**
Go directly to running your first container.

📄 [Go to CLI Essentials](../3-hands-on/01-cli-essentials.md)

---

## 👨‍🏫 Tip from Your Mentor

> **"Understanding comes before memorizing."**
>
> Don't try to memorize all the commands yet. First, understand WHY Docker exists. The commands will make more sense once you know what problem they're solving.
>
> Ask yourself: "If I were designing Docker, how would I solve the 'works on my machine' problem?"

---

**Next: [Lesson 1.1: Virtualization vs Containers](./01-virtualization-vs-containers.md)**
