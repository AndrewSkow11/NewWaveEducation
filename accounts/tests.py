from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User


class UserListAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )

    def test_user_list_api_view(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('accounts_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserCreateAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'testpass123'
        }

    def test_user_create_api_view(self):
        response = self.client.post(reverse('account_create'), self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UserRetrieveUpdateDestroyAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )

    def test_user_retrieve_api_view(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse(
            'account_rud', kwargs={'pk': self.user.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_update_api_view(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(reverse(
            'account_rud',
            kwargs={'pk': self.user.id}),
            {'username': 'John'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_destroy_api_view(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(reverse(
            'account_rud', kwargs={'pk': self.user.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
