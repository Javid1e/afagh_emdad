# cars/tasks.py
from celery import shared_task
from .models import Car


@shared_task
def update_car_details(car_id, details):
    car = Car.objects.get(id=car_id)
    car.details = details
    car.save()
