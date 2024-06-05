from graphene_django import DjangoObjectType
from .models import SupportTicket


class SupportTicketType(DjangoObjectType):
    class Meta:
        model = SupportTicket
