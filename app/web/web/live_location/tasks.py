# live_location/tasks.py
from celery import shared_task
from .models import LiveLocation


@shared_task
def track_live_location(location_data):
    # //Todo Logic to track live location
    pass
