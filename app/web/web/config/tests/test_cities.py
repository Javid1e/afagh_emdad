# tests/test_cities.py

from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from cities.models import City
import json
from graphene_django.utils.testing import GraphQLTestCase


class CityModelTest(TestCase):
    def setUp(self):
        self.city = City.objects.create(
            name='تهران',
            description='پایتخت ایران'
        )

    def test_city_creation(self):
        self.assertEqual(self.city.name, 'تهران')
        self.assertEqual(self.city.description, 'پایتخت ایران')


class CityAPITest(APITestCase):
    def setUp(self):
        self.city = City.objects.create(name='تهران', description='پایتخت ایران')

    def test_create_city(self):
        url = reverse('city-list')
        data = {'name': 'تهران', 'description': 'پایتخت ایران'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'تهران')

    def test_get_city(self):
        url = reverse('city-detail', kwargs={'pk': self.city.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.city.name)


class CityGraphQLTest(GraphQLTestCase):
    def setUp(self):
        self.city = City.objects.create(name='تهران', description='پایتخت ایران')

    def test_all_cities_query(self):
        response = self.query(
            '''
            query {
                allCities {
                    name
                    description
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['allCities'][0]['name'], self.city.name)

    def test_create_city_mutation(self):
        response = self.query(
            '''
            mutation {
                createCity(name: "تهران", description: "پایتخت ایران") {
                    city {
                        name
                        description
                    }
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['createCity']['city']['name'], 'تهران')
