# Rutgers Dashboard

## Overview
### Group Members
- Jenny Shi
- Gloria Leung
- Changling Huang
- David Goldman

###Our Project
We made a dashboard web application intended for Rutgers students. It displays information useful for everyday happenings, such as Nextbus, dining hall menus, and the current weather. This web app is hosted on the hackerspace server and can also be displayed on a monitor through a Raspberry Pi.

## Method
###Key Software
- Arduino (previous attempt)
- Raspberry Pi
- Display screen (Lilliput)
- Web server
- Various APIs (wunderground, nextbus, etc.)

###Final Design
Our initial idea was to display useful information on a scrolling LED screen powered by an Arduino. This was later changed to the Raspberry Pi and display monitor, since it would provide more space and capability to display more useful information. The information is a web application written in Python, styled with the Foundation framework, and served through Flask.

To run the script, type `python app.py`. This will spin up a localhost server at `http://0.0.0.0:8080`, where the dashboard will be displayed. If this script is run on the hackerspace server, the app can be reached at `http://hs-rack2.cs.rutgers.edu:8080`. Anyone connected to the Rutgers network can reach this page.

## Results
![Arduino LED screen](https://raw.githubusercontent.com/jennpeare/hackerspace_proj/master/static/img/arduino.jpg "Arduino LED screen")

	Previous attempt to display information on an Arduino.

![Dashboard Screenshot](https://raw.githubusercontent.com/jennpeare/hackerspace_proj/master/static/img/dashboard.png "Dashboard Screenshot")
	
	Final version of the web application

![Pi Setup](https://raw.githubusercontent.com/jennpeare/hackerspace_proj/master/static/img/pisetup.jpg "Pi Setup")

	Raspberry Pi and Lilliput display screen setup

## Final thoughts
###Future work, extensions
- Fix the clock javascript so that it will display EST instead of reading it from local computer time
- Include current location detection for Nextbus and food menus
- Applications for other schools (useful not only for Rutgers students)
- User customization: they can pick widgets to display
- Possibly make it into a Chrome extension

###Pitfalls and snags
- A lot of trouble getting initial project idea (Arduino) to work
	- Issue with LED displaying scrolling text: would not scroll on one line
- Lack of experience with Python and Raspberry Pi, trouble setting things up at first

###Things you'd do differently next time
- More planning and sketching out ideas before diving into code