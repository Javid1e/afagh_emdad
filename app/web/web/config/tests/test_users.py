# tests/test_users.py

from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User
import json
from graphene_django.utils.testing import GraphQLTestCase


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            email='testuser@example.com',
            phone_number='09123456789',
            role='client'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertEqual(self.user.phone_number, '09123456789')


class UserAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', phone_number='09123456789',
                                             password='password', role='client')

    def test_create_user(self):
        url = reverse('user-list')
        data = {'username': 'newuser', 'email': 'newuser@example.com', 'phone_number': '09123456788',
                'password': 'password'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], 'newuser')

    def test_get_user(self):
        url = reverse('user-detail', kwargs={'pk': self.user.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)


class UserGraphQLTest(GraphQLTestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', phone_number='09123456789',
                                             password='password', role='client')

    def test_all_users_query(self):
        response = self.query(
            '''
            query {
                allUsers {
                    username
                    email
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['allUsers'][0]['username'], self.user.username)

    def test_create_user_mutation(self):
        response = self.query(
            '''
            mutation {
                createUser(username: "newuser", email: "newuser@example.com", phoneNumber: "09123456788", password: "password") {
                    user {
                        username
                        email
                    }
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['createUser']['user']['username'], 'newuser')
