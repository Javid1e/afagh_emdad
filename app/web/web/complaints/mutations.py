# complaints/mutations.py
import graphene
from .models import Complaint
from .types import ComplaintType
from django.core.exceptions import ValidationError


class CreateComplaint(graphene.Mutation):
    complaint = graphene.Field(ComplaintType)

    class Arguments:
        user_id = graphene.Int(required=True)
        description = graphene.String(required=True)

    def mutate(self, info, user_id, description):
        complaint = Complaint(user_id=user_id, description=description)
        try:
            complaint.full_clean()
            complaint.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return CreateComplaint(complaint=complaint)


class UpdateComplaint(graphene.Mutation):
    complaint = graphene.Field(ComplaintType)

    class Arguments:
        id = graphene.Int(required=True)
        description = graphene.String()

    def mutate(self, info, id, description=None):
        complaint = Complaint.objects.get(pk=id)
        if description:
            complaint.description = description
        try:
            complaint.full_clean()
            complaint.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return UpdateComplaint(complaint=complaint)


class DeleteComplaint(graphene.Mutation):
    complaint = graphene.Field(ComplaintType)

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        complaint = Complaint.objects.get(pk=id)
        complaint.delete()
        return DeleteComplaint(complaint=complaint)
