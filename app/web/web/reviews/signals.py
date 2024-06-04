from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Review
from ..notifications.models import Notification


@receiver(post_save, sender=Review)
def notify_client_on_review_create(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.client,
            type='push',
            message=f'New review created: {instance.id}'
        )


@receiver(post_delete, sender=Review)
def handle_review_deletion(sender, instance, **kwargs):
    # //Todo Logic to handle review deletion, if needed
    pass
