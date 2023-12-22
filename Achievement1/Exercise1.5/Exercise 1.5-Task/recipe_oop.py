class Recipe(object):
    all_ingredients = []

    def __init__(self, name, ingredients, cooking_time):
        self.name = name
        self.ingredients = ingredients
        self.cooking_time = cooking_time
        self.difficulty = self.calculate_difficulty()

    def calculate_difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients) < 4:
            return "Easy"
        elif self.cooking_time < 10 and len(self.ingredients) >= 4:
            return "Medium"
        elif self.cooking_time >= 10 and len(self.ingredients) < 4:
            return "Intermediate"
        else:
            return "Hard"
        
    def get_name(self):
        return self.name
    
    def get_cooking_time(self):
        return self.cooking_time
    
    def get_ingredients(self):
        return self.ingredients
    
    def get_difficulty(self):
        if self.difficulty == None:
            self.difficulty = self.calculate_difficulty()
        return self.difficulty

    def set_name(self, name):
        self.name = name

    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time
        self.difficulty = self.calculate_difficulty()

    def add_ingredient(self, *ingredients):
        for ingredient in ingredients:
            if ingredient not in self.ingredients:
                self.ingredients.append(ingredient)
        
        self.difficulty = self.calculate_difficulty()
    
    def search_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            return True
        else:
            return False
        
    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in Recipe.all_ingredients:
                Recipe.all_ingredients.append(ingredient)

    def __str__(self):
        result = f"Name: {self.name}\n"
        result += f"Cooking Time (min): {self.cooking_time}\n"
        result += f"Difficulty: {self.difficulty}\n"
        result += "Ingredients:\n"
        for ingredient in self.ingredients:
            result += f"\t{ingredient}\n"
        result += "-------------------------"
        result += "\n"
        return result

    def recipe_search(data, search_term):
        print(f"Searching for recipes containing {search_term}...")
        for recipe in data:
            if recipe.search_ingredient(search_term):
                print(recipe)
        print("-------------------------")


tea = Recipe("Tea", ["Tea Leaves", "Sugar", "Water"], 5)

print(tea)

coffee = Recipe("Coffee", ["Coffee Powder", "Sugar", "Water"], 5)
cake = Recipe("Cake", ["Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk"], 50)
banana_smoothie = Recipe("Banana Smoothie", ["Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes"], 5)

print(coffee)
print(cake)
print(banana_smoothie)

recipe_list = [tea, coffee, cake, banana_smoothie]

Recipe.recipe_search(recipe_list, "Water")
Recipe.recipe_search(recipe_list, "Sugar")
Recipe.recipe_search(recipe_list, "Bananas")