
`Part 3`

Create a RESTful API for our Talk project
==============================================

## SYNOPSIS 

We now attempt to convert our "Talk" project into a RESTful application.
We shall use Django Rest Framework (DRF), 
a tool used for rapidly building RESTful APIs based on Django models.
This project is a [JavaScript/jQuery] front on [python/django] back.


## IMPORTANT

** You need, but are not limited to,
   - python 3+
   - Django 1.11.6
   - Django Rest Framework 3.9.1
   - jQuery 3.3.1 (or higher version)(or other JS-framework)
   - Foundation (or other CSS framework)
   - Modern Browser (Chrome is recommended)


## GET - STARTED

### Assumptions

   - Configure your Version Control
   - Fork the repository

### Configure (same process from Part 1)

   - Fork the repository, into your virtual environment, and activate the environment.
     (Notice that the root project folder: django-form-ajax is auto-created)

   - From the root folder, switch, cd part3.
     And run `pip install` to install the requirements.   

   - Switch to new root folder, cd talk_project.
     And run `python manage.py makemigrations`, then `migrate` to sync the database

   - Create main user, run `python manage.py createsuperuser` and enter username/password

   - Finally, run `python manage.py runserver` to fire up the server on `localhost:8000`

### Work flow

    - DRF Setup:
      Update your settings.py, add 'rest_framework' to INSTALLED_APPS

    - RESTful Structure:
      In a RESTful API, endpoints (URLs) define the structure of the API and 
      how end users access data from our application using the HTTP methods: GET, POST, PUT, DELETE. Endpoints should be logically organized around collections and elements, both of which are resources. In our case, we have one single resource, posts, so we will use the following URLS - 
      /posts/ and /posts/<id> for collections and elements, respectively.

    - Model Serializer:
      DRF’s Serializers convert model instances to Python dictionaires, 
      which are then rendered in various API appropriate formats - like JSON or XML. 
      Like Django ModelForm class, DRF comes with a concise format for its Serializers, the ModelSerializer class. It’s simple to use, just declare the fields you want to use from the mode (see talk/serializers.py).

    - Update Views [GET]:
      Refactor the current views to fit the RESTful paradigm (see talk/views.py).
      The @api_view decorator checks that the right HTTP request is passed into the view function (at this point, we’re only accepting GET requests). Then, the view fetches all the data, 
      if it’s for the collection, or just a single post, if it’s for an element.
      Finally, the data is serialized to JSON and returned.

    - Update the URLs:
      Add the api endpoints to the url() so as to link to the view functions (see talk/urls.py).
      Fire up the server, and navigate to: http://127.0.0.1:8000/api/v1/posts/?format=json.
      Also check out the Browsable API. Navigate to http://127.0.0.1:8000/api/v1/posts/.
      Notice that DRF generates a human-readable output of our API, with no extra work on our part.
      Nice! This is a sure win for DRF.

    - Refactor for REST:
      On the initial page load, we want to display all posts, right? (see talk/scripts/main.js)
      We then need to update our AJAX code. Notice especially how we’re handling a success -
      we iterate through objects and append each to the DOM, since the API sends back a number of objects. A key change also is we update, json[i].postpk to json[i].id, as we are serializing the post id.

    - Make the datetime human-friendly:
      Have you noticed the datetime format? That is not what we want, right? 
      We want a readable datetime format.
      Let's include MomentJS, a JavaScript library that easily formats the date anyway we want.
      We create a new function that accepts a string, and returns a formatted date.
      And we include that function in our loop, and pass it a dateString argument.

    - Update to handle [POST]:
      Till this point, our app only handles 'GET'. 
      Let's implement the functionality for the 'POST' requests too.
      We update the post_collection() function (see talk/views.py).
        With request.DATA (which extends Django’s HTTPRequest), we get the content from the request body. 
        And if the deserialization process works, we return a response with a code of 201 (created).
        On the other hand, if the deserialization process fails, we return a 400 response.
      We then update the create_post() AJAX function (see talk/scripts/main.js).
        We update the url to the api endpoint. We update the handling of the dates correctly 
        as well as changing json.postpk to json.id.

    - Author format:
      So far, we have been displaying an author id vs. username.
      We have a few options to handle this, either to be really RESTFUL and 
      make another call to get the user info, which is not good for performance or 
      to utilize the SlugRelatedField relation. We opted for the latter option.
      Within talk/serializers.py, we refactor the PostSerializer.
        The SlugRelatedField allows us to change the target of the author field from id to username.
        And by default, the username field is both readable and writeable thus this relation will work for both GET and POST requests.
      We refactor the data variable in the views as well (see talk/views.py) to [author] = request.user

    - Implement [DELETE]:
      As of now, if you try our delete link, you will get a 404 error.
      Of course, we need to update the url endpoint for the delete_post() AJAX function.
        But what should we target the collection or an individual element?
        Unless we want to delete all posts, other wise we need to hit the element endpoint.
      And we need to refactor our post_element() view function to handle 'DELETE' request.
        Once the 'DELETE' verb is added, we can handle the request by removing the post with 
        the delete() method and returning a 204 response. Does it work? Only one way to find out. 
        This time when you test make sure that, first, the post is actually deleted and 
        removed from the DOM and, secondly, that a 204 status code is returned 
        (you can confirm this in the Network tab within Chrome Developer Tools).


### Further help

    - For more on this subject, follow this blog on realpython
      (https://realpython.com/django-and-ajax-form-submissions-more-practise/)

    - Django Rest Framework official documentation
      (https://www.django-rest-framework.org/api-guide/)  

### Contribution guidelines
   - Making this code DRYer
   - Need an extra challenge? Add the ability to update posts with the PUT request.
   - Writing tests (Unit and Functional tests)
   - Other guidelines shall be issued with time.

### Who i talk to?
   - Contact: @MwamiTovi on GitHub
   - Email directly: matovu.synergy@gmail.com
