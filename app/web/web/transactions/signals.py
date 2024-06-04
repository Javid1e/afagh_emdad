# transactions/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Transaction
from .tasks import notify_transaction


@receiver(post_save, sender=Transaction)
def notify_transaction_on_create(sender, instance, created, **kwargs):
    if created:
        notify_transaction.delay(instance.user.id, instance.id)
