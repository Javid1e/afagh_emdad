# notifications/views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import gettext as _
from .models import Notification
from .serializers import NotificationSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            response.data['message'] = _("Notification created successfully")
            return response
        except Exception as e:
            return Response({'error': _("Error creating notification"), 'details': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            response.data['message'] = _("Notification updated successfully")
            return response
        except Exception as e:
            return Response({'error': _("Error updating notification"), 'details': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            super().destroy(request, *args, **kwargs)
            return Response({'message': _("Notification deleted successfully")}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': _("Error deleting notification"), 'details': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'], url_path='mark-as-read')
    def mark_as_read(self, request, pk=None):
        try:
            notification = self.get_object()
            notification.read_status = True
            notification.save()
            return Response({'message': _("Notification marked as read")}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': _("Error marking notification as read"), 'details': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)
