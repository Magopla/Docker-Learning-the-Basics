# Exercise 3: Managing Containers

This exercise is about inspection and control: once a container exists, how do you understand what it is doing?

## Learning Goal

By the end of this exercise, you should be able to:

- start, stop, and restart a container
- run commands inside a running container
- inspect metadata
- read logs
- copy files in and out of a container

## Step 1: Create A Working Container

```bash
docker create --name my-app nginx:alpine
docker start my-app
docker ps
```

This separation is useful:

- `docker create` makes the container
- `docker start` starts an existing container
- `docker run` is a shortcut that does both

## Step 2: Control The Lifecycle

```bash
docker stop my-app
docker start my-app
docker restart my-app
docker pause my-app
docker unpause my-app
```

These commands help you understand that a container is an object with a lifecycle, not just a single one-shot command.

## Step 3: Run Commands Inside The Container

```bash
docker exec my-app ls /usr/share/nginx/html
docker exec my-app cat /etc/alpine-release
docker exec -it my-app sh
```

`docker exec` is one of the most useful debugging tools in Docker.

Inside the shell, try:

```bash
ps
env
exit
```

## Step 4: Inspect Metadata

```bash
docker inspect my-app
docker inspect --format '{{.Config.Image}}' my-app
docker inspect --format '{{.State.Status}}' my-app
docker inspect --format '{{json .NetworkSettings.Ports}}' my-app
```

Use `inspect` when you want facts instead of guesses.

## Step 5: Read Logs

```bash
docker logs my-app
docker logs --tail 20 my-app
docker logs -f my-app
```

Logs are usually the first thing to check when a container exits or behaves unexpectedly.

## Step 6: Copy Files

```bash
docker cp my-app:/etc/nginx/nginx.conf ./nginx.conf
docker cp ./nginx.conf my-app:/tmp/nginx.conf
docker exec my-app ls /tmp
```

This is useful when you want to inspect configuration or move a quick test file in or out.

## Step 7: View Runtime Stats

```bash
docker stats --no-stream my-app
```

This gives you a quick snapshot of resource usage.

## Challenge

Do this workflow end to end:

1. Start an Nginx container named `debug-test`.
2. Read its logs.
3. Open a shell inside it.
4. Copy `/etc/nginx/nginx.conf` to your host.
5. Stop and remove the container.

## Checklist

- [ ] I can explain `create` vs `run`
- [ ] I can use `docker exec`
- [ ] I can use `docker inspect`
- [ ] I know logs are the first place to check for many failures
- [ ] I can copy a file out of a container

## Next Step

Continue to [`04-networks-volumes.md`](./04-networks-volumes.md).
