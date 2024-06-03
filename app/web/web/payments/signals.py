from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Payment
from ..notifications.models import Notification


@receiver(post_save, sender=Payment)
def notify_client_on_payment_create(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.request.client,
            type='push',
            message=f'New payment created: {instance.id}'
        )
