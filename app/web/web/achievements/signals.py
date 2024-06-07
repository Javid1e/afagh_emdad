# achievements/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Achievement
from .tasks import notify_achievement


@receiver(post_save, sender=Achievement)
def notify_achievement_on_create(sender, instance, created, **kwargs):
    if created:
        notify_achievement.delay(instance.user.id, instance.id)
