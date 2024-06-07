# tests/test_payments.py

from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User
from reqs.models import Request
from payments.models import Payment
import json
from graphene_django.utils.testing import GraphQLTestCase


class PaymentModelTest(TestCase):
    def setUp(self):
        self.client = User.objects.create(username='clientuser', email='client@example.com', phone_number='09123456789',
                                          role='client')
        self.request = Request.objects.create(client=self.client, status='pending', description='نیاز به کمک دارم')
        self.payment = Payment.objects.create(
            request=self.request,
            amount=1000,
            status='pending'
        )

    def test_payment_creation(self):
        self.assertEqual(self.payment.request.client.username, 'clientuser')
        self.assertEqual(self.payment.amount, 1000)
        self.assertEqual(self.payment.status, 'pending')


class PaymentAPITest(APITestCase):
    def setUp(self):
        self.client_user = User.objects.create_user(username='clientuser', email='client@example.com',
                                                    phone_number='09123456789', password='password', role='client')
        self.client.force_authenticate(user=self.client_user)
        self.request = Request.objects.create(client=self.client_user, status='pending', description='نیاز به کمک دارم')
        self.payment = Payment.objects.create(request=self.request, amount=1000, status='pending')

    def test_create_payment(self):
        url = reverse('payment-list')
        data = {'request': self.request.id, 'amount': 1000, 'status': 'pending'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['amount'], 1000)

    def test_get_payment(self):
        url = reverse('payment-detail', kwargs={'pk': self.payment.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['amount'], self.payment.amount)


class PaymentGraphQLTest(GraphQLTestCase):
    def setUp(self):
        self.client_user = User.objects.create_user(username='clientuser', email='client@example.com',
                                                    phone_number='09123456789', password='password', role='client')
        self.request = Request.objects.create(client=self.client_user, status='pending', description='نیاز به کمک دارم')
        self.payment = Payment.objects.create(request=self.request, amount=1000, status='pending')

    def test_all_payments_query(self):
        response = self.query(
            '''
            query {
                allPayments {
                    amount
                    status
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['allPayments'][0]['amount'], self.payment.amount)

    def test_create_payment_mutation(self):
        response = self.query(
            '''
            mutation {
                createPayment(requestId: ''' + str(self.request.id) + ''', amount: 1000, status: "pending") {
                    payment {
                        amount
                        status
                    }
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['createPayment']['payment']['amount'], 1000)
