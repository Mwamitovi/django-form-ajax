# talk/views.py
from talk.models import Post
from talk.forms import PostForm
from talk.serializers import PostSerializer

from django.shortcuts import render
from rest_framework.mixins import \
    ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView


def home(request):
    tmpl_vars = {'form': PostForm()}
    return render(request, 'talk/index.html', tmpl_vars)


# ------- CLASS_BASED VIEWS ----------


class PostCollection(ListModelMixin, CreateModelMixin, GenericAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, * args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostMember(RetrieveModelMixin, DestroyModelMixin, GenericAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# ------- FUNCTIONAL VIEWS ----------


# from django.shortcuts import get_object_or_404
# from django.http import HttpResponse, QueryDict
# import json
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status


# @api_view(['GET', 'POST'])
# def post_collection(request):
#     if request.method == 'GET':
#         _posts = Post.objects.all()
#         serializer = PostSerializer(_posts, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         _data = {
#             'text': request.data.get('the_post'),
#             'author': request.user
#         }
#         serializer = PostSerializer(data=_data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'DELETE'])
# def post_element(request, pk):
#     post = get_object_or_404(Post, id=pk)
#
#     if request.method == 'GET':
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#
#     elif request.method == 'DELETE':
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
