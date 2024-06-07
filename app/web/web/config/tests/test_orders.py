# tests/test_orders.py

from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User
from orders.models import Order
import json
from graphene_django.utils.testing import GraphQLTestCase


class OrderModelTest(TestCase):
    def setUp(self):
        self.client = User.objects.create(username='clientuser', email='client@example.com', phone_number='09123456789',
                                          role='client')
        self.order = Order.objects.create(
            user=self.client,
            service_type='towing',
            status='pending'
        )

    def test_order_creation(self):
        self.assertEqual(self.order.user.username, 'clientuser')
        self.assertEqual(self.order.service_type, 'towing')
        self.assertEqual(self.order.status, 'pending')


class OrderAPITest(APITestCase):
    def setUp(self):
        self.client_user = User.objects.create_user(username='clientuser', email='client@example.com',
                                                    phone_number='09123456789', password='password', role='client')
        self.client.force_authenticate(user=self.client_user)
        self.order = Order.objects.create(user=self.client_user, service_type='towing', status='pending')

    def test_create_order(self):
        url = reverse('order-list')
        data = {'user': self.client_user.id, 'service_type': 'towing', 'status': 'pending'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['service_type'], 'towing')

    def test_get_order(self):
        url = reverse('order-detail', kwargs={'pk': self.order.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['service_type'], self.order.service_type)


class OrderGraphQLTest(GraphQLTestCase):
    def setUp(self):
        self.client_user = User.objects.create_user(username='clientuser', email='client@example.com',
                                                    phone_number='09123456789', password='password', role='client')
        self.order = Order.objects.create(user=self.client_user, service_type='towing', status='pending')

    def test_all_orders_query(self):
        response = self.query(
            '''
            query {
                allOrders {
                    serviceType
                    status
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['allOrders'][0]['serviceType'], self.order.service_type)

    def test_create_order_mutation(self):
        response = self.query(
            '''
            mutation {
                createOrder(userId: ''' + str(self.client_user.id) + ''', serviceType: "towing", status: "pending") {
                    order {
                        serviceType
                        status
                    }
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['createOrder']['order']['serviceType'], 'towing')
