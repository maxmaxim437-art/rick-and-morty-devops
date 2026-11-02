
from app import app


def test_characters_status_code():
    client = app.test_client()

    response = client.get("/characters")

    assert response.status_code == 200


def test_characters_returns_list():
    client = app.test_client()

    response = client.get("/characters")

    assert isinstance(response.json, list)
    assert len(response.json) > 0


def test_characters_have_required_fields():
    client = app.test_client()

    response = client.get("/characters")

    characters = response.json

    for character in characters:
        assert "Name" in character
        assert "Location" in character
        assert "Image" in character


def test_character_fields_are_not_empty():
    client = app.test_client()

    response = client.get("/characters")

    for character in response.json:
        assert character["Name"]
        assert character["Location"]
        assert character["Image"]
