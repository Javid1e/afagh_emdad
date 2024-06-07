from graphene_django import DjangoObjectType
from .models import Service


class ServiceType(DjangoObjectType):
    class Meta:
        model = Service
