# roles/schema.py
import graphene
from graphene_django import DjangoObjectType
from .models import Role
from .mutations import CreateRole, UpdateRole, DeleteRole
from .types import RoleType


class Query(graphene.ObjectType):
    all_roles = graphene.List(RoleType)
    role = graphene.Field(RoleType, id=graphene.Int())

    def resolve_all_roles(self, info, **kwargs):
        return Role.objects.all()

    def resolve_role(self, info, id):
        return Role.objects.get(pk=id)


class Mutation(graphene.ObjectType):
    create_role = CreateRole.Field()
    update_role = UpdateRole.Field()
    delete_role = DeleteRole.Field()
