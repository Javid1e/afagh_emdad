# tests/test_roles.py

import pytest
from graphene.test import Client
from config.schema import schema


@pytest.mark.django_db
def test_create_role():
    client = Client(schema)
    mutation = '''
        mutation {
            createRole(name: "Test Role", permissions: []) {
                role {
                    id
                    name
                }
            }
        }
    '''
    executed = client.execute(mutation)
    assert 'errors' not in executed
    assert executed['data']['createRole']['role']['name'] == 'Test Role'


@pytest.mark.django_db
def test_get_roles():
    client = Client(schema)
    query = '''
        query {
            allRoles {
                id
                name
            }
        }
    '''
    executed = client.execute(query)
    assert 'errors' not in executed
    assert isinstance(executed['data']['allRoles'], list)
