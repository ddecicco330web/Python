# Exercise 2.3: Django Models

## Learning Goals

⦁	Discuss Django models, the “M” part of Django’s MVT architecture
⦁	Create apps and models representing different parts of your web application 
⦁	Write and run automated tests

## Reflection Questions

⦁	Do some research on Django models. In your own words, write down how Django models work and what their benefits are.
- Django models make it easy to manage data in a database. To use it, you make a class that inherits from the django model class. Each class represents a table in your database. Each attribute is a column in the table and each object created using the class is a row in the table. When making the class, attributes are assigned using the model class's methods. With models, you don't have to interact with an ORM object.
- Example:<br>
  ```
  class Recipe(models.Model):
    name = models.CharField(max_length=50)
    cook_time = models.PositiveIntegerField(help_text="In minutes")
  ```

⦁	In your own words, explain why it is crucial to write test cases from the beginning of a project. You can take an example project to explain your answer.
- It is important to write test cases from the beginning because you can catch bugs whenever someone makes a change to the code. Test cases can also help with documentation because they show how the app is intended to be used. You can write test cases to test methods and attributes in your classes.
- Example:<br>
```
    def test_recipe_difficulty_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('difficulty').max_length
        self.assertEqual(max_length, 20)

    def test_recipe_str_method(self):
        recipe = Recipe.objects.get(id=1)
        expected_object_name = "Name: Test Recipe, Description: Test Description, Cook Time (min): 10, Difficulty: Easy"
        self.assertEqual(expected_object_name, str(recipe))
```

