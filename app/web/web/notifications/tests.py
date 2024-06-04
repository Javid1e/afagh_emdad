# notifications/tests.py
from django.test import TestCase
from users.models import User
from .models import Notification


class NotificationModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', phone_number='09123456789',
                                             password='password123')

    def test_create_notification(self):
        notification = Notification.objects.create(user=self.user, type='email', message='Notification message')
        self.assertEqual(notification.user, self.user)
        self.assertEqual(notification.type, 'email')
        self.assertEqual(notification.message, 'Notification message')
