# Lesson 1.1: Virtual Machines vs Containers

This lesson explains the biggest conceptual shift new Docker users need to make: a container is not a full machine.

## Core Idea

A virtual machine includes its own operating system.

A container shares the host kernel and packages only the application and the dependencies it needs.

That one difference explains most of the practical tradeoffs.

## Quick Comparison

| Topic | Virtual Machine | Container |
| --- | --- | --- |
| Includes full OS | Yes | No |
| Startup time | Usually slower | Usually faster |
| Size | Often larger | Often smaller |
| Isolation | Stronger OS-level isolation | Process-level isolation |
| Best for | Different OS or strong isolation needs | App packaging and repeatable environments |

## Why Containers Feel Lightweight

With VMs, each instance has to carry:

- its own guest OS
- system services
- more disk usage
- more boot overhead

With containers, multiple workloads can share the same host kernel while staying isolated enough for many application use cases.

That is why Docker is popular for:

- local development
- CI pipelines
- microservices
- temporary databases and tools

## When A VM Is Still The Better Fit

Use a VM when you need:

- a different operating system from the host
- stricter isolation boundaries
- legacy software that expects full machine behavior
- low-level system control that containers do not provide cleanly

## When A Container Is Usually The Better Fit

Use a container when you want:

- fast startup
- reproducible app environments
- simple dependency packaging
- easy cleanup and redeployment
- multiple services on one development machine

## Docker Learning Lens

For this repository, the important takeaway is simple:

- VMs are entire machines
- containers are isolated application environments

If you keep that in mind, Docker commands will make much more sense.

## Summary

- Containers are lighter because they do not boot a full guest OS.
- VMs are heavier, but provide stronger isolation and OS independence.
- Most beginner Docker workflows are about packaging and running apps, so containers are the right model for this course.

## Next Step

Continue to [`02-images-containers.md`](./02-images-containers.md).
