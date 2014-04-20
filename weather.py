import json, requests
from pprint import pprint
from secrets import wunder_key

weatherURL="http://api.wunderground.com/api/" + wunder_key + "/conditions/q/autoip.json"

def main():
    cc = get_weather()
    for s in cc:
        print s
    pprint(requests.get(weatherURL).json())

def get_weather():
    weatherdata = requests.get(weatherURL).json()
    info = weatherdata["current_observation"]
    location = weatherdata["current_observation"]["display_location"]
    degree_sign= u"\N{DEGREE SIGN}"

    current_cond = {}
    current_cond["location"] = location["city"].upper() + ", " + location["state"] # location
    current_cond["cond_image"] = info["icon_url"]
    current_cond["condition"] = info["weather"]
    current_cond["temp_f"] = str(info["temp_f"]) + degree_sign + "F"
    current_cond["temp_c"] = str(info["temp_c"]) + degree_sign + "C"
    current_cond["url"] = info["forecast_url"]
    return current_cond

if __name__ == "__main__":
    main()
