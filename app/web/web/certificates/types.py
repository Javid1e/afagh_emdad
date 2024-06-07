from graphene_django import DjangoObjectType
from .models import Certificate


class CertificateType(DjangoObjectType):
    class Meta:
        model = Certificate
