import pytest
import uuid
import random
from api import app


@pytest.fixture()
def app_fixture():
    app.config.update(
        {
            "TESTING": True,
        }
    )
    yield app


@pytest.fixture()
def client(app_fixture, monkeypatch):
    random.seed(3200)
    monkeypatch.setattr(uuid, "uuid4", lambda: "test_id")
    return app_fixture.test_client()
