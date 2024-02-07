## Exercise 2.5: Django MVT Revisited

# Learning Goals

-	Add images to the model and display them on the frontend of your application
-	Create complex views with access to the model
-	Display records with views and templates


# Reflection Questions

-	In your own words, explain Django static files and how Django handles them.<br><br>
Static files are files that will not change. These are files like images and css files. To use static files in Django, you have to create a media folder under the source folder.
In the settings.py file of your project, you have to specify the path.
```
  MEDIA_URL = '/media/'
  MEDIA_ROOT= BASE_DIR / 'media'
```
Then you have to add the document root and media url to your url patterns inside the urls.py file.

```
  from django.conf import settings
  from django.conf.urls.static import static
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
The media folder is used for global static files.
Users can add files to the media file using the data inside the database.
`pic = models.ImageField(upload_to='customers', default='no_picture.jpg')`
If you want to store static files in an app you should have your folders structured like this:
```
<app_name>
|-- static
   |-- <app_name>
```
To use the static file you should load static in the template. 
```
{% load static %}
<img src="{% static 'sales/images/bookstore.jpg' %}" alt="home" width="600" height="300"/>
```
<br>

-	Look up the following two Django packages on Django’s official documentation and/or other trusted sources. Write a brief description of each.<br><br>
Package	Description<br><br>
ListView:	<br>
ListView usually contains a list of objects that are contained in self.objects_list. These objects are items inside a table in your database.
Usually in the template, you would use a for loop to show each object in the list.
```
  {% for object in object_list %}
    <tr>
      <td>
        <a href="{{object.get_absolute_url}}"> {{object.name}} </a>
      </td>
      <td><img src="{{object.pic.url}}" width="150" height="200" /></td>
    </tr>
  {% endfor %}
```
<br>
DetailView:	<br>
DetailView contains an object that is an item inside one of your tables. DetailView is used to display the attributes of the object. 
You use a path that has an argument when using a DetailView.
<br>
<br>
You’re now more than halfway through Achievement 2! Take a moment to reflect on your learning in the course so far. How is it going? What’s something you’re proud of so far? Is there something you’re struggling with? What do you need more practice with? You can use these notes to guide your next mentor call. 
