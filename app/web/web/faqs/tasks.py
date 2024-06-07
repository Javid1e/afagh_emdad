# faqs/tasks.py
from celery import shared_task
from .models import FAQ


@shared_task
def update_faq_details(faq_id, details):
    faq = FAQ.objects.get(id=faq_id)
    faq.details = details
    faq.save()
