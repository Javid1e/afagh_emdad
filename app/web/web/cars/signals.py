# cars/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Car
from .tasks import update_car_details


@receiver(post_save, sender=Car)
def update_car_on_save(sender, instance, **kwargs):
    update_car_details.delay(instance.id, instance.details)
