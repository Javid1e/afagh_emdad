from graphene_django import DjangoObjectType
from .models import Notification


class NotificationType(DjangoObjectType):
    class Meta:
        model = Notification
