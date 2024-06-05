# reqs/converters.py
import graphene
from graphene_django.converter import convert_django_field
from django.contrib.gis.db.models import PointField
from graphene.types import Scalar
from graphql.language import ast


class PointType(Scalar):
    """PointType to handle PointField serialization and deserialization."""

    @staticmethod
    def serialize(point):
        return str(point)

    @staticmethod
    def parse_literal(node):
        if isinstance(node, ast.StringValue):
            return node.value

    @staticmethod
    def parse_value(value):
        return value


@convert_django_field.register(PointField)
def convert_point_field_to_string(field, registry=None):
    return PointType(description=field.help_text, required=not field.null)
