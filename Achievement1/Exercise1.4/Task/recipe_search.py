import pickle

def display_recipe(recipe):
    print("")
    print("Recipe: " + recipe["name"])
    print("Cooking Time(min): " + str(recipe["cooking_time"]))
    print("Ingredients: ")
    for ingredient in recipe["ingredients"]:
        print(ingredient)
    print("Difficulty: " + recipe["difficulty"])

def search_ingredient(data):
    print("")
    print("Ingredients Across All Recipes: ")
    print("--------------------")
    for pos, ingredient in enumerate(data["all_ingredients"]):
        print(str(pos) + ". " + ingredient)
    print("")

    try:
        ingredient_searched = int(input("Enter an ingredient number: "))
    except:
        print("Invalid Input!")
    else:
        for recipe in data["recipes_list"]:
            if data["all_ingredients"][ingredient_searched] in recipe["ingredients"]:
                display_recipe(recipe)

filename = input("Enter the filename: ")

try:
    my_file = open(filename, 'rb')
    data = pickle.load(my_file)
except:
    print("File not found!")
else:
    search_ingredient(data)