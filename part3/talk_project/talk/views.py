# talk/views.py
from django.shortcuts import render
from talk.forms import PostForm


def home(request):
    tmpl_vars = {'form': PostForm()}
    return render(request, 'talk/index.html', tmpl_vars)
