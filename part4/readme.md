
`Part 4`

Create a RESTful API for our Talk project
==============================================

## SYNOPSIS 

Finally, we make use of the generic Django Rest Framework (DRF) Class-based views (CBVs).
We refactor our functional views into the DRF CBVs, to advantage of inheritance.
And if the project grows larger with similar views, CBVs are great way to scale our views.
Remember, this project is a [JavaScript/jQuery] front on [python/django] back.


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

### Configure (same process from Part 3)

   - Fork the repository, into your virtual environment, and activate the environment.
     (Notice that the root project folder: django-form-ajax is auto-created)

   - From the root folder, switch, cd part4.
     And run `pip install` to install the requirements.   

   - Switch to new root folder, cd talk_project.
     And run `python manage.py makemigrations`, then `migrate` to sync the database

   - Create main user, run `python manage.py createsuperuser` and enter username/password

   - Finally, run `python manage.py runserver` to fire up the server on `localhost:8000`

### Work flow

    - Class-based views (CBVs):
      We define PostCollection() and PostMembers() views to inherit from rest_framework,
      ListCreateAPIView() and RetrieveUpdateDestroyAPIView() respectively (see talk/views.py).
      Note that with CBVs, we can still handle all the same requests as before, 
      but we can now handle PUT requests to update each member.

    - Update the URLs:
      Update the urlpatterns (talk/urls.py) to reference the CBVs.
      We 'commented' out the function-based views (FBVs), just for future reference.

    - Update the template:
      We explicitly fetch the username from the request method.
      Attach an "id" to {{ request.user.username }} (see templates/talk/index.html)

    - Refactor the AJAX:
      Update the create_post(), the data object to include text / author fields.
      This is required by ajax, as we process the form, if using CBVs (see main.js).


### Further help

    - For more on this subject, follow this blog on realpython
      (https://realpython.com/django-and-ajax-form-submissions-more-practise/)

    - Django Rest Framework official documentation
      (https://www.django-rest-framework.org/api-guide/)  

### Contribution guidelines
   - Making this code DRYer
   - Need an extra challenge? 
     Add pagination, permissions and maybe basic validation.
   - Writing tests (Unit and Functional tests)
   - Other guidelines shall be issued with time.

### Who i talk to?
   - Contact: @MwamiTovi on GitHub
   - Email directly: matovu.synergy@gmail.com
