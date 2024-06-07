# complaints/tasks.py
from celery import shared_task
from .models import Complaint
from django.utils.translation import gettext as _


@shared_task
def notify_complaint_status_change(complaint_id):
    complaint = Complaint.objects.get(id=complaint_id)
    complaint.user.notify(
        _("Your complaint status has been changed to {status}").format(status=complaint.status)
    )
