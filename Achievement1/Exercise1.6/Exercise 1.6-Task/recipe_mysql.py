import mysql.connector

conn = mysql.connector.connect(host="localhost", user="cf-python", passwd="password")

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

cursor.execute("USE task_database")

cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes 
               (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), 
               ingredients VARCHAR(255), 
               cooking_time INT, 
               difficulty VARCHAR(20))''')

ID = 0
NAME = 1
INGREDIENTS = 2
COOKING_TIME = 3
DIFFICULTY = 4



def create_recipe(conn, cursor):
    try:
        name = input("Please enter the name of the recipe: ")
        if(len(name) > 50):
            print("Name is too long (50 char max), please try again")
            return
        
        cooking_time = int(input("Please enter the cooking time: "))
        if(cooking_time < 0):
            print("Invalid cooking time, please try again")
            return
        
        ingredients = input("Please enter the ingredients (separate with comma and space): ")
        if(len(ingredients) > 255):
            print("Ingredients are too long (255 char max), please try again")
            return
        else:
            ingredients = ingredients.split(", ")
    except:
        print("Invalid input, please try again")
        return
    
    difficulty = calculate_difficulty(cooking_time, ingredients)
    ingredients = ", ".join(ingredients)

    try:
        sql = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
        val = (name, ingredients, cooking_time, difficulty)

        cursor.execute(sql, val)
        conn.commit()
    except:
        print("Error inserting into database, please try again")
        return


def calculate_difficulty(cooking_time, ingredients):
    MAX_EASY_TIME = 10
    MAX_EASY_INGREDIENTS = 4

    difficulty = "Hard"
    if(cooking_time < MAX_EASY_TIME and len(ingredients) < MAX_EASY_INGREDIENTS):
        difficulty = "Easy"
    elif(cooking_time < MAX_EASY_TIME):
        difficulty = "Medium"
    elif(len(ingredients) < MAX_EASY_INGREDIENTS):
        difficulty = "Intermediate"
    return difficulty

def search_recipe(conn, cursor):
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()
    all_ingredients = []

    for row in results:
        ingredient_list = row[0].split(", ")
        for ingredient in ingredient_list:
            if(ingredient not in all_ingredients):
                all_ingredients.append(ingredient)

    print("Ingredients")
    print("===========================")
    for pos, ingredient in enumerate(all_ingredients):
        print(str(pos) + ". " + ingredient)

    print("")

    try:
        search_ingredient = int(input("Please enter the id corresponding with your ingredient: "))
    except:
        print("Invalid input, please try again")
        return
    
    if(search_ingredient < 0 or search_ingredient >= len(all_ingredients)):
        print("Invalid input, please try again")
        return
    
    try:
        cursor.execute("SELECT * FROM Recipes WHERE ingredients LIKE '%" + all_ingredients[search_ingredient] + "%'")
        results = cursor.fetchall()
    except:
        print("Error searching database, please try again")
        return
    
    print("")
    print("Results")
    print("===========================")

    for row in results:
        print("Name: " + row[NAME])
        print("Ingredients: " + row[INGREDIENTS])
        print("Cooking Time: " + str(row[COOKING_TIME]))
        print("Difficulty: " + row[DIFFICULTY])
        print("")

def display_recipes(recipe_list):
    print("Recipes")
    print("===========================")
    for pos, row in enumerate(recipe_list):
        print(str(pos) + ". " + row[NAME])

    print("")

def select_recipe():
    selected_recipe = -1
    try:
        selected_recipe = int(input("Please enter the id corresponding with your recipe: "))
        return selected_recipe
    except:
        print("Invalid input, please try again")
        return selected_recipe

def update_recipe(conn, cursor):
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()
    display_recipes(results)
    update_recipe = select_recipe()
    if(update_recipe < 0):
        return
    if(update_recipe >= len(results)):
        print("Invalid input, please try again")
        return

    col = input("Please enter the what you would like to update (name, cooking_time, ingredients): ")
    if(col == 'name'):
        new_name = input("Please enter the new name: ")
        if(len(new_name) > 50):
            print("Name is too long (50 char max), please try again")
            return
    elif(col == 'cooking_time'):
        try:
            new_cooking_time = int(input("Please enter the new cooking time: "))
            
            if(new_cooking_time < 0):
                print("Invalid cooking time, please try again")
                return
        except:
            print("Invalid input, please try again")
            return
        
        new_difficulty = calculate_difficulty(new_cooking_time, results[update_recipe][INGREDIENTS])
    elif(col == 'ingredients'):
        new_ingredients = input("Please enter the updated ingredients list (separate with comma and space): ")
        if(len(new_ingredients) > 255):
            print("Ingredients are too long (255 char max), please try again")
            return
        else:
            new_ingredients = new_ingredients.split(", ")
            new_difficulty = calculate_difficulty(results[update_recipe][COOKING_TIME], new_ingredients)
    else:
        print("Invalid input, please try again")
        return
    
    try:
        if(col == 'name'):
            sql = "UPDATE Recipes SET name = %s WHERE id = %s"
            val = (new_name, results[update_recipe][ID])
        else:
            if(new_difficulty != results[update_recipe][DIFFICULTY]):
                diff_sql = "UPDATE Recipes SET difficulty = %s WHERE id = %s"
                diff_val = (new_difficulty, results[update_recipe][ID])
                cursor.execute(diff_sql, diff_val)

            if(col == 'cooking_time'):
                sql = "UPDATE Recipes SET cooking_time = %s WHERE id = %s"
                val = (new_cooking_time, results[update_recipe][ID])
            else:
                new_ingredients = ", ".join(new_ingredients)
                sql = "UPDATE Recipes SET ingredients = %s WHERE id = %s"
                val = (new_ingredients, results[update_recipe][ID])

        cursor.execute(sql, val)
        conn.commit()
    except:
        print("Error updating database, please try again")
        return
        
def delete_recipe(conn, cursor):
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()
    display_recipes(results)
    delete_recipe = select_recipe()
    if(delete_recipe < 0):
        return
    
    sql = "DELETE FROM Recipes WHERE id = %s"
    val = (results[delete_recipe][ID],)
    cursor.execute(sql, val)
    conn.commit()
    
def main_menu(conn, cursor):
    choice = ""
    while (choice != 'quit'):
        print("1. Create recipe")
        print("2. Search for recipe by ingredient")
        print("3. Update recipe")
        print("4. Delete recipe")
        print("Type quite to exit")
        print("")

        choice = input("Please select an option: ")
        print("")
        if(choice == "1"):
            create_recipe(conn, cursor)
        elif(choice == "2"):
            search_recipe(conn, cursor)
        elif(choice == "3"):
            update_recipe(conn, cursor)
        elif(choice == "4"):
            delete_recipe(conn, cursor)
        elif(choice != "quit"):
            print("Invalid option, please try again")
    
    conn.commit()
    conn.close()

main_menu(conn, cursor)