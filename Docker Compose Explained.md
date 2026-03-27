# Docker Compose Explained

## Overview

Docker Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application's services, networks, and volumes, then with a single command, you create and start all the services from your configuration.

```
┌─────────────────────────────────────────────────────────────────┐
│                   Docker Compose Workflow                         │
│                                                                  │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐    │
│  │ docker-     │     │   docker-   │     │   docker-   │    │
│  │ compose.yml │────▶│   compose   │────▶│   up        │    │
│  │             │     │   config    │     │   (running)  │    │
│  └─────────────┘     └─────────────┘     └─────────────┘    │
│         │                                        │             │
│         │                                        ▼             │
│         │                            ┌─────────────────┐      │
│         │                            │  Multiple       │      │
│         │                            │  Containers     │      │
│         │                            │  ┌───┐ ┌───┐   │      │
│         │                            │  │app│ │ db │   │      │
│         │                            │  └───┘ └───┘   │      │
│         │                            └─────────────────┘      │
└─────────────────────────────────────────────────────────────────┘
```

---

## Why Docker Compose?

### Problems Without Compose

| Problem | Without Compose | With Compose |
|---------|-----------------|---------------|
| **Multi-container setup** | Run multiple `docker run` commands | Single YAML file |
| **Service dependencies** | Manual startup order | Automatic dependency handling |
| **Configuration** | Complex CLI flags | Human-readable YAML |
| **Reproducibility** | Hard to reproduce | Version controlled config |
| **Cleanup** | Remove containers individually | Single command |

### Key Benefits

- **Define services** in a declarative YAML file
- **Manage dependencies** between services
- **Scale services** easily
- **Reproducible environments** across team members
- **Single command deployment** for entire stack

---

## Installation

### macOS (with Docker Desktop)

Docker Compose is included with Docker Desktop.

```bash
# Verify installation
docker-compose --version
docker compose version
```

### Linux

```bash
# Download binary
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# Make executable
sudo chmod +x /usr/local/bin/docker-compose

# Verify
docker-compose --version
```

### Using Python pip

```bash
pip install docker-compose
```

---

## Basic Syntax

### File Structure

```yaml
# docker-compose.yml
version: "3.8"                    # Compose file version

services:                           # Define services (containers)
  web:
    image: nginx:latest
    ports:
      - "8080:80"
    depends_on:
      - api
    networks:
      - frontend
  
  api:
    build: ./api
    environment:
      - DB_HOST=database
    depends_on:
      - database
  
  database:
    image: postgres:16
    volumes:
      - db-data:/var/lib/postgresql/data
    networks:
      - backend

networks:                           # Define networks
  frontend:
  backend:

volumes:                            # Define volumes
  db-data:
```

### Version Compatibility

| Version | Docker Engine | Features |
|---------|---------------|----------|
| "3.x" | 17.12.0+ | Latest features, Swarm mode |
| "2.x" | 1.10.0+ | Legacy compatibility |
| "3.8" | 19.03.0+ | GPU support, BuildKit |
| "3.9" | 25.0+ | Latest enhancements |

---

## Service Configuration

### Image

```yaml
services:
  web:
    image: nginx:alpine              # Use official image
    image: username/myapp:v1         # Private registry image
    image: redis:7-alpine            # Specific tag
```

### Build

```yaml
services:
  web:
    build:
      context: ./app                 # Build context directory
      dockerfile: Dockerfile.prod   # Custom Dockerfile
      args:                         # Build arguments
        - VERSION=1.0
        - ENV=production
    image: myapp:latest             # Name the built image
```

### Ports

```yaml
services:
  web:
    ports:
      - "3000"                       # Container port only
      - "8080:80"                   # Host:Container
      - "127.0.0.1:8080:80"        # Specific host interface
      - "9090-9091:80-81"          # Port range mapping
```

### Environment Variables

```yaml
services:
  web:
    environment:
      - NODE_ENV=production         # Array syntax
      - DB_HOST=database
      - DB_PORT=5432
    
    # Or as a dictionary
    environment:
      NODE_ENV: production
      DB_HOST: database
```

### Environment File

```yaml
services:
  web:
    env_file:
      - .env
      - .env.production
      - ./config/dev.env
```

### Volumes

