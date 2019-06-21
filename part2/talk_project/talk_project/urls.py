# talk_project/urls.py
from django.conf.urls import include, url
from django.contrib.auth.views import login
from django.contrib import admin
from talk_project import views

admin.autodiscover()


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', login),
    url(r'^logout/$', views.logout_page),
    url(r'^', include('talk.urls')),
]
