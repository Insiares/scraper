import subprocess
from flask import Flask, redirect
from pymongo import MongoClient
from waitress import serve

app = Flask(__name__)


@app.route("/scrap")
def scrap():
    spider_name = "quotes"

    try:
        subprocess.check_output(["scrapy", "crawl", spider_name])
        return redirect("/quote", code=302)
    except Exception:
        return "Scraping failed"


@app.route("/quote")
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
        return f"""<h1>Quote of the Day</h1>
                <h2>{quote["author"]}</h2>
                <p>{quote["content"]}</p>"""
    except Exception:
        return """<h1>There is no quote to display</h1>
        <h2>Sadge</h2>
        <p>use /scrap route to populate our knowledge</p>"""


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)
