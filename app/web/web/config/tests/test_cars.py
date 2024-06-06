# tests/test_cars.py

import pytest
from graphene.test import Client
from config.schema import schema


@pytest.mark.django_db
def test_create_car():
    client = Client(schema)
    mutation = '''
        mutation {
            createCar(userId: 1, make: "Test Make", model: "Test Model") {
                car {
                    id
                    make
                    model
                }
            }
        }
    '''
    executed = client.execute(mutation)
    assert 'errors' not in executed
    assert executed['data']['createCar']['car']['make'] == 'Test Make'
    assert executed['data']['createCar']['car']['model'] == 'Test Model'


@pytest.mark.django_db
def test_get_cars():
    client = Client(schema)
    query = '''
        query {
            allCars {
                id
                make
                model
            }
        }
    '''
    executed = client.execute(query)
    assert 'errors' not in executed
    assert isinstance(executed['data']['allCars'], list)
