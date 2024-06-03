from rest_framework import viewsets
from .models import LiveLocation
from .serializers import LiveLocationSerializer


class LiveLocationViewSet(viewsets.ModelViewSet):
    queryset = LiveLocation.objects.all()
    serializer_class = LiveLocationSerializer
