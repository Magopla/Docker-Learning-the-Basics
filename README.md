# Docker Learning the Basics

This repository is organized as a small self-paced course for learning Docker by reading a little, then running things locally.

It is aimed at beginners, especially people in data and platform-adjacent roles who want enough Docker knowledge to:

- understand what containers are and why they exist
- run and inspect containers from the CLI
- work with ports, volumes, and environment variables
- use Docker Compose for simple multi-container setups
- build confidence before moving on to more advanced tools
- finish with a small capstone that combines the basics

## How To Use This Repo

Follow the modules in order:

| Module | Focus | Outcome |
| --- | --- | --- |
| `0-prerequisites` | Installation checks | Docker is installed and working |
| `1-docker-concepts` | Core ideas | You understand images, containers, and architecture |
| `2-setup` | Local environment | You verify your machine and optional tools |
| `3-hands-on` | Guided practice | You run real commands and small labs |
| `4-reference` | Quick lookup | You have a cheatsheet while practicing |
| `resources` | External reading | You know where to go deeper |

Recommended flow:

1. Read [`0-prerequisites/README.md`](./0-prerequisites/README.md)
2. Read [`1-docker-concepts/README.md`](./1-docker-concepts/README.md)
3. Complete [`2-setup/README.md`](./2-setup/README.md)
4. Work through [`3-hands-on/README.md`](./3-hands-on/README.md)
5. Keep [`4-reference/commands-cheatsheet.md`](./4-reference/commands-cheatsheet.md) open while practicing

## Quick Start

If Docker is already installed, you can start here:

```bash
docker run hello-world
docker run -d --name quick-nginx -p 8080:80 nginx:alpine
docker ps
docker logs quick-nginx
docker stop quick-nginx
docker rm quick-nginx
```

Then continue with [`3-hands-on/01-cli-essentials.md`](./3-hands-on/01-cli-essentials.md).

## Repository Structure

```text
Docker Learning the Basics/
├── README.md
├── 0-prerequisites/
├── 1-docker-concepts/
├── 2-setup/
├── 3-hands-on/
│   ├── 01-cli-essentials.md
│   ├── 02-running-containers.md
│   ├── 03-managing-containers.md
│   ├── 04-networks-volumes.md
│   ├── 05-docker-compose.md
│   ├── 06-portainer.md
│   └── labs/
├── 4-reference/
└── resources/
```

## What Makes This Repo Useful For Learning

- concepts are separated from practice
- the hands-on section increases in difficulty gradually
- the repository now includes small lab assets under `3-hands-on/labs`
- the repository now includes quick self-checks and a capstone lab
- each module is intended to answer one question clearly:
  - what is Docker?
  - how do I install it?
  - how do I run containers?
  - how do I work with multiple services?

## Learning Pattern

The repository now follows a simple pattern in most sections:

1. Read a short explanation.
2. Try a focused exercise.
3. Check your understanding with a mini quiz or checklist.
4. Finish the hands-on module with a capstone lab.

## Suggested Learning Routes

Use one of these routes depending on your goal:

| Goal | Path |
| --- | --- |
| Learn Docker properly from scratch | `0 → 1 → 2 → 3` |
| Just get hands-on quickly | `2 → 3` |
| Refresh before an interview or project | `1 → 4` |
| Learn Docker Compose specifically | `1.2 → 3.4 → 3.5` |

## Notes

- Commands assume Docker Desktop or a local Docker Engine is already running.
- Some examples use `open http://localhost:...`, which is most convenient on macOS.
- Portainer is optional. The CLI exercises are the primary learning path.

## Next Step

Start with [`0-prerequisites/README.md`](./0-prerequisites/README.md).
