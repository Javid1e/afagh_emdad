import graphene
from graphene_django import DjangoObjectType
from .models import FAQ
from .mutations import CreateFAQ, UpdateFAQ, DeleteFAQ
from .types import FAQType


class Query(graphene.ObjectType):
    all_faqs = graphene.List(FAQType)
    faq = graphene.Field(FAQType, id=graphene.Int())

    def resolve_all_faqs(self, info, **kwargs):
        return FAQ.objects.all()

    def resolve_faq(self, info, id):
        return FAQ.objects.get(pk=id)


class Mutation(graphene.ObjectType):
    create_faq = CreateFAQ.Field()
    update_faq = UpdateFAQ.Field()
    delete_faq = DeleteFAQ.Field()
