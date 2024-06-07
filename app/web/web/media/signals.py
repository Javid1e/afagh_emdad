# media/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Media
from .tasks import clean_unused_media


@receiver(post_delete, sender=Media)
def clean_media_on_delete(sender, instance, **kwargs):
    clean_unused_media.delay()
