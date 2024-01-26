import subprocess
from flask import Flask, redirect, render_template, request
from pymongo import MongoClient
from waitress import serve
import logging
from module.logger import init_logger
# from flask_mail import Mail, Message

app = Flask(__name__)


# Logging in
logger, file_handler = init_logger()


@app.route("/scrap")
def scrap():
    spider_name = "quotes"
    user_value = request.headers.get('User-Agent')
    try:
        client = MongoClient()
        db = client.quote_db
        collection = db.quotes
        # Check if the indexes are already created
        if not collection.index_information():
            # Create the compound indexes
            collection.create_index([("content", 1)], unique=True)
            collection.create_index([("author", 1)])
        client.close()
        subprocess.check_output(["scrapy", "crawl", spider_name])
        logging.info(f'''Endpoint:
                     /scrap accessed.
                     User-Agent: {user_value}''')
        return redirect("/", code=302)

    except Exception:
        logging.info(f'''Endpoint:
                     /scrap accessed.
                     Scrapping Failed
                     User-Agent: {user_value}''')
        return "Scraping failed", 400


@app.route("/")
def quoting():
    user_value = request.headers.get('User-Agent')
    # Connect to MongoDB
    client = MongoClient()
    # Access the database
    db = client.quote_db

    # Get a random quote at each request
    try:
        # List comprehension that calls a random sample from mongodb
        quote_sample = [doc for doc in db.quotes.aggregate([{
            "$sample": {"size": 1}}])][0]
        client.close()
        logging.info(f'''Endpoint:
                     /quoting accessed.
                     User-Agent: {user_value}''')
        return render_template("quote.html",
                               quote=quote_sample["content"],
                               author=quote_sample["author"]), 200
    except IndexError:
        logging.info(f'''Endpoint:
                     /quoting accessed with empty DB.
                     User-Agent: {user_value}''')
        return render_template("quote.html", quote=None), 200
    except Exception:
        logging.info(f'''Endpoint:
                     /quoting failed
                     User-Agent: {user_value}''')
        return "Quoting failed", 400


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)
