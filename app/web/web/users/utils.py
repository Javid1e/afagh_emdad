import random
import requests
from django.core.mail import send_mail
from django.conf import settings
from django.utils.translation import gettext_lazy as _


def generate_otp():
    return str(random.randint(100000, 999999))


def verify_otp(user_otp, otp):
    return user_otp == otp


def send_sms(phone_number, message):
    url = "https://api.smsprovider.com/send"
    payload = {
        'phone_number': phone_number,
        'message': message,
        'api_key': settings.SMS_API_KEY
    }
    response = requests.post(url, data=payload)
    if response.status_code != 200:
        raise Exception(_('SMS sending failed'))


def send_push_notification(user, title, message):
    url = "https://api.pushnotificationprovider.com/send"
    payload = {
        'user_id': user.id,
        'title': title,
        'message': message,
        'api_key': settings.PUSH_NOTIFICATION_API_KEY
    }
    response = requests.post(url, data=payload)
    if response.status_code != 200:
        raise Exception(_('Push notification sending failed'))


def send_email(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        recipient_list,
        fail_silently=False,
    )
