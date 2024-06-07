# support_tickets/models.py
from django.db import models
from users.models import User
from .validations import validate_subject, validate_status


class SupportTicket(models.Model):
    STATUS_CHOICES = [('open', 'Open'), ('in_progress', 'In Progress'), ('closed', 'Closed')]
    user = models.ForeignKey(User, related_name='support_tickets', on_delete=models.CASCADE)
    subject = models.CharField(max_length=200, validators=[validate_subject])
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open', validators=[validate_status])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Support Ticket {self.id} - {self.status}"
