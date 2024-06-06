# reqs/types.py
import graphene
from graphene.types import Scalar
from graphql.language import ast
from graphene_django import DjangoObjectType
from .models import Request


class RequestType(DjangoObjectType):
    class Meta:
        model = Request


class PointType(Scalar):
    @staticmethod
    def serialize(point):
        return {
            'x': point.x,
            'y': point.y,
        }

    @staticmethod
    def parse_literal(node):
        if isinstance(node, ast.ObjectValue):
            return {
                'x': node.fields['x'].value,
                'y': node.fields['y'].value,
            }

    @staticmethod
    def parse_value(value):
        return {
            'x': value['x'],
            'y': value['y'],
        }
