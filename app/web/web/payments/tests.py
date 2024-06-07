# payments/tests.py
from django.test import TestCase
from requests.models import Request
from users.models import User
from .models import Payment


class PaymentModelTest(TestCase):

    def setUp(self):
        self.client_user = User.objects.create_user(username='clientuser', email='client@example.com',
                                                    phone_number='09123456789', password='password123')
        self.request = Request.objects.create(client=self.client_user, status='pending',
                                              location='POINT(51.5074 0.1278)', description='Need help')

    def test_create_payment(self):
        payment = Payment.objects.create(request=self.request, amount=100.0, status='pending')
        self.assertEqual(payment.request, self.request)
        self.assertEqual(payment.amount, 100.0)
        self.assertEqual(payment.status, 'pending')
