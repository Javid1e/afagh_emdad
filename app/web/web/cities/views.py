# cities/views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import gettext as _
from .models import City
from .serializers import CitySerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            response.data['message'] = _("City created successfully")
            return response
        except Exception as e:
            return Response({'error': _("Error creating city"), 'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            response.data['message'] = _("City updated successfully")
            return response
        except Exception as e:
            return Response({'error': _("Error updating city"), 'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            super().destroy(request, *args, **kwargs)
            return Response({'message': _("City deleted successfully")}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': _("Error deleting city"), 'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'], url_path='details')
    def city_details(self, request, pk=None):
        city = self.get_object()
        serializer = CitySerializer(city)
        return Response(serializer.data)
