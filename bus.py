import requests, json
from pprint import pprint

busURL = "http://runextbus.herokuapp.com/config"

def main():
    pprint(get_predictions_for("Hill Center"))
    pprint(get_predictions_for("Busch Campus Center"))

def get_stops_info():

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


def get_predictions_for(stop):

    url_stop = stop.replace(" ", "%20")
    url = "http://runextbus.herokuapp.com/stop/" + url_stop
    data = requests.get(url).json()

    res = []

    for route in data:
        if route["predictions"] is not None:
            bus = {}
            bus["route"] = route["title"]
            bus["direction"] = route["direction"]
            predictions = []
            for time in route["predictions"]:
                predictions.append(time["minutes"])
            bus["predictions"] = predictions
            res.append(bus)

    return res

if __name__ == "__main__":
    main()
