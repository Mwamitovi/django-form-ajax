
`Part 2`

Adding AJAX (DELETE) Capability to Django Form
==============================================

## SYNOPSIS 

This is basic form handling with Django/AJAX, a continuation from part 1.
We shall now delete a post, and remove it from the DOM (without page reload).
Project focuses on AJAX functionality, for web 2.0 apps.
This project is a [JavaScript/jQuery] front on [python/django] back.


## IMPORTANT

** You need, but are not limited to,
   - python 3+
   - Django 1.11.6
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

   - From the root folder, switch, cd part2.
     And run `pip install` to install the requirements.   

   - Switch to new root folder, cd talk_project.
     And run `python manage.py makemigrations`, then `migrate` to sync the database

   - Create main user, run `python manage.py createsuperuser` and enter username/password

   - Finally, run `python manage.py runserver` to fire up the server on `localhost:8000`

### Work flow

    - Setup Event Handler:
      When the user clicks the 'delete' link, this “event” needs to be handled in javascript code.
      On Click, we get the post primary key, added to an id- while a new post was added to the DOM.

    - Create the AJAX Request:
      We create the delete_post() function, which is called on 'delete'.
      This function takes a 'post_primary_key' argument, calls the confirm() method for user to acertain.
      And of course, we use the HTTP method 'DELETE'. Remember, some older browsers only support GET and POST requests, so you might need to utilize POST tunneling as a work around. (see main.js)

    - Update the Django View:
      This 'DELETE' request is sent to the server-side, and first handled by urls.py (urlpatterns).
      With the url() in place, the request is then routed to the view, delete_post().
      Once the post is deleted, a response dict is created, and serialized into JSON, 
      then sent as the response back to the client-side. (see talk/views.py)

      Question: 
      What happens if that primary key doesn’t exist? This results in an unexpected side effect.
      In other words, we’ll get an error that is not properly handled. 
      Can you figure out how to catch this error, and then use try/except statement to properly handle it.

    - Handle the Callback:
      How are we handling a success callback?
      We update delet_post() to hide a tag with a specific id and log a success message to the console. e.g. if we delete a post with pk=20, then the tag associated with the id='post-20' will be hidden.

    - Update the DOM:
      Open talk/index.html, add the 'id' to our list of posts.
      Go back to create_post() function (from part 1) and update the code which adds a new post to the DOM to include 'json.post_primary_key'.

### Further help

    - For more on this subject, follow this blog on realpython
      (https://realpython.com/django-and-ajax-form-submissions-more-practise/)

### Contribution guidelines
   - Making this code DRYer
   - Handling the 'DELETE' error, if the primary_key doesn't exist
   - Writing tests (Unit and Functional tests)
   - Other guidelines shall be issued with time.

### Who i talk to?
   - Contact: @MwamiTovi on GitHub
   - Email directly: matovu.synergy@gmail.com
