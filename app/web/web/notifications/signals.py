# notifications/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Notification
from push_notifications.models import GCMDevice, APNSDevice, WebPushDevice


@receiver(post_save, sender=Notification)
def send_notification(sender, instance, created, **kwargs):
    if created:
        devices = GCMDevice.objects.filter(user=instance.user)
        devices.send_message(instance.message)

        devices = APNSDevice.objects.filter(user=instance.user)
        devices.send_message(instance.message)

        devices = WebPushDevice.objects.filter(user=instance.user)
        devices.send_message(instance.message)
