# certificates/tests.py
from django.test import TestCase
from users.models import User
from .models import Certificate


class CertificateModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', phone_number='09123456789',
                                             password='password123')

    def test_create_certificate(self):
        certificate = Certificate.objects.create(user=self.user, name='First Aid', issued_by='Red Cross',
                                                 issue_date='2023-01-01', expiry_date='2024-01-01')
        self.assertEqual(certificate.user, self.user)
        self.assertEqual(certificate.name, 'First Aid')
        self.assertEqual(certificate.issued_by, 'Red Cross')
        self.assertEqual(certificate.issue_date, '2023-01-01')
        self.assertEqual(certificate.expiry_date, '2024-01-01')
