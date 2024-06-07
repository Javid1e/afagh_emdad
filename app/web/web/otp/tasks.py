# otp/tasks.py
from celery import shared_task
from django.utils import timezone
from django.utils.translation import gettext as _
from .models import OTP
from kavenegar import KavenegarAPI


@shared_task
def send_otp(user_id, phone_number):
    otp_code = OTP.objects.create(user_id=user_id, code='123456',
                                  expires_at=timezone.now() + timezone.timedelta(minutes=5))
    api = KavenegarAPI('your_api_key')
    params = {
        'receptor': phone_number,
        'message': _('Your OTP code is {code}').format(code=otp_code.code)
    }
    api.sms_send(params)
