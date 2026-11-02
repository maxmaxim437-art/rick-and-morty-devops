from app import app


def test_healthcheck():
    client = app.test_client()

    response = client.get("/healthcheck")

    assert response.status_code == 200
    assert response.json == {"status": "healthy"}
