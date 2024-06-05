from graphene_django import DjangoObjectType
from .models import City


class CityType(DjangoObjectType):
    class Meta:
        model = City
