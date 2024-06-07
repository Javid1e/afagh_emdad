# roles/tasks.py
from celery import shared_task
from .models import Role
from users.models import User


@shared_task
def assign_role(user_id, role_id):
    user = User.objects.get(id=user_id)
    role = Role.objects.get(id=role_id)
    user.role = role.name
    user.save()
