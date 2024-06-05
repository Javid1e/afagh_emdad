# media/mutations.py
import graphene
from .models import Media
from .types import MediaType
from django.core.exceptions import ValidationError


class CreateMedia(graphene.Mutation):
    media = graphene.Field(MediaType)

    class Arguments:
        file = graphene.String(required=True)
        content_object = graphene.String()

    def mutate(self, info, file, content_object=None):
        media = Media(file=file, content_object=content_object)
        try:
            media.full_clean()
            media.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return CreateMedia(media=media)


class UpdateMedia(graphene.Mutation):
    media = graphene.Field(MediaType)

    class Arguments:
        id = graphene.Int(required=True)
        file = graphene.String()
        content_object = graphene.String()

    def mutate(self, info, id, file=None, content_object=None):
        media = Media.objects.get(pk=id)
        if file:
            media.file = file
        if content_object:
            media.content_object = content_object
        try:
            media.full_clean()
            media.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return UpdateMedia(media=media)


class DeleteMedia(graphene.Mutation):
    media = graphene.Field(MediaType)

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        media = Media.objects.get(pk=id)
        media.delete()
        return DeleteMedia(media=media)
