import os
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import Depends, FastAPI, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.service import (
    ensure_league_seeded,
    get_dashboard_data,
    get_matchday_groups,
    get_recent_results,
    get_standings,
    get_top_scorers,
    get_upcoming_fixtures,
    reset_league,
)


BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    with Session(engine) as db:
        ensure_league_seeded(db)
    yield


app = FastAPI(
    title="Football League Simulator",
    description="A Flashscore-inspired football dashboard powered by fake generated results.",
    version=os.getenv("APP_VERSION", "0.2.0"),
    lifespan=lifespan,
)

app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")


@app.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)) -> HTMLResponse:
    dashboard = get_dashboard_data(db)
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context=dashboard,
    )


@app.get("/health")
def health(db: Session = Depends(get_db)) -> dict:
    return {
        "status": "ok",
        "environment": os.getenv("APP_ENV", "local"),
        "app_name": os.getenv("APP_NAME", "data-engineering-league-simulator"),
        "version": os.getenv("APP_VERSION", "0.2.0"),
        "teams_seeded": len(get_standings(db)),
    }


@app.get("/api/standings")
def standings(db: Session = Depends(get_db)) -> dict:
    return {"league": "Data Engineering Premier League", "items": get_standings(db)}


@app.get("/api/scorers")
def scorers(db: Session = Depends(get_db)) -> dict:
    return {"items": get_top_scorers(db)}


@app.get("/api/results")
def results(db: Session = Depends(get_db)) -> dict:
    return {"items": get_recent_results(db)}


@app.get("/api/fixtures")
def fixtures(db: Session = Depends(get_db)) -> dict:
    return {"items": get_upcoming_fixtures(db)}


@app.get("/api/matchdays")
def matchdays(db: Session = Depends(get_db)) -> dict:
    return {"items": get_matchday_groups(db)}


@app.post("/api/simulation/generate")
def generate_simulation(
    seed: int | None = Query(default=None, description="Optional seed for reproducible fake results."),
    db: Session = Depends(get_db),
) -> dict:
    return reset_league(db, seed=seed)

