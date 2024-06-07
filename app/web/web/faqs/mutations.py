# faqs/mutations.py
import graphene
from .models import FAQ
from .types import FAQType
from django.core.exceptions import ValidationError


class CreateFAQ(graphene.Mutation):
    faq = graphene.Field(FAQType)

    class Arguments:
        question = graphene.String(required=True)
        answer = graphene.String(required=True)

    def mutate(self, info, question, answer):
        faq = FAQ(question=question, answer=answer)
        try:
            faq.full_clean()
            faq.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return CreateFAQ(faq=faq)


class UpdateFAQ(graphene.Mutation):
    faq = graphene.Field(FAQType)

    class Arguments:
        id = graphene.Int(required=True)
        question = graphene.String()
        answer = graphene.String()

    def mutate(self, info, id, question=None, answer=None):
        faq = FAQ.objects.get(pk=id)
        if question:
            faq.question = question
        if answer:
            faq.answer = answer
        try:
            faq.full_clean()
            faq.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return UpdateFAQ(faq=faq)


class DeleteFAQ(graphene.Mutation):
    faq = graphene.Field(FAQType)

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        faq = FAQ.objects.get(pk=id)
        faq.delete()
        return DeleteFAQ(faq=faq)
