# Module 4: Operations and Production

This module builds on the hands-on exercises and shifts the focus from "how do I run containers?" to "how do I run them more responsibly?"

## Learning Goal

By the end of this module, you should be able to:

- explain the difference between a learning setup and a production deployment
- use Portainer for ongoing image and container management
- apply basic container security best practices

## Sections

| Section | Focus | Outcome |
| --- | --- | --- |
| [`01-production-deployment.md`](./01-production-deployment.md) | Deploying containers in production | You understand rollout, configuration, logs, persistence, and recovery concerns |
| [`02-portainer-operations.md`](./02-portainer-operations.md) | Managing Docker images and containers with Portainer | You can use Portainer as an operational dashboard |
| [`03-security-best-practices.md`](./03-security-best-practices.md) | Security best practices | You know the most important early safety habits |

## Why This Module Matters

A local Docker demo can succeed even with habits that would cause pain in real environments.

This module is here to help you avoid common beginner mistakes such as:

- relying on `latest`
- storing secrets directly in Compose files
- treating containers as if they are pets instead of replaceable units
- mounting sensitive host paths without understanding the risk
- exposing services publicly without thinking about access control

## Mini Quiz

1. Why is a Compose file that works on your laptop not automatically production-ready?
2. Why is Portainer useful even if you already know the CLI?
3. Why is mounting `/var/run/docker.sock` powerful and risky?

## Next Step

Start with [`01-production-deployment.md`](./01-production-deployment.md).
