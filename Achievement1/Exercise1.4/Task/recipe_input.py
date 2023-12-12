import pickle

def take_recipe():
    recipe = {}
    recipe['name'] = input("Enter the name of the recipe: ")
    recipe['cooking_time'] = int(input("Enter the cooking time (min): "))
    recipe['ingredients'] = list(input("Enter the ingredients: ").split(", "))
    calc_difficulty(recipe)
    return recipe

def calc_difficulty(recipe):
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
        recipe['difficulty'] = 'Easy'
    elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
        recipe['difficulty'] = 'Medium'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
        recipe['difficulty'] = 'Intermediate'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 4:
        recipe['difficulty'] = 'Hard'


recipes_list = []
all_ingredients = []

filename = input("Enter the filename: ")


try:
    my_file = open(filename, 'rb')
    data = pickle.load(my_file)
except FileNotFoundError:
    data = {'recipes_list': [], 'all_ingredients': []}
except:
    data = {'recipes_list': [], 'all_ingredients': []}
else:
    my_file.close()
finally:
    recipes_list = data['recipes_list']
    all_recipes = data['all_ingredients']

n = int(input("How many recipes do you want to enter? "))

for i in range(n):
    recipe = take_recipe()

    for ingredient in recipe["ingredients"]:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)

    recipes_list.append(recipe)

data['recipes_list'] = recipes_list
data['all_ingredients'] = all_ingredients

with open(filename, 'wb') as my_file:
    pickle.dump(data, my_file)