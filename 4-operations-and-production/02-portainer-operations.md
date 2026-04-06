# Section 4.2: Managing Docker Images and Containers with Portainer

Portainer is helpful when you want a visual operational view of your Docker environment. It does not replace Docker concepts, but it can make them easier to inspect quickly.

## What Portainer Is Good For

Portainer is especially useful for:

- seeing all containers at once
- checking image versions
- reviewing ports, volumes, and networks
- reading logs quickly
- restarting or removing services without remembering every CLI flag

## Common Operational Tasks

### Review Running Containers

In Portainer, check:

- container status
- image name and tag
- published ports
- mounted volumes
- restart policy

This is often the fastest way to spot drift or a surprising configuration.

### Review Images

Use Portainer to answer:

- which images are actually present locally
- which tags are in use
- which images look unused

This is helpful when learners start experimenting with many examples and lose track of what is running from what.

### Read Logs and Inspect Containers

For a broken service, Portainer can help you quickly:

1. open the container
2. read its logs
3. inspect environment variables and mounts
4. open a console if needed

The same debugging logic still applies as with the CLI:

- start with logs
- then inspect config
- then check connectivity and data paths

### Update Or Redeploy Carefully

Portainer can make container actions look easy, but production-minded habits still matter:

- know which image tag you are deploying
- know whether the service has persistent data
- know whether a restart may interrupt users

## Operational Checklist

- [ ] I can identify what image tag a container is using
- [ ] I can find published ports in Portainer
- [ ] I can inspect logs before restarting a failing service
- [ ] I can tell whether a container uses volumes
- [ ] I understand that Portainer actions still affect the same Docker environment underneath

## Mini Quiz

1. Why is checking the image tag important before restarting or recreating a container?
2. Why should logs usually come before random restarts in a debugging workflow?
3. What extra risk appears when Portainer has access to the Docker socket?

## Next Step

Continue to [`03-security-best-practices.md`](./03-security-best-practices.md).
