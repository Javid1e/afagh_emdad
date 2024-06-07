# tests/test_services.py

from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from services.models import Service
import json
from graphene_django.utils.testing import GraphQLTestCase


class ServiceModelTest(TestCase):
    def setUp(self):
        self.service = Service.objects.create(
            name='یدک‌کشی',
            description='خدمات یدک‌کشی خودرو',
            price=500000
        )

    def test_service_creation(self):
        self.assertEqual(self.service.name, 'یدک‌کشی')
        self.assertEqual(self.service.description, 'خدمات یدک‌کشی خودرو')
        self.assertEqual(self.service.price, 500000)


class ServiceAPITest(APITestCase):
    def setUp(self):
        self.service = Service.objects.create(name='یدک‌کشی', description='خدمات یدک‌کشی خودرو', price=500000)

    def test_create_service(self):
        url = reverse('service-list')
        data = {'name': 'یدک‌کشی', 'description': 'خدمات یدک‌کشی خودرو', 'price': 500000}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'یدک‌کشی')

    def test_get_service(self):
        url = reverse('service-detail', kwargs={'pk': self.service.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.service.name)


class ServiceGraphQLTest(GraphQLTestCase):
    def setUp(self):
        self.service = Service.objects.create(name='یدک‌کشی', description='خدمات یدک‌کشی خودرو', price=500000)

    def test_all_services_query(self):
        response = self.query(
            '''
            query {
                allServices {
                    name
                    description
                    price
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['allServices'][0]['name'], self.service.name)

    def test_create_service_mutation(self):
        response = self.query(
            '''
            mutation {
                createService(name: "یدک‌کشی", description: "خدمات یدک‌کشی خودرو", price: 500000) {
                    service {
                        name
                        description
                        price
                    }
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['createService']['service']['name'], 'یدک‌کشی')
