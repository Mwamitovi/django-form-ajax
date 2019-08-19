# talk/urls.py
from django.conf.urls import url
from talk import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^create_post/$', views.create_post),
    url(r'^delete_post/$', views.delete_post),
]
