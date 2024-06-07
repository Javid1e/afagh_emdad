# tests/test_faq.py

from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from faq.models import FAQ
import json
from graphene_django.utils.testing import GraphQLTestCase


class FAQModelTest(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question='سوال تستی',
            answer='جواب تستی'
        )

    def test_faq_creation(self):
        self.assertEqual(self.faq.question, 'سوال تستی')
        self.assertEqual(self.faq.answer, 'جواب تستی')


class FAQAPITest(APITestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(question='سوال تستی', answer='جواب تستی')

    def test_create_faq(self):
        url = reverse('faq-list')
        data = {'question': 'سوال جدید', 'answer': 'جواب جدید'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['question'], 'سوال جدید')

    def test_get_faq(self):
        url = reverse('faq-detail', kwargs={'pk': self.faq.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['question'], self.faq.question)


class FAQGraphQLTest(GraphQLTestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(question='سوال تستی', answer='جواب تستی')

    def test_all_faqs_query(self):
        response = self.query(
            '''
            query {
                allFaqs {
                    question
                    answer
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['allFaqs'][0]['question'], self.faq.question)

    def test_create_faq_mutation(self):
        response = self.query(
            '''
            mutation {
                createFaq(question: "سوال جدید", answer: "جواب جدید") {
                    faq {
                        question
                        answer
                    }
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['createFaq']['faq']['question'], 'سوال جدید')
