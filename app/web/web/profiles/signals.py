# profiles/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile
from .tasks import update_profile


@receiver(post_save, sender=Profile)
def profile_post_save(sender, instance, **kwargs):
    update_profile.delay(instance.user.id, instance.personal_information, instance.car_information)


@receiver(post_delete, sender=Profile)
def profile_post_delete(sender, instance, **kwargs):
    # Logic to handle profile deletion, if needed
    pass
