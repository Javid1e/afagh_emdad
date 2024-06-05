from graphene_django import DjangoObjectType
from .models import Request


class RequestType(DjangoObjectType):
    class Meta:
        model = Request
