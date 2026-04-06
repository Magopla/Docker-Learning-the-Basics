# Exercise 7: Capstone Lab

This capstone ties the core ideas from the repository into one small local stack.

## Goal

By the end of this exercise, you should be able to work through a multi-service Docker setup and explain:

- which images are being used
- which containers are created
- which ports are published
- where configuration comes from
- which data is persisted
- how services talk to each other

## Capstone Stack

The lab lives here:

```text
3-hands-on/labs/07-capstone-stack/
├── .env.example
├── compose.yml
└── site/
    └── index.html
```

The stack includes:

- `web`: Nginx serving a local static page through a bind mount
- `db`: PostgreSQL using environment variables and a named volume
- `adminer`: a simple database UI that connects to `db` over the Compose network

## Step 1: Prepare The Lab

```bash
cd 3-hands-on/labs/07-capstone-stack
cp .env.example .env
docker compose -f compose.yml config
```

Before you start the stack, read the Compose file and identify:

- the three services
- the published ports
- the bind mount
- the named volume
- the environment variables

## Step 2: Start The Stack

```bash
docker compose -f compose.yml up -d
docker compose -f compose.yml ps
```

Open:

- `http://localhost:8088` for the static site
- `http://localhost:8081` for Adminer

Use the `.env` values in Adminer and connect to:

- System: `PostgreSQL`
- Server: `db`

Notice that `db` works as the hostname because Compose created a shared network for the services.

## Step 3: Inspect The Running Stack

Run these commands and explain the result to yourself:

```bash
docker compose -f compose.yml logs web
docker compose -f compose.yml logs db
docker compose -f compose.yml logs adminer
docker compose -f compose.yml exec db env
docker compose -f compose.yml exec db psql -U ${POSTGRES_USER:-student} -d ${POSTGRES_DB:-learn_capstone} -c '\l'
docker volume ls
docker network ls
```

Questions to answer while doing this:

1. Which service is using a bind mount?
2. Which service is using a named volume?
3. Which service depends on another service name?
4. Which data would still exist after `docker compose down`?

## Step 4: Change Something Intentionally

Edit the static page:

```bash
open site/index.html
```

Refresh `http://localhost:8088` and confirm the change appears without rebuilding the stack.

That confirms the bind mount is working.

## Step 5: Stop The Stack

```bash
docker compose -f compose.yml down
```

Then inspect what remains:

```bash
docker volume ls
```

The named volume should still exist.

Remove everything, including the volume:

```bash
docker compose -f compose.yml down -v
```

## Capstone Checklist

- [ ] I can explain image vs container using this stack
- [ ] I can point to a bind mount in the Compose file
- [ ] I can point to a named volume in the Compose file
- [ ] I understand why Adminer connects to `db` by service name
- [ ] I know the difference between `down` and `down -v`

## Mini Quiz

1. Why does changing `site/index.html` affect the running web service immediately?
2. Why can Adminer use `db` as the database host?
3. What survives `docker compose down` but not `docker compose down -v`?
4. Where are the PostgreSQL credentials defined for this lab?

## Done Well If

You have really finished the capstone if you can explain the whole stack without reading the file line by line.

That is the moment Docker starts to feel understandable instead of magical.

## Next Step

Continue to [`../4-operations-and-production/README.md`](../4-operations-and-production/README.md).
