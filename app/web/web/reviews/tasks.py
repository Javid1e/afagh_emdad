# reviews/tasks.py
from celery import shared_task
from .models import Review
from notifications.models import Notification
from django.utils.translation import gettext as _


@shared_task
def notify_review_submitted(review_id):
    review = Review.objects.get(id=review_id)
    Notification.objects.create(
        user=review.client,
        type='push',
        message=_('Your review has been submitted successfully.')
    )
