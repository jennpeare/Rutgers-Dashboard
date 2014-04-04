import requests, json
from pprint import pprint

busURL = "http://runextbus.herokuapp.com/config"

busdata = requests.get(busURL).json()

stops_buses = {}

for stopinfo in busdata["stops"].itervalues():
    stops_buses[stopinfo["title"]] = stopinfo["routes"]

keylist = stops_buses.keys()
keylist.sort()

for stop in keylist:
    print stop + ": [",
    for bus in stops_buses[stop]:
        print bus.upper(),
    print "]"
