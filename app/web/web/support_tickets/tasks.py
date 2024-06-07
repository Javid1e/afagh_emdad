# support_tickets/tasks.py
from celery import shared_task
from .models import SupportTicket
from django.utils.translation import gettext as _


@shared_task
def notify_support_ticket_update(ticket_id):
    ticket = SupportTicket.objects.get(id=ticket_id)
    ticket.user.notify(
        _("Your support ticket has been updated.")
    )
