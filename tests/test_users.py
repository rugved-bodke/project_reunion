from fastapi.testclient import TestClient
from api import main

app = main._get_app()
client = TestClient(app)

def test_check_db():
    response = client.get("/check_db")
    assert response.status_code == 200