# Docker Learning the Basics

This repository is organized as a self-paced Docker course for beginners who want to move from first concepts to practical local stacks and production-minded habits.

It is especially useful for people in data, analytics, and platform-adjacent roles who want to:

- understand what containers are and why they exist
- run and inspect containers from the CLI
- work with ports, volumes, networks, and environment variables
- use Docker Compose for simple multi-container applications
- understand how to think about production deployment and container security
- manage images and containers visually with Portainer
- see a realistic Data Engineering-flavored local stack

## Learning Path

Follow the modules in order:

| Module | Focus | Outcome |
| --- | --- | --- |
| `0-prerequisites` | Installation checks | Docker is installed and working |
| `1-docker-concepts` | Core ideas | You understand images, containers, tags, and architecture |
| `2-setup` | Local environment | You verify Docker Desktop and optional Portainer |
| `3-hands-on` | Guided practice | You learn the CLI and Compose through small labs |
| `4-operations-and-production` | Production, Portainer operations, security | You develop better operational judgment |
| `5-data-engineering-example` | Realistic local stack | You see how Docker fits a data workflow |
| `6-reference` | Quick lookup | You have a cheatsheet and starter Compose template |
| `resources` | External reading | You know where to go deeper |

Recommended flow:

1. Read [`0-prerequisites/README.md`](./0-prerequisites/README.md)
2. Read [`1-docker-concepts/README.md`](./1-docker-concepts/README.md)
3. Complete [`2-setup/README.md`](./2-setup/README.md)
4. Work through [`3-hands-on/README.md`](./3-hands-on/README.md)
5. Continue to [`4-operations-and-production/README.md`](./4-operations-and-production/README.md)
6. Finish with [`5-data-engineering-example/README.md`](./5-data-engineering-example/README.md)
7. Keep [`6-reference/commands-cheatsheet.md`](./6-reference/commands-cheatsheet.md) open while practicing

## Quick Start

If Docker is already installed, start here:

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
├── 4-operations-and-production/
├── 5-data-engineering-example/
├── 6-reference/
└── resources/
```

## What Makes This Repo Useful For Learning

- concepts are separated from practice
- the hands-on path increases in difficulty gradually
- the repository includes small labs and a capstone
- the operations module adds production, Portainer, and security thinking
- the Data Engineering example grounds Docker in a realistic use case

## Learning Pattern

Most modules follow the same pattern:

1. Read a short explanation.
2. Try a focused exercise.
3. Check your understanding with a mini quiz or checklist.
4. Apply the ideas in a bigger example.

## Suggested Routes

| Goal | Path |
| --- | --- |
| Learn Docker properly from scratch | `0 → 1 → 2 → 3 → 4 → 5` |
| Just get hands-on quickly | `2 → 3` |
| Learn production-minded Docker basics | `1 → 3 → 4` |
| Learn from a data example | `1 → 3.5 → 5` |

## Notes

- Commands assume Docker Desktop or a local Docker Engine is running.
- Some examples use `open http://localhost:...`, which is most convenient on macOS.
- Portainer is optional, but it becomes more useful in the operations module.

## Next Step

Start with [`0-prerequisites/README.md`](./0-prerequisites/README.md).
