import pytest
from pymongo import MongoClient
from app import scrap, quoting, init_logger


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


@pytest.fixture()
def run_logger():
    logger, file_handler = init_logger()
    return logger, file_handler


# Test scrap function
def test_scrap(run_logger):
    try:
        scrap()
    except Exception:
        pytest.fail("Scraping failed")


# test quote function
def test_quote(run_logger):
    try:
        quoting()
    except Exception:
        pytest.fail("Quoting failed")
