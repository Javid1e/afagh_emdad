# users/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from django.utils.translation import gettext as _
from .models import User


@shared_task
def send_welcome_email(user_id):
    user = User.objects.get(id=user_id)
    send_mail(
        _("Welcome to Afagh Emdad"),
        _("Hello {username}, welcome to Afagh Emdad!").format(username=user.username),
        'from@example.com',
        [user.email],
        fail_silently=False,
    )
