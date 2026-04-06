import os
from pathlib import Path

from fastapi.testclient import TestClient


TEST_DB_PATH = Path("test_league.db")
if TEST_DB_PATH.exists():
    TEST_DB_PATH.unlink()
os.environ["DATABASE_URL"] = f"sqlite:///{TEST_DB_PATH}"

from app.main import app  # noqa: E402


client = TestClient(app)


def teardown_module() -> None:
    if TEST_DB_PATH.exists():
        TEST_DB_PATH.unlink()


def test_homepage_renders_new_navigation_and_controls() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert "Play New Week" in response.text
    assert "Previous Results" in response.text
    assert "Season Calendar" in response.text
    assert "Cup Trophy" in response.text


def test_health_endpoint_reports_20_teams() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert payload["teams_seeded"] == 20
    assert payload["current_week"] >= 4


def test_standings_endpoint_returns_20_team_league() -> None:
    response = client.get("/api/standings")
    assert response.status_code == 200
    payload = response.json()
    assert len(payload["items"]) == 20
    assert all(item["played"] <= 38 for item in payload["items"])


def test_play_week_advances_season() -> None:
    before = client.get("/health").json()["current_week"]
    response = client.post("/api/simulation/play-week")
    assert response.status_code == 200
    payload = response.json()
    assert payload["advanced"] is True
    assert payload["week_played"] == before + 1


def test_calendar_contains_full_league_schedule() -> None:
    response = client.get("/api/calendar")
    assert response.status_code == 200
    weeks = response.json()["items"]
    assert len(weeks) == 38
    league_matches = sum(
        1
        for week in weeks
        for match in week["matches"]
        if match["competition"] == "league"
    )
    assert league_matches == 380


def test_cup_view_exists() -> None:
    response = client.get("/cup")
    assert response.status_code == 200
    assert "Knockout round every two weeks" in response.text
