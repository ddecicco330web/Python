from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("mysql://cf-python:password@localhost/task_database")

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Create Recipe table that will hold information about recipes
class Recipe(Base):
    __tablename__ = "final_recipes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    ingredients = Column(String(255))
    cooking_time = Column(Integer, nullable=False)   
    difficulty = Column(String(20), nullable=False)

    # _repr_ method to print out the recipe information
    def __repr__(self):
        return f"ID: {self.id}, Recipe: {self.name}, Difficulty: {self.difficulty}"
    
    # _str_ method to print out the recipe information
    def __str__(self):
        recipe_string = self.name + "\n"
        recipe_string += "="*10
        recipe_string += "\n"
        recipe_string += f"Cooking Time (min): {self.cooking_time}\n"
        recipe_string += f"Difficulty: {self.difficulty}\n"
        recipe_string += "\n"
        recipe_string += "Ingredients:\n"
        recipe_string += "\t" + self.ingredients.replace(", ", "\n\t")
        recipe_string += "\n"
        return recipe_string

    # calculate_difficulty method to calculate the difficulty of the recipe by using cooking_time and ingredients
    def calculate_difficulty(self):
        MAX_EASY_TIME = 10
        MAX_EASY_INGREDIENTS = 4

        ingredients = self.return_ingredients_as_list()

        self.difficulty = "Hard"
        if(self.cooking_time < MAX_EASY_TIME and len(ingredients) < MAX_EASY_INGREDIENTS):
            self.difficulty = "Easy"
        elif(self.cooking_time < MAX_EASY_TIME):
            self.difficulty = "Medium"
        elif(len(ingredients) < MAX_EASY_INGREDIENTS):
            self.difficulty = "Intermediate"

    # return_ingredients_as_list method to return the ingredients as a list
    def return_ingredients_as_list(self):
        if(self.ingredients == None):
            return []
        
        return self.ingredients.split(", ")
    

Base.metadata.create_all(engine)

# get_name_input method to get the name of the recipe from the user
def get_name_input():
    name = input("Please enter the name of the recipe: ")
    if(name == "" or name.isnumeric() == True):
        print("Invalid input, please try again\n")
        return None
    if(len(name) > 50):
        print("Name is too long (50 char max), please try again\n")
        return None
    return name

# get_cooking_time_input method to get the cooking time of the recipe from the user
def get_cooking_time_input():
    cooking_time = input("Please enter the cooking time: ")
    if(cooking_time.isnumeric() == False):
        print("Invalid input, please try again\n")
        return None
    
    cooking_time = int(cooking_time)
    if(cooking_time < 0):
        print("Invalid cooking time, please try again\n")
        return None
    
    return cooking_time

# get_ingredients_input method to get the ingredients of the recipe from the user
def get_ingredients_input():
    ingredients = []
    number_of_ingredients = input("Please enter the number of ingredients: ")

    if(number_of_ingredients.isnumeric() == False):
        print("Invalid input, please try again\n")
        return None
    
    number_of_ingredients = int(number_of_ingredients)
    if(number_of_ingredients < 0):
        print("Invalid cooking time, please try again\n")
        return None
    
    # get user input for ingredients
    for i in range(number_of_ingredients):
        # only continue for loop if input is valid
        while(True):
            ingredient = input("Please enter the ingredient: ")
            if(ingredient == "" or ingredient.isnumeric() == True):
                print("Invalid input, please try again\n")
                continue
            elif(ingredient in ingredients):
                print("Ingredient already added, please try again\n")
                continue
            else:
                ingredients.append(ingredient)
                break
    
    ingredients = ", ".join(ingredients)
    if(len(ingredients) > 255):
        print("Ingredients list is too long (255 char max), please try again\n")
        return None
    
    return ingredients

# get_recipe_id_input method to get the recipe id from the user and return the recipe object
def get_recipe_by_id_input():
    recipe_id = input("Please enter the id corresponding with your recipe: ")
    if(recipe_id.isnumeric() == False):
        print("Invalid input, please try again\n")
        return None
    if(int(recipe_id) < 0):
        print("Invalid input, please try again\n")
        return None
    
    recipe_to_get = session.query(Recipe).filter(Recipe.id == int(recipe_id)).first()
    if(recipe_to_get == None):
        print("Recipe not found\n")
        return None
    
    return recipe_to_get

# print_recipes method to print out the id and name of all the recipes in the database
# Returns True if printed, False if table is empty
def print_recipe_options():
    if(session.query(Recipe).count() == 0):
        print("No recipes found\n")
        return False
    
    results = session.query(Recipe.id, Recipe.name).all()
    for row in results:
        print(str(row.id) + ". " + row.name)
    return True

