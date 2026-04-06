# Data Engineering League Simulator

This project is a small Python web application that simulates one fake football league using a generated results API, PostgreSQL persistence, Docker, and Jenkins.

## What You Build

- a FastAPI app with a Flashscore-inspired football dashboard
- a fake internal API that generates random league results
- PostgreSQL persistence for clubs, fixtures, matches, and scorers
- a Docker image and Docker Compose stack for local execution
- a Jenkins pipeline for build, test, and deployment practice

## Project Structure

```text
.
├── app/
├── static/
├── templates/
├── tests/
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
├── requirements.txt
└── README.md
```

## Run Locally With Docker

```bash
docker compose up --build
```

Then open:

- `http://localhost:8000/`
- `http://localhost:8000/docs`
- `http://localhost:8000/api/standings`
- `http://localhost:8000/api/scorers`

## Run Tests

The test suite defaults to a temporary SQLite database so it can run without an external Postgres service:

```bash
docker build -t data-engineering-league-simulator:test .
docker run --rm data-engineering-league-simulator:test pytest
```

## Example Jenkins Flow

The included `Jenkinsfile` performs:

1. source checkout
2. Docker image build
3. API test execution inside the container
4. local image tagging
5. local deployment with Docker Compose and PostgreSQL

## Main API Endpoints

- `GET /api/standings` for the league table
- `GET /api/scorers` for the top scorers list
- `GET /api/results` for recent results
- `GET /api/fixtures` for upcoming fixtures
- `GET /api/matchdays` for grouped fixtures by matchday
- `POST /api/simulation/generate?seed=123` to regenerate the full league with fake random data

## Product Notes

- One league only: `Data Engineering Premier League`
- Eight clubs with generated fixtures and results
- Roughly half the season is already played so the homepage can show both results and upcoming fixtures
- The UI takes inspiration from [Flashscore](https://www.flashscore.com/) with a dense scores-first layout, but it is a simpler single-league learning project

## Create The Private Remote Repository

You can create the remote when ready with GitHub CLI:

```bash
git init
git add .
git commit -m "Initial commit"
gh repo create data-engineering-learning-webapp --private --source=. --remote=origin --push
```
