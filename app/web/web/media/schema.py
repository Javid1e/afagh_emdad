import graphene
from graphene_django import DjangoObjectType
from .models import Media
from .mutations import CreateMedia, UpdateMedia, DeleteMedia
from .types import MediaType


class Query(graphene.ObjectType):
    all_media = graphene.List(MediaType)
    media = graphene.Field(MediaType, id=graphene.Int())

    def resolve_all_media(self, info, **kwargs):
        return Media.objects.all()

    def resolve_media(self, info, id):
        return Media.objects.get(pk=id)


class Mutation(graphene.ObjectType):
    create_media = CreateMedia.Field()
    update_media = UpdateMedia.Field()
    delete_media = DeleteMedia.Field()
