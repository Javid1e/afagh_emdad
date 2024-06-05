from graphene_django import DjangoObjectType
from .models import FAQ


class FAQType(DjangoObjectType):
    class Meta:
        model = FAQ
