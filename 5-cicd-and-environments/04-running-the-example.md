# Section 5.4: Running the Example

This section walks through the example data product and its three Docker environments.

## Lab Location

```text
5-cicd-and-environments/labs/data-product/
├── Dockerfile
├── Jenkinsfile
├── compose.local.yml
├── compose.dev.yml
├── compose.prod.yml
├── .env.local.example
├── .env.dev.example
├── .env.prod.example
├── app/
└── tests/
```

## Step 1: Run The Product Locally

```bash
cd 5-cicd-and-environments/labs/data-product
cp .env.local.example .env.local
docker compose --env-file .env.local -f compose.local.yml up --build
```

Open:

- `http://localhost:8000/health`
- `http://localhost:8000/datasets`
- `http://localhost:8000/summary`

This local setup is optimized for sprint development:

- source code is mounted
- the server runs with reload
- iteration is fast

## Step 2: Inspect The Dev Environment File

Review:

- `.env.dev.example`
- `compose.dev.yml`

Notice the main change:

- the dev environment uses an image tag rather than a bind-mounted source tree

That is closer to what CI/CD deploys.

## Step 3: Inspect The Production File

Review:

- `.env.prod.example`
- `compose.prod.yml`

Look for the differences compared with local:

- production-oriented environment values
- healthcheck
- restart policy
- no bind mount for source code

## Step 4: Read The Jenkinsfile

Open `Jenkinsfile` and connect it to the environment files:

- local is for developer iteration
- dev is for shared validation
- prod is for stable release

## Checklist

- [ ] I can explain the difference between local, dev, and prod in this example
- [ ] I know why local uses a bind mount
- [ ] I know why dev and prod use an image tag
- [ ] I understand how Jenkins promotes the same image through environments

## Next Step

Continue to [`../6-data-engineering-example/README.md`](../6-data-engineering-example/README.md).
