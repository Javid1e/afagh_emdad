from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SupportTicket
from ..notifications.models import Notification


@receiver(post_save, sender=SupportTicket)
def notify_user_on_support_ticket_create(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.user,
            type='push',
            message=f'New support ticket created: {instance.id}'
        )
