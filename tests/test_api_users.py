import pytest
from utils.api_client import APIClient
from utils.config_reader import load_config

config = load_config()
api = APIClient(config["api_base_url"])


def test_get_users():
    response = api.get("/users")

    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_posts():
    response = api.get("/posts")

    assert response.status_code == 200
    assert len(response.json()) > 0
    print(config)