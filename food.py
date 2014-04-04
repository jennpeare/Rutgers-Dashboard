import requests, json
from pprint import pprint

foodURL = "https://rumobile.rutgers.edu/1/rutgers-dining.txt"

fooddata = requests.get(foodURL).json()

#pprint(fooddata)

for location in fooddata:
    print location["location_name"]
    for meals in location["meals"]:
        print "\t" + meals["meal_name"]
        if meals["meal_avail"] == True:
            for genres in meals["genres"]:
                print "\t\t" + genres["genre_name"]
                for item in genres["items"]:
                    print "\t\t\t" + item


