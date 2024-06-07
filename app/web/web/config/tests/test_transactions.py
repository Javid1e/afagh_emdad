# tests/test_transactions.py

from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from payments.models import Payment
from transactions.models import Transaction
import json
from graphene_django.utils.testing import GraphQLTestCase


class TransactionModelTest(TestCase):
    def setUp(self):
        self.payment = Payment.objects.create(request_id=1, amount=100000, status='completed',
                                              transaction_details='جزئیات تراکنش')
        self.transaction = Transaction.objects.create(
            payment=self.payment,
            amount=100000,
            status='completed',
            date='2023-06-01T12:00:00Z'
        )

    def test_transaction_creation(self):
        self.assertEqual(self.transaction.amount, 100000)
        self.assertEqual(self.transaction.status, 'completed')
        self.assertEqual(self.transaction.date, '2023-06-01T12:00:00Z')


class TransactionAPITest(APITestCase):
    def setUp(self):
        self.payment = Payment.objects.create(request_id=1, amount=100000, status='completed',
                                              transaction_details='جزئیات تراکنش')
        self.transaction = Transaction.objects.create(payment=self.payment, amount=100000, status='completed',
                                                      date='2023-06-01T12:00:00Z')

    def test_create_transaction(self):
        url = reverse('transaction-list')
        data = {'payment': self.payment.id, 'amount': 200000, 'status': 'pending', 'date': '2023-06-02T12:00:00Z'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['amount'], 200000)

    def test_get_transaction(self):
        url = reverse('transaction-detail', kwargs={'pk': self.transaction.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['amount'], self.transaction.amount)


class TransactionGraphQLTest(GraphQLTestCase):
    def setUp(self):
        self.payment = Payment.objects.create(request_id=1, amount=100000, status='completed',
                                              transaction_details='جزئیات تراکنش')
        self.transaction = Transaction.objects.create(payment=self.payment, amount=100000, status='completed',
                                                      date='2023-06-01T12:00:00Z')

    def test_all_transactions_query(self):
        response = self.query(
            '''
            query {
                allTransactions {
                    amount
                    status
                    date
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['allTransactions'][0]['amount'], self.transaction.amount)

    def test_create_transaction_mutation(self):
        response = self.query(
            '''
            mutation {
                createTransaction(paymentId: ''' + str(self.payment.id) + ''', amount: 200000, status: "pending", date: "2023-06-02T12:00:00Z") {
                    transaction {
                        amount
                        status
                        date
                    }
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['createTransaction']['transaction']['amount'], 200000)
