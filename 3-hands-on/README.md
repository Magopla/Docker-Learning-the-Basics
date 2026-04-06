# Module 3: Hands-On

This module is the practical part of the repository. The goal is to move from "I read about Docker" to "I can use Docker without guessing."

## Recommended Order

| Exercise | Topic | Main Skill |
| --- | --- | --- |
| [`01-cli-essentials.md`](./01-cli-essentials.md) | Basic CLI workflow | Pull, run, list, stop, remove |
| [`02-running-containers.md`](./02-running-containers.md) | Runtime options | Ports, env vars, bind mounts, interactive mode |
| [`03-managing-containers.md`](./03-managing-containers.md) | Container lifecycle | Logs, exec, inspect, restart |
| [`04-networks-volumes.md`](./04-networks-volumes.md) | Persistence and communication | Named volumes and container networking |
| [`05-docker-compose.md`](./05-docker-compose.md) | Multi-container applications | Compose services, env files, startup flow |
| [`06-portainer.md`](./06-portainer.md) | Optional GUI | Visual inspection and management |
| [`07-capstone.md`](./07-capstone.md) | Final practice | Combine images, containers, ports, volumes, networks, and Compose |

## Before You Start

Make sure Docker is running:

```bash
docker info | head -5
```

If that fails, go back to [`../2-setup/README.md`](../2-setup/README.md).

## Labs Included In This Repo

The `labs` folder contains small assets you can use while learning:

```text
3-hands-on/labs/
├── 01-static-site/
│   └── index.html
├── 05-compose-postgres-adminer/
│   ├── .env.example
│   └── compose.yml
└── 07-capstone-stack/
    ├── .env.example
    ├── compose.yml
    └── site/
        └── index.html
```

These are intentionally small so you can focus on Docker itself instead of application code.

## Suggested Way To Practice

For each exercise:

1. Read the explanation once.
2. Type the commands yourself.
3. Run `docker ps`, `docker logs`, or `docker inspect` after each major step.
4. Clean up before moving on unless the next exercise builds on the current one.

## Cleanup Shortcuts

Use these carefully while learning:

```bash
docker ps -a
docker volume ls
docker network ls
docker container prune
docker image prune
```

Avoid running `docker system prune -a` unless you understand that it can remove a lot more than the current exercise.

## Learning Mindset

Good signs while learning Docker:

- you can explain what the container is doing
- you know why a port or volume flag was added
- you can inspect state instead of retrying randomly

If something breaks, that is useful. Docker becomes much easier once you learn how to inspect failures calmly.

## Module Challenge

When you finish exercises 1 through 6, complete [`07-capstone.md`](./07-capstone.md).

That capstone is designed to make you use several ideas together instead of one at a time:

- image tags
- published ports
- environment variables
- bind mounts
- named volumes
- service-to-service communication through Compose

## Mini Quiz

1. Which command tells you what containers are currently running?
2. Which command is better when you want facts about configuration: `docker logs` or `docker inspect`?
3. What is the difference between a bind mount and a named volume?

## Next Step

Start with [`01-cli-essentials.md`](./01-cli-essentials.md).
