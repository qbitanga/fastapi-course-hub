from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Course Hub API"}

def test_list_courses() -> None:
    response = client.get("/courses")
    assert response.status_code == 200
    assert len(response.json()) == 3

def test_unkown_route_returns_404() -> None:
    response = client.get("/unknown")
    assert response.status_code == 404

def test_wrong_method_returns_405() -> None:
    response = client.post("/")
    assert response.status_code == 405
