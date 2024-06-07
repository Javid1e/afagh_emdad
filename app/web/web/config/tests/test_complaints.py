# tests/test_complaints.py
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User
from orders.models import Order
from complaints.models import Complaint
import json
from graphene_django.utils.testing import GraphQLTestCase


class ComplaintModelTest(TestCase):
    def setUp(self):
        self.client = User.objects.create(username='clientuser', email='client@example.com', phone_number='09123456789',
                                          role='client')
        self.order = Order.objects.create(user=self.client, service_type='towing', status='completed')
        self.complaint = Complaint.objects.create(
            user=self.client,
            order=self.order,
            description='مشکل در خدمات'
        )

    def test_complaint_creation(self):
        self.assertEqual(self.complaint.user.username, 'clientuser')
        self.assertEqual(self.complaint.order.service_type, 'towing')
        self.assertEqual(self.complaint.description, 'مشکل در خدمات')


class ComplaintAPITest(APITestCase):
    def setUp(self):
        self.client_user = User.objects.create_user(username='clientuser', email='client@example.com',
                                                    phone_number='09123456789', password='password', role='client')
        self.client.force_authenticate(user=self.client_user)
        self.order = Order.objects.create(user=self.client_user, service_type='towing', status='completed')
        self.complaint = Complaint.objects.create(user=self.client_user, order=self.order, description='مشکل در خدمات')

    def test_create_complaint(self):
        url = reverse('complaint-list')
        data = {'user': self.client_user.id, 'order': self.order.id, 'description': 'مشکل در خدمات'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['description'], 'مشکل در خدمات')

    def test_get_complaint(self):
        url = reverse('complaint-detail', kwargs={'pk': self.complaint.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], self.complaint.description)


class ComplaintGraphQLTest(GraphQLTestCase):
    def setUp(self):
        self.client_user = User.objects.create_user(username='clientuser', email='client@example.com',
                                                    phone_number='09123456789', password='password', role='client')
        self.order = Order.objects.create(user=self.client_user, service_type='towing', status='completed')
        self.complaint = Complaint.objects.create(user=self.client_user, order=self.order, description='مشکل در خدمات')

    def test_all_complaints_query(self):
        response = self.query(
            '''
            query {
                allComplaints {
                    description
                    status
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['allComplaints'][0]['description'], self.complaint.description)

    def test_create_complaint_mutation(self):
        response = self.query(
            '''
            mutation {
                createComplaint(userId: ''' + str(self.client_user.id) + ''', orderId: ''' + str(self.order.id) + ''', description: "شکایت جدید") {
                    complaint {
                        description
                        status
                    }
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['createComplaint']['complaint']['description'], 'شکایت جدید')
