from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Request
from notifications.models import Notification
from .tasks import notify_rescuers_nearby


@receiver(post_save, sender=Request)
def notify_rescuers_on_create(sender, instance, created, **kwargs):
    if created:
        notify_rescuers_nearby.delay(instance.id)


@receiver(post_delete, sender=Request)
def handle_request_deletion(sender, instance, **kwargs):
    # //Todo Logic to handle request deletion, if needed
    pass
