from rest_framework import viewsets
from .models import OTP
from .serializers import OTPSerializer


class OTPViewSet(viewsets.ModelViewSet):
    queryset = OTP.objects.all()
    serializer_class = OTPSerializer
