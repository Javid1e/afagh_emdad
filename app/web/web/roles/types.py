from graphene_django import DjangoObjectType
from .models import Role


class RoleType(DjangoObjectType):
    class Meta:
        model = Role
