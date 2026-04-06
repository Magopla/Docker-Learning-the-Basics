# Exercise 2: Running Containers

This exercise focuses on the flags you will use most often with `docker run`.

## Learning Goal

By the end of this exercise, you should be comfortable with:

- port mapping
- environment variables
- bind mounts
- named volumes
- interactive containers

## 1. Port Mapping

Containers are isolated from your host machine. To access a service from your browser or another tool on your machine, you usually publish a port.

```bash
docker run -d --name web -p 8080:80 nginx:alpine
docker ps
docker port web
open http://localhost:8080
```

What this means:

- `8080` is the host port
- `80` is the container port

Clean up:

```bash
docker stop web
docker rm web
```

## 2. Environment Variables

Environment variables are a common way to configure a container at startup.

```bash
docker run -d --name db \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_DB=mydb \
  postgres:16-alpine

docker exec db env | grep POSTGRES
```

Clean up:

```bash
docker stop db
docker rm db
```

## 3. Bind Mounts

Bind mounts connect a host path to a path inside the container. They are very useful while learning because you can change local files and immediately see the effect in the container.

This repository already includes a tiny static-site lab:

```text
3-hands-on/labs/01-static-site/index.html
```

From the repository root, run:

```bash
docker run -d --name static-site \
  -p 8080:80 \
  -v "$(pwd)/3-hands-on/labs/01-static-site:/usr/share/nginx/html:ro" \
  nginx:alpine
```

Then open:

```bash
open http://localhost:8080
```

Now edit `3-hands-on/labs/01-static-site/index.html`, refresh the browser, and confirm the change appears immediately.

Clean up:

```bash
docker stop static-site
docker rm static-site
```

## 4. Named Volumes

Named volumes are managed by Docker and are useful when container data should survive container removal.

```bash
docker volume create my-data

docker run -d --name db \
  -e POSTGRES_PASSWORD=secret \
  -v my-data:/var/lib/postgresql/data \
  postgres:16-alpine
```

You can remove the container and keep the volume:

```bash
docker rm -f db
docker volume ls
```

To clean up fully:

```bash
docker volume rm my-data
```

## 5. Interactive Containers

Interactive mode is useful for debugging or quickly exploring an image.

```bash
docker run -it --name my-ubuntu ubuntu:22.04 bash
```

Inside the container, try:

```bash
whoami
cat /etc/os-release
exit
```

You can also use a smaller Alpine image:

```bash
docker run -it --name my-alpine alpine sh
```

## 6. Detached vs Interactive

| Mode | Typical flag | Good for |
| --- | --- | --- |
| Detached | `-d` | Web servers, databases, background services |
| Interactive | `-it` | Shells, debugging, REPL sessions |
| One-off command | `--rm` | Short commands that should clean themselves up |

Examples:

```bash
docker run -d --name web nginx:alpine
docker run -it --name py python:3.12 python
docker run --rm python:3.12 python -c "print('hello from a one-off container')"
```

## Challenge

Create a container that:

1. runs Nginx
2. publishes port `8081`
3. uses the static-site lab folder as a read-only bind mount
4. is named `challenge-web`

Expected shape:

```bash
docker run -d --name challenge-web \
  -p 8081:80 \
  -v "$(pwd)/3-hands-on/labs/01-static-site:/usr/share/nginx/html:ro" \
  nginx:alpine
```

## Checklist

- [ ] I can explain host port vs container port
- [ ] I can pass environment variables with `-e`
- [ ] I can use a bind mount for local files
- [ ] I understand why named volumes are different from bind mounts
- [ ] I can open an interactive shell in a container

## Next Step

Continue to [`03-managing-containers.md`](./03-managing-containers.md).
