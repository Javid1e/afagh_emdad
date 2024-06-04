# reviews/tests.py
from django.test import TestCase
from users.models import User
from .models import Review


class ReviewModelTest(TestCase):

    def setUp(self):
        self.client_user = User.objects.create_user(username='clientuser', email='client@example.com',
                                                    phone_number='09123456789', password='password123')

    def test_create_review(self):
        review = Review.objects.create(client=self.client_user, rating=5, comments='Great service')
        self.assertEqual(review.client, self.client_user)
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.comments, 'Great service')
