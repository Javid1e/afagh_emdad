# requests/tests.py
from django.test import TestCase
from django.contrib.gis.geos import Point
from users.models import User
from .models import Request


class RequestModelTest(TestCase):

    def setUp(self):
        self.client_user = User.objects.create_user(username='clientuser', email='client@example.com',
                                                    phone_number='09123456789', password='password123')

    def test_create_request(self):
        request = Request.objects.create(client=self.client_user, status='pending', location=Point(51.5074, 0.1278),
                                         description='Need help')
        self.assertEqual(request.client, self.client_user)
        self.assertEqual(request.status, 'pending')
        self.assertEqual(request.location, Point(51.5074, 0.1278))
        self.assertEqual(request.description, 'Need help')
