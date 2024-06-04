# otp/views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import gettext as _
from .models import OTP
from .serializers import OTPSerializer
from .tasks import send_otp


class OTPViewSet(viewsets.ModelViewSet):
    queryset = OTP.objects.all()
    serializer_class = OTPSerializer

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            send_otp.delay(response.data['id'])
            response.data['message'] = _("OTP created successfully")
            return response
        except Exception as e:
            return Response({'error': _("Error creating OTP"), 'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            response.data['message'] = _("OTP updated successfully")
            return response
        except Exception as e:
            return Response({'error': _("Error updating OTP"), 'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            super().destroy(request, *args, **kwargs)
            return Response({'message': _("OTP deleted successfully")}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': _("Error deleting OTP"), 'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='verify')
    def verify_otp(self, request):
        user = request.data.get('user')
        code = request.data.get('code')
        otp = OTP.objects.filter(user=user, code=code).first()
        if otp:
            if otp.expires_at < timezone.now():
                return Response({'error': _("OTP expired")}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'message': _("Login successful")}, status=status.HTTP_200_OK)
        return Response({'error': _("Invalid OTP")}, status=status.HTTP_400_BAD_REQUEST)
