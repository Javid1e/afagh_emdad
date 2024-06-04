# faqs/tests.py
from django.test import TestCase
from .models import FAQ


class FAQModelTest(TestCase):

    def test_create_faq(self):
        faq = FAQ.objects.create(question='How to use the service?',
                                 answer='You can use the service by registering and making a request.')
        self.assertEqual(faq.question, 'How to use the service?')
        self.assertEqual(faq.answer, 'You can use the service by registering and making a request.')
