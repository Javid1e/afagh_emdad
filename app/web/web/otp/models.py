# otp/models.py
from django.db import models
from ..users.models import User


class OTP(models.Model):
    user = models.ForeignKey(User, related_name='otps', on_delete=models.CASCADE)
    code = models.CharField(maxlength=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def __str__(self):
        return f"OTP for {self.user.username}"
