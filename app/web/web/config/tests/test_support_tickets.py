# tests/test_support_tickets.py

from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User
from support_tickets.models import SupportTicket
import json
from graphene_django.utils.testing import GraphQLTestCase


class SupportTicketModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com', phone_number='09123456789',
                                        role='client')
        self.support_ticket = SupportTicket.objects.create(
            user=self.user,
            subject='مشکل تستی',
            description='این یک مشکل تستی است',
            status='open'
        )

    def test_support_ticket_creation(self):
        self.assertEqual(self.support_ticket.subject, 'مشکل تستی')
        self.assertEqual(self.support_ticket.description, 'این یک مشکل تستی است')
        self.assertEqual(self.support_ticket.status, 'open')


class SupportTicketAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', phone_number='09123456789',
                                             password='password', role='client')
        self.client.force_authenticate(user=self.user)
        self.support_ticket = SupportTicket.objects.create(user=self.user, subject='مشکل تستی',
                                                           description='این یک مشکل تستی است', status='open')

    def test_create_support_ticket(self):
        url = reverse('supportticket-list')
        data = {'user': self.user.id, 'subject': 'مشکل جدید', 'description': 'این یک مشکل جدید است', 'status': 'open'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['subject'], 'مشکل جدید')

    def test_get_support_ticket(self):
        url = reverse('supportticket-detail', kwargs={'pk': self.support_ticket.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['subject'], self.support_ticket.subject)


class SupportTicketGraphQLTest(GraphQLTestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', phone_number='09123456789',
                                             password='password', role='client')
        self.support_ticket = SupportTicket.objects.create(user=self.user, subject='مشکل تستی',
                                                           description='این یک مشکل تستی است', status='open')

    def test_all_support_tickets_query(self):
        response = self.query(
            '''
            query {
                allSupportTickets {
                    subject
                    description
                    status
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['allSupportTickets'][0]['subject'], self.support_ticket.subject)

    def test_create_support_ticket_mutation(self):
        response = self.query(
            '''
            mutation {
                createSupportTicket(userId: ''' + str(self.user.id) + ''', subject: "مشکل جدید", description: "این یک مشکل جدید است", status: "open") {
                    supportTicket {
                        subject
                        description
                        status
                    }
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['createSupportTicket']['supportTicket']['subject'], 'مشکل جدید')
