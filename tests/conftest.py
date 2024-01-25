import pytest
from pymongo import MongoClient
from app import app


@pytest.fixture()
def app2():
    app.config.update({
        "TESTING": True,
    })
    yield app


@pytest.fixture()
def client(app2):
    return app2.test_client()


@pytest.fixture()
def runner(app2):
    return app2.test_cli_runner()


def test_api(client):
    response = client.get("/")
    assert response.status_code == 200


def test_scrap(client):
    response = client.get("/scrap")
    assert response.status_code == 302


# testing the mongodb connection
@pytest.fixture()
def mongo_connection():
    try:
        client = MongoClient()
        return client
    except Exception:
        pytest.fail("Could not yield DB client")


def test_mongo_db(mongo_connection):
    try:
        mongo_connection.quote_db
    except Exception:
        pytest.fail("Could not connect to MongoDB")
