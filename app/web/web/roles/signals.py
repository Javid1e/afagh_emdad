# roles/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Role
from .tasks import assign_role


@receiver(post_save, sender=Role)
def assign_role_on_create(sender, instance, created, **kwargs):
    if created:
        assign_role.delay(instance.user.id, instance.id)
