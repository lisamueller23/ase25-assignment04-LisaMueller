import json


# get the list with all meals
def get_meals(data):
    keys = list(data.keys())
    print("We have the following meals: ")
    for meals in keys:
        print(meals)
    return keys


# check if the input is a meal from the list with meals
def check_meal(meal, keys, data):
    if meal in keys:
        get_ingredients(data, meal)
    else:
        print("Error. Invalid input. Check if you write the name of the meal correct!")


# gives the ingredients from the meal back
def get_ingredients(data, meal):
    print(f"The ingredients for {meal} are: ")
    for ingredient in data[meal]:
        print(ingredient)


if __name__ == '__main__':

    meals_ingredients = "./sample_data/meal-ingredients.json"   # put here the json file with the meals and ingredients

    with open(meals_ingredients, 'r') as f:
        file = json.load(f)

    print("Welcome to SmartCater!")

    # ask for the input of a meal or to quit the program
    while True:
        list_meals = get_meals(file)
        selected_meal = input("Select the meal by entering the name (or exit to quit): ")

        if selected_meal == "exit":
            print("Goodbye!")
            break
        if selected_meal != "exit":
            check_meal(selected_meal, list_meals, file)
