# tests/test_reviews.py

from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User
from reviews.models import Review
import json
from graphene_django.utils.testing import GraphQLTestCase


class ReviewModelTest(TestCase):
    def setUp(self):
        self.client = User.objects.create(username='clientuser', email='client@example.com', phone_number='09123456789',
                                          role='client')
        self.review = Review.objects.create(
            client=self.client,
            rating=5,
            comments='بسیار عالی'
        )

    def test_review_creation(self):
        self.assertEqual(self.review.client.username, 'clientuser')
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.comments, 'بسیار عالی')


class ReviewAPITest(APITestCase):
    def setUp(self):
        self.client_user = User.objects.create_user(username='clientuser', email='client@example.com',
                                                    phone_number='09123456789', password='password', role='client')
        self.client.force_authenticate(user=self.client_user)
        self.review = Review.objects.create(client=self.client_user, rating=5, comments='بسیار عالی')

    def test_create_review(self):
        url = reverse('review-list')
        data = {'client': self.client_user.id, 'rating': 5, 'comments': 'بسیار عالی'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['comments'], 'بسیار عالی')

    def test_get_review(self):
        url = reverse('review-detail', kwargs={'pk': self.review.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['comments'], self.review.comments)


class ReviewGraphQLTest(GraphQLTestCase):
    def setUp(self):
        self.client_user = User.objects.create_user(username='clientuser', email='client@example.com',
                                                    phone_number='09123456789', password='password', role='client')
        self.review = Review.objects.create(client=self.client_user, rating=5, comments='بسیار عالی')

    def test_all_reviews_query(self):
        response = self.query(
            '''
            query {
                allReviews {
                    rating
                    comments
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['allReviews'][0]['comments'], self.review.comments)

    def test_create_review_mutation(self):
        response = self.query(
            '''
            mutation {
                createReview(clientId: ''' + str(self.client_user.id) + ''', rating: 5, comments: "نقد جدید") {
                    review {
                        rating
                        comments
                    }
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['createReview']['review']['comments'], 'نقد جدید')
