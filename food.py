import requests, json
from pprint import pprint

foodURL = "https://rumobile.rutgers.edu/1/rutgers-dining.txt"

def main():
    get_food_all()
    get_food_dhall("Livingston Dining Commons", "Dinner")

def get_food_master():
    food = {}

    busch = {}
    busch["busch_breakfast"] = get_food_dhall("Busch Dining Hall", "Breakfast")
    busch["busch_lunch"] = get_food_dhall("Busch Dining Hall", "Lunch")
    busch["busch_dinner"] = get_food_dhall("Busch Dining Hall", "Dinner")
    busch["busch_takeout"] = get_food_dhall("Busch Dining Hall", "Takeout")

    livi = {}
    livi["livi_breakfast"] = get_food_dhall("Livingston Dining Commons", "Breakfast")
    livi["livi_lunch"] = get_food_dhall("Livingston Dining Commons", "Lunch")
    livi["livi_dinner"] = get_food_dhall("Livingston Dining Commons", "Dinner")
    livi["livi_takeout"] = get_food_dhall("Livingston Dining Commons", "Takeout")

    brower = {}
    busch["brower_breakfast"] = get_food_dhall("Brower Commons", "Breakfast")
    busch["brower_lunch"] = get_food_dhall("Brower Commons", "Lunch")
    busch["brower_dinner"] = get_food_dhall("Brower Commons", "Dinner")
    busch["brower_takeout"] = get_food_dhall("Brower Commons", "Takeout")

    neilson = {}
    livi["neilson_breakfast"] = get_food_dhall("Neilson Dining Hall", "Breakfast")
    livi["neilson_lunch"] = get_food_dhall("Neilson Dining Hall", "Lunch")
    livi["neilson_dinner"] = get_food_dhall("Neilson Dining Hall", "Dinner")
    livi["neilson_takeout"] = get_food_dhall("Neilson Dining Hall", "Takeout")

    food["busch"] = busch
    food["livi"] = livi
    food["brower"] = busch
    food["neilson"] = livi

    return food

def get_food_dhall(dhall, meal):

    dining_halls = get_food_all()

    dhall = dining_halls.get(dhall)
    if dhall is not None:
        meal = dhall.get(meal)
    return meal

def get_food_all():

    fooddata = requests.get(foodURL).json()
    dining_halls = {}

    for location in fooddata:
        meal_name = {}
        for meals in location["meals"]:
            category = []
            if meals["meal_avail"] == True:
                for genres in meals["genres"]:
                    genre = {}
                    genre["name"] = genres["genre_name"]
                    food = [] # new food list for every genre
                    for item in genres["items"]:
                        food.append(item)
                    genre["items"] = food
                    category.append(genre)
                meal_name[meals["meal_name"]] = category
        dining_halls[location["location_name"]] = meal_name

    return dining_halls

if __name__ == "__main__":
    main()
