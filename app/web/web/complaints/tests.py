# complaints/tests.py
from django.test import TestCase
from users.models import User
from orders.models import Order
from .models import Complaint


class ComplaintModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', phone_number='09123456789',
                                             password='password123')
        self.order = Order.objects.create(user=self.user, service_type='towing', status='pending', location='Location')

    def test_create_complaint(self):
        complaint = Complaint.objects.create(user=self.user, order=self.order, description='Complaint description',
                                             status='open')
        self.assertEqual(complaint.user, self.user)
        self.assertEqual(complaint.order, self.order)
        self.assertEqual(complaint.description, 'Complaint description')
        self.assertEqual(complaint.status, 'open')
