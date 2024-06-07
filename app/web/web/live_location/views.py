# live_location/views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import gettext as _
from .models import LiveLocation
from .serializers import LiveLocationSerializer


class LiveLocationViewSet(viewsets.ModelViewSet):
    queryset = LiveLocation.objects.all()
    serializer_class = LiveLocationSerializer

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            response.data['message'] = _("Live location created successfully")
            return response
        except Exception as e:
            return Response({'error': _("Error creating live location"), 'details': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            response.data['message'] = _("Live location updated successfully")
            return response
        except Exception as e:
            return Response({'error': _("Error updating live location"), 'details': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            super().destroy(request, *args, **kwargs)
            return Response({'message': _("Live location deleted successfully")}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': _("Error deleting live location"), 'details': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)
