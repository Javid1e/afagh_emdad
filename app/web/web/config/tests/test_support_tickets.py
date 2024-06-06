# tests/test_support_tickets.py

import pytest
from graphene.test import Client
from config.schema import schema


@pytest.mark.django_db
def test_create_support_ticket():
    client = Client(schema)
    mutation = '''
        mutation {
            createSupportTicket(userId: 1, subject: "This is a test support ticket", message: "Help me!") {
                supportTicket {
                    id
                    subject
                    message
                }
            }
        }
    '''
    executed = client.execute(mutation)
    assert 'errors' not in executed
    assert executed['data']['createSupportTicket']['supportTicket']['subject'] == 'This is a test support ticket'
    assert executed['data']['createSupportTicket']['supportTicket']['message'] == 'Help me!'


@pytest.mark.django_db
def test_get_support_tickets():
    client = Client(schema)
    query = '''
        query {
            allSupportTickets {
                id
                subject
                message
            }
        }
    '''
    executed = client.execute(query)
    assert 'errors' not in executed
    assert isinstance(executed['data']['allSupportTickets'], list)


@pytest.mark.django_db
def test_update_support_ticket():
    client = Client(schema)
    create_mutation = '''
        mutation {
            createSupportTicket(userId: 1, subject: "This is a test support ticket", message: "Help me!") {
                supportTicket {
                    id
                    subject
                    message
                }
            }
        }
    '''
    executed = client.execute(create_mutation)
    ticket_id = executed['data']['createSupportTicket']['supportTicket']['id']

    update_mutation = f'''
        mutation {{
            updateSupportTicket(id: {ticket_id}, subject: "Updated support ticket subject", message: "Updated help message") {{
                supportTicket {{
                    id
                    subject
                    message
                }}
            }}
        }}
    '''
    executed = client.execute(update_mutation)
    assert 'errors' not in executed
    assert executed['data']['updateSupportTicket']['supportTicket']['subject'] == 'Updated support ticket subject'
    assert executed['data']['updateSupportTicket']['supportTicket']['message'] == 'Updated help message'


@pytest.mark.django_db
def test_delete_support_ticket():
    client = Client(schema)
    create_mutation = '''
        mutation {
            createSupportTicket(userId: 1, subject: "This is a test support ticket", message: "Help me!") {
                supportTicket {
                    id
                    subject
                    message
                }
            }
        }
    '''
    executed = client.execute(create_mutation)
    ticket_id = executed['data']['createSupportTicket']['supportTicket']['id']

    delete_mutation = f'''
        mutation {{
            deleteSupportTicket(id: {ticket_id}) {{
                supportTicket {{
                    id
                    subject
                }}
            }}
        }}
    '''
    executed = client.execute(delete_mutation)
    assert 'errors' not in executed
    assert executed['data']['deleteSupportTicket']['supportTicket']['id'] == ticket_id
