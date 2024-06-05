import graphene
from graphene_django import DjangoObjectType
from .models import User
from .mutations import CreateUser, UpdateUser, DeleteUser
from .types import UserType


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.Int())

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_user(self, info, id):
        return User.objects.get(pk=id)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()
