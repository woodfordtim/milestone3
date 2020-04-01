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
    # events=mongo.db.events.find()
    # print(events)
    return render_template("events.html", events=mongo.db.events.find())

    # sorry, messing with the code, but I see what you're doing now. I still can't see where the 'event.'
    # refers to in the html. It's not clear in the lesson back in the mini-project.

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
