# certificates/tasks.py
from celery import shared_task
from .models import Certificate
from ..users.models import User


@shared_task
def notify_certificate(user_id, certificate_id):
    user = User.objects.get(id=user_id)
    certificate = Certificate.objects.get(id=certificate_id)
    user.notify(
        _("You have received a certificate: {name}").format(name=certificate.name)
    )
