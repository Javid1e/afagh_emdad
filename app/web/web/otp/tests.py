# otp/tests.py
from django.test import TestCase
from users.models import User
from .models import OTP


class OTPModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', phone_number='09123456789',
                                             password='password123')

    def test_create_otp(self):
        otp = OTP.objects.create(user=self.user, code='123456')
        self.assertEqual(otp.user, self.user)
        self.assertEqual(otp.code, '123456')
