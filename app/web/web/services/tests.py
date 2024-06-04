# services/tests.py
from django.test import TestCase
from .models import Service


class ServiceModelTest(TestCase):

    def test_create_service(self):
        service = Service.objects.create(name='Towing', description='Towing service', price=100.0)
        self.assertEqual(service.name, 'Towing')
        self.assertEqual(service.description, 'Towing service')
        self.assertEqual(service.price, 100.0)
