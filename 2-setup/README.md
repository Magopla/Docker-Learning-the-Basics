# Module 2: Setup

This module is about one thing: making sure Docker works reliably on your machine before you move into the exercises.

## Learning Goal

By the end of this module, you should be able to answer "yes" to all of these:

- Docker is installed
- the Docker daemon is running
- `docker` and `docker compose` both work
- I can start and stop a simple container

Portainer is optional and comes last.

## Step 1: Install Docker Desktop

On macOS, the easiest route is Docker Desktop:

1. Download it from [Docker Desktop](https://www.docker.com/products/docker-desktop/).
2. Choose the correct build for your machine:
   - Apple Silicon: `aarch64`
   - Intel: `x86_64`
3. Move Docker to `Applications`.
4. Launch Docker Desktop and wait until it reports that Docker is running.

## Step 2: Verify The Installation

Run these commands:

```bash
docker --version
docker compose version
docker info | head -10
docker run hello-world
docker ps -a
```

What you are checking:

- `docker --version`: the CLI is installed
- `docker compose version`: Compose support is available
- `docker info`: the daemon is reachable
- `docker run hello-world`: Docker can pull and run a container
- `docker ps -a`: you can inspect container history

## Step 3: Run A Real Container

Start a small web server:

```bash
docker run -d --name my-nginx -p 8080:80 nginx:alpine
docker ps
docker logs my-nginx
open http://localhost:8080
docker stop my-nginx
docker rm my-nginx
```

If that worked, your setup is good enough for the rest of the repository.

## Optional: Install Portainer

Portainer gives you a GUI for seeing containers, images, networks, and volumes. It is useful for beginners, but not required.

You can start it with the compose file already included in this folder:

```bash
cd 2-setup
docker compose up -d
docker compose ps
```

Open one of these:

- `http://localhost:9000`
- `https://localhost:9443`

When you are done:

```bash
docker compose down
```

## Common Problems

### "Cannot connect to the Docker daemon"

Docker Desktop is probably not running yet. Open it and wait for it to finish starting:

```bash
open -a Docker
docker ps
```

### `docker compose` is not available

You may have an incomplete or older Docker installation. Reinstall Docker Desktop and verify again with:

```bash
docker compose version
```

### Port `8080` is already in use

Use a different host port:

```bash
docker run -d --name my-nginx -p 8081:80 nginx:alpine
```

## Ready To Continue?

If the verification steps worked, continue to [`../3-hands-on/README.md`](../3-hands-on/README.md).

## Mini Quiz

1. What is the difference between the Docker CLI being installed and the Docker daemon running?
2. Why do we test with both `docker info` and `docker run hello-world`?
3. If port `8080` is busy, what part of `-p 8080:80` should you change?
