import os
from os import path
from flask import Flask, render_template, redirect, request, url_for, request, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)  # (__name__) is a built in Flask variable

app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.config["MONGODB_NAME"] = os.environ.get('MONGODB_NAME')
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html")

""" function for page to display a list all events """
@app.route('/find_events')
def find_events():
    events = list(mongo.db.events.find())
    return render_template("events.html", events=events)


""" function for form to add events """
@app.route('/add_event')
def add_event():
    return render_template('add_event.html', 
        sports=mongo.db.sports.find())


""" sumbit a new event to form http method POST and create a new event """
@app.route('/insert_event', methods=["GET", "POST"])
def insert_event():
    events = mongo.db.events
    print(request.form.to_dict())
    events.insert_one(request.form.to_dict())  # insert in a request object and then convert the form to dictionary
    return redirect(url_for('find_events'))  # redirect back to list of events page

""" enable user to edit event """
@app.route('/edit_event/<event_id>', methods=["GET", "POST"])
def edit_event(event_id):
    the_event = mongo.db.events.find_one({"_id": ObjectId(event_id)})
    all_sports = mongo.db.sports.find()
    return render_template('edit_event.html', 
        event = the_event, sports=all_sports)


""" send edited data back to MongoDB and update database """
@app.route('/update_event/<event_id>', methods=['POST']) 
def update_event(event_id):
    events = mongo.db.events
    events.update({'_id': ObjectId(event_id)},
    {
        'event_name': request.form.get('event_name'),
        'sport_name': request.form.get('sport_name'),
        'event_distance': request.form.get('event_distance'),
        'cost': request.form.get('cost'),
        'location': request.form.get('location'),
        'event_coordinates': request.form.get('event_coordinates'),
        'event_date': request.form.get('event_date'),
        'last_updated': request.form.get('last_updated'),
        'event_contacts': request.form.get('event_contacts'),
        'author': request.form.get('author'),
        'link': request.form.get('link'),
        'img_url': request.form.get('img_url'),
        'description': request.form.get('description')
    })
    return redirect(url_for('find_events'))  # redirect back to list of events page

""" allow deletion of events """
@app.route('/delete_event/<event_id>')
def delete_event(event_id):
    mongo.db.events.remove({'_id': ObjectId(event_id)})
    return redirect(url_for('find_events'))  # redirect back to list of events page
    

""" display list of sports """
@app.route('/find_sports')
def find_sports():
    return render_template('sports.html', 
        sports=mongo.db.sports.find()) 

""" edit a sport """
@app.route('/edit_sport/<sports_id>', methods=["GET", "POST"]) 
def edit_sport(sports_id):
    print(sports_id)
    if request.method == "POST":
        sports = mongo.db.sports.find_one({'_id': ObjectId(sports_id)})
        mongo.db.sports.update_one(sports, {"$set": request.form.to_dict()})
        return render_template('sports.html', 
            sports=mongo.db.sports.find())
    return render_template('edit_sport.html', 
        sports=mongo.db.sports.find_one({'_id': ObjectId(sports_id)}))


""" update sport in database """
@app.route('/update_sport/<sports_id>', methods=['POST'])
def update_sport(sports_id):
    print(sports_id)
    mongo.db.sports.update(
        {'id': ObjectId(sports_id)},
        {'sport_name': request.form.get('sport_name')})
    return redirect(url_for('find_sports'))

""" delete a sport """
@app.route('/delete_sport/<sports_id>')
def delete_sport(sports_id):
    mongo.db.sports.remove({'_id': ObjectId(sports_id)})
    return redirect(url_for('find_sports'))

""" add new sport """
@app.route('/insert_sport', methods=['POST'])
def insert_sport():
    sports=mongo.db.sports  # access the mongo DB
    sports_doc = {'sport_name': request.form.get('sport_name')} 
    sports.insert_one(sports_doc)  # insert sport to data collection
    return redirect(url_for('find_sports'))  # redirect back to list of sports


""" render view to add new sport """
@app.route('/add_sport')
def add_sport():
    return render_template('add_sport.html')

""" view more info on event """
@app.route('/view_event/<event_id>')
def view_event(event_id):
    the_event = mongo.db.events.find_one({"_id": ObjectId(event_id)})
    return render_template('view_event.html', event=the_event)


""" Logo on feature - new feature for next version """
@app.route('/<username>')
def user(username):
    return "Welcome, " + username

@app.route('/logon', methods = ["GET", "POST"])
def logon():

    if request.method  == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(session["username"])
    
    return render_template('logon.html')


if __name__ == '__main__': # __main__ is the name of the default module in Python
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
            debug=True)
