# notifications/models.py
from django.db import models
from users.models import User
from .validations import validate_notification_type


class Notification(models.Model):
    TYPE_CHOICES = [('email', 'Email'), ('sms', 'SMS'), ('push', 'Push')]
    user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, validators=[validate_notification_type])
    message = models.TextField()
    read_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification {self.id} for {self.user.username}"
