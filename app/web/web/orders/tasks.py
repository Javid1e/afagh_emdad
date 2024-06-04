# orders/tasks.py
from celery import shared_task
from .models import Order
from django.utils.translation import gettext as _


@shared_task
def notify_order_status_change(order_id):
    order = Order.objects.get(id=order_id)
    order.user.notify(
        _("Your order status has been changed to {status}").format(status=order.status)
    )
