from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from ..profiles.models import Profile
from .tasks import send_welcome_email


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        send_welcome_email.delay(instance.id)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
