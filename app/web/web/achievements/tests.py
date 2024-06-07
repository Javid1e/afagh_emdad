# achievements/tests.py
from django.test import TestCase
from .models import Achievement


class AchievementModelTest(TestCase):

    def test_create_achievement(self):
        achievement = Achievement.objects.create(title='First Service', description='Completed first service',
                                                 date='2023-01-01')
        self.assertEqual(achievement.title, 'First Service')
        self.assertEqual(achievement.description, 'Completed first service')
        self.assertEqual(achievement.date, '2023-01-01')
