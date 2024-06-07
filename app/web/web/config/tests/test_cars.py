# tests/test_cars.py

from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User
from cars.models import Car
import json
from graphene_django.utils.testing import GraphQLTestCase


class CarModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com', phone_number='09123456789',
                                        role='client')
        self.car = Car.objects.create(
            user=self.user,
            make='تویوتا',
            model='کرولا',
            year=2020,
            license_plate='12الف123'
        )

    def test_car_creation(self):
        self.assertEqual(self.car.make, 'تویوتا')
        self.assertEqual(self.car.model, 'کرولا')
        self.assertEqual(self.car.year, 2020)
        self.assertEqual(self.car.license_plate, '12الف123')


class CarAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', phone_number='09123456789',
                                             password='password', role='client')
        self.client.force_authenticate(user=self.user)
        self.car = Car.objects.create(user=self.user, make='تویوتا', model='کرولا', year=2020, license_plate='12الف123')

    def test_create_car(self):
        url = reverse('car-list')
        data = {'user': self.user.id, 'make': 'هوندا', 'model': 'سیویک', 'year': 2019, 'license_plate': '34ب123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['make'], 'هوندا')

    def test_get_car(self):
        url = reverse('car-detail', kwargs={'pk': self.car.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['make'], self.car.make)


class CarGraphQLTest(GraphQLTestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', phone_number='09123456789',
                                             password='password', role='client')
        self.car = Car.objects.create(user=self.user, make='تویوتا', model='کرولا', year=2020, license_plate='12الف123')

    def test_all_cars_query(self):
        response = self.query(
            '''
            query {
                allCars {
                    make
                    model
                    year
                    licensePlate
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['allCars'][0]['make'], self.car.make)

    def test_create_car_mutation(self):
        response = self.query(
            '''
            mutation {
                createCar(userId: ''' + str(self.user.id) + ''', make: "هوندا", model: "سیویک", year: 2019, licensePlate: "34ب123") {
                    car {
                        make
                        model
                        year
                        licensePlate
                    }
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['createCar']['car']['make'], 'هوندا')
