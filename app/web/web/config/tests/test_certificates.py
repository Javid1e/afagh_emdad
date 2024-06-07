# tests/test_certificates.py

from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from certificates.models import Certificate
import json
from graphene_django.utils.testing import GraphQLTestCase


class CertificateModelTest(TestCase):
    def setUp(self):
        self.certificate = Certificate.objects.create(
            name='گواهینامه رانندگی',
            issued_by='سازمان راهنمایی و رانندگی',
            date='2023-06-01',
            description='گواهینامه رانندگی معتبر'
        )

    def test_certificate_creation(self):
        self.assertEqual(self.certificate.name, 'گواهینامه رانندگی')
        self.assertEqual(self.certificate.issued_by, 'سازمان راهنمایی و رانندگی')
        self.assertEqual(self.certificate.date, '2023-06-01')
        self.assertEqual(self.certificate.description, 'گواهینامه رانندگی معتبر')


class CertificateAPITest(APITestCase):
    def setUp(self):
        self.certificate = Certificate.objects.create(name='گواهینامه رانندگی', issued_by='سازمان راهنمایی و رانندگی',
                                                      date='2023-06-01', description='گواهینامه رانندگی معتبر')

    def test_create_certificate(self):
        url = reverse('certificate-list')
        data = {'name': 'گواهینامه رانندگی', 'issued_by': 'سازمان راهنمایی و رانندگی', 'date': '2023-06-01',
                'description': 'گواهینامه رانندگی معتبر'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'گواهینامه رانندگی')

    def test_get_certificate(self):
        url = reverse('certificate-detail', kwargs={'pk': self.certificate.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.certificate.name)


class CertificateGraphQLTest(GraphQLTestCase):
    def setUp(self):
        self.certificate = Certificate.objects.create(name='گواهینامه رانندگی', issued_by='سازمان راهنمایی و رانندگی',
                                                      date='2023-06-01', description='گواهینامه رانندگی معتبر')

    def test_all_certificates_query(self):
        response = self.query(
            '''
            query {
                allCertificates {
                    name
                    issuedBy
                    date
                    description
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['allCertificates'][0]['name'], self.certificate.name)

    def test_create_certificate_mutation(self):
        response = self.query(
            '''
            mutation {
                createCertificate(name: "گواهینامه رانندگی", issuedBy: "سازمان راهنمایی و رانندگی", date: "2023-06-01", description: "گواهینامه رانندگی معتبر") {
                    certificate {
                        name
                        issuedBy
                        date
                        description
                    }
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['createCertificate']['certificate']['name'], 'گواهینامه رانندگی')
