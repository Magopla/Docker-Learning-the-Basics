# Exercise 6: Portainer

Portainer is optional in this repository, but it can be very helpful when you are new to Docker and want a visual view of what the CLI is doing.

## Learning Goal

By the end of this exercise, you should be able to:

- open Portainer
- inspect containers, images, networks, and volumes
- read logs and open a console
- understand Portainer as a companion to the CLI, not a replacement for it

## Step 1: Start Portainer

From the repository root:

```bash
cd 2-setup
docker compose up -d
docker compose ps
```

Then open:

- `http://localhost:9000`
- or `https://localhost:9443`

On first launch:

1. Create an admin password.
2. Choose the local Docker environment.
3. Finish the setup wizard.

## Step 2: Explore The Dashboard

Look for these sections:

- containers
- images
- networks
- volumes

As you click around, compare what you see in Portainer with what you already know from:

- `docker ps`
- `docker images`
- `docker network ls`
- `docker volume ls`

## Step 3: Inspect A Container

If you still have any practice containers running, open one in Portainer and review:

- its status
- mapped ports
- logs
- environment variables
- mounted volumes

If not, create a simple one from the CLI first:

```bash
docker run -d --name portainer-demo -p 8080:80 nginx:alpine
```

Then refresh Portainer and inspect that container there.

## Step 4: Try A Few GUI Actions

In Portainer, practice:

1. viewing container logs
2. opening the console
3. stopping and starting a container
4. removing a container you no longer need

This is useful because it reinforces the same Docker concepts from a different angle.

## Important Security Note

Portainer usually works by mounting the Docker socket into the Portainer container. That gives it powerful access to your Docker environment.

That is fine for local learning, but it is something to treat carefully in shared or production environments.

## Checklist

- [ ] I can open Portainer locally
- [ ] I can find containers, images, networks, and volumes
- [ ] I can inspect logs and runtime details from the UI
- [ ] I understand that Portainer is using Docker underneath, not replacing it

## Next Step

Use [`../4-reference/commands-cheatsheet.md`](../4-reference/commands-cheatsheet.md) as your quick reference while repeating the exercises.
