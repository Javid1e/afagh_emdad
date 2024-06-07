# tests/test_requests.py

from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User
from reqs.models import Request
import json
from graphene_django.utils.testing import GraphQLTestCase


class RequestModelTest(TestCase):
    def setUp(self):
        self.client = User.objects.create(username='clientuser', email='client@example.com', phone_number='09123456789',
                                          role='client')
        self.request = Request.objects.create(
            client=self.client,
            status='pending',
            description='نیاز به کمک دارم'
        )

    def test_request_creation(self):
        self.assertEqual(self.request.client.username, 'clientuser')
        self.assertEqual(self.request.status, 'pending')
        self.assertEqual(self.request.description, 'نیاز به کمک دارم')


class RequestAPITest(APITestCase):
    def setUp(self):
        self.client_user = User.objects.create_user(username='clientuser', email='client@example.com',
                                                    phone_number='09123456789', password='password', role='client')
        self.client.force_authenticate(user=self.client_user)
        self.request = Request.objects.create(client=self.client_user, status='pending', description='نیاز به کمک دارم')

    def test_create_request(self):
        url = reverse('request-list')
        data = {'client': self.client_user.id, 'status': 'pending', 'description': 'نیاز به کمک دارم'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['description'], 'نیاز به کمک دارم')

    def test_get_request(self):
        url = reverse('request-detail', kwargs={'pk': self.request.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], self.request.description)


class RequestGraphQLTest(GraphQLTestCase):
    def setUp(self):
        self.client_user = User.objects.create_user(username='clientuser', email='client@example.com',
                                                    phone_number='09123456789', password='password', role='client')
        self.request = Request.objects.create(client=self.client_user, status='pending', description='نیاز به کمک دارم')

    def test_all_requests_query(self):
        response = self.query(
            '''
            query {
                allRequests {
                    description
                    status
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['allRequests'][0]['description'], self.request.description)

    def test_create_request_mutation(self):
        response = self.query(
            '''
            mutation {
                createRequest(clientId: ''' + str(self.client_user.id) + ''', status: "pending", description: "درخواست جدید") {
                    request {
                        description
                        status
                    }
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['createRequest']['request']['description'], 'درخواست جدید')
