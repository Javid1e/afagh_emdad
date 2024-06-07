# tests/test_live_location.py
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User
from reqs.models import Request
from live_location.models import LiveLocation
import json
from graphene_django.utils.testing import GraphQLTestCase


class LiveLocationModelTest(TestCase):
    def setUp(self):
        self.client = User.objects.create(username='clientuser', email='client@example.com', phone_number='09123456789',
                                          role='client')
        self.rescuer = User.objects.create(username='rescueruser', email='rescuer@example.com',
                                           phone_number='09123456788', role='rescuer')
        self.request = Request.objects.create(client=self.client, status='pending', description='نیاز به کمک دارم')
        self.live_location = LiveLocation.objects.create(
            request=self.request,
            rescuer=self.rescuer,
            latitude=35.6892,
            longitude=51.3890
        )

    def test_live_location_creation(self):
        self.assertEqual(self.live_location.request.client.username, 'clientuser')
        self.assertEqual(self.live_location.rescuer.username, 'rescueruser')
        self.assertEqual(self.live_location.latitude, 35.6892)
        self.assertEqual(self.live_location.longitude, 51.3890)


class LiveLocationAPITest(APITestCase):
    def setUp(self):
        self.client_user = User.objects.create_user(username='clientuser', email='client@example.com',
                                                    phone_number='09123456789', password='password', role='client')
        self.rescuer_user = User.objects.create_user(username='rescueruser', email='rescuer@example.com',
                                                     phone_number='09123456788', password='password', role='rescuer')
        self.client.force_authenticate(user=self.client_user)
        self.request = Request.objects.create(client=self.client_user, status='pending', description='نیاز به کمک دارم')
        self.live_location = LiveLocation.objects.create(request=self.request, rescuer=self.rescuer_user,
                                                         latitude=35.6892, longitude=51.3890)

    def test_create_live_location(self):
        url = reverse('livelocation-list')
        data = {'request': self.request.id, 'rescuer': self.rescuer_user.id, 'latitude': 35.6892, 'longitude': 51.3890}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['latitude'], 35.6892)

    def test_get_live_location(self):
        url = reverse('livelocation-detail', kwargs={'pk': self.live_location.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['latitude'], self.live_location.latitude)


class LiveLocationGraphQLTest(GraphQLTestCase):
    def setUp(self):
        self.client_user = User.objects.create_user(username='clientuser', email='client@example.com',
                                                    phone_number='09123456789', password='password', role='client')
        self.rescuer_user = User.objects.create_user(username='rescueruser', email='rescuer@example.com',
                                                     phone_number='09123456788', password='password', role='rescuer')
        self.request = Request.objects.create(client=self.client_user, status='pending', description='نیاز به کمک دارم')
        self.live_location = LiveLocation.objects.create(request=self.request, rescuer=self.rescuer_user,
                                                         latitude=35.6892, longitude=51.3890)

    def test_all_live_locations_query(self):
        response = self.query(
            '''
            query {
                allLiveLocations {
                    latitude
                    longitude
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['allLiveLocations'][0]['latitude'], self.live_location.latitude)

    def test_create_live_location_mutation(self):
        response = self.query(
            '''
            mutation {
                createLiveLocation(requestId: ''' + str(self.request.id) + ''', rescuerId: ''' + str(
                self.rescuer_user.id) + ''', latitude: 35.6892, longitude: 51.3890) {
                    liveLocation {
                        latitude
                        longitude
                    }
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['createLiveLocation']['liveLocation']['latitude'], 35.6892)
