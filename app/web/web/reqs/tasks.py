# requests/tasks.py
from celery import shared_task
from django.utils.translation import gettext as _
from .models import Request
from notifications.models import Notification
from users.models import User


@shared_task
def notify_rescuers_nearby(request_id):
    rescue_request = Request.objects.get(id=request_id)
    rescuers = User.objects.filter(role='rescuer')
    for rescuer in rescuers:
        Notification.objects.create(
            user=rescuer,
            type='push',
            message=_('New request nearby with ID: {request_id}').format(request_id=rescue_request.id)
        )
