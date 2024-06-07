# media/tasks.py
from celery import shared_task
from .models import Media


@shared_task
def clean_unused_media():
    # //Todo Logic to clean up unused media files
    pass
