# Exercise 2.6: User Authentication in Django

## Learning Goals

-	Create authentication for your web application
-	Use GET and POST methods 
-	Password protect your web application’s views

## Reflection Questions

-	In your own words, write down the importance of incorporating authentication into an application. You can take an example application to explain your answer. <br><br>
It is important to incorporate authentification because it can keep your website secure and you can provide user-specific content for your app.
Authentification can keep your app safe by only allowing registered users to access your app. The ways you can protect a view on your app is as follows:
```
#to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin
class BookListView(LoginRequiredMixin, ListView):
  ...
```
```
#to protect function-based views
from django.contrib.auth.decorators import login_required
@login_required
def records(request):
```

-	In your own words, explain the steps you should take to create a login for your Django web application.<br><br>
    - First, you should add views.py to my project folder and create a login view as a function-based view.
    - In the view, if the request method is POST, the form is valid, and the user is valid, we will call Django's login function and redirect the user to another page.
    - For the template, you should have a folder structure like this.<br>
  Src<br>
  |--Templates<br>
&nbsp;&nbsp;|--auth<br>
    &nbsp;&nbsp;&nbsp;&nbsp;|--login.html<br>
    - In the template, you should use the form from your view. Inside the form, you should use the tag `{% csrf_token %}`
    - In the project's settings.py, you should update the templates by adding `'DIRS': [BASE_DIR / 'templates']` To protect the views you should add `LOGIN_URL='/login/'`
    - In the project's urls.py, you should add a path to the login view:
      ```
      urlpatterns = [
        ...
        path('login/', login_view, name='login'),
      ]
      ```
      - In one of your templates, you can add a link to the login view `<a href ="{%url 'login' %}"> Login </a>`<br>

-	Look up the following three Django functions on Django’s official documentation and/or other trusted sources and write a brief description of each.

<br>
Function	Description<br>
authenticate():<br>	
authenticate() is used to verify credentials. If the username and password are valid, the function will return a User object. If the credentials are invalid, the function will return None.
redirect():	<br>
redirect() is used to navigate to another view. It returns an HTTPResponseRedirect. For the arguments, you can pass a model's get_absolute_url(), a view name, or an absolute or relative URL.
include():	<br>
include() is used within URL patterns to add other URL patterns from other modules. 
