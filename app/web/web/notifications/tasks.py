# notifications/tasks.py
from celery import shared_task
from kavenegar import KavenegarAPI
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_sms(phone_number, message):
    api = KavenegarAPI(settings.KAVENEGAR_API_KEY)
    params = {
        'sender': '',
        'receptor': phone_number,
        'message': message,
    }
    api.sms_send(params)


@shared_task
def send_email(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        'from@example.com',
        recipient_list,
        fail_silently=False,
    )
