import sys

sys.path.insert(0, ".")

from app.main import app


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "UP"


def test_ready():
    client = app.test_client()

    response = client.get("/ready")

    assert response.status_code == 200
    assert response.get_json()["status"] == "READY"