# users/tests.py
from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import User


class UserModelTest(TestCase):

    def test_create_user(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', phone_number='09123456789',
                                        password='password123')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.phone_number, '09123456789')

    def test_phone_number_validation(self):
        with self.assertRaises(ValidationError):
            user = User(username='testuser', email='test@example.com', phone_number='123', password='password123')
            user.full_clean()
