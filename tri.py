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

# function for page to display a list all events
@app.route('/')
@app.route('/find_events')
def find_events():
    return render_template("events.html", 
    events=mongo.db.events.find())


# function for form to add events
@app.route('/add_event')
def add_event():
    return render_template('add_event.html', 
    sports=mongo.db.sports.find()) # event_type refers to Collection so must be accurate


# function to sumbit a new event to form http method POST (default is GET) and create a new event
@app.route('/create_event', methods=['POST'])
def create_event():
    events=mongo.db.events
    print(request.form.to_dict())
    events.insert_one(request.form.to_dict()) #insert when you submit info to a uri it does so in a request object and then convert the form to dictionary so it can be understood by MongoDB
    return redirect(url_for('find_events')) #redirect back to list of events page

# function to enable user to edit event
@app.route('/edit_event/<event_id>')
def edit_event(event_id):
    the_event = mongo.db.events.find_one({"_id": ObjectId(event_id)})
    all_sports = mongo.db.sports.find()
    return render_template('edit_event.html', event=the_event, sports=all_sports)


# function to send edited data back to MongoDB and update database
@app.route('/update_event/<event_id>', methods=['POST']) 
def update_event(event_id):
    events = mongo.db.events
    events.update( {'_id': ObjectId(event_id)},
    {
        'event_name': request.form.get('event_name'),
        'sports': request.form.get('sports'),
        'distance': request.form.get('distance'),
        'cost': request.form.get('cost'),
        'difficulty': request.form.get('difficulty'),
        'location_url': request.form.get('location_url'),
        'event_date': request.form.get('event_date'),
        'last_updated': request.form.get('last_updated'),
        'event_contacts': request.form.get('event_contacts'),
        'author': request.form.get('author'),
        'link': request.form.get('link')
    })
    return redirect(url_for('find_events')) #redirect back to list of events page

# function allow deletion of events
@app.route('/delete_event/<event_id>')
def delete_event(event_id):
    mongo.db.events.remove({'_id': ObjectId(event_id)})
    return redirect(url_for('find_events')) #redirect back to list of events page
    

# function for page to display list all event types (i.e categories)
@app.route('/find_sports')
def find_sports():
    return render_template('sports.html', 
    sports=mongo.db.sports.find()) #sports refers to for collection

# function take the user to editable page (a form)
@app.route('/edit_sport/<sports_id>') #'url for' points towards the name of a function, not the name of the route
def edit_sport(sports_id): # sports_id as a parameter to search for document in db to feed edit into form
    return render_template('edit_sport.html',
    sports=mongo.db.sports.find_one( #should there be an s in eventtypes... or not?
    {'_id': ObjectId(sports_id)}))


# update is used to carry out the update to the database
@app.route('/update_sport/<sports_id>', methods=['POST'])
def update_sport(sports_id):
    mongo.db.sports.update(
        {'id': ObjectId(sports_id)},
        {'sport_name': request.form.get('sport_name')})
    return redirect(url_for('find_sports'))


@app.route('/delete_sport/<sports_id>')
def delete_sport(sports_id):
    mongo.db.event_type.remove({'_id': ObjectId(sports_id)})
    return redirect(url_for('find_sports'))


@app.route('/insert_sport', methods=['POST'])
def insert_sport():
    sports=mongo.db.sports #access the mongo DB
    sports_doc = {'sports': request.form.get('sport')} #'sports' refers to form field
    mongo.db.event_type.insert_one(sports_doc) #inserts new event type to data collection
    return redirect(url_for('find_sports')) #redirects back to list of event_types


# function to direct us and render the view that allows us to insert sport
@app.route('/new_sport')
def new_sport():
    return render_template('add_sport.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
