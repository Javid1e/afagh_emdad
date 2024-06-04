# certificates/views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import gettext as _
from .models import Certificate
from .serializers import CertificateSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            response.data['message'] = _("Certificate created successfully")
            return response
        except Exception as e:
            return Response({'error': _("Error creating certificate"), 'details': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            response.data['message'] = _("Certificate updated successfully")
            return response
        except Exception as e:
            return Response({'error': _("Error updating certificate"), 'details': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            super().destroy(request, *args, **kwargs)
            return Response({'message': _("Certificate deleted successfully")}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': _("Error deleting certificate"), 'details': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'], url_path='details')
    def certificate_details(self, request, pk=None):
        certificate = self.get_object()
        serializer = CertificateSerializer(certificate)
        return Response(serializer.data)
