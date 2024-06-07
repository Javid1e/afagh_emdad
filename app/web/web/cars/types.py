from graphene_django import DjangoObjectType
from .models import Car


class CarType(DjangoObjectType):
    class Meta:
        model = Car
