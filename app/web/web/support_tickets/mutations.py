# support_tickets/mutations.py
import graphene
from .models import SupportTicket
from .types import SupportTicketType
from django.core.exceptions import ValidationError


class CreateSupportTicket(graphene.Mutation):
    support_ticket = graphene.Field(SupportTicketType)

    class Arguments:
        user_id = graphene.Int(required=True)
        subject = graphene.String(required=True)
        message = graphene.String(required=True)

    def mutate(self, info, user_id, subject, message):
        support_ticket = SupportTicket(user_id=user_id, subject=subject, message=message)
        try:
            support_ticket.full_clean()
            support_ticket.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return CreateSupportTicket(support_ticket=support_ticket)


class UpdateSupportTicket(graphene.Mutation):
    support_ticket = graphene.Field(SupportTicketType)

    class Arguments:
        id = graphene.Int(required=True)
        subject = graphene.String()
        message = graphene.String()

    def mutate(self, info, id, subject=None, message=None):
        support_ticket = SupportTicket.objects.get(pk=id)
        if subject:
            support_ticket.subject = subject
        if message:
            support_ticket.message = message
        try:
            support_ticket.full_clean()
            support_ticket.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return UpdateSupportTicket(support_ticket=support_ticket)


class DeleteSupportTicket(graphene.Mutation):
    support_ticket = graphene.Field(SupportTicketType)

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        support_ticket = SupportTicket.objects.get(pk=id)
        support_ticket.delete()
        return DeleteSupportTicket(support_ticket=support_ticket)
