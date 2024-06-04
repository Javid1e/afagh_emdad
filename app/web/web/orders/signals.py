from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Order
from ..notifications.models import Notification


@receiver(post_save, sender=Order)
def notify_user_on_order_create(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.user,
            type='push',
            message=f'New order created: {instance.id}'
        )


@receiver(post_delete, sender=Order)
def handle_order_deletion(sender, instance, **kwargs):
    # //Todo Logic to handle order deletion, if needed
    pass
