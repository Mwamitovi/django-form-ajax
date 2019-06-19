from django.shortcuts import render
from django.http import HttpResponseRedirect
from talk.models import Post
from talk.forms import PostForm


def home(request, template_name):
    all_posts = Post.objects.reverse()
    form = PostForm()
    return render(request, template_name, locals())


def create_post(request, template_name):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm()
    return render(request, template_name, {'form': form})
