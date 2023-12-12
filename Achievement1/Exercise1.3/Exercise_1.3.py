recipes_list = []
ingredients_list = []

def take_recipe():
    name = input("Enter the name of the recipe: ")
    cooking_time = int(input("Enter the cooking time: "))
    ingredients = list(input("Enter the ingredients separated by commas: ").split(", "))
    recipe = {"name": name, "cooking_time": cooking_time, "ingredients": ingredients}
    print("")
    return recipe

n = int(input("How many recipes do you want to enter? "))

for i in range(n):
    recipe = take_recipe()

    for ingredient in recipe["ingredients"]:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)

    recipes_list.append(recipe)

for recipe in recipes_list:
    difficulty = "Not Set"
    if recipe["cooking_time"] < 10 and len(recipe["ingredients"]) < 4:
        difficulty = "Easy"
    elif recipe["cooking_time"] < 10 and len(recipe["ingredients"]) >= 4:
        difficulty = "Medium"
    elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) < 4:
        difficulty = "Intermediate"
    elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) >= 4:
        difficulty = "Hard"

    print("")
    print("Recipe: " + recipe["name"])
    print("Cooking Time(min): " + str(recipe["cooking_time"]))
    
    print("Ingredients: ")
    for ingredient in recipe["ingredients"]:
        print(ingredient)
    print("Difficulty: " + difficulty)
    print("")

ingredients_list.sort()

print("Ingredients Across All Recipes: ")
print("--------------------")
for ingredient in ingredients_list:
    print(ingredient)