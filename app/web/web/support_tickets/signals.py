# support_tickets/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import SupportTicket
from .tasks import notify_support_ticket_update


@receiver(post_save, sender=SupportTicket)
def notify_support_ticket_on_update(sender, instance, **kwargs):
    notify_support_ticket_update.delay(instance.id)
