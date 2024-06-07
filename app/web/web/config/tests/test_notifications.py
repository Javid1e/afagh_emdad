# tests/test_notifications.py

from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User
from notifications.models import Notification
import json
from graphene_django.utils.testing import GraphQLTestCase


class NotificationModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com', phone_number='09123456789',
                                        role='client')
        self.notification = Notification.objects.create(
            user=self.user,
            type='email',
            message='پیام تستی',
            read_status=False
        )

    def test_notification_creation(self):
        self.assertEqual(self.notification.type, 'email')
        self.assertEqual(self.notification.message, 'پیام تستی')
        self.assertFalse(self.notification.read_status)


class NotificationAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', phone_number='09123456789',
                                             password='password', role='client')
        self.client.force_authenticate(user=self.user)
        self.notification = Notification.objects.create(user=self.user, type='email', message='پیام تستی',
                                                        read_status=False)

    def test_create_notification(self):
        url = reverse('notification-list')
        data = {'user': self.user.id, 'type': 'sms', 'message': 'پیام جدید', 'read_status': False}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['type'], 'sms')

    def test_get_notification(self):
        url = reverse('notification-detail', kwargs={'pk': self.notification.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['type'], self.notification.type)


class NotificationGraphQLTest(GraphQLTestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', phone_number='09123456789',
                                             password='password', role='client')
        self.notification = Notification.objects.create(user=self.user, type='email', message='پیام تستی',
                                                        read_status=False)

    def test_all_notifications_query(self):
        response = self.query(
            '''
            query {
                allNotifications {
                    type
                    message
                    readStatus
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['allNotifications'][0]['type'], self.notification.type)

    def test_create_notification_mutation(self):
        response = self.query(
            '''
            mutation {
                createNotification(userId: ''' + str(self.user.id) + ''', type: "sms", message: "پیام جدید", readStatus: false) {
                    notification {
                        type
                        message
                        readStatus
                    }
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['createNotification']['notification']['type'], 'sms')
