# orders/models.py
from django.db import models
from ..users.models import User


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    service_type = models.CharField(max_length=100)
    status = models.CharField(maxlength=20, choices=STATUS_CHOICES, default='pending')
    request_time = models.DateTimeField()
    completion_time = models.DateTimeField(blank=True, null=True)
    location = models.CharField(maxlength=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} - {self.status}"
