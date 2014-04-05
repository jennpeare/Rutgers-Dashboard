import requests, json
from pprint import pprint

foodURL = "https://rumobile.rutgers.edu/1/rutgers-dining.txt"
dining_halls = {}

def main():
    get_food_all()
    get_food_dhall("Brower Commons", "Dinner")

def get_food_dhall(dhall, meal):
    dhall = dining_halls.get(dhall)
    if dhall is not None:
        meal = dhall.get(meal)
    return meal

def get_food_all():
    fooddata = requests.get(foodURL).json()

    for location in fooddata:
        #print location["location_name"]
        meal_name = {}
        for meals in location["meals"]:
            #print "\t" + meals["meal_name"]
            category = {}
            if meals["meal_avail"] == True:
                for genres in meals["genres"]:
                    #print "\t\t" + genres["genre_name"]
                    food = [] # new food list for every genre
                    for item in genres["items"]:
                        food.append(item)
                    category[genres["genre_name"]] = food
                meal_name[meals["meal_name"]] = category
        dining_halls[location["location_name"]] = meal_name

    return dining_halls

if __name__ == "__main__":
    main()
