# certificates/schema.py
import graphene
from graphene_django import DjangoObjectType
from .models import Certificate
from .mutations import CreateCertificate, UpdateCertificate, DeleteCertificate
from .types import CertificateType


class Query(graphene.ObjectType):
    all_certificates = graphene.List(CertificateType)
    certificate = graphene.Field(CertificateType, id=graphene.Int())

    def resolve_all_certificates(self, info, **kwargs):
        return Certificate.objects.all()

    def resolve_certificate(self, info, id):
        return Certificate.objects.get(pk=id)


class Mutation(graphene.ObjectType):
    create_certificate = CreateCertificate.Field()
    update_certificate = UpdateCertificate.Field()
    delete_certificate = DeleteCertificate.Field()
