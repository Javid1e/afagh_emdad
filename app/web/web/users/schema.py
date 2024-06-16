import graphene
from graphene_django import DjangoObjectType
from users.models import User
from users.types import UserType
from users.mutations import CreateUser, UpdateUser, DeleteUser, LoginUser, LogoutUser
from users.queries import Query as UserQuery


class Query(UserQuery, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()
    login_user = LoginUser.Field()
    logout_user = LogoutUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
