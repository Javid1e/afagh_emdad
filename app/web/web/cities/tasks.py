# cities/tasks.py
from celery import shared_task
from .models import City


@shared_task
def update_city_details(city_id, details):
    city = City.objects.get(id=city_id)
    city.details = details
    city.save()
