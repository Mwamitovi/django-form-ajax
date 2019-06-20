# talk/views.py
import json
from django.shortcuts import render
from django.http import HttpResponse
from talk.models import Post
from talk.forms import PostForm


def home(request, template_name):
    all_posts = Post.objects.reverse()
    form = PostForm()
    return render(request, template_name, locals())


def create_post(request, template_name):
    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        post = Post(text=post_text, author=request.user)
        post.save()

        response_data = {
            'result': 'Create post successful',
            'postpk': post.pk,
            'text': post.text,
            'created': post.created.strftime('%B %d, %Y %I:%M %p'),
            'author': post.author.username
        }

        return HttpResponse(
            json.dumps(response_data), content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )




































