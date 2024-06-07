# roles/tests.py
from django.test import TestCase
from .models import Role


class RoleModelTest(TestCase):

    def test_create_role(self):
        role = Role.objects.create(name='admin', permissions={'can_view': True, 'can_edit': False})
        self.assertEqual(role.name, 'admin')
        self.assertEqual(role.permissions, {'can_view': True, 'can_edit': False})
