from typing import List
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Post, User
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from django.db.models import Avg, Max, Min, Sum


class PostApi(ListAPIView):
    serializer_class = PostSerializer
    lookup_field = 'post_id'

    def get_queryset(self):
        posts = Post.objects.all()
        return posts

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

# api for all posts


@api_view(['GET'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

# api for specific post


@api_view(['GET'])
def post_detail(request, id):

    try:
        post = Post.objects.get(post_id=id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

# api for specific user


@api_view(['GET'])
def post_stats(request, id):

    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        posts = user.posts
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def avg_number_of_likes(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        posts = user.posts.all().aggregate(Avg('likes'))
        return Response(posts)
