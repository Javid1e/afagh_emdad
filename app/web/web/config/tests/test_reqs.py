# tests/test_reqs.py

import pytest
from graphene.test import Client
from config.schema import schema


@pytest.mark.django_db
def test_create_request():
    client = Client(schema)
    mutation = '''
        mutation {
            createRequest(clientId: 1, description: "This is a test request", location: "POINT (12.9715987 77.5945627)") {
                request {
                    id
                    description
                    status
                }
            }
        }
    '''
    executed = client.execute(mutation)
    assert 'errors' not in executed
    assert executed['data']['createRequest']['request']['description'] == 'This is a test request'
    assert executed['data']['createRequest']['request']['status'] == 'pending'


@pytest.mark.django_db
def test_get_requests():
    client = Client(schema)
    query = '''
        query {
            allRequests {
                id
                description
                status
            }
        }
    '''
    executed = client.execute(query)
    assert 'errors' not in executed
    assert isinstance(executed['data']['allRequests'], list)


@pytest.mark.django_db
def test_update_request():
    client = Client(schema)
    create_mutation = '''
        mutation {
            createRequest(clientId: 1, description: "This is a test request", location: "POINT (12.9715987 77.5945627)") {
                request {
                    id
                    description
                    status
                }
            }
        }
    '''
    executed = client.execute(create_mutation)
    request_id = executed['data']['createRequest']['request']['id']

    update_mutation = f'''
        mutation {{
            updateRequest(id: {request_id}, description: "Updated request description", status: "accepted") {{
                request {{
                    id
                    description
                    status
                }}
            }}
        }}
    '''
    executed = client.execute(update_mutation)
    assert 'errors' not in executed
    assert executed['data']['updateRequest']['request']['description'] == 'Updated request description'
    assert executed['data']['updateRequest']['request']['status'] == 'accepted'


@pytest.mark.django_db
def test_delete_request():
    client = Client(schema)
    create_mutation = '''
        mutation {
            createRequest(clientId: 1, description: "This is a test request", location: "POINT (12.9715987 77.5945627)") {
                request {
                    id
                    description
                    status
                }
            }
        }
    '''
    executed = client.execute(create_mutation)
    request_id = executed['data']['createRequest']['request']['id']

    delete_mutation = f'''
        mutation {{
            deleteRequest(id: {request_id}) {{
                request {{
                    id
                    description
                }}
            }}
        }}
    '''
    executed = client.execute(delete_mutation)
    assert 'errors' not in executed
    assert executed['data']['deleteRequest']['request']['id'] == request_id