# create_recipe method to create a recipe and add it to the database
def create_recipe():
    # get user input for recipe name
    name = get_name_input()
    if(name == None):
        return
    
    # get user input for cooking time
    cooking_time = get_cooking_time_input()
    if(cooking_time == None):
        return
      
    # get user input for ingredients
    ingredients = get_ingredients_input()
    if(ingredients == None):
        return
    
    # create recipe entry and add to database
    recipe_entry = Recipe(name=name, ingredients=ingredients, cooking_time=cooking_time)
    recipe_entry.calculate_difficulty()

    session.add(recipe_entry)
    session.commit()

# view_all_recipes method to view all the recipes in the database
def view_all_recipes():
    recipes = session.query(Recipe).all()

    if(len(recipes) == 0):
        print("No recipes found\n")
        return

    for recipe in recipes:
        print(recipe)

# search_by_ingredient method to search for recipes by ingredient  
def search_by_ingredient():
    if(session.query(Recipe).count() == 0):
        print("No recipes found\n")
        return
    
    # get all ingredients from database and print them out
    results = session.query(Recipe.ingredients).all()
    all_ingredients = []

    for row in results:
        ingredient_list = row[0].split(", ")
        for ingredient in ingredient_list:
            if(ingredient not in all_ingredients):
                all_ingredients.append(ingredient)

    for pos, ingredient in enumerate(all_ingredients):
        print(str(pos) + ". " + ingredient)

    # get user input for ingredients to search for
    search_indexes = input("Please enter the ingredient numbers separated by a space: ")
    search_indexes = search_indexes.split(" ")

    search_ingredients = []
    for i in search_indexes:
        if(i.isnumeric() == False):
            print("Invalid input, please try again\n")
            return
        
        
        if(int(i) < 0 or int(i) >= len(all_ingredients)):
            print("Invalid input, please try again\n")
            return
        else:
            if(all_ingredients[int(i)] not in search_ingredients):
                search_ingredients.append(all_ingredients[int(i)])

    # search for recipes with the ingredients    
    conditions = []
    for ingredient in search_ingredients:
        like_term = f"%{ingredient}%"
        conditions.append(Recipe.ingredients.like(like_term))

    search_results = session.query(Recipe).filter(*conditions).all()

    # print out search results
    for recipe in search_results:
        print(recipe)

# edit_recipe method to edit a recipe in the database
def edit_recipe():
    # get all recipes from database and print them out
    if(print_recipe_options() == False):
        return

    # get user input for recipe to edit    
    recipe_to_edit = get_recipe_by_id_input()
    if(recipe_to_edit == None):
        return
    
    # print out recipe information
    print("")
    print(f"1. Name: {recipe_to_edit.name}")
    print(f"2. Cooking Time: {recipe_to_edit.cooking_time}")
    print("3. Ingredients:")
    for ingredient in recipe_to_edit.return_ingredients_as_list():
        print("\t" + ingredient)
    print("")

    # get user input for what to edit
    edit_choice = input("Please enter the number corresponding with what you would like to edit: ")
    if(edit_choice.isnumeric() == False):
        print("Invalid input, please try again\n")
        return
    if(int(edit_choice) < 1 or int(edit_choice) > 3):
        print("Invalid input, please try again\n")
        return
    
    # get user input for new value
    if(int(edit_choice) == 1):
        new_value = get_name_input()
        if(new_value == None):
            return
        recipe_to_edit.name = new_value
    elif(int(edit_choice) == 2):
        new_value = get_cooking_time_input()
        if(new_value == None):
            return

        recipe_to_edit.cooking_time = new_value
        recipe_to_edit.calculate_difficulty()
    elif(int(edit_choice) == 3):
        new_value = get_ingredients_input()
        if(new_value == None):
            return

        recipe_to_edit.ingredients = new_value
        recipe_to_edit.calculate_difficulty()

    session.commit()
    
# delete_recipe method to delete a recipe from the database
def delete_recipe():
    # get all recipes from database and print them out
    if(print_recipe_options() == False):
        return

    # get user input for recipe to delete
    recipe_to_delete = get_recipe_by_id_input()
    
    confirm_delete = input(f"Are you sure you want to delete {recipe_to_delete.name}? (yes/no): ")
    if(confirm_delete == "yes" or confirm_delete == "y"):
        session.delete(recipe_to_delete)
        session.commit()
        print("Recipe deleted\n")
    else:
        print("Recipe deletion cancelled\n")

def main_menu():
    choice = ""
    while(choice != "quit"):
        print("1. Create recipe")
        print("2. View all recipes")
        print("3. Search for recipe by ingredient")
        print("4. Edit recipe")
        print("5. Delete recipe")
        print("Type 'quit' to exit")
        print("")

        choice = input("Please enter the number corresponding with your choice: ")
        print("")
        if(choice == "1"):
            create_recipe()
        elif(choice == "2"):
            view_all_recipes()
        elif(choice == "3"):
            search_by_ingredient()
        elif(choice == "4"):
            edit_recipe()
        elif(choice == "5"):
            delete_recipe()
        elif(choice == "quit"):
            print("Goodbye")
        else:
            print("Invalid input, please try again\n")

    session.close()
    engine.dispose()

main_menu()