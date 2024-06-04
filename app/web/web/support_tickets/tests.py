# support_tickets/tests.py
from django.test import TestCase
from users.models import User
from .models import SupportTicket


class SupportTicketModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', phone_number='09123456789',
                                             password='password123')

    def test_create_support_ticket(self):
        support_ticket = SupportTicket.objects.create(user=self.user, subject='Support ticket subject',
                                                      description='Support ticket description', status='open')
        self.assertEqual(support_ticket.user, self.user)
        self.assertEqual(support_ticket.subject, 'Support ticket subject')
        self.assertEqual(support_ticket.description, 'Support ticket description')
        self.assertEqual(support_ticket.status, 'open')
