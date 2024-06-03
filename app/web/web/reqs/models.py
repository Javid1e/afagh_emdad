# requests/models.py
from django.contrib.gis.db import models as geomodels
from django.db import models
from ..users.models import User


class Request(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    client = models.ForeignKey(User, related_name='requests_as_client', on_delete=models.CASCADE)
    rescuer = models.ForeignKey(User, related_name='requests_as_rescuer', on_delete=models.SET_NULL, null=True,
                                blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    location = geomodels.PointField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Request {self.id} - {self.status}"
