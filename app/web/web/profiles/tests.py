# profiles/tests.py
from django.test import TestCase
from users.models import User
from .models import Profile


class ProfileModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', phone_number='09123456789',
                                             password='password123')

    def test_create_profile(self):
        profile = Profile.objects.create(user=self.user, personal_information={'age': 30},
                                         car_information={'make': 'Toyota'})
        self.assertEqual(profile.user, self.user)
        self.assertEqual(profile.personal_information['age'], 30)
        self.assertEqual(profile.car_information['make'], 'Toyota')
