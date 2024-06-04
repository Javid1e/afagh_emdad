# transactions/tests.py
from django.test import TestCase
from users.models import User
from .models import Transaction


class TransactionModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', phone_number='09123456789',
                                             password='password123')

    def test_create_transaction(self):
        transaction = Transaction.objects.create(user=self.user, amount=100.0, transaction_type='payment')
        self.assertEqual(transaction.user, self.user)
        self.assertEqual(transaction.amount, 100.0)
        self.assertEqual(transaction.transaction_type, 'payment')
