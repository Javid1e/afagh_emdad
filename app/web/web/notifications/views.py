# notifications/views.py
from rest_framework import viewsets
from push_notifications.models import GCMDevice, APNSDevice, WebPushDevice
from .serializers import GCMDeviceSerializer, APNSDeviceSerializer, WebPushDeviceSerializer


class GCMDeviceViewSet(viewsets.ModelViewSet):
    queryset = GCMDevice.objects.all()
    serializer_class = GCMDeviceSerializer


class APNSDeviceViewSet(viewsets.ModelViewSet):
    queryset = APNSDevice.objects.all()
    serializer_class = APNSDeviceSerializer


class WebPushDeviceViewSet(viewsets.ModelViewSet):
    queryset = WebPushDevice.objects.all()
    serializer_class = WebPushDeviceSerializer
