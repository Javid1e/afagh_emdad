from graphene_django import DjangoObjectType
from .models import LiveLocation


class LiveLocationType(DjangoObjectType):
    class Meta:
        model = LiveLocation
