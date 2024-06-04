# faqs/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import FAQ
from .tasks import update_faq_details


@receiver(post_save, sender=FAQ)
def update_faq_on_save(sender, instance, **kwargs):
    update_faq_details.delay(instance.id, instance.details)
