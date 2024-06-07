# requests/views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import gettext as _
from .models import Request
from .serializers import RequestSerializer


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            response.data['message'] = _("Request created successfully")
            return response
        except Exception as e:
            return Response({'error': _("Error creating request"), 'details': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            response.data['message'] = _("Request updated successfully")
            return response
        except Exception as e:
            return Response({'error': _("Error updating request"), 'details': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            super().destroy(request, *args, **kwargs)
            return Response({'message': _("Request deleted successfully")}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': _("Error deleting request"), 'details': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'], url_path='accept')
    def accept_request(self, request, pk=None):
        try:
            req = self.get_object()
            req.status = 'accepted'
            req.save()
            return Response({'message': _("Request accepted")}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': _("Error accepting request"), 'details': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'], url_path='cancel')
    def cancel_request(self, request, pk=None):
        try:
            req = self.get_object()
            req.status = 'cancelled'
            req.save()
            return Response({'message': _("Request cancelled")}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': _("Error cancelling request"), 'details': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)
