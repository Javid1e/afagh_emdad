from graphene_django import DjangoObjectType
from .models import Achievement


class AchievementType(DjangoObjectType):
    class Meta:
        model = Achievement
