# tests/test_live_location.py

import pytest
from graphene.test import Client
from config.schema import schema


@pytest.mark.django_db
def test_create_live_location():
    client = Client(schema)
    mutation = '''
        mutation {
            createLiveLocation(requestId: 1, location: "POINT(0 0)") {
                liveLocation {
                    id
                    location
                }
            }
        }
    '''
    executed = client.execute(mutation)
    assert 'errors' not in executed
    assert executed['data']['createLiveLocation']['liveLocation']['location'] == 'POINT(0 0)'


@pytest.mark.django_db
def test_get_live_locations():
    client = Client(schema)
    query = '''
        query {
            allLiveLocations {
                id
                location
            }
        }
    '''
    executed = client.execute(query)
    assert 'errors' not in executed
    assert isinstance(executed['data']['allLiveLocations'], list)
