from fastapi.testclient import TestClient

from api.main import app
from api.settings import Settings

client = TestClient(app)


def test_health_ok() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["model_loaded"] is False


def test_cors_origins_parsed_from_comma_list() -> None:
    settings = Settings(cors_origins="https://a.example, https://b.example,")
    assert settings.cors_origin_list == ["https://a.example", "https://b.example"]
