# Docker Commands Cheatsheet

Use this page as a quick reminder while practicing. It favors safe, common commands over destructive shortcuts.

## Containers

```bash
docker run nginx:alpine
docker run -d --name web nginx:alpine
docker run -p 8080:80 nginx:alpine
docker run -e NODE_ENV=production nginx:alpine
docker run -v my-data:/data nginx:alpine
docker run --rm nginx:alpine
docker ps
docker ps -a
docker stop web
docker start web
docker restart web
docker rm web
docker rm -f web
```

## Inspection and Debugging

```bash
docker logs web
docker logs -f web
docker logs --tail 50 web
docker inspect web
docker inspect --format '{{.State.Status}}' web
docker port web
docker exec -it web sh
docker exec web env
docker cp web:/etc/nginx/nginx.conf ./nginx.conf
docker stats --no-stream web
```

## Images

```bash
docker images
docker pull nginx:alpine
docker rmi nginx:alpine
docker build -t myapp:1.0 .
docker tag myapp:1.0 myuser/myapp:1.0
docker history nginx:alpine
```

## Networks

```bash
docker network ls
docker network create my-net
docker network inspect my-net
docker network connect my-net web
docker network disconnect my-net web
docker network rm my-net
```

## Volumes

```bash
docker volume ls
docker volume create my-data
docker volume inspect my-data
docker volume rm my-data
```

## Compose

```bash
docker compose up -d
docker compose up -d --build
docker compose ps
docker compose logs -f
docker compose exec web sh
docker compose config
docker compose down
docker compose down -v
```

## System Info and Cleanup

```bash
docker info
docker version
docker system df
docker container prune
docker image prune
docker volume prune
docker system prune
```

Prefer targeted cleanup while learning. Avoid broad commands like `docker system prune -a` unless you are sure you want to remove a lot of cached data and unused images.

## Common Flags

| Flag | Meaning |
| --- | --- |
| `-d` | Detached mode |
| `-it` | Interactive terminal |
| `-p host:container` | Publish a port |
| `-e KEY=value` | Set an environment variable |
| `-v source:target` | Mount a volume or bind mount |
| `--name` | Give the container a stable name |
| `--rm` | Remove the container when it exits |
| `--network` | Attach container to a network |

## Useful Mental Shortcuts

- `docker pull`: download an image
- `docker run`: create and start a container
- `docker exec`: run something inside a running container
- `docker logs`: read container output
- `docker inspect`: ask Docker for structured metadata

## Next Step

Use this together with [`../3-hands-on/README.md`](../3-hands-on/README.md).
