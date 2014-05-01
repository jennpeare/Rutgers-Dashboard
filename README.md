# Rutgers Dashboard

## Overview
### Group Members
- Jenny Shi
- Changling Huang
- Gloria Leung
- David Goldman

###Our Project
We made a dashboard web application intended for Rutgers students. It displays information useful for everyday happenings, such as Nextbus, dining hall menus, and the current weather. This web app is hosted on the hackerspace server and can also be displayed on a monitor through a Raspberry Pi.

## Method
###Key Software
- Arduino (previous attempt)
- Raspberry Pi
- Display monitor (Lilliput)
- Web server
- Various APIs (Wunderground, Nextbus, etc.)

###Final Design
Our initial idea was to display useful information on a scrolling LED screen powered by an Arduino. This was later changed to the Raspberry Pi and display monitor, since it would provide more space and capability to display more useful information. The information is a web application written in Python, styled with the Foundation framework, and served through Flask.

To run the script, type `python app.py`. This will spin up a localhost server at `http://0.0.0.0:8080`, where the dashboard will be displayed. If this script is run on the hackerspace server, the app can be reached at `http://hs-rack2.cs.rutgers.edu:8080`. Anyone connected to the Rutgers network can reach this page.

The web app itself will display the following information:

- Live clock (local time)
- Useful links
- Quote of the Day (that actually changes with every refresh)
- Weather and temperature at current location, with link to full forecast
- Nextbus predictions at Hill Center and BCC
- Dining hall menus for all four dining halls

## Results
![Arduino LED screen](https://raw.githubusercontent.com/jennpeare/hackerspace_proj/master/static/img/arduino.jpg "Arduino LED screen")

	Previous attempt to display information on an Arduino.

![Dashboard Screenshot](https://raw.githubusercontent.com/jennpeare/hackerspace_proj/master/static/img/dashboard.png "Dashboard Screenshot")
	
	Final version of the web application

![Pi Setup](https://raw.githubusercontent.com/jennpeare/hackerspace_proj/master/static/img/pisetup.jpg "Pi Setup")

	Raspberry Pi and Lilliput display screen setup

## Final thoughts
###Future work, extensions
- Fix the clock javascript to display correct time zone (EST) instead of from local computer time (UK time for the pi)
- Include current location detection for Nextbus and food menus
- Applications for other schools (expand target users beyond Rutgers students)
- User customization: pick preferred widgets to display
- Possibly make it into a Chrome extension

###Pitfalls and snags
- A lot of trouble getting initial project idea (Arduino) to work
	- Issue with LED displaying scrolling text: would not scroll on one line
- Lack of experience with Python--learning experience :)
- Trouble setting up the Raspberry Pi

###Things you'd do differently next time
- More planning and sketching out ideas before diving into code
- Better coordination for team meetings