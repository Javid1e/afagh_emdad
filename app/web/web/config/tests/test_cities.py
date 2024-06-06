# tests/test_cities.py
import pytest
from graphene.test import Client
from config.schema import schema


@pytest.mark.django_db
def test_create_city():
    client = Client(schema)
    mutation = '''
        mutation {
            createCity(name: "Test City") {
                city {
                    id
                    name
                }
            }
        }
    '''
    executed = client.execute(mutation)
    assert 'errors' not in executed
    assert executed['data']['createCity']['city']['name'] == 'Test City'


@pytest.mark.django_db
def test_get_cities():
    client = Client(schema)
    query = '''
        query {
            allCities {
                id
                name
            }
        }
    '''
    executed = client.execute(query)
    assert 'errors' not in executed
    assert isinstance(executed['data']['allCities'], list)
