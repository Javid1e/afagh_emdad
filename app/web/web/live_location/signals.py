# live_location/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import LiveLocation
from .tasks import track_live_location


@receiver(post_save, sender=LiveLocation)
def track_location_on_update(sender, instance, **kwargs):
    track_live_location.delay(instance.id)
