# Tri-Events
This website is a community driven site to share sporting events. Its focus is, but not exlusive to, triathlon events (inlcuding swimmming, cycling and running). 

This web application can ve found at:
[Tri-Events](https://tri-events.herokuapp.com/)

## UX
### User Stories
* As a triathlete I want to be able to find an event that is near to home, be able to get a summary of the event, know where I can find more information and book the event.

Triathletes and other sports-people can browse events on the 'Find an Event' page, using the map or the cards. They can gain a brief summary of the event from the card or click on ''More info' to get further details.

* As an event organiser I want to be able to promote my event quickly and easily so that like minded triathletes and sports-people can find an event that suits their preferences.

Event organisers can add events by following the 'Create an Event' link in the navbar or from the home page. They can use the forms to add the relevant details about the event and once submitted this will appear on the 'Find an Event' page. Event organisers can also edit and update their events by by following the 'Edit Event' links. Event organisers can also add different sports from within the forms if there sport is not listed in the drop down.


### Wireframes - links from Adobe XD
The wireframes for this web app were created using AdobeXD.

[Wireframe](https://xd.adobe.com/view/61e47119-c405-4e15-aaf0-9628d2dbf283-34b7/)

PDF files also available in the project folders.

## Features
### Feature 1 - Find an event
By following the link in the navbar users are directed to a route that contains a list of the events that have been added. Users can also use the map as quick way to locate events within the preferred area. Click on the marker to take you straight to the event.

Users can find out more information about an event by following the 'More Info' links.

### Feature 2 - Create an event
Users can Create a new event to share with the community using a form.

### Feature 3 - Edit an event
Users can edit an existing event using a form, if required.

### Feature 4 - View an Event
Users can view more information about an event, including an additional map for location.

### Feature 5 - Add a sport
Users can add, edit and delete sports, if required.


## Technologies Used
* CSS
* html
* Python
* Flask
* Jinja
* Materialise (css styling)
* JavaScript
* JQuery (for Materialize features)
* Leaflet - an open-source JavaScript library for mobile-friendly interactive maps. https://leafletjs.com/examples/quick-start/
* Heroku - for Deployment
* GitPod - the IDE use to develop this web app
* MongoDB - the database used to create the web app

## Testing
###  Test 1: Find an Event
Try to find an event by clicking on the link in the navbar and this takes you to the 'find an event' page. The events are listed in a series of cards as expected.

### Test 2: Edit an Event
Click on 'Edit Event' from the 'Find an Events' page takes you to the appropriate form for that event as expected. The event cost was edited and the form submitted and as a result the new cost was displayed correctly.

### Test 3: Create a new event
Following the 'Create an Event' in the Navbar a form is loaded for the user to be able to add a new event. Completing all of the fields correcttly and clicking on 'Create Event' ensures that new event is added correctly to the 'find an event' page. Clciking cancel returns the user back to the 'find an event' page without changes.

### Test 4: Add new sport
Once in the new event form users, clicking on the 'Add Sport' button takes the user to a new page with a list of sports. By clicking 'Add Sport' a single field form loads for the user to add a new sport. Clicking 'add sport' adds the sport to the list of other sports. 

However, there is currently no way of returning to the event that was being edited. Clicking 'Cancel' takes the user back to the 'find events' page. This needs to be updated so that the user can be redirected with a 'return to event form' button.

### Test 4: home page button test
All buttons on the home page redirect you to the correct page.


### Device Testing
The application loads well on all three devices testes, which include iPhone 11, iPad Pro (9 inch version), Windows laptop.

Basic automated testing has been set up in the test_events.py as a starting point. This follows the Python unittest framework, which can be found here:

[Python Unittest](https://docs.python.org/3/library/unittest.html)

## Bugs and Problems
### Getting the map to show each event on the view_event page
There cannot be any events with missing or incorrect coordinates or the site will not load the map for any event. To fix this issue ensure 'coordinates is a required field in the forms.

### Deployment
#### Heroku
The site was deployed using Heroku. 

1. Create an Heroku app with a unique app name.
2. Link Heroku to your local GutHub respository
3. Create the following files, using the CLI as stated below:
    - pip3 freeze --local > requirements.txt
    - echo web: python app.py > Procfile

Link to the Heroku web app:
[Tri-Events](https://tri-events.herokuapp.com/)


#### Local Deployment
You can also deploy the project locally by following the `clone / download` link from the main repository page and copy the link. 
Then, open up a new terminal in your IDE and type 'git clone' followed directly by the copied link.

## New Features to follow in the next version
* Improve styling on the homepage, including adding images to cards.
* Add pop-up to warns users if they are about to delete an event so they do not lose data.
* Ensure redirection from 'Sports' categories returns to the event rather the 'find_events' page.
* Add banner image to improve styling on each page (as per wireframe).
* Add a search and/or filter feature so that events can be located by the users more efficiently.
* Add a log-in feature for authorisation and authentification to be able to prevent unwanted or mailicious loss of data.
* Add further validation for the form in order to prevent duplication and incorrect entries.


## Credits
* Jon Williams (Code Institute student)- Hikes website. Inspiration and how to add maps so that this can show events on a map for the find events and view events pages. [JonWil91_GitHub](https://github.com/JonWil91/Milestone-3), [AddHikes](https://ms3-hikingtrails.herokuapp.com/home)
* Materialize for css styling
* the structure thos development project is based around the 'Task-Manager' mini-project from the Data-centric Development from the Code Institute
* Images are courtesy of [pexels.com](https://www.pexels.com/) and this image is from photographer Pixabay but no specific attributions is required.
