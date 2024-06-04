# achievements/tasks.py
from celery import shared_task
from .models import Achievement
from ..users.models import User


@shared_task
def notify_achievement(user_id, achievement_id):
    user = User.objects.get(id=user_id)
    achievement = Achievement.objects.get(id=achievement_id)
    user.notify(
        _("You have achieved {title}!").format(title=achievement.title)
    )
