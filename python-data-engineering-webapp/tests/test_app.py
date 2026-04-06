import os
from pathlib import Path

from fastapi.testclient import TestClient


TEST_DB_PATH = Path("test_league.db")
os.environ["DATABASE_URL"] = f"sqlite:///{TEST_DB_PATH}"

from app.main import app  # noqa: E402


client = TestClient(app)


def teardown_module() -> None:
    if TEST_DB_PATH.exists():
        TEST_DB_PATH.unlink()


def test_homepage_renders_dashboard() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert "Data Engineering Premier League" in response.text
    assert "Top Scorers" in response.text


def test_health_endpoint_returns_seeded_team_count() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert payload["teams_seeded"] == 8


def test_standings_endpoint_returns_single_league_table() -> None:
    response = client.get("/api/standings")
    assert response.status_code == 200
    payload = response.json()
    assert payload["league"] == "Data Engineering Premier League"
    assert len(payload["items"]) == 8
    assert payload["items"][0]["points"] >= payload["items"][-1]["points"]


def test_generate_simulation_endpoint_resets_league() -> None:
    response = client.post("/api/simulation/generate?seed=123")
    assert response.status_code == 200
    payload = response.json()
    assert payload["seeded"] is True
    assert payload["teams"] == 8
    assert payload["matchdays"] == 14
