# notifications/serializers.py
from rest_framework import serializers
from push_notifications.models import GCMDevice, APNSDevice, WebPushDevice


class GCMDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = GCMDevice
        fields = ['id', 'user', 'registration_id', 'active', 'date_created']


class APNSDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = APNSDevice
        fields = ['id', 'user', 'registration_id', 'active', 'date_created']


class WebPushDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebPushDevice
        fields = ['id', 'user', 'registration_id', 'active', 'date_created']
