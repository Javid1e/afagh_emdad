# certificates/mutations.py
import graphene
from .models import Certificate
from .types import CertificateType
from django.core.exceptions import ValidationError


class CreateCertificate(graphene.Mutation):
    certificate = graphene.Field(CertificateType)

    class Arguments:
        user_id = graphene.Int(required=True)
        title = graphene.String(required=True)
        description = graphene.String()

    def mutate(self, info, user_id, title, description=None):
        certificate = Certificate(user_id=user_id, title=title, description=description)
        try:
            certificate.full_clean()
            certificate.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return CreateCertificate(certificate=certificate)


class UpdateCertificate(graphene.Mutation):
    certificate = graphene.Field(CertificateType)

    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String()
        description = graphene.String()

    def mutate(self, info, id, title=None, description=None):
        certificate = Certificate.objects.get(pk=id)
        if title:
            certificate.title = title
        if description:
            certificate.description = description
        try:
            certificate.full_clean()
            certificate.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return UpdateCertificate(certificate=certificate)


class DeleteCertificate(graphene.Mutation):
    certificate = graphene.Field(CertificateType)

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        certificate = Certificate.objects.get(pk=id)
        certificate.delete()
        return DeleteCertificate(certificate=certificate)
