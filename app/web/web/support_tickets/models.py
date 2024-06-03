# support_tickets/models.py
from django.db import models
from ..users.models import User


class SupportTicket(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
    ]
    user = models.ForeignKey(User, related_name='support_tickets', on_delete=models.CASCADE)
    subject = models.CharField(maxlength=200)
    description = models.TextField()
    status = models.CharField(maxlength=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Support Ticket {self.id} - {self.status}"
