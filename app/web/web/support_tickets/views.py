# support_tickets/views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import gettext as _
from .models import SupportTicket
from .serializers import SupportTicketSerializer


class SupportTicketViewSet(viewsets.ModelViewSet):
    queryset = SupportTicket.objects.all()
    serializer_class = SupportTicketSerializer

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            response.data['message'] = _("Support ticket created successfully")
            return response
        except Exception as e:
            return Response({'error': _("Error creating support ticket"), 'details': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            response.data['message'] = _("Support ticket updated successfully")
            return response
        except Exception as e:
            return Response({'error': _("Error updating support ticket"), 'details': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            super().destroy(request, *args, **kwargs)
            return Response({'message': _("Support ticket deleted successfully")}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': _("Error deleting support ticket"), 'details': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'], url_path='close')
    def close_ticket(self, request, pk=None):
        try:
            ticket = self.get_object()
            ticket.status = 'closed'
            ticket.save()
            return Response({'message': _("Support ticket closed")}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': _("Error closing support ticket"), 'details': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)
