# complaints/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Complaint
from .tasks import notify_complaint_status_change


@receiver(post_save, sender=Complaint)
def notify_complaint_on_status_change(sender, instance, **kwargs):
    notify_complaint_status_change.delay(instance.id)


@receiver(post_delete, sender=Complaint)
def handle_complaint_deletion(sender, instance, **kwargs):
    #//Todo Logic to handle complaint deletion, if needed
    pass
