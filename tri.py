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

# function for page to list all events
@app.route('/')
@app.route('/find_events')
def find_events():
    return render_template("events.html", events=mongo.db.events.find())

# function for form to add events
@app.route('/add_event')
def add_event():
    return render_template('add_event.html', 
    event_type=mongo.db.event_type.find()) # event_type refers to Collection so must be accurate

# function to sumbit a form http method POST - default is GET
@app.route('/create_event', methods=['POST'])
def create_event():
    events=mongo.db.events
    events.insert_one(request.form.to_dict()) #insert when you submit info to a uri it does so in a request object and then convert the form to dictionary so it can be understood by MongoDB
    return redirect(url_for('/find_events'))

@app.route('/edit_event/<event_id>')
def edit_event(event_id):
    the_event = mongo.db.events.find_one({"_id": ObjectId(event_id)})
    all_event_type = mongo.db.event_type.find()
    return render_template('edit_event.html', event=the_event, event_type=all_event_type)

@app.route('/update_event/<event_id>', methods=['POST']) 
def update_event(event_id):
    events = mongo.db.events
    events.update( {'_id': ObjectId(event_id)},
    {
        'event_name': request.form.get('event_name'),
        'event_type': request.form.get('event_type'),
        'event_distance': request.form.get('event_distance'),
        'cost': request.form.get('cost'),
        'difficulty': request.form.get('difficulty'),
        'location_url': request.form.get('location_url'),
        'event_date': request.form.get('event_date'),
        'last_updated': request.form.get('last_updated'),
        'event_contacts': request.form.get('event_contacts'),
        'author': request.form.get('author'),
        'link': request.form.get('link')
    })
    return redirect(url_for('find_events'))

@app.route('/delete_event/<event_id>')
def delete_event(event_id):
    mongo.db.events.remove({'_id': ObjectId(event_id)})
    return redirect(url_for('find_events'))

@app.route('/find_event_type')
def find_event_type():
    return render_template('event_type.html', 
                            event_types=mongo.db.event_type.find()) #event_types refers to for loop (?)

@app.route('/edit_event_type/<event_type_id>')
def edit_event_type(event_type_id): #event_type_id as a parameter to search for document in db to feed edit into form
    return render_template('edit_event_type.html',
                            event_type=mongo.db.event_type.find_one(
                            {'_id': ObjectId(event_type_id)}))

@app.route('/update_event_type/<event_type_id>', methods=['POST'])
def update_event_type(event_type_id):
    mongo.db.event_type.update({'id': ObjectId(event_type_id)},
        {'event_type': request.form.get('event_type')})
    return redirect(url_for('find_event_type'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
