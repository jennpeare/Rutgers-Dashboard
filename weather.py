import json, requests
from pprint import pprint
from secrets import wunder_key

weatherURL="http://api.wunderground.com/api/" + wunder_key + "/conditions/q/autoip.json"
current_cond = []
def main():
    cc = get_weather()
    for s in cc:
        print s

def get_weather():
    weatherdata = requests.get(weatherURL).json()
    info = weatherdata["current_observation"]
    location = weatherdata["current_observation"]["display_location"]
    degree_sign= u"\N{DEGREE SIGN}"

    current_cond.append("Location: " + location["city"] + ", " + location["state"]) # location
    current_cond.append("Current Condition: " + info["weather"])
    current_cond.append("Current temperature: " + str(info["temp_f"]) + degree_sign + "F | " + str(info["temp_c"]) + degree_sign + "C") 
    current_cond.append("Feels like: " + str(info["feelslike_f"]) + degree_sign + "F | " + str(info["feelslike_c"]) + degree_sign + "C")

    return current_cond

if __name__ == "__main__":
    main()
