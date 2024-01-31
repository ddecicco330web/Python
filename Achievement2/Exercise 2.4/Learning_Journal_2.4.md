# Exercise 2.4: Django Views and Templates

## Learning Goals

⦁	Summarize the process of creating views, templates, and URLs 
⦁	Explain how the “V” and “T” parts of MVT architecture work
⦁	Create a frontend page for your web application

## Reflection Questions

*	Do some research on Django views. In your own words, use an example to explain how Django views work.
    * A view uses a function to take in an HTTP request and return an HTTP response. It renders the template you specify in the render method.
    * Ex:
      ```
      def home(request):
        return render(request, 'recipes/recipes_home.html')
      ```
*	Imagine you’re working on a Django web development project, and you anticipate that you’ll have to reuse lots of code in various parts of the project. In this scenario, will you use Django function-based views or class-based views, and why?
    * I would use class-based views because it is easy to reuse due to their class-based nature. You can use a generic view to use in many parts of the project.
*	 Read Django’s documentation on the ⦁	Django template language and make some notes on its basics.
    * Templates contain the static elements of HTML as well as some syntax for the dynamic parts that will be inserted.
 	 
 	  * Variables are surrounded by {{ and }} Ex: `` My first name is {{ first_name }}. My last name is {{ last_name }}. ``
*	
    * Tags are surrounded by {% and %} Ex: `` {% if user.is_authenticated %}Hello, {{ user.username }}.{% endif %}``
* 
    * Filters transform the values of variables and tag arguments. They look like this: Ex: ``{{ django|title }}``
* 
    * Comments: ``{# this won't be rendered #}``
