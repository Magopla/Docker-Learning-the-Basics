# Docker Cheat Sheet

A comprehensive quick reference guide for Docker commands, Dockerfile instructions, and Docker Compose configuration.

---

## Table of Contents

1. [Basic Docker CLIs](#basic-docker-clis)
2. [Container Management](#container-management)
3. [Inspecting Containers](#inspecting-containers)
4. [Interacting with Containers](#interacting-with-containers)
5. [Image Management](#image-management)
6. [Image Transfer Commands](#image-transfer-commands)
7. [Builder Commands](#builder-commands)
8. [Dockerfile Reference](#dockerfile-reference)
9. [Docker Compose](#docker-compose)
10. [Docker Scout (Security)](#docker-scout-security)
11. [Cleanup Commands](#cleanup-commands)
12. [Docker Swarm](#docker-swarm)

---

## Basic Docker CLIs

```bash
docker --version              # Show Docker version
docker info                   # Display system information
docker login                  # Login to Docker Hub
docker logout                 # Logout from Docker Hub
docker search <term>          # Search Docker Hub for images
docker version                # Show Docker version info
```

---

## Container Management

### Creating Containers

```bash
docker create [options] IMAGE
  -a, --attach               # Attach stdout/stderr
  -i, --interactive          # Attach stdin (interactive)
  -t, --tty                  # Pseudo-TTY
  --name NAME                # Assign container name
  -p, --publish 5000:5000   # Port mapping (host:container)
  --expose 5432              # Expose port to linked containers
  -P, --publish-all          # Publish all exposed ports
  --link container:alias     # Link to another container
  -v, --volume `pwd`:/app    # Mount directory
  -e, --env NAME=hello       # Environment variables
```

**Example:**
```bash
docker create --name app_redis_1 --expose 6379 redis:3.0.2
```

### Running Containers

```bash
docker run [options] IMAGE
  -d                          # Run in detached mode (background)
  -it                         # Interactive with TTY
  --rm                        # Remove container after exit
  --name myapp               # Name the container
  -p 8080:80                 # Port mapping
  -e ENV=production          # Environment variable
  -v /host/path:/container/path  # Volume mount
```

**Examples:**
```bash
docker run hello-world                       # Run hello world
docker run -d nginx:latest                   # Run nginx in background
docker run -it ubuntu bash                   # Interactive Ubuntu shell
docker run -p 8080:80 -v $(pwd):/usr/share/nginx/html nginx  # With volume
```

### Starting, Stopping, Restarting

```bash
docker start <container>        # Start a stopped container
docker stop <container>         # Stop a running container
docker restart <container>      # Restart a container
docker pause <container>        # Pause all processes
docker unpause <container>      # Unpause processes
```

### Listing Containers

```bash
docker ps                      # List running containers
docker ps -a                   # List all containers
docker ps -q                   # Show only container IDs
docker ps -l                   # Show latest container
```

**Format output:**
```bash
docker ps --format "table {{.ID}}\t{{.Names}}\t{{.Status}}"
```

### Removing Containers

```bash
docker rm <container>          # Remove stopped container
docker rm -f <container>       # Force remove running container
docker rm $(docker ps -aq)    # Remove all containers
docker container prune        # Remove stopped containers
```

### Container Lifecycle Commands

| Command | Description |
|---------|-------------|
| `docker create` | Create container from image |
| `docker start` | Start existing container |
| `docker run` | Create and start container |
| `docker stop` | Stop running container |
| `docker restart` | Stop and start container |
| `docker pause` | Pause container processes |
| `docker unpause` | Resume container processes |
| `docker rm` | Remove container |

---

## Inspecting Containers

```bash
docker inspect <container>     # Show container details (JSON)
docker logs <container>        # Show container logs
docker logs -f <container>     # Follow log output
docker logs --tail 50 <container>  # Show last 50 lines
docker stats                  # Show resource usage
docker diff <container>        # Show changed files
docker port <container>        # Show port mappings
```

**Get specific info:**
```bash
docker inspect --format '{{.NetworkSettings.IPAddress}}' <container>
docker inspect --format '{{.Config.Image}}' <container>
```

---

## Interacting with Containers

### Executing Commands

```bash
docker exec [options] CONTAINER COMMAND
  -d, --detach        # Run in background
  -i, --interactive   # Interactive stdin
  -t, --tty           # Allocate pseudo-TTY
```

**Examples:**
```bash
docker exec my-container ls -la /app
docker exec -it my-container bash
docker exec -u postgres my-container psql
```

### Copying Files

```bash
docker cp <container>:/path/to/file ./local/path   # Copy from container
docker cp ./local/file <container>:/path/to/file     # Copy to container
```

### Container Processes

```bash
docker top <container>         # Show running processes
docker attach <container>      # Attach to running container
```

---

## Image Management

### Pulling Images

```bash
docker pull <image>            # Pull latest tag
docker pull <image>:tag       # Pull specific tag
docker pull -a <image>        # Pull all tags
docker pull --quiet <image>   # Silent mode
```

### Listing Images

```bash
docker images                 # List local images
docker images -a              # Include intermediate images
docker image ls               # List images (new syntax)
docker image ls -a            # List all images
```

### Building Images

```bash
docker build [options] .
  -t "app/container_name"     # Tag the image
  -f Dockerfile.name         # Specify Dockerfile
  --build-arg KEY=value       # Build arguments
  --no-cache                 # Build without cache
```

### Tagging Images

```bash
docker tag <source> <target>  # Create a tag
docker tag myapp:latest username/myapp:v1.0
```

### Removing Images

```bash
docker rmi <image>            # Remove image
docker rmi $(docker images -q)  # Remove all images
docker image prune            # Remove unused images
docker image prune -a         # Remove all unused images
```

### Image Commands Reference

| Command | Description |
|---------|-------------|
| `docker pull` | Download image from registry |
| `docker push` | Upload image to registry |
| `docker images` | List local images |
| `docker build` | Build image from Dockerfile |
| `docker tag` | Tag an image |
| `docker rmi` | Remove image |
| `docker import` | Import filesystem as image |
| `docker export` | Export container as tar |
| `docker load` | Load image from tar |
| `docker save` | Save image as tar |

---

## Image Transfer Commands

```bash
docker save redis > redis.tar              # Save image to tar
docker load < redis.tar                    # Load image from tar
docker export <container> > container.tar # Export container filesystem
docker import container.tar                # Import tar as image
```

**OCI Directory:**
```bash
skopeo copy --override-os linux docker://alpine oci:alpine
```

---

## Builder Commands

```bash
docker build              # Build image from Dockerfile
docker buildx             # Extended build capabilities
docker builder           # Manage builds
docker image build       # Build image (new syntax)
```

**BuildKit features:**
```bash
DOCKER_BUILDKIT=1 docker build .
docker buildx build --platform linux/amd64,linux/arm64 .
```

---

## Dockerfile Reference

### Inheritance

```dockerfile
FROM ruby:2.2.2
FROM python:3.12-slim
FROM nginx:alpine
```

### Variables

```dockerfile
ENV APP_HOME /myapp
ENV PORT=3000
ARG VERSION=1.0
```

### Working Directory

```dockerfile
WORKDIR /myapp
WORKDIR /workspace
RUN mkdir $APP_HOME
```

### Files Operations

```dockerfile
COPY file.xyz /file.xyz
COPY --chown=user:group host_file.xyz /path/container_file.xyz
ADD archive.tar.gz /extract/here
ADD http://example.com/file.zip /download/
```

### RUN Commands

```dockerfile
RUN apt-get update && apt-get install -y nginx
RUN pip install flask==2.0.0
RUN npm install
```

### Volume Mount Points

```dockerfile
VOLUME ["/data"]
VOLUME ["/var/lib/postgresql/data", "/var/log"]
```

### Expose Ports

```dockerfile
EXPOSE 5900
EXPOSE 3000 8080
```

### Environment Variables

```dockerfile
ENV NODE_ENV=production
ENV DATABASE_URL=postgres://localhost:5432/mydb
```

### Set Default Command

```dockerfile
CMD ["bundle", "exec", "rails", "server"]
CMD python app.py
CMD ["npm", "start"]
```

### Entrypoint (Executable)

```dockerfile
ENTRYPOINT ["executable", "param1", "param2"]
ENTRYPOINT ["python", "app.py"]
```

**With CMD as arguments:**
```dockerfile
ENTRYPOINT ["python", "app.py"]
CMD ["--debug"]
```

### Metadata

```dockerfile
LABEL version="1.0"
LABEL "com.example.vendor"="ACME Incorporated"
LABEL description="This text illustrates \
that label-values can span multiple lines."
```

### Onbuild Triggers

```dockerfile
ONBUILD RUN bundle install
ONBUILD COPY package*.json ./
ONBUILD RUN chmod +x script.sh
```

### Health Checks

```dockerfile
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost/ || exit 1
```

### User

```dockerfile
USER postgres
USER root
USER 1000
```

### Shell Form

```dockerfile
RUN echo $HOME
RUN apt-get update && apt-get install -y curl
```

---

## Docker Compose

### Basic Example

```yaml
# docker-compose.yml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/code
    environment:
      - FLASK_ENV=development
    depends_on:
      - redis

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
```

### Build Configuration

```yaml
services:
  web:
    build:
      context: ./dir
      dockerfile: Dockerfile.dev
    image: myapp:latest
```

### Port Configuration

```yaml
services:
  web:
    ports:
      - "3000"              # Single port
      - "8000:80"           # host:container
      - "127.0.0.1:8001:80" # Specific host interface
    
    expose:                 # Expose to linked services
      - "3000"
```

### Environment Variables

```yaml
services:
  web:
    environment:
      RACK_ENV: development
    env_file:
      - .env
      - .development.env
```

### Dependencies

```yaml
services:
  web:
    depends_on:
      - db
      - redis
    
    links:
      - db:database
      - redis
```

### Volumes

```yaml
services:
  db:
    volumes:
      - db-data:/var/lib/postgresql/data
      - ./logs:/var/log

volumes:
  db-data:
```

### Labels

```yaml
services:
  web:
    labels:
      com.example.description: "Accounting web app"
      com.example.department: "Finance"
```

### DNS Configuration

```yaml
services:
  web:
    dns: 8.8.8.8
    dns:
      - 8.8.8.8
      - 8.8.4.4
```

### Extra Hosts

```yaml
services:
  web:
    extra_hosts:
      - "somehost:192.168.1.100"
      - "api.local:192.168.1.101"
```

### Commands

```bash
docker-compose up -d           # Start in background
docker-compose down            # Stop and remove
docker-compose stop            # Stop services
docker-compose start           # Start services
docker-compose restart         # Restart services
docker-compose ps              # List containers
docker-compose logs -f         # View logs
docker-compose build            # Build images
docker-compose pull            # Pull images
docker-compose exec service cmd # Execute command
docker-compose scale web=3     # Scale service
```

---

## Docker Scout (Security)

### Basic Commands

```bash
docker scout                       # Docker Scout CLI
docker scout cves <image>          # Analyze vulnerabilities
docker scout quickview <image>     # Quick overview
docker scout compare <img1> <img2> # Compare two images
```

### Vulnerability Analysis

```bash
docker scout cves redis:6.0                    # Show CVEs
docker scout cves --format sarif redis:6.0    # SARIF format
docker scout compare --to redis:6.0 redis:7   # Compare versions
```

### Export Options

```bash
docker scout cves --format sarif --output report.sarif.json redis
docker scout cves --format sbom redis        # Software Bill of Materials
```

---

## Cleanup Commands

```bash
docker image prune              # Remove unused images
docker image prune -a          # Remove all unused images
docker container prune         # Remove stopped containers
docker system prune            # Remove unused data (containers, networks, images)
docker system prune -a          # Full cleanup
docker volume prune            # Remove unused volumes
docker network prune           # Remove unused networks
docker builder prune           # Remove build cache
```

**Complete cleanup:**
```bash
docker system prune --volumes  # Include volumes
docker rm $(docker ps -aq)     # Remove all containers
docker rmi $(docker images -q) # Remove all images
docker volume rm $(docker volume ls -q)  # Remove all volumes
```

---

## Docker Swarm

### Service Management

```bash
docker service ls                          # List services
docker service create <image>              # Create service
docker service ps <service>                # List service tasks
docker service logs <service>             # View service logs
docker service scale <service>=5          # Scale service
docker service rm <service>                # Remove service
```

### Stack Management

```bash
docker stack ls                    # List stacks
docker stack deploy -c file.yml myapp  # Deploy stack
docker stack services myapp       # List stack services
docker stack ps myapp             # List stack tasks
docker stack rm myapp             # Remove stack
```

### Node Management

```bash
docker node ls                    # List nodes
docker node inspect <node>       # Inspect node
docker node promote <node>       # Promote to manager
docker node demote <node>        # Demote to worker
docker swarm leave               # Leave swarm
```

---

## Quick Reference Tables

### Common Flags

| Flag | Short | Description |
|------|-------|-------------|
| `--name` | | Container name |
| `-d` | `--detach` | Detached mode |
| `-it` | `--interactive --tty` | Interactive |
| `-p` | `--publish` | Port mapping |
| `-v` | `--volume` | Volume mount |
| `-e` | `--env` | Environment variable |
| `--rm` | | Remove after exit |
| `-f` | `--force` | Force action |

### Status Codes

| Code | Meaning |
|------|---------|
| `Exited (0)` | Clean exit |
| `Exited (1)` | General error |
| `Exited (137)` | OOM killed |
| `Exited (139)` | Segfault |
| `Exited (143)` | SIGTERM |

### Port Mapping Syntax

| Syntax | Description |
|--------|-------------|
| `8080` | Container port 8080 (random host port) |
| `8080:80` | Map host 8080 to container 80 |
| `127.0.0.1:8080:80` | Bind to specific interface |
| `8080-8085:80` | Range mapping |

---

## External Resources

| Resource | URL |
|----------|-----|
| Docker Official Docs | https://docs.docker.com/ |
| Docker Hub | https://hub.docker.com/ |
| Collabnix Cheatsheet | https://dockerlabs.collabnix.com/docker/cheatsheet/ |
| Docker CLI Reference | https://docs.docker.com/engine/reference/commandline/ |
| Dockerfile Reference | https://docs.docker.com/engine/reference/builder/ |
| Docker Compose Reference | https://docs.docker.com/compose/compose-file/ |
