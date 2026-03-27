# Exercise 5: Docker Compose
## Multi-Container Applications Made Easy

---

## 🎯 Goal

Learn to:
- Write Docker Compose YAML files
- Define services, networks, and volumes
- Run multi-container applications
- Scale services

**Time: ~40 minutes**

---

## 1️⃣ What is Docker Compose?

Docker Compose lets you define **multi-container applications** in a single YAML file.

```yaml
# docker-compose.yml
version: "3.8"

services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
  
  api:
    image: node:20
    ports:
      - "3000:3000"
```

Then run everything with one command:

```bash
docker compose up -d      # Start all services
docker compose down         # Stop all services
```

---

## 2️⃣ Your First docker-compose.yml

Create a file named `docker-compose.yml`:

```yaml
version: "3.8"

services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html:ro
```

Create the HTML folder:

```bash
mkdir -p html
echo "<h1>Hello from Docker Compose!</h1>" > html/index.html
```

Run it:

```bash
docker compose up -d

# Check
docker compose ps

# Visit http://localhost:8080
open http://localhost:8080

# Stop
docker compose down
```

---

## 3️⃣ Services with Environment Variables

```yaml
version: "3.8"

services:
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: mydb
      POSTGRES_USER: user
      POSTGRES_PASSWORD: secret
    volumes:
      - db-data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  adminer:
    image: adminer
    ports:
      - "8080:8080"
    depends_on:
      - db

volumes:
  db-data:
```

Run:

```bash
docker compose up -d

# Access Adminer at http://localhost:8080
# Server: db
# Username: user
# Password: secret
# Database: mydb

# Clean up
docker compose down -v
```

---

## 4️⃣ Real-World Example: Node.js + PostgreSQL

Create `docker-compose.yml`:

```yaml
version: "3.8"

services:
  api:
    build: .
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgres://user:secret@db:5432/mydb
    depends_on:
      db:
        condition: service_healthy
    volumes:
      - ./src:/app/src

  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: mydb
      POSTGRES_USER: user
      POSTGRES_PASSWORD: secret
    volumes:
      - db-data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user"]
      interval: 5s
      timeout: 5s
      retries: 5

volumes:
  db-data:
```

### Commands

```bash
# Start all services
docker compose up -d

# View logs
docker compose logs -f api

# Execute command in service
docker compose exec api node --version

# Scale service
docker compose up -d --scale api=3

# Stop all
docker compose down -v
```

---

## 5️⃣ Common Commands

| Command | What it does |
|---------|-------------|
| `docker compose up -d` | Start all services (background) |
| `docker compose up --build` | Build images before starting |
| `docker compose down` | Stop and remove containers |
| `docker compose down -v` | Also remove volumes |
| `docker compose ps` | List services |
| `docker compose logs -f` | Follow logs |
| `docker compose exec <service> <cmd>` | Run command in service |
| `docker compose restart <service>` | Restart a service |
| `docker compose stop` | Stop services (keep containers) |
| `docker compose config` | Validate compose file |

---

## 6️⃣ Environment Variables in Compose

### .env file

Create `.env`:

```
POSTGRES_DB=mydb
POSTGRES_USER=user
POSTGRES_PASSWORD=secret123
```

Reference in `docker-compose.yml`:

```yaml
services:
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
```

---

## 🧪 Challenge

Create a complete stack:
- Nginx as reverse proxy (port 80)
- Node.js app (port 3000)
- Redis cache (port 6379)

```yaml
version: "3.8"

services:
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - app

  app:
    image: node:20-slim
    working_dir: /app
    volumes:
      - ./src:/app
    command: node server.js
    environment:
      - REDIS_HOST=redis
    depends_on:
      - redis

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  redis-data:
```

---

## ✅ Checklist

- [ ] Create a docker-compose.yml file
- [ ] Run multiple services with compose
- [ ] Use environment variables
- [ ] Define volumes
- [ ] Use `depends_on` for dependencies
- [ ] Stop all services with compose down

---

## 🚀 Next Steps

**Go to Exercise 6:** [Portainer](./06-portainer.md)
