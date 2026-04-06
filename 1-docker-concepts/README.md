# Module 1: Docker Concepts

This module gives you the mental model that makes the CLI exercises easier to understand.

## Learning Goal

By the end of this module, you should be able to explain:

- why containers exist
- how containers differ from virtual machines
- what an image is
- what a container is
- what a registry and a tag are
- what the Docker client and daemon each do

## Lessons

| Lesson | Focus | Why it matters |
| --- | --- | --- |
| [`01-virtualization-vs-containers.md`](./01-virtualization-vs-containers.md) | VMs vs containers | Explains why Docker feels faster and lighter |
| [`02-images-containers.md`](./02-images-containers.md) | Images, containers, registries, tags | Gives you the core Docker vocabulary |
| [`03-architecture.md`](./03-architecture.md) | Client, daemon, socket, objects | Helps you reason about how Docker works under the hood |

## Recommended Reading Order

1. Read the VM vs container comparison.
2. Learn the image/container/registry/tag model.
3. Finish with the Docker architecture overview.

## What To Pay Attention To

While reading, focus on these ideas:

- containers are not tiny virtual machines
- images are templates, containers are running instances
- registries store images
- tags identify versions or variants
- the Docker CLI talks to the Docker daemon

If you understand those five points, the hands-on section becomes much easier.

## Quick Self-Check

Try answering these before moving on:

1. Why are containers usually faster to start than VMs?
2. What is the difference between `nginx:alpine` and a running container named `web`?
3. Where does Docker pull an image from if it is not available locally?
4. Why is relying on `latest` usually a bad idea for reproducible environments?

## Module Exercise

Write short answers to these in your own words:

1. Explain image vs container using one concrete example.
2. Explain why containers usually start faster than VMs.
3. Explain what role the daemon plays when you run `docker run`.

If you can answer those without looking back, you are ready for the setup and CLI practice modules.

## Checklist

- [ ] I can explain image vs container
- [ ] I can explain VM vs container at a high level
- [ ] I know what a registry does
- [ ] I know what a tag represents
- [ ] I know the Docker client is not the same thing as the daemon

## Next Step

Start with [`01-virtualization-vs-containers.md`](./01-virtualization-vs-containers.md).
