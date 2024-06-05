# notifications/schema.py
import graphene
from graphene_django import DjangoObjectType
from .models import Notification
from .mutations import CreateNotification, UpdateNotification, DeleteNotification
from .types import NotificationType


class Query(graphene.ObjectType):
    all_notifications = graphene.List(NotificationType)
    notification = graphene.Field(NotificationType, id=graphene.Int())

    def resolve_all_notifications(self, info, **kwargs):
        return Notification.objects.all()

    def resolve_notification(self, info, id):
        return Notification.objects.get(pk=id)


class Mutation(graphene.ObjectType):
    create_notification = CreateNotification.Field()
    update_notification = UpdateNotification.Field()
    delete_notification = DeleteNotification.Field()
