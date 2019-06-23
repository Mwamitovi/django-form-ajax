# talk/views.py
from django.shortcuts import render
from django.http import HttpResponse, QueryDict
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from talk.models import Post
from talk.forms import PostForm
from talk.serializers import PostSerializer


def home(request):
    tmpl_vars = {'form': PostForm()}
    return render(request, 'talk/index.html', tmpl_vars)


def create_post(request):
    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        response_data = {}

        post = Post(text=post_text, author=request.user)
        post.save()

        response_data['result'] = 'Create post successful!'
        response_data['postpk'] = post.pk
        response_data['text'] = post.text
        response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
        response_data['author'] = post.author.username

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def delete_post(request):
    if request.method == 'DELETE':
        post = Post.objects.get(
            pk=int(QueryDict(request.body).get('postpk'))
        )
        post.delete()

        response_data = {'msg': 'Post was deleted.'}

        response = json.dumps(response_data)
    else:
        response = json.dumps({"nothing to see": "this isn't happening"})

    return HttpResponse(
        response,
        content_type="application/json"
    )


@api_view(['GET', 'POST'])
def post_collection(request):
    if request.method == 'GET':
        _posts = Post.objects.all()
        serializer = PostSerializer(_posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        _data = {
            'text': request.data.get('the_post'),
            'author': request.user
        }
        serializer = PostSerializer(data=_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serailizer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def post_element(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
