# tests/test_profiles.py

import pytest
from graphene.test import Client
from config.schema import schema


@pytest.mark.django_db
def test_create_profile():
    client = Client(schema)
    mutation = '''
        mutation {
            createProfile(userId: 1, bio: "This is a test bio", location: "Test Location") {
                profile {
                    id
                    bio
                    location
                }
            }
        }
    '''
    executed = client.execute(mutation)
    assert 'errors' not in executed
    assert executed['data']['createProfile']['profile']['bio'] == 'This is a test bio'
    assert executed['data']['createProfile']['profile']['location'] == 'Test Location'


@pytest.mark.django_db
def test_get_profiles():
    client = Client(schema)
    query = '''
        query {
            allProfiles {
                id
                bio
                location
            }
        }
    '''
    executed = client.execute(query)
    assert 'errors' not in executed
    assert isinstance(executed['data']['allProfiles'], list)


@pytest.mark.django_db
def test_update_profile():
    client = Client(schema)
    create_mutation = '''
        mutation {
            createProfile(userId: 1, bio: "This is a test bio", location: "Test Location") {
                profile {
                    id
                    bio
                    location
                }
            }
        }
    '''
    executed = client.execute(create_mutation)
    profile_id = executed['data']['createProfile']['profile']['id']

    update_mutation = f'''
        mutation {{
            updateProfile(id: {profile_id}, bio: "Updated bio", location: "Updated Location") {{
                profile {{
                    id
                    bio
                    location
                }}
            }}
        }}
    '''
    executed = client.execute(update_mutation)
    assert 'errors' not in executed
    assert executed['data']['updateProfile']['profile']['bio'] == 'Updated bio'
    assert executed['data']['updateProfile']['profile']['location'] == 'Updated Location'


@pytest.mark.django_db
def test_delete_profile():
    client = Client(schema)
    create_mutation = '''
        mutation {
            createProfile(userId: 1, bio: "This is a test bio", location: "Test Location") {
                profile {
                    id
                    bio
                    location
                }
            }
        }
    '''
    executed = client.execute(create_mutation)
    profile_id = executed['data']['createProfile']['profile']['id']

    delete_mutation = f'''
        mutation {{
            deleteProfile(id: {profile_id}) {{
                profile {{
                    id
                    bio
                }}
            }}
        }}
    '''
    executed = client.execute(delete_mutation)
    assert 'errors' not in executed
    assert executed['data']['deleteProfile']['profile']['id'] == profile_id
