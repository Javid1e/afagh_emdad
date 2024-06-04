# cities/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import City
from .tasks import update_city_details


@receiver(post_save, sender=City)
def update_city_on_save(sender, instance, **kwargs):
    update_city_details.delay(instance.id, instance.details)
# //Todo:{Complete This}
