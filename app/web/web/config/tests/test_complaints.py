# tests/test_complaints.py

import pytest
from graphene.test import Client
from config.schema import schema


@pytest.mark.django_db
def test_create_complaint():
    client = Client(schema)
    mutation = '''
        mutation {
            createComplaint(userId: 1, description: "This is a test complaint") {
                complaint {
                    id
                    description
                    status
                }
            }
        }
    '''
    executed = client.execute(mutation)
    assert 'errors' not in executed
    assert executed['data']['createComplaint']['complaint']['description'] == 'This is a test complaint'
    assert executed['data']['createComplaint']['complaint']['status'] == 'pending'


@pytest.mark.django_db
def test_get_complaints():
    client = Client(schema)
    query = '''
        query {
            allComplaints {
                id
                description
                status
            }
        }
    '''
    executed = client.execute(query)
    assert 'errors' not in executed
    assert isinstance(executed['data']['allComplaints'], list)


@pytest.mark.django_db
def test_update_complaint():
    client = Client(schema)
    create_mutation = '''
        mutation {
            createComplaint(userId: 1, description: "This is a test complaint") {
                complaint {
                    id
                    description
                    status
                }
            }
        }
    '''
    executed = client.execute(create_mutation)
    complaint_id = executed['data']['createComplaint']['complaint']['id']

    update_mutation = f'''
        mutation {{
            updateComplaint(id: {complaint_id}, description: "Updated complaint description", status: "resolved") {{
                complaint {{
                    id
                    description
                    status
                }}
            }}
        }}
    '''
    executed = client.execute(update_mutation)
    assert 'errors' not in executed
    assert executed['data']['updateComplaint']['complaint']['description'] == 'Updated complaint description'
    assert executed['data']['updateComplaint']['complaint']['status'] == 'resolved'


@pytest.mark.django_db
def test_delete_complaint():
    client = Client(schema)
    create_mutation = '''
        mutation {
            createComplaint(userId: 1, description: "This is a test complaint") {
                complaint {
                    id
                    description
                    status
                }
            }
        }
    '''
    executed = client.execute(create_mutation)
    complaint_id = executed['data']['createComplaint']['complaint']['id']

    delete_mutation = f'''
        mutation {{
            deleteComplaint(id: {complaint_id}) {{
                complaint {{
                    id
                    description
                }}
            }}
        }}
    '''
    executed = client.execute(delete_mutation)
    assert 'errors' not in executed
    assert executed['data']['deleteComplaint']['complaint']['id'] == complaint_id
