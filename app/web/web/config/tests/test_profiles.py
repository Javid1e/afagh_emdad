# tests/test_profiles.py

from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User
from profiles.models import Profile
import json
from graphene_django.utils.testing import GraphQLTestCase


class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com', phone_number='09123456789',
                                        role='client')
        self.profile = Profile.objects.create(
            user=self.user,
            personal_information={'first_name': 'Test', 'last_name': 'User'},
            car_information={'make': 'Toyota', 'model': 'Corolla'}
        )

    def test_profile_creation(self):
        self.assertEqual(self.profile.personal_information['first_name'], 'Test')
        self.assertEqual(self.profile.car_information['make'], 'Toyota')


class ProfileAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', phone_number='09123456789',
                                             password='password', role='client')
        self.client.force_authenticate(user=self.user)
        self.profile = Profile.objects.create(user=self.user,
                                              personal_information={'first_name': 'Test', 'last_name': 'User'},
                                              car_information={'make': 'Toyota', 'model': 'Corolla'})

    def test_create_profile(self):
        url = reverse('profile-list')
        data = {'user': self.user.id, 'personal_information': {'first_name': 'New', 'last_name': 'User'},
                'car_information': {'make': 'Honda', 'model': 'Civic'}}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['personal_information']['first_name'], 'New')

    def test_get_profile(self):
        url = reverse('profile-detail', kwargs={'pk': self.profile.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['personal_information']['first_name'],
                         self.profile.personal_information['first_name'])


class ProfileGraphQLTest(GraphQLTestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', phone_number='09123456789',
                                             password='password', role='client')
        self.profile = Profile.objects.create(user=self.user,
                                              personal_information={'first_name': 'Test', 'last_name': 'User'},
                                              car_information={'make': 'Toyota', 'model': 'Corolla'})

    def test_all_profiles_query(self):
        response = self.query(
            '''
            query {
                allProfiles {
                    personalInformation
                    carInformation
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['allProfiles'][0]['personalInformation']['first_name'],
                         self.profile.personal_information['first_name'])

    def test_create_profile_mutation(self):
        response = self.query(
            '''
            mutation {
                createProfile(userId: ''' + str(self.user.id) + ''', personalInformation: {first_name: "New", last_name: "User"}, carInformation: {make: "Honda", model: "Civic"}) {
                    profile {
                        personalInformation
                        carInformation
                    }
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['createProfile']['profile']['personalInformation']['first_name'], 'New')
