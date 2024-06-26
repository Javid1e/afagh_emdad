# payments/models.py
from django.db import models
from reqs.models import Request
from .validations import validate_amount, validate_status


class Payment(models.Model):
    STATUS_CHOICES = [('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')]
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_amount])
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', validators=[validate_status])
    transaction_details = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment {self.id} - {self.status}"
