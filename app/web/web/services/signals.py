# services/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Service
from .tasks import update_service_details


@receiver(post_save, sender=Service)
def update_service_on_save(sender, instance, **kwargs):
    update_service_details.delay(instance.id, instance.details)
