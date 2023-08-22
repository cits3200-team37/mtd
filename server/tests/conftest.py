import pytest
from server import app


@pytest.fixture()
def app_fixture():
    app.config.update(
        {
            "TESTING": True,
        }
    )
    yield app


@pytest.fixture()
def client(app_fixture):
    return app_fixture.test_client()
