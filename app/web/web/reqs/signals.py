from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Request
from ..notifications.models import Notification
from .tasks import notify_rescuers_nearby


@receiver(post_save, sender=Request)
def notify_rescuers_on_create(sender, instance, created, **kwargs):
    if created:
        notify_rescuers_nearby.delay(instance.id)
