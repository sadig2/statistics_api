from itertools import count
from django.http import response
from django.test import TestCase
from django.urls.base import reverse
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Post, User


class TestPost(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(
            username="sadig",
        )
        self.user.set_password('password')
        self.user.save()
        self.post = Post.objects.create(
            user_id=self.user,
            post_id=2,
            likes=3
        )

    def test_getall_posts(self):
        response = self.client.get(reverse('all_posts'))
        print(reverse('all_posts'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_url(self):
        response = self.client.get('/api/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_single_post(self):
        response = self.client.get(
            reverse('single_post', kwargs={"id": 2}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'sadig')

    def test_post_stats(self):
        response = self.client.get(
            reverse('post_stats', kwargs={'id': self.user.id}))
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_likes(self):
        countoflikes = 0
        posts = self.user.posts.all()
        for post in posts:
            countoflikes += post.likes

        response = self.client.get(
            reverse('number_of_likes_per_user', kwargs={'id': self.user.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['likes__sum'], countoflikes)
