# Section 5.2: Running the Stack

This section walks through the local data platform example.

## Lab Location

```text
5-data-engineering-example/labs/local-data-platform/
├── .env.example
└── compose.yml
```

## Step 1: Prepare The Environment

```bash
cd 5-data-engineering-example/labs/local-data-platform
cp .env.example .env
docker compose -f compose.yml config
```

Review the config and identify:

- which ports are published
- which services use named volumes
- which values come from `.env`

## Step 2: Start The Stack

```bash
docker compose -f compose.yml up -d
docker compose -f compose.yml ps
```

Expected host endpoints:

- PostgreSQL: `localhost:5432`
- Adminer: `http://localhost:8082`
- MinIO API: `http://localhost:9000`
- MinIO Console: `http://localhost:9001`
- Notebook: `http://localhost:8888`

## Step 3: Inspect The Stack

Run:

```bash
docker compose -f compose.yml logs postgres
docker compose -f compose.yml logs minio
docker compose -f compose.yml logs notebook
docker volume ls
docker network ls
```

Try to explain:

1. Which service stores relational data?
2. Which service stores object-style files?
3. Which services are mostly interfaces for humans?
4. Which services would still have data after the containers were recreated?

## Step 4: Think Like A Data Engineer

A simple mental model for this stack:

- PostgreSQL stores structured tables and metadata
- MinIO stores raw files and datasets
- the notebook is where a person explores and connects to both
- Adminer is a quick inspection tool for the database

This is not the only valid architecture, but it is a useful local learning platform.

## Production Reminder

This stack is intentionally local-first and education-focused.

It is useful for learning:

- service separation
- persistence
- local tooling
- Compose-based orchestration

It is not a production architecture by itself. If you were hardening it, you would revisit:

- secrets handling
- network exposure
- authentication
- backups
- monitoring
- image lifecycle and updates

## Step 5: Stop The Stack

```bash
docker compose -f compose.yml down
```

To remove the volumes too:

```bash
docker compose -f compose.yml down -v
```

## Checklist

- [ ] I can explain what each service is for
- [ ] I can identify the persistent volumes
- [ ] I know where the credentials come from
- [ ] I understand why Compose is useful for a stack like this

## Mini Quiz

1. Why does MinIO fit naturally into a data-learning stack?
2. Why is a notebook service useful in a local platform example?
3. Which data survives `docker compose down` but not `docker compose down -v`?

## Next Step

Continue to [`../6-reference/commands-cheatsheet.md`](../6-reference/commands-cheatsheet.md) for quick command review.
