# support_tickets/schema.py
import graphene
from graphene_django import DjangoObjectType
from .models import SupportTicket
from .mutations import CreateSupportTicket, UpdateSupportTicket, DeleteSupportTicket
from .types import SupportTicketType


class Query(graphene.ObjectType):
    all_support_tickets = graphene.List(SupportTicketType)
    support_ticket = graphene.Field(SupportTicketType, id=graphene.Int())

    def resolve_all_support_tickets(self, info, **kwargs):
        return SupportTicket.objects.all()

    def resolve_support_ticket(self, info, id):
        return SupportTicket.objects.get(pk=id)


class Mutation(graphene.ObjectType):
    create_support_ticket = CreateSupportTicket.Field()
    update_support_ticket = UpdateSupportTicket.Field()
    delete_support_ticket = DeleteSupportTicket.Field()
