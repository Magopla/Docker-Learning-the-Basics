# Exercise 4: Networks and Volumes

This exercise covers two ideas that show up in almost every real Docker setup:

- how containers talk to each other
- how data survives container replacement

## Learning Goal

By the end of this exercise, you should be able to:

- create a user-defined network
- connect multiple containers to it
- use container names as hostnames
- create and inspect named volumes
- explain bind mounts vs named volumes

## Step 1: Create A Network

```bash
docker network create demo-net
docker network ls
docker network inspect demo-net
```

The important thing is not the command itself, but the idea: containers on the same user-defined bridge network can usually discover each other by name.

## Step 2: Put Two Containers On The Same Network

```bash
docker run -d --name web --network demo-net nginx:alpine
docker run -d --name client --network demo-net alpine sleep infinity
```

Now test connectivity:

```bash
docker exec client ping -c 3 web
docker exec client wget -O- http://web
```

Because both containers are on `demo-net`, `web` works as a hostname.

## Step 3: Clean Up The Network Demo

```bash
docker rm -f web client
docker network rm demo-net
```

## Step 4: Create A Named Volume

```bash
docker volume create postgres-data
docker volume ls
docker volume inspect postgres-data
```

Named volumes are managed by Docker and are usually the best choice for persistent container data.

## Step 5: Use The Volume With PostgreSQL

```bash
docker run -d \
  --name pg-demo \
  -e POSTGRES_PASSWORD=secret \
  -v postgres-data:/var/lib/postgresql/data \
  postgres:16-alpine
```

Now remove the container but keep the volume:

```bash
docker rm -f pg-demo
docker volume ls
```

That is the key idea: the data can outlive the container.

## Bind Mount vs Named Volume

Use a bind mount when:

- you want to work with files from your host directly
- you are developing locally
- you want immediate file changes to be visible in the container

Use a named volume when:

- Docker-managed persistence is enough
- the data belongs to the containerized service
- you do not need to edit the files directly from the host

## Quick Bind Mount Reminder

You already used a bind mount in the static-site lab:

```bash
-v "$(pwd)/3-hands-on/labs/01-static-site:/usr/share/nginx/html:ro"
```

That is a host folder mounted into the container.

## Challenge

Build a small networked setup:

1. Create a network called `redis-net`.
2. Run Redis on that network.
3. Use a one-off Redis client container on the same network to set a key.
4. Use another one-off client container to get the key back.

Suggested commands:

```bash
docker network create redis-net
docker run -d --name redis --network redis-net redis:7-alpine
docker run --rm --network redis-net redis:7-alpine redis-cli -h redis SET test "hello"
docker run --rm --network redis-net redis:7-alpine redis-cli -h redis GET test
docker rm -f redis
docker network rm redis-net
```

## Checklist

- [ ] I can create and inspect a network
- [ ] I know why container names work as hostnames on a user-defined network
- [ ] I can create and inspect a named volume
- [ ] I understand why data can survive container removal
- [ ] I can explain bind mount vs named volume

## Next Step

Continue to [`05-docker-compose.md`](./05-docker-compose.md).
