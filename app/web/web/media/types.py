from graphene_django import DjangoObjectType
from .models import Media


class MediaType(DjangoObjectType):
    class Meta:
        model = Media
