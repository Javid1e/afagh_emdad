# tests/test_roles.py

from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from roles.models import Role
import json
from graphene_django.utils.testing import GraphQLTestCase


class RoleModelTest(TestCase):
    def setUp(self):
        self.role = Role.objects.create(
            name='مدیر',
            permissions={'can_edit': True, 'can_delete': True}
        )

    def test_role_creation(self):
        self.assertEqual(self.role.name, 'مدیر')
        self.assertTrue(self.role.permissions['can_edit'])


class RoleAPITest(APITestCase):
    def setUp(self):
        self.role = Role.objects.create(name='مدیر', permissions={'can_edit': True, 'can_delete': True})

    def test_create_role(self):
        url = reverse('role-list')
        data = {'name': 'کاربر', 'permissions': {'can_edit': False, 'can_delete': False}}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'کاربر')

    def test_get_role(self):
        url = reverse('role-detail', kwargs={'pk': self.role.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.role.name)


class RoleGraphQLTest(GraphQLTestCase):
    def setUp(self):
        self.role = Role.objects.create(name='مدیر', permissions={'can_edit': True, 'can_delete': True})

    def test_all_roles_query(self):
        response = self.query(
            '''
            query {
                allRoles {
                    name
                    permissions
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['allRoles'][0]['name'], self.role.name)

    def test_create_role_mutation(self):
        response = self.query(
            '''
            mutation {
                createRole(name: "کاربر", permissions: {can_edit: false, can_delete: false}) {
                    role {
                        name
                        permissions
                    }
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['createRole']['role']['name'], 'کاربر')
