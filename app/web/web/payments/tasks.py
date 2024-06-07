# payments/tasks.py
from celery import shared_task
from .models import Payment
from notifications.models import Notification
from django.utils.translation import gettext as _


@shared_task
def process_payment(payment_id):
    payment = Payment.objects.get(id=payment_id)
    # //Todo  فرض کنید اینجا کد پردازش پرداخت داریم
    payment.status = 'completed'
    payment.save()
    Notification.objects.create(
        user=payment.request.client,
        type='push',
        message=_('Your payment for request ID: {request_id} has been processed.').format(request_id=payment.request.id)
    )
