from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Study Tasks API działa!"}

def test_create_task():
    response = client.post("/tasks", json={"name": "Test DevOps"})
    assert response.status_code == 200
    assert response.json()["task"]["name"] == "Test DevOps"
