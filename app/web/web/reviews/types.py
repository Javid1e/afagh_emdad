from graphene_django import DjangoObjectType
from .models import Review


class ReviewType(DjangoObjectType):
    class Meta:
        model = Review
