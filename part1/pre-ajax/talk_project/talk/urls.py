# talk/urls.py
from django.conf.urls import url
from talk import views


urlpatterns = [
    url(r'^$', views.home, {'template_name': 'talk/index.html'}),
    url(r'^create_post/$', views.create_post, {'template_name': 'talk/post.html'})
]
