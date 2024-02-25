# Exercise 2.8: Deploying a Django Project
## Learning Goals

-	Enhance user experience and look and feel of your web application using CSS and JS
-	Deploy your Django web application on a web server 
-	Curate project deliverables for your portfolio

## Reflection Questions

-	Explain how you can use CSS and JavaScript in your Django web application.<br><br>
You can use CSS to customize the style for the elements in your page without it cluttering up you templates.
You can use javascript to write custom tasks that will happen on your page. For example, I used JS to create a modal and tabs. 
<br>

-	In your own words, explain the steps you’d need to take to deploy your Django web application. <br><br>

    - Create a Procfile that points to your projects wsgi file. Make sure gunicorn is installed.
    - Configure the database. Install dj-database-url and update the database in your project settings.
      Install pyscopg2-binary or you can put this in your requirements file later.
    - In your projects settings, set up your settings directory and update static root.
    - To serve your static files, you need to install whitenoise. Put 'whitenoise.middleware.WhiteNoiseMiddleware' in your middleware array.
    - Set Debug to False
    - Replace your secret key with this line ```SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY','django-insecure-ml49cp(e)=yakpevh4xz)3w)6xuq6kv7g&3^xf^)gr-n3&p#%9')```
    - Create your requirements file by using ```pip freeze > requirements.txt```
    - Push the updates on GitHub
    <br>
    
    - To deploy to Heroku, install the Heroku CLI if not installed already.
    - Login using ```heroku login```
    - Create a new app with ```heroku create```
    - Add the app to your allowed hosts array inside of your settings.
    - Push code to heroku using ```git push heroku main```
    - Set up the database on heroku by using ```heroku run python manage.py migrate```
    - Create a super user for the app on heroku using ```heroku run python manage.py createsuperuser```
    - Set your heroku secret key by using ```heroku config:set DJANGO_SECRET_KEY="a-very-long-key-comprised-of-atleast-50-random-characters-including-CAPS-NUMBERS0123456789-and-$p€ccharacters"```
    - After this all you have to do is add data to your database and your site should be good to go.

-	You’ve now finished Achievement 2 and, with it, the whole course! Take a moment to reflect on your learning:
    -	What went well during this Achievement? <br><br>
    I think setting up the models and the views for my app went well. I learned about how to make a many-to-many relationship in Django.<br><br>
    -	What’s something you’re proud of? <br><br>
      I'm proud of being able to use information I learned from outside of the course to apply to my project.
     	For example, I'm happy about storing and reading files from an AWS bucket and using JS with Django.<br><br>
    -	What was the most challenging aspect of this Achievement? <br><br>
    The hardest part for me was getting the website to work properly after deploying to Heroku.
I spent a lot of time trying to figure out how to get images in the media folder to persist on Heroku.<br><br>
    -	Did this Achievement meet your expectations? Did it give you the confidence to start working with your new Django skills?<br><br>
    I enjoyed this achievement. It had a good amount of challenge. It gives me confidence to start my own Django projects and it has shown me that there is still a lot left to learn to improve my skills.

