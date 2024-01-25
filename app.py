import subprocess
from flask import Flask, redirect, render_template, request
from pymongo import MongoClient
from waitress import serve
import logging
# from flask_mail import Mail, Message

app = Flask(__name__)


# Logging init
def init_logger():

    format_string = '%(asctime)s - %(levelname)s - %(message)s'
    logger = logging.basicConfig(level=logging.INFO,
                                 format=format_string,
                                 datefmt='[%d/%b/%Y %H:%M:%S]')
    file_handler = logging.FileHandler('./logs/app.log')
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter(format_string, datefmt='[%d/%b/%Y %H:%M:%S]')
    file_handler.setFormatter(formatter)
    logging.getLogger(logger).addHandler(file_handler)

    return logger, file_handler


logger, file_handler = init_logger()


@app.route("/scrap")
def scrap():
    spider_name = "quotes"

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
                     User-Agent: {request.headers.get('User-Agent')}''')
        return redirect("/", code=302)

    except Exception:
        logging.info(f'''Endpoint:
                     /scrap accessed.
                     Scrapping Failed
                     User-Agent: {request.headers.get('User-Agent')}''')
        return "Scraping failed"


@app.route("/")
def quoting():
    # Connect to MongoDB
    client = MongoClient()
    # Access the database
    db = client.quote_db

    # Get a random quote at each request
    try:
        quote_sample = [doc for doc in db.quotes.aggregate([{
            "$sample": {"size": 1}}])][0]
        client.close()
        logging.info(f'''Endpoint:
                     /quoting accessed.
                     User-Agent: {request.headers.get('User-Agent')}''')
        return render_template("quote.html",
                               quote=quote_sample["content"],
                               author=quote_sample["author"])
    except RuntimeError:
        return "Error"
    except Exception:
        logging.info(f'''Endpoint:
                     /quoting accessed with empty DB.
                     User-Agent: {request.headers.get('User-Agent')}''')
        return render_template("quote.html", quote=None)


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)
