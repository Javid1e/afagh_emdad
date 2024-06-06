# tests/test_users.py

import pytest
from graphene.test import Client
from config.schema import schema


@pytest.mark.django_db
def test_create_user():
    client = Client(schema)
    mutation = '''
        mutation {
            createUser(username: "testuser", email: "test@example.com", phoneNumber: "09123456789", password: "password") {
                user {
                    id
                    username
                    email
                    phoneNumber
                }
            }
        }
    '''
    executed = client.execute(mutation)
    assert 'errors' not in executed
    assert executed['data']['createUser']['user']['username'] == 'testuser'
    assert executed['data']['createUser']['user']['email'] == 'test@example.com'
    assert executed['data']['createUser']['user']['phoneNumber'] == '09123456789'


@pytest.mark.django_db
def test_get_user():
    client = Client(schema)
    query = '''
        query {
            allUsers {
                id
                username
                email
                phoneNumber
            }
        }
    '''
    executed = client.execute(query)
    assert 'errors' not in executed
    assert isinstance(executed['data']['allUsers'], list)


@pytest.mark.django_db
def test_update_user():
    client = Client(schema)
    create_mutation = '''
        mutation {
            createUser(username: "testuser", email: "test@example.com", phoneNumber: "09123456789", password: "password") {
                user {
                    id
                    username
                    email
                    phoneNumber
                }
            }
        }
    '''
    executed = client.execute(create_mutation)
    user_id = executed['data']['createUser']['user']['id']

    update_mutation = f'''
        mutation {{
            updateUser(id: {user_id}, username: "updateduser", email: "updated@example.com", phoneNumber: "09129876543") {{
                user {{
                    id
                    username
                    email
                    phoneNumber
                }}
            }}
        }}
    '''
    executed = client.execute(update_mutation)
    assert 'errors' not in executed
    assert executed['data']['updateUser']['user']['username'] == 'updateduser'
    assert executed['data']['updateUser']['user']['email'] == 'updated@example.com'
    assert executed['data']['updateUser']['user']['phoneNumber'] == '09129876543'


@pytest.mark.django_db
def test_delete_user():
    client = Client(schema)
    create_mutation = '''
        mutation {
            createUser(username: "testuser", email: "test@example.com", phoneNumber: "09123456789", password: "password") {
                user {
                    id
                    username
                    email
                    phoneNumber
                }
            }
        }
    '''
    executed = client.execute(create_mutation)
    user_id = executed['data']['createUser']['user']['id']

    delete_mutation = f'''
        mutation {{
            deleteUser(id: {user_id}) {{
                user {{
                    id
                    username
                }}
            }}
        }}
    '''
    executed = client.execute(delete_mutation)
    assert 'errors' not in executed
    assert executed['data']['deleteUser']['user']['id'] == user_id
