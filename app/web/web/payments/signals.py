from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Payment
from notifications.models import Notification
from .tasks import process_payment


@receiver(post_save, sender=Payment)
def notify_client_on_payment_create(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.request.client,
            type='push',
            message=f'New payment created: {instance.id}'
        )


@receiver(post_save, sender=Payment)
def start_payment_processing(sender, instance, created, **kwargs):
    if created:
        process_payment.delay(instance.id)


@receiver(post_delete, sender=Payment)
def handle_payment_deletion(sender, instance, **kwargs):
    # Logic to handle payment deletion, if needed
    pass
