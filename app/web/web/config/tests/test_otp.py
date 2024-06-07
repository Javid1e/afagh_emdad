# tests/test_otp.py

from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User
from otp.models import OTP
import json
from graphene_django.utils.testing import GraphQLTestCase


class OTPModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com', phone_number='09123456789',
                                        role='client')
        self.otp = OTP.objects.create(
            user=self.user,
            code='123456',
            valid_until='2023-06-01T12:00:00Z'
        )

    def test_otp_creation(self):
        self.assertEqual(self.otp.code, '123456')
        self.assertEqual(self.otp.valid_until, '2023-06-01T12:00:00Z')


class OTPAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', phone_number='09123456789',
                                             password='password', role='client')
        self.client.force_authenticate(user=self.user)
        self.otp = OTP.objects.create(user=self.user, code='123456', valid_until='2023-06-01T12:00:00Z')

    def test_create_otp(self):
        url = reverse('otp-list')
        data = {'user': self.user.id, 'code': '654321', 'valid_until': '2023-06-02T12:00:00Z'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['code'], '654321')

    def test_get_otp(self):
        url = reverse('otp-detail', kwargs={'pk': self.otp.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['code'], self.otp.code)


class OTPGraphQLTest(GraphQLTestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', phone_number='09123456789',
                                             password='password', role='client')
        self.otp = OTP.objects.create(user=self.user, code='123456', valid_until='2023-06-01T12:00:00Z')

    def test_all_otps_query(self):
        response = self.query(
            '''
            query {
                allOtps {
                    code
                    validUntil
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['allOtps'][0]['code'], self.otp.code)

    def test_create_otp_mutation(self):
        response = self.query(
            '''
            mutation {
                createOtp(userId: ''' + str(self.user.id) + ''', code: "654321", validUntil: "2023-06-02T12:00:00Z") {
                    otp {
                        code
                        validUntil
                    }
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['createOtp']['otp']['code'], '654321')
