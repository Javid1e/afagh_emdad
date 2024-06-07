# profiles/schema.py
import graphene
from graphene_django import DjangoObjectType
from .models import Profile
from .mutations import CreateProfile, UpdateProfile, DeleteProfile
from .types import ProfileType


class Query(graphene.ObjectType):
    all_profiles = graphene.List(ProfileType)
    profile = graphene.Field(ProfileType, id=graphene.Int())

    def resolve_all_profiles(self, info, **kwargs):
        return Profile.objects.all()

    def resolve_profile(self, info, id):
        return Profile.objects.get(pk=id)


class Mutation(graphene.ObjectType):
    create_profile = CreateProfile.Field()
    update_profile = UpdateProfile.Field()
    delete_profile = DeleteProfile.Field()
