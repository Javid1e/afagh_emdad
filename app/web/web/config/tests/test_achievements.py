# tests/test_achievements.py

from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from achievements.models import Achievement
import json
from graphene_django.utils.testing import GraphQLTestCase


class AchievementModelTest(TestCase):
    def setUp(self):
        self.achievement = Achievement.objects.create(
            title='دستاورد نمونه',
            description='این یک دستاورد نمونه است',
            date='2023-06-01'
        )

    def test_achievement_creation(self):
        self.assertEqual(self.achievement.title, 'دستاورد نمونه')
        self.assertEqual(self.achievement.description, 'این یک دستاورد نمونه است')
        self.assertEqual(self.achievement.date, '2023-06-01')


class AchievementAPITest(APITestCase):
    def setUp(self):
        self.achievement = Achievement.objects.create(title='دستاورد نمونه', description='این یک دستاورد نمونه است',
                                                      date='2023-06-01')

    def test_create_achievement(self):
        url = reverse('achievement-list')
        data = {'title': 'دستاورد جدید', 'description': 'این یک دستاورد جدید است', 'date': '2023-06-01'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'دستاورد جدید')

    def test_get_achievement(self):
        url = reverse('achievement-detail', kwargs={'pk': self.achievement.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.achievement.title)


class AchievementGraphQLTest(GraphQLTestCase):
    def setUp(self):
        self.achievement = Achievement.objects.create(title='دستاورد نمونه', description='این یک دستاورد نمونه است',
                                                      date='2023-06-01')

    def test_all_achievements_query(self):
        response = self.query(
            '''
            query {
                allAchievements {
                    title
                    description
                    date
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['allAchievements'][0]['title'], self.achievement.title)

    def test_create_achievement_mutation(self):
        response = self.query(
            '''
            mutation {
                createAchievement(title: "دستاورد جدید", description: "این یک دستاورد جدید است", date: "2023-06-01") {
                    achievement {
                        title
                        description
                        date
                    }
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['createAchievement']['achievement']['title'], 'دستاورد جدید')
