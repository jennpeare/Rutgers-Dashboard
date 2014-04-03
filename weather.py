import json, requests
from pprint import pprint
from secrets import wunder_key

weatherURL="http://api.wunderground.com/api/" + wunder_key + "/conditions/q/autoip.json"

if __name__ == "__main__":
    #pprint(requests.get(weatherURL).json())
    weatherdata = (requests.get(weatherURL).json())

info = weatherdata["current_observation"]
location = weatherdata["current_observation"]["display_location"]
degree_sign= u"\N{DEGREE SIGN}"

print location["city"] + ", " + location["state"] # location
print info["weather"]
print "Current temperature: " + str(info["temp_f"]) + degree_sign + "F | " + str(info["temp_c"]) + degree_sign + "C"
print "Feels like: " + str(info["feelslike_f"]) + degree_sign + "F | " + str(info["feelslike_c"]) + degree_sign + "C"


