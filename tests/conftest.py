import pytest
from pymongo import MongoClient
from app import scrap, quoting


# testing the mongodb connection
@pytest.fixture
def mongo_connection():
    try:
        client = MongoClient()
        yield client
    except Exception:
        pytest.fail("Could not yield DB client")


def test_mongo_db(mongo_connection):
    try:
        db = mongo_connection.quote_db
        yield db
    except Exception:
        pytest.fail("Could not connect to MongoDB")


# Test scrap function
def test_scrap():
    try:
        scrap()
    except Exception:
        pytest.fail("Scraping failed")


# test quote function
def test_quote():
    try:
        quoting()
    except Exception:
        pytest.fail("Quoting failed")
