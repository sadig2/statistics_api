from api.models import Post
from .views import post_list, post_detail, PostApi, post_stats,\
    number_of_likes_per_user
from django.urls import path

urlpatterns = [
    path(r'posts/', post_list, name="all_posts"),
    path(r'post/<int:id>/', post_detail, name="single_post"),
    path(r'postapi/', PostApi.as_view()),
    path(r'post_stats/<int:id>/', post_stats, name="post_stats"),
    path(r'number_of_likes_per_user/<int:id>/', number_of_likes_per_user,
         name="number_of_likes_per_user")
]
