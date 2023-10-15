import pytest
import uuid
import random
from api import app
import random
import numpy as np


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
    random.seed(3200)
    np.random.seed(3200)
    return app_fixture.test_client()
