# tests/test_services.py

import pytest
from graphene.test import Client
from config.schema import schema


@pytest.mark.django_db
def test_create_service():
    client = Client(schema)
    mutation = '''
        mutation {
            createService(name: "Test Service", description: "Service Description") {
                service {
                    id
                    name
                    description
                }
            }
        }
    '''
    executed = client.execute(mutation)
    assert 'errors' not in executed
    assert executed['data']['createService']['service']['name'] == 'Test Service'
    assert executed['data']['createService']['service']['description'] == 'Service Description'


@pytest.mark.django_db
def test_get_services():
    client = Client(schema)
    query = '''
        query {
            allServices {
                id
                name
                description
            }
        }
    '''
    executed = client.execute(query)
    assert 'errors' not in executed
    assert isinstance(executed['data']['allServices'], list)
