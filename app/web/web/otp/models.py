# otp/models.py
from django.db import models
from users.models import User
from .validations import validate_otp_code


class OTP(models.Model):
    user = models.ForeignKey(User, related_name='otps', on_delete=models.CASCADE)
    code = models.CharField(max_length=6, validators=[validate_otp_code])
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def __str__(self):
        return f"OTP for {self.user.username}"
