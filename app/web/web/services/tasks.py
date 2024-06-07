# services/tasks.py
from celery import shared_task
from .models import Service


@shared_task
def update_service_details(service_id, details):
    service = Service.objects.get(id=service_id)
    service.details = details
    service.save()
