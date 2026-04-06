from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_endpoint_returns_ok() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert "environment" in payload


def test_summary_endpoint_has_expected_shape() -> None:
    response = client.get("/summary")
    assert response.status_code == 200
    payload = response.json()
    assert payload["total_datasets"] == 3
    assert payload["stale_datasets"] >= 0
    assert payload["total_records"] > 0
