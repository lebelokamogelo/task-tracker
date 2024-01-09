from rest_framework.test import APITestCase

from .models import User


class TestUser(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            **{"email": "test@example.com", "password": "test1234"})

    def test_user(self):
        self.assertEqual(str(self.user), 'test@example.com')
