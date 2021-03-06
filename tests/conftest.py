import pytest
from config import ConfigNames
from main import create_app, db


@pytest.fixture(autouse=True, scope='session')
def setup_db():
    app = create_app(ConfigNames.TESTING)

    with app.test_client() as client:
        with app.app_context():
            db.drop_all()
            db.create_all()
        yield client


@pytest.fixture
def client():
    app = create_app(ConfigNames.TESTING)

    with app.test_client() as client:
        with app.app_context():
            pass
        yield client