```yaml
services:
  web:
    volumes:
      - ./html:/usr/share/nginx/html:ro   # Host:Container
      - nginx-config:/etc/nginx           # Named volume
      - /host/path:/container/path        # Absolute path
      - ~/data:/data                     # Tilde expansion
      
    # Or use named volumes
    volumes:
      - db-data:/var/lib/postgresql/data
```

### Dependencies (depends_on)

```yaml
services:
  api:
    depends_on:
      - database              # Simple dependency
      - cache
    
    # With healthcheck condition
    depends_on:
      database:
        condition: service_healthy
      cache:
        condition: service_started
```

---

## Advanced Configuration

### Health Checks

```yaml
services:
  database:
    image: postgres:16
    healthcheck:
      test: ["CMD", "pg_isready", "-U", "postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s
```

### Resource Limits

```yaml
services:
  web:
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M
```

### Restart Policies

```yaml
services:
  web:
    restart: "no"           # No restart
    restart: on-failure    # Restart on failure
    restart: always        # Always restart
    restart: unless-stopped # Restart unless stopped
```

### Networks

```yaml
services:
  frontend:
    networks:
      - frontend-net
  
  backend:
    networks:
      - frontend-net
      - backend-net
  
  database:
    networks:
      - backend-net

networks:
  frontend-net:
    driver: bridge
    ipam:
      config:
        - subnet: 172.20.0.0/16
  backend-net:
    driver: bridge
```

### Labels

```yaml
services:
  web:
    labels:
      com.example.description: "Web application"
      com.example.department: "Engineering"
      com.example.team: "Platform"
```

### DNS Configuration

```yaml
services:
  web:
    dns: 8.8.8.8
    dns:
      - 8.8.8.8
      - 8.8.4.4
    domainname: example.com
    hostname: web-server
```

### User Configuration

```yaml
services:
  web:
    user: "1000:1000"          # UID:GID
    working_dir: /app
    command: npm start
    entrypoint: /entrypoint.sh
```

---

## Networks Explained

### Network Types

| Driver | Description | Use Case |
|--------|-------------|----------|
| `bridge` | Default network type | Single host, isolated containers |
| `host` | Remove network isolation | Performance critical apps |
| `overlay` | Multi-host networking | Swarm clusters |
| `none` | Disable networking | Isolated containers |

### Communication Between Services

```
┌─────────────────────────────────────────────────────────┐
│                    bridge network                        │
│                                                          │
│  ┌─────────────┐         ┌─────────────┐               │
│  │   web       │────────▶│   api       │               │
│  │  :80        │         │  :3000      │               │
│  └─────────────┘         └──────┬──────┘               │
│                                  │                       │
│                                  ▼                       │
│                          ┌─────────────┐               │
│                          │  database   │               │
│                          │  :5432      │               │
│                          └─────────────┘               │
└─────────────────────────────────────────────────────────┘
```

Services can communicate using service names as hostnames:
- `web` connects to `api` via `http://api:3000`
- `api` connects to `database` via `postgres://database:5432`

---

## Volumes Explained

### Volume Types

| Type | Description | Example |
|------|-------------|---------|
| **Named volumes** | Managed by Docker | `db-data:/var/lib/postgresql` |
| **Bind mounts** | Host directory | `./data:/container/data` |
| **tmpfs mounts** | Memory only | tmpfs data in RAM |
| **named pipes** | Windows only | Windows pipe |

### Named Volumes

```yaml
services:
  database:
    image: postgres:16
    volumes:
      - db-data:/var/lib/postgresql/data

volumes:
  db-data:
    driver: local
    driver_opts:
      type: none
      o: bind
      device: /path/to/host/directory
```

### Where Volumes Are Stored

