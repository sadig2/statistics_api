from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import PROTECT


class User(AbstractUser):
    pass


class Post(models.Model):
    user_id = models.ForeignKey(User, related_name="posts", on_delete=PROTECT)
    post_id = models.IntegerField()
    likes = models.IntegerField()
