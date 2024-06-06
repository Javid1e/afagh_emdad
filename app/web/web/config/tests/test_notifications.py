# tests/test_notifications.py

import pytest
from graphene.test import Client
from config.schema import schema


@pytest.mark.django_db
def test_create_notification():
    client = Client(schema)
    mutation = '''
        mutation {
            createNotification(userId: 1, message: "This is a test notification") {
                notification {
                    id
                    message
                }
            }
        }
    '''
    executed = client.execute(mutation)
    assert 'errors' not in executed
    assert executed['data']['createNotification']['notification']['message'] == 'This is a test notification'


@pytest.mark.django_db
def test_get_notifications():
    client = Client(schema)
    query = '''
        query {
            allNotifications {
                id
                message
            }
        }
    '''
    executed = client.execute(query)
    assert 'errors' not in executed
    assert isinstance(executed['data']['allNotifications'], list)
