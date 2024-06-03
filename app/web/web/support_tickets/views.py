from rest_framework import viewsets
from .models import SupportTicket
from .serializers import SupportTicketSerializer


class SupportTicketViewSet(viewsets.ModelViewSet):
    queryset = SupportTicket.objects.all()
    serializer_class = SupportTicketSerializer
