# Exercise 2.7: Data Analysis and Visualization in Django

## Learning Goals

-	Work on elements of two-way communication like creating forms and buttons
-	Implement search and visualization (reports/charts) features
-	Use QuerySet API, DataFrames (with pandas), and plotting libraries (with matplotlib)

## Reflection Questions

-	Consider your favorite website/application (you can also take CareerFoundry). Think about the various data that your favorite website/application collects. Write down how analyzing the collected data could help the website/application. 
    - For this example, I will use YouTube. I think YouTube collects data on the number of views a video gets, subscribers, video tags, and watch time. This can help show users popular/trending videos, creators, and topics.
      
-	"https://docs.djangoproject.com/en/3.2/ref/models/querysets/" Read the Django official documentation on QuerySet API. Note down the different ways in which you can evaluate a QuerySet.
    -	You can iterate through a QuerySet like so...
      ```
      for e in Entry.objects.all():
        print(e.headline)
      ```
    - You can slice an evaluated QuerySet and it will return a list.
    - You can use repr() to show the values in your QuerySet
    - You can use len() to show the length of your QuerySet
    - You can use list() to evaluate a QuerySet like so...
      ``entry_list = list(Entry.objects.all())``
    - You can use bool, or, and, or if to test a QuerySet like so...
      ```
      if Entry.objects.filter(headline="Test"):
       print("There is at least one Entry with the headline Test")
      ```
    - If you are reloading a cached QuerySet, you can pickle the QuerySet to load it into memory.
      ```
        import pickle
        query = pickle.loads(s)     # Assuming 's' is the pickled string.
        qs = MyModel.objects.all()
        qs.query = query            # Restore the original 'query'.
      ```
-	In the Exercise, you converted your QuerySet to DataFrame. Now do some research on the advantages and disadvantages of QuerySet and DataFrame, and explain the ways in which DataFrame is better for data processing.
	  - DataFrame streamlines data representation for the user.
	  - You can use less code to achieve want you want with DataFrame.
	  - DataFrame provides features to help analyze the data like filtering.
	  - DataFrame imports large amounts of data quickly.
    - DataFrame allows user to customize the data.
    - Is made for Python, so it can easily be used with other Python libraries like madplotlib.
