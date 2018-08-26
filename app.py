import sys
from flask import Flask, render_template, jsonify, redirect
import pymongo
import scrape_mars 

app = Flask(__name__)

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient()
db = client.mars_db

@app.route("/")
def home():
     mars = db.mars_db.find_one()
     return render_template('index.html', mars = mars)

@app.route('/scrape')
def scrape():
    db.mars_db.drop()
    mars_data = scrape()
    db.mars_db.update( 
        {},
        mars_data,
        upsert=True
        )
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)