
Django Form Handling, with AJAX (POST)
======================================

## SYNOPSIS

This is basic form handling with Django/AJAX.
We enter text, and post it to the DOM (without page reload).
Project focuses on AJAX functionality, for web 2.0 apps.
This project is a [JavaScript/jQuery] front on [python/django] back.


## IMPORTANT

** You need, but are not limited to,
   - python 3+
   - Django 1.11.1
   - jQuery 3.3.1 (or higher version)(or other JS-framework)
   - Foundation (or other CSS framework)
   - Modern Browser (Chrome is recommended)


## GET - STARTED

### Assumptions

   - Configure your Version Control
   - Fork the repository

### Configure

   - Fork the repository, into your virtual environment, and activate the environment.
     (Notice that the root project folder: django-form-ajax is auto-created)

   - From the root folder, switch, cd part1/form-using-ajax.
     And run `pip install` to install the requirements.   

   - Switch to new root folder, cd talk_project.
     And run `python manage.py makemigrations`, then `migrate` to sync the database

   - Create main user, run `python manage.py createsuperuser` and enter username/password

   - Finally, run `python manage.py runserver` to fire up the server on `localhost:8000`

### Work flow

    - User protection:
      Forms are at risk for Cross-Site Request Forgeries (csrf), often in django, 
      we add the {% csrf_token %} template tag to the form. However, for AJAX requests,
      we cannot pass that token using a JavaScript object since scripts are static.
      To get around this, we create a custom header that includes the token (see "main.js")

    - Handling Events:
      On 'submit' event prevents default browser behavior for form submission,
      and calls the create_post() function where we shall add our AJAX code.

    - Adding AJAX:
      First, we give our form field[text] a widget to describe the 'id' mainly (see talk/fomrs.py).
      Then define create_post(), and add AJAX functionality for a `POST` method (see main.js).
      Finally, define a create_() view function, fetchs AJAX data, and returns JSON response (see talk/views.py)

    - Updating the DOM:
      Update the talk/index.html template, to add errors display.
      And also refactor create_post() to 'prepend' a new post to the DOM, if submit process is a success (see main.js)

### Further help

    - For more on this subject, follow this blog on realpython
      (https://realpython.com/blog/python/django-and-ajax-form-submissions/)

### Contribution guidelines
   - Making this code DRYer
   - Update the project to be RESTful
   - Writing tests (Unit and Functional tests)
   - Other guidelines shall be issued with time.

### Who i talk to?
   - Contact: @MwamiTovi on GitHub
   - Email directly: matovu.synergy@gmail.com