| Platform | Location |
|----------|----------|
| **macOS (Docker Desktop)** | Inside VM: `~/Library/Containers/com.docker.docker/Data/vms/...` |
| **Linux** | `/var/lib/docker/volumes/` |
| **Windows (Docker Desktop)** | `C:\ProgramData\docker\volumes\` |
| **WSL2** | `\\wsl$\docker-desktop-data\data\docker\volumes\` |

---

## The Docker Socket (/var/run/docker.sock)

### What is it?

The Docker socket (`/var/run/docker.sock`) is the Unix socket that the Docker daemon listens on by default. It allows communication between the Docker client (CLI) and the Docker daemon.

```
┌─────────────────────────────────────────────────────────┐
│                     Host Machine                         │
│                                                          │
│   ┌──────────────┐           ┌──────────────────┐     │
│   │   Docker     │           │   Docker Daemon   │     │
│   │   Client     │──────────▶│   (dockerd)       │     │
│   │   (CLI)      │  socket   │                   │     │
│   └──────────────┘           └────────┬─────────┘     │
│                                        │                 │
│                                        ▼                 │
│                              ┌──────────────────┐      │
│                              │ /var/run/        │      │
│                              │ docker.sock      │      │
│                              └──────────────────┘      │
└─────────────────────────────────────────────────────────┘
```

### Why Container Access to Socket?

Containers like Portainer need access to manage Docker:

```bash
docker run -d \
  -p 9000:9000 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  portainer/portainer
```

### Security Considerations

| Concern | Risk | Mitigation |
|---------|------|------------|
| Root access | Container gets root on host | Avoid in production |
| Container escape | Access host from container | Use read-only mounts |
| Privilege escalation | Full daemon control | Use Docker API proxies |

### Safe Alternatives

```bash
# Read-only socket mount
-v /var/run/docker.sock:/var/run/docker.sock:ro

# Or use Docker API proxy (docker-cli-bindproxy)
```

---

## Command Reference

### Common Commands

```bash
# Start services
docker-compose up -d                  # Start in background
docker-compose up                     # Start in foreground
docker-compose up --build            # Build images first

# Stop services
docker-compose down                  # Stop and remove containers
docker-compose down -v              # Also remove volumes
docker-compose down --rmi all       # Also remove images

# Restart services
docker-compose restart
docker-compose restart web

# View logs
docker-compose logs                  # All services
docker-compose logs -f              # Follow logs
docker-compose logs web             # Specific service

# Execute commands
docker-compose exec web bash        # Interactive shell
docker-compose exec db psql -U postgres  # Run command

# Scale services
docker-compose up -d --scale web=3

# Build images
docker-compose build
docker-compose build --no-cache

# Pull images
docker-compose pull

# List containers
docker-compose ps

# Check configuration
docker-compose config              # Validate and show config
```

### Advanced Commands

```bash
# Run one-time command
docker-compose run web npm test

# Pause/Unpause
docker-compose pause
docker-compose unpause

# Remove stopped containers
docker-compose rm

# Build without cache
docker-compose build --no-cache

# Force recreate containers
docker-compose up -d --force-recreate

# Create volumes
docker-compose create

# Start specific services
docker-compose up -d web api
```

---

## Complete Examples

### Example 1: Web Application Stack

```yaml
version: "3.8"

services:
  web:
    build: .
    ports:
      - "8080:80"
    environment:
      - NODE_ENV=production
      - DATABASE_URL=postgres://db:5432/myapp
    depends_on:
      db:
        condition: service_healthy
    networks:
      - frontend
      - backend
  
  worker:
    build: ./worker
    environment:
      - DATABASE_URL=postgres://db:5432/myapp
    depends_on:
      db:
        condition: service_healthy
    networks:
      - backend
  
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - db-data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - backend
  
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - web
    networks:
      - frontend

networks:
  frontend:
  backend:

volumes:
  db-data:
```

### Example 2: Data Pipeline (Kafka, Spark, MongoDB)

```yaml
version: "3"

