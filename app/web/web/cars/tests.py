# cars/tests.py
from django.test import TestCase
from users.models import User
from .models import Car


class CarModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', phone_number='09123456789',
                                             password='password123')

    def test_create_car(self):
        car = Car.objects.create(user=self.user, make='Toyota', model='Corolla', year=2020, license_plate='ABC1234')
        self.assertEqual(car.user, self.user)
        self.assertEqual(car.make, 'Toyota')
        self.assertEqual(car.model, 'Corolla')
        self.assertEqual(car.year, 2020)
        self.assertEqual(car.license_plate, 'ABC1234')
