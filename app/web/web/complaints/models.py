# complaints/models.py
from django.db import models
from ..users.models import User
from ..orders.models import Order


class Complaint(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]
    user = models.ForeignKey(User, related_name='complaints', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name='complaints', on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(maxlength=20, choices=STATUS_CHOICES, default='open')
    resolution = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Complaint {self.id} - {self.status}"
