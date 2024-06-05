# profiles/mutations.py
import graphene
from .models import Profile
from .types import ProfileType
from django.core.exceptions import ValidationError


class CreateProfile(graphene.Mutation):
    profile = graphene.Field(ProfileType)

    class Arguments:
        user_id = graphene.Int(required=True)
        bio = graphene.String()

    def mutate(self, info, user_id, bio=None):
        profile = Profile(user_id=user_id, bio=bio)
        try:
            profile.full_clean()
            profile.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return CreateProfile(profile=profile)


class UpdateProfile(graphene.Mutation):
    profile = graphene.Field(ProfileType)

    class Arguments:
        id = graphene.Int(required=True)
        bio = graphene.String()

    def mutate(self, info, id, bio=None):
        profile = Profile.objects.get(pk=id)
        if bio:
            profile.bio = bio
        try:
            profile.full_clean()
            profile.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return UpdateProfile(profile=profile)


class DeleteProfile(graphene.Mutation):
    profile = graphene.Field(ProfileType)

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        profile = Profile.objects.get(pk=id)
        profile.delete()
        return DeleteProfile(profile=profile)
