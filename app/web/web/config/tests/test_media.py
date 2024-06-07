# tests/test_media.py

from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User
from media.models import Media
import json
from graphene_django.utils.testing import GraphQLTestCase


class MediaModelTest(TestCase):
    def setUp(self):
        self.client = User.objects.create(username='clientuser', email='client@example.com', phone_number='09123456789',
                                          role='client')
        self.media = Media.objects.create(
            associated_model=self.client,
            file_url='http://example.com/file.jpg',
            file_type='image'
        )

    def test_media_creation(self):
        self.assertEqual(self.media.associated_model.username, 'clientuser')
        self.assertEqual(self.media.file_url, 'http://example.com/file.jpg')
        self.assertEqual(self.media.file_type, 'image')


class MediaAPITest(APITestCase):
    def setUp(self):
        self.client_user = User.objects.create_user(username='clientuser', email='client@example.com',
                                                    phone_number='09123456789', password='password', role='client')
        self.client.force_authenticate(user=self.client_user)
        self.media = Media.objects.create(associated_model=self.client_user, file_url='http://example.com/file.jpg',
                                          file_type='image')

    def test_create_media(self):
        url = reverse('media-list')
        data = {'associated_model': self.client_user.id, 'file_url': 'http://example.com/file.jpg',
                'file_type': 'image'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['file_url'], 'http://example.com/file.jpg')

    def test_get_media(self):
        url = reverse('media-detail', kwargs={'pk': self.media.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['file_url'], self.media.file_url)


class MediaGraphQLTest(GraphQLTestCase):
    def setUp(self):
        self.client_user = User.objects.create_user(username='clientuser', email='client@example.com',
                                                    phone_number='09123456789', password='password', role='client')
        self.media = Media.objects.create(associated_model=self.client_user, file_url='http://example.com/file.jpg',
                                          file_type='image')

    def test_all_media_query(self):
        response = self.query(
            '''
            query {
                allMedia {
                    fileUrl
                    fileType
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['allMedia'][0]['fileUrl'], self.media.file_url)

    def test_create_media_mutation(self):
        response = self.query(
            '''
            mutation {
                createMedia(associatedModelId: ''' + str(self.client_user.id) + ''', fileUrl: "http://example.com/file.jpg", fileType: "image") {
                    media {
                        fileUrl
                        fileType
                    }
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['createMedia']['media']['fileUrl'], 'http://example.com/file.jpg')
