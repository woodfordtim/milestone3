import os
from os import path
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

if path.exists("env.py"):
    import env

app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.config["MONGODB_NAME"] = os.environ.get('MONGODB_NAME')

mongo = PyMongo(app)

@app.route('/')
@app.route('/find_events')
def find_events():
    return render_template("events.html", events=mongo.db.events.find())

@app.route('/add_event')
def add_event():
    return render_template('addevent.html', 
    event_type=mongo.db.event_type.find()) # event_type refers to Collection so must be accurate

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
