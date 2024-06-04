# otp/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OTP
from .tasks import send_otp


@receiver(post_save, sender=OTP)
def send_otp_on_create(sender, instance, created, **kwargs):
    if created:
        send_otp.delay(instance.user.id, instance.user.phone_number)
