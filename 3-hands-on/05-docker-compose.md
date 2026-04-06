# Exercise 5: Docker Compose

This exercise introduces Docker Compose as the tool for running related services together from one YAML file.

## Learning Goal

By the end of this exercise, you should be able to:

- read and write a small Compose file
- understand `services`, `ports`, `volumes`, and `environment`
- start and stop a multi-container stack
- use an `.env` file to keep configuration out of the Compose file

## Why Compose Matters

Running one container with `docker run` is a great first step.

But real projects usually need more than one service, for example:

- an app
- a database
- a cache
- an admin UI

Compose lets you describe that setup once and run it with:

```bash
docker compose up -d
docker compose down
```

## Lab For This Exercise

This repository includes a small lab:

```text
3-hands-on/labs/05-compose-postgres-adminer/
├── .env.example
└── compose.yml
```

It starts:

- PostgreSQL
- Adminer, a lightweight database UI

## Step 1: Inspect The Compose File

Open [`labs/05-compose-postgres-adminer/compose.yml`](./labs/05-compose-postgres-adminer/compose.yml) and identify:

- the two services
- which ports are exposed
- which environment variables are used
- which named volume stores database data

The important idea is that both services are declared in one file and share the same default network created by Compose.

## Step 2: Prepare The Environment File

Copy the example file:

```bash
cd 3-hands-on/labs/05-compose-postgres-adminer
cp .env.example .env
```

Then review the values:

```bash
cat .env
```

## Step 3: Validate The Configuration

Before starting the stack, ask Compose to render the final config:

```bash
docker compose -f compose.yml config
```

This is a useful habit. It catches syntax issues and shows you the fully resolved configuration.

## Step 4: Start The Stack

```bash
docker compose -f compose.yml up -d
docker compose -f compose.yml ps
```

Then open:

- `http://localhost:8080`

Use these values in Adminer:

- System: `PostgreSQL`
- Server: `db`
- Username: value from `.env`
- Password: value from `.env`
- Database: value from `.env`

## Step 5: Inspect What Compose Created

Run:

```bash
docker compose -f compose.yml logs db
docker compose -f compose.yml logs adminer
docker volume ls
docker network ls
```

Things to notice:

- Compose created containers for both services
- Compose created a project-scoped network
- Compose created a named volume for PostgreSQL data
- the Adminer container connects to PostgreSQL using the service name `db`

## Step 6: Stop The Stack

```bash
docker compose -f compose.yml down
```

The containers and network are removed, but the named volume remains.

To remove the volume too:

```bash
docker compose -f compose.yml down -v
```

## What To Learn From This Exercise

Compose teaches a few core Docker ideas at once:

- service names become stable hostnames on the Compose network
- volumes exist outside a single container lifecycle
- environment variables make configuration easier to change
- one file can define an entire local development stack

## Challenge

Try these small changes one at a time:

1. Change Adminer from port `8080` to `8081`.
2. Change the database name in `.env`, then restart the stack from scratch.
3. Run `docker compose -f compose.yml down` and verify whether the volume still exists.
4. Run `docker compose -f compose.yml down -v` and verify the difference.

## Checklist

- [ ] I can explain what each service does
- [ ] I can start a two-service stack with Compose
- [ ] I know where the database credentials are defined
- [ ] I understand the difference between `down` and `down -v`

## Next Step

Continue to [`06-portainer.md`](./06-portainer.md) if you want a GUI, or return to [`../6-reference/commands-cheatsheet.md`](../6-reference/commands-cheatsheet.md) for quick command review.
