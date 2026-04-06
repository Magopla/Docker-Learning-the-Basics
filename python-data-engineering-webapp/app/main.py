import os
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import Depends, FastAPI, Query, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.service import (
    ensure_league_seeded,
    get_calendar_view,
    get_cup_overview,
    get_dashboard_data,
    get_matches_by_week,
    get_previous_results,
    get_results_by_week,
    get_results_archive,
    get_standings,
    get_top_scorers,
    play_next_week,
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
    description="A Flashscore-inspired single-league football simulator with league and cup play.",
    version=os.getenv("APP_VERSION", "0.3.0"),
    lifespan=lifespan,
)

app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")


def _layout_context(active_page: str) -> dict:
    return {"active_page": active_page}


@app.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)) -> HTMLResponse:
    context = get_dashboard_data(db) | _layout_context("home")
    return templates.TemplateResponse(request=request, name="index.html", context=context)


@app.get("/results", response_class=HTMLResponse)
def results_page(request: Request, db: Session = Depends(get_db)) -> HTMLResponse:
    dashboard = get_dashboard_data(db)
    context = {
        "league": dashboard["league"],
        "season": dashboard["season"],
        "result_weeks": get_results_archive(db),
    } | _layout_context("results")
    return templates.TemplateResponse(request=request, name="results.html", context=context)


@app.get("/calendar", response_class=HTMLResponse)
def calendar_page(request: Request, db: Session = Depends(get_db)) -> HTMLResponse:
    dashboard = get_dashboard_data(db)
    context = {
        "league": dashboard["league"],
        "season": dashboard["season"],
        "calendar_weeks": get_calendar_view(db),
    } | _layout_context("calendar")
    return templates.TemplateResponse(request=request, name="calendar.html", context=context)


@app.get("/cup", response_class=HTMLResponse)
def cup_page(request: Request, db: Session = Depends(get_db)) -> HTMLResponse:
    dashboard = get_dashboard_data(db)
    context = {
        "league": dashboard["league"],
        "season": dashboard["season"],
        "cup": get_cup_overview(db),
    } | _layout_context("cup")
    return templates.TemplateResponse(request=request, name="cup.html", context=context)


@app.post("/play-week")
def play_week(db: Session = Depends(get_db)) -> RedirectResponse:
    play_next_week(db)
    return RedirectResponse(url="/", status_code=303)


@app.get("/health")
def health(db: Session = Depends(get_db)) -> dict:
    dashboard = get_dashboard_data(db)
    return {
        "status": "ok",
        "environment": os.getenv("APP_ENV", "local"),
        "app_name": os.getenv("APP_NAME", "data-engineering-league-simulator"),
        "version": os.getenv("APP_VERSION", "0.3.0"),
        "teams_seeded": len(dashboard["standings"]),
        "current_week": dashboard["season"]["current_week"],
    }


@app.get("/api/standings")
def standings(db: Session = Depends(get_db)) -> dict:
    return {"league": "Data Engineering Premier League", "items": get_standings(db)}


@app.get("/api/scorers")
def scorers(db: Session = Depends(get_db)) -> dict:
    return {"items": get_top_scorers(db)}


@app.get("/api/results")
def results(week: int | None = Query(default=None), db: Session = Depends(get_db)) -> dict:
    if week is None:
        return {"items": get_previous_results(db, weeks=38)}
    return {"week": week, "items": get_results_by_week(db, week)}


@app.get("/api/calendar")
def calendar(db: Session = Depends(get_db)) -> dict:
    return {"items": get_calendar_view(db)}


@app.get("/api/cup")
def cup(db: Session = Depends(get_db)) -> dict:
    return get_cup_overview(db)


@app.post("/api/simulation/generate")
def generate_simulation(
    seed: int | None = Query(default=None, description="Optional seed for reproducible fake results."),
    db: Session = Depends(get_db),
) -> dict:
    return reset_league(db, seed=seed)


@app.post("/api/simulation/play-week")
def play_week_api(db: Session = Depends(get_db)) -> dict:
    return play_next_week(db)
