# cities/tests.py
from django.test import TestCase
from .models import City


class CityModelTest(TestCase):

    def test_create_city(self):
        city = City.objects.create(name='Tehran', description='Capital city of Iran')
        self.assertEqual(city.name, 'Tehran')
        self.assertEqual(city.description, 'Capital city of Iran')
