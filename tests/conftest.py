import pytest
from pymongo import MongoClient
import requests


# testing the mongodb connection
@pytest.fixture
def mongo_connection():
    client = MongoClient()
    yield client


@pytest.fixture
def mongo_db(mongo_connection):
    try:
        db = mongo_connection.quote_db
        yield db
    except Exception:
        pytest.fail("Could not connect to MongoDB")


# Test api response
@pytest.fixture
def api_response():
    FLASK_API_URL = "http://127.0.0.1:5000/quote"
    try:
        response = requests.get(FLASK_API_URL)
        yield response
    except Exception:
        pytest.fail("Could not connect to API")


def test_api_response(api_response):
    assert api_response.status_code == 200
