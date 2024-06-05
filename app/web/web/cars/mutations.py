# cars/mutations.py
import graphene
from .models import Car
from .types import CarType
from django.core.exceptions import ValidationError


class CreateCar(graphene.Mutation):
    car = graphene.Field(CarType)

    class Arguments:
        owner_id = graphene.Int(required=True)
        make = graphene.String(required=True)
        model = graphene.String(required=True)
        year = graphene.Int(required=True)
        license_plate = graphene.String(required=True)

    def mutate(self, info, owner_id, make, model, year, license_plate):
        car = Car(owner_id=owner_id, make=make, model=model, year=year, license_plate=license_plate)
        try:
            car.full_clean()
            car.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return CreateCar(car=car)


class UpdateCar(graphene.Mutation):
    car = graphene.Field(CarType)

    class Arguments:
        id = graphene.Int(required=True)
        make = graphene.String()
        model = graphene.String()
        year = graphene.Int()
        license_plate = graphene.String()

    def mutate(self, info, id, make=None, model=None, year=None, license_plate=None):
        car = Car.objects.get(pk=id)
        if make:
            car.make = make
        if model:
            car.model = model
        if year:
            car.year = year
        if license_plate:
            car.license_plate = license_plate
        try:
            car.full_clean()
            car.save()
        except ValidationError as e:
            raise Exception(e.message_dict)
        return UpdateCar(car=car)


class DeleteCar(graphene.Mutation):
    car = graphene.Field(CarType)

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        car = Car.objects.get(pk=id)
        car.delete()
        return DeleteCar(car=car)
