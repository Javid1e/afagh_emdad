# certificates/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Certificate
from .tasks import notify_certificate


@receiver(post_save, sender=Certificate)
def notify_certificate_on_create(sender, instance, created, **kwargs):
    if created:
        notify_certificate.delay(instance.user.id, instance.id)
# //Todo:{Complete This}