services:
  zookeeper:
    image: bitnami/zookeeper:3.7
    ports:
      - "2181:2181"
    environment:
      ALLOW_ANONYMOUS_LOGIN: "yes"
    networks:
      - streaming
  
  kafka:
    image: bitnami/kafka:2.8
    ports:
      - "9093:9093"
    environment:
      - KAFKA_BROKER_ID=1
      - KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper:2181
      - ALLOW_PLAINTEXT_LISTENER=yes
      - KAFKA_CFG_LISTENERS=CLIENT://:9092,EXTERNAL://:9093
      - KAFKA_CFG_ADVERTISED_LISTENERS=CLIENT://kafka:9092,EXTERNAL://localhost:9093
      - KAFKA_INTER_BROKER_LISTENER_NAME=CLIENT
    depends_on:
      - zookeeper
    networks:
      - streaming
  
  spark:
    image: jupyter/pyspark-notebook:spark-3
    ports:
      - "8888:8888"
      - "4040-4080:4040-4080"
    volumes:
      - ./spark:/home/jovyan/work
    networks:
      - streaming
  
  mongodb:
    image: mongo
    volumes:
      - mongodb-data:/data/db
    ports:
      - "27017:27017"
    environment:
      MONGO_INITDB_ROOT_USERNAME: root
      MONGO_INITDB_ROOT_PASSWORD: example
    networks:
      - streaming
  
  mongo-express:
    image: mongo-express
    ports:
      - "8081:8081"
    environment:
      ME_CONFIG_MONGODB_SERVER: mongodb
      ME_CONFIG_MONGODB_ADMINUSERNAME: root
      ME_CONFIG_MONGODB_ADMINPASSWORD: example
    depends_on:
      - mongodb
    networks:
      - streaming

networks:
  streaming:
    driver: bridge

volumes:
  mongodb-data:
```

### Example 3: Development Environment

```yaml
version: "3.8"

services:
  app:
    build:
      context: .
      target: development
    volumes:
      - .:/app
      - /app/node_modules
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=development
      - DEBUG=true
    command: npm run dev
    depends_on:
      - db
      - redis
  
  db:
    image: postgres:16
    volumes:
      - postgres-data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    environment:
      POSTGRES_DB: devdb
      POSTGRES_USER: devuser
      POSTGRES_PASSWORD: devpass
    healthcheck:
      test: ["CMD", "pg_isready", "-U", "devuser"]
  
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis-data:/data
  
  mailhog:
    image: mailhog/mailhog
    ports:
      - "1025:1025"
      - "8025:8025"

volumes:
  postgres-data:
  redis-data:
```

---

## Best Practices

### Security

| Practice | Description |
|----------|-------------|
| Use specific image tags | Avoid `:latest` in production |
| Run as non-root user | `USER` directive in Dockerfile |
| Use secrets | For sensitive data |
| Read-only root filesystem | `read_only: true` |
| Scan images | Use `docker scout` or similar |

### Performance

| Practice | Description |
|----------|-------------|
| Minimize layers | Combine RUN commands |
| Use `.dockerignore` | Exclude unnecessary files |
| Multi-stage builds | Reduce final image size |
| Health checks | Monitor service health |
| Resource limits | Prevent resource exhaustion |

### Organization

| Practice | Description |
|----------|-------------|
| Use version file | Document Docker versions |
| Separate environments | dev, staging, prod configs |
| Externalize config | Use env files |
| Named everything | Services, volumes, networks |
| Document dependencies | Use comments |

---

## Troubleshooting

### Common Issues

#### Service won't start

```bash
# Check configuration
docker-compose config

# View logs
docker-compose logs service-name

# Check container
docker-compose ps
docker inspect container_name
```

#### Port conflicts

```bash
# Check what's using the port
lsof -i :8080

# Change port mapping in compose file
```

#### Volume permissions

```bash
# Fix ownership
docker-compose exec service chown -R user:group /path

# Or use named volumes with specific driver
```

#### Build failures

```bash
# Build with no cache
docker-compose build --no-cache

# Clear builder cache
docker builder prune
```

---

## Additional Resources

| Resource | Description |
|----------|-------------|
| [Docker Compose Documentation](https://docs.docker.com/compose/) | Official Compose docs |
| [Compose File Reference](https://docs.docker.com/compose/compose-file/) | Complete YAML reference |
| [Compose CLI Reference](https://docs.docker.com/compose/reference/) | Command reference |
| [Docker-Fundamentals](https://github.com/team-data-science/Docker-Fundamentals) | Docker basics repo |
| [Document Streaming Example](https://github.com/team-data-science/document-streaming/blob/main/docker-compose-kafka-spark-mongodb.yml) | Kafka/Spark/MongoDB example |
| [Docker Socket Explained](https://betterprogramming.pub/about-var-run-docker-sock-3bfd276e12fd) | Understanding /var/run/docker.sock |
| [Docker Volumes Location (WSL)](https://stackoverflow.com/questions/61083772/where-are-docker-volumes-located-when-running-wsl-using-docker-desktop) | Volume storage on WSL |
