# live_location/tests.py
from django.test import TestCase
from django.contrib.gis.geos import Point
from users.models import User
from requests.models import Request
from .models import LiveLocation


class LiveLocationModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', phone_number='09123456789',
                                             password='password123')
        self.request = Request.objects.create(client=self.user, status='pending', location=Point(51.5074, 0.1278),
                                              description='Need help')

    def test_create_live_location(self):
        live_location = LiveLocation.objects.create(user=self.user, request=self.request,
                                                    location=Point(51.5074, 0.1278))
        self.assertEqual(live_location.user, self.user)
        self.assertEqual(live_location.request, self.request)
        self.assertEqual(live_location.location, Point(51.5074, 0.1278))
