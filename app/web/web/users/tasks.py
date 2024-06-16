from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
import requests


@shared_task
def send_email_task(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        recipient_list,
        fail_silently=False,
    )


@shared_task
def send_sms_task(phone_number, message):
    url = "https://api.smsprovider.com/send"
    payload = {
        'phone_number': phone_number,
        'message': message,
        'api_key': settings.SMS_API_KEY
    }
    response = requests.post(url, data=payload)
    if response.status_code != 200:
        raise Exception('SMS sending failed')


@shared_task
def send_push_notification_task(user_id, title, message):
    url = "https://api.pushnotificationprovider.com/send"
    payload = {
        'user_id': user_id,
        'title': title,
        'message': message,
        'api_key': settings.PUSH_NOTIFICATION_API_KEY
    }
    response = requests.post(url, data=payload)
    if response.status_code != 200:
        raise Exception('Push notification sending failed')
