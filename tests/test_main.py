from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to DevOps TODO Application"


def test_get_todos():
    response = client.get("/todos")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_todo():
    response = client.get("/todos/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_get_invalid_todo():
    response = client.get("/todos/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "TODO not found"


def test_create_todo():
    response = client.post(
        "/todos",
        json={
            "task": "Learn GitHub Actions"
        }
    )

    assert response.status_code == 200
    assert response.json()["task"] == "Learn GitHub Actions"


def test_update_todo():
    response = client.put(
        "/todos/1",
        json={
            "task": "Learn Docker",
            "completed": True
        }
    )

    assert response.status_code == 200
    assert response.json()["completed"] is True


def test_delete_todo():
    response = client.delete("/todos/2")

    assert response.status_code == 200
    assert response.json()["message"] == "TODO deleted successfully"