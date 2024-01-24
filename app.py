import subprocess
from flask import Flask, redirect, render_template
from pymongo import MongoClient
from waitress import serve

app = Flask(__name__)


@app.route("/scrap")
def scrap():
    spider_name = "quotes"

    try:
        subprocess.check_output(["scrapy", "crawl", spider_name])
        return redirect("/", code=302)
    except Exception:
        return "Scraping failed"


@app.route("/")
def quoting():
    # Connect to MongoDB
    client = MongoClient()
    # Access the database
    db = client.quote_db

    # Get a random quote at each request
    try:
        quote = [doc for doc in db.quotes.aggregate([{
            "$sample": {"size": 1}}])][0]
        client.close()
        return render_template("quote.html", 
                               quote=quote["content"], 
                               author=quote["author"])
    except Exception:
        return render_template("quote.html", quote=None)


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)
