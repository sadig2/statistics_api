from django.test import TestCase
from django.urls.base import reverse
from rest_framework.test import APIClient
from rest_framework import status


class TestPost(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()

    def test_get_post(self):
        response = self.client.get(reverse('all_posts'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
