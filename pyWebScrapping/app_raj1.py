# import necessary libraries
from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_raj

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/visipedia_annotation_toolkit"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index_raj.html", mars=mars)


@app.route("/scrape")
def scraper():
    mars = mongo.db.mars
    mars_info = scrape_raj.scrape()
    mars.update(
        {},
        mars_info,
        upsert=True
    )
    return index()


if __name__ == "__main__":
    app.run(debug=True)