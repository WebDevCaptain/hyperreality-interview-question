import pytest
from database.models.passenger import Passenger, PassengerSchema
from server_config import db
from app import connexion_app
from seed_database import seed


@pytest.fixture
def test_client():
    seed()
    flask_app = connexion_app.app

    with flask_app.test_client() as test_client:
        yield test_client


@pytest.fixture
def cleanup():
    yield
    # This is executed when the test using the fixture is done
    db.session.remove()
    db.drop_all()
