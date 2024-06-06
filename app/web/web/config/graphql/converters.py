# config/graphql/converters.py
from graphene import ObjectType, Float
from graphene_django.converter import convert_django_field
from django.contrib.gis.db.models import PointField


class PointType(ObjectType):
    latitude = Float()
    longitude = Float()

    def resolve_latitude(self, info):
        return self.y

    def resolve_longitude(self, info):
        return self.x


@convert_django_field.register(PointField)
def convert_point_field_to_graphene_field(field, registry=None):
    return PointType()
