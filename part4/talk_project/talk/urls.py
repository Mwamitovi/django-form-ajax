# talk/urls.py
from django.conf.urls import url
from talk import views


urlpatterns = [
    url(r'^$', views.home),
    # api-class_based-views
    url(r'^api/v1/posts/$', views.PostCollection.as_view()),
    url(r'^api/v1/posts/(?P<pk>[0-9]+)$', views.PostMember.as_view()),
    # api-function-views
    # url(r'^api/v1/posts/$', views.post_collection),
    # url(r'^api/v1/posts/(?P<pk>[0-9]+)$', views.post_element),
]
