# profiles/tasks.py
from celery import shared_task
from .models import Profile


@shared_task
def update_profile(user_id, personal_info, car_info):
    profile = Profile.objects.get(user_id=user_id)
    profile.personal_information = personal_info
    profile.car_information = car_info
    profile.save()
