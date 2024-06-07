# orders/serializers.py
from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'service_type', 'status', 'request_time', 'completion_time', 'location', 'created_at',
                  'updated_at']
