# Module 5: CI/CD and Environments

This module shows how Docker helps a team move from local development to a shared dev environment and then to production using the same application image with environment-specific configuration.

## Learning Goal

By the end of this module, you should be able to:

- explain how Docker supports CI/CD workflows
- distinguish local, dev, and production environments
- understand how a Dockerized data product moves through a sprint
- read a simple Jenkins pipeline that builds, tests, and promotes a container

## Sections

| Section | Focus | Outcome |
| --- | --- | --- |
| [`01-docker-for-cicd.md`](./01-docker-for-cicd.md) | Why Docker fits CI/CD | You understand repeatable builds and promotions |
| [`02-environments-dev-to-production.md`](./02-environments-dev-to-production.md) | Local, dev, and prod environments | You understand what changes and what should stay the same |
| [`03-jenkins-pipeline.md`](./03-jenkins-pipeline.md) | Jenkins pipeline example | You can read a simple build-test-deploy flow |
| [`04-running-the-example.md`](./04-running-the-example.md) | End-to-end example | You can run the sample data product locally and inspect the env files and Compose setups |

## Example Lab

The module includes a small data product:

```text
5-cicd-and-environments/labs/data-product/
├── Dockerfile
├── Jenkinsfile
├── compose.local.yml
├── compose.dev.yml
├── compose.prod.yml
├── requirements.txt
├── app/
└── tests/
```

It is intentionally small so the learning focus stays on Docker, CI/CD, and environments rather than application complexity.

## Sprint Mental Model

A simple sprint flow for this example looks like this:

1. A developer changes code locally and runs the local Docker setup.
2. The team pushes the sprint work.
3. Jenkins builds and tests a new image.
4. The image is deployed to a shared dev environment.
5. After validation, the same image is promoted to production.

That promotion idea is the key lesson: Docker helps you move the same built artifact through environments instead of rebuilding it differently each time.

## Next Step

Start with [`01-docker-for-cicd.md`](./01-docker-for-cicd.md).
