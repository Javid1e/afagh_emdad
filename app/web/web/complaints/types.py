from graphene_django import DjangoObjectType
from .models import Complaint


class ComplaintType(DjangoObjectType):
    class Meta:
        model = Complaint
