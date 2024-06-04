# orders/tests.py
from django.test import TestCase
from users.models import User
from .models import Order


class OrderModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', phone_number='09123456789',
                                             password='password123')

    def test_create_order(self):
        order = Order.objects.create(user=self.user, service_type='towing', status='pending', location='Location')
        self.assertEqual(order.user, self.user)
        self.assertEqual(order.service_type, 'towing')
        self.assertEqual(order.status, 'pending')
        self.assertEqual(order.location, 'Location')
