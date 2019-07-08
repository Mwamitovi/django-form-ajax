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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def post_element(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
