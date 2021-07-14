from rest_framework import serializers
from .models import User
from django.db.models.deletion import PROTECT


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    password = serializers.CharField()


class PostSerializer(serializers.Serializer):
    user_id = UserSerializer()
    post_id = serializers.IntegerField()
    likes = serializers.IntegerField()
