# Exercise 1: Docker CLI Essentials

This exercise introduces the basic command loop you will use constantly in Docker: pull, run, inspect, stop, and remove.

## Learning Goal

By the end of this exercise, you should be able to:

- pull an image
- run a container
- list containers and images
- read basic logs
- stop and remove a container

## Step 1: Verify Docker Works

```bash
docker --version
docker compose version
docker info | head -10
```

If `docker info` fails, go back to [`../2-setup/README.md`](../2-setup/README.md).

## Step 2: Run The First Test Container

```bash
docker run hello-world
docker ps -a
```

Why this is useful:

- Docker proves it can pull an image
- Docker creates and runs a container
- the container exits after printing a success message

## Step 3: Pull A Few Images

```bash
docker pull nginx:alpine
docker pull ubuntu:22.04
docker pull python:3.12-slim
docker images
```

This teaches an important distinction:

- pulling downloads an image
- running creates a container from an image

## Step 4: Run A Long-Lived Container

```bash
docker run -d --name web-server nginx:alpine
docker ps
docker logs web-server
docker inspect web-server | head -20
```

This container stays alive because Nginx is a long-running service.

## Step 5: Stop And Remove It

```bash
docker stop web-server
docker ps -a
docker rm web-server
docker ps -a
```

This is the basic cleanup loop you will use often while learning.

## Useful Commands From This Exercise

| Command | Purpose |
| --- | --- |
| `docker pull <image>` | Download an image |
| `docker run <image>` | Create and start a container |
| `docker ps` | Show running containers |
| `docker ps -a` | Show all containers, including stopped ones |
| `docker images` | Show local images |
| `docker logs <name>` | Read container logs |
| `docker stop <name>` | Stop a running container |
| `docker rm <name>` | Remove a container |

## Challenge

Try this without copying the solution first:

1. Pull `redis:7-alpine`.
2. Run it as `my-redis`.
3. Confirm it appears in `docker ps`.
4. Stop and remove it.

Reference solution:

```bash
docker pull redis:7-alpine
docker run -d --name my-redis redis:7-alpine
docker ps
docker stop my-redis
docker rm my-redis
```

## Checklist

- [ ] I can pull an image
- [ ] I can run a container
- [ ] I know the difference between an image and a container
- [ ] I can read logs
- [ ] I can stop and remove a container

## Next Step

Continue to [`02-running-containers.md`](./02-running-containers.md).
