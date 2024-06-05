# complaints/schema.py
import graphene
from graphene_django import DjangoObjectType
from .models import Complaint
from .mutations import CreateComplaint, UpdateComplaint, DeleteComplaint
from .types import ComplaintType


class Query(graphene.ObjectType):
    all_complaints = graphene.List(ComplaintType)
    complaint = graphene.Field(ComplaintType, id=graphene.Int())

    def resolve_all_complaints(self, info, **kwargs):
        return Complaint.objects.all()

    def resolve_complaint(self, info, id):
        return Complaint.objects.get(pk=id)


class Mutation(graphene.ObjectType):
    create_complaint = CreateComplaint.Field()
    update_complaint = UpdateComplaint.Field()
    delete_complaint = DeleteComplaint.Field()
