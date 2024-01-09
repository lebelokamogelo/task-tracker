from django.shortcuts import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.models import User
from .models import Todo
from .serializers import TodoSerializer


class TestUser(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            **{"email": "test@example.com", "password": "test1234"})
        self.todo = Todo.objects.create(
            **{"user": self.user, "title": "django test",
               "description": "Test description", "priority": "Low"})
        self.client.force_login(self.user)

    def test_user(self):
        self.assertEqual(str(self.todo), 'django test')

    def test_todo_serializer(self):
        serializer = TodoSerializer(self.todo)
        self.assertEqual(serializer.data.get("url"), '/api/todo/1/')

    def test_validators(self):
        try:
            self.client.post(reverse('todos'),
                             data={"user": self.user,
                                   "title": "hello", "description":
                                   "Test description",
                                   "priority": "Low"})
            raise ValueError("Not allowed")
        except ValueError as e:
            self.assertEqual(str(e), 'Not allowed')

    def test_validators_valid(self):
        response_valid = self.client.post(reverse('todos'),
                                          data={"user": self.user,
                                                "title": "valid test",
                                                "description":
                                                "Test description"}
                                          )
        self.assertEqual(response_valid.status_code, status.HTTP_200_OK)

    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_todos_get(self):
        response = self.client.get(reverse('todos'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_todos_get_query(self):
        response = self.client.get(reverse('todos'), data={'query': 'django'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_todos_post(self):
        response = self.client.post(reverse('todos'),
                                    data={"user": self.user,
                                          "title": "new todo",
                                          "description": "Test description",
                                          "priority": "High"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_todo_get(self):
        response = self.client.get(reverse('todo', kwargs={'pk': '1'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_todo_put(self):
        response = self.client.put(reverse('todo', kwargs={'pk': '1'}),
                                   data={"user": self.user,
                                         "title": "django test",
                                         "description": "Test description",
                                         "priority": "High"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_todo_put_not_modified(self):
        response = self.client.put(reverse('todo', kwargs={'pk': '1'}),
                                   data={"user": self.user,
                                         "title": "django test",
                                         "description": "Test description",
                                         "priority": ""})
        self.assertEqual(response.status_code, status.HTTP_304_NOT_MODIFIED)

    def test_todo_delete(self):
        response = self.client.delete(reverse('todo', kwargs={'pk': '1'}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
