# tests/test_media.py

import pytest
from graphene.test import Client
from config.schema import schema


@pytest.mark.django_db
def test_create_media():
    client = Client(schema)
    mutation = '''
        mutation {
            createMedia(filePath: "/path/to/media", description: "Test media file") {
                media {
                    id
                    filePath
                    description
                }
            }
        }
    '''
    executed = client.execute(mutation)
    assert 'errors' not in executed
    assert executed['data']['createMedia']['media']['filePath'] == '/path/to/media'
    assert executed['data']['createMedia']['media']['description'] == 'Test media file'


@pytest.mark.django_db
def test_get_media():
    client = Client(schema)
    query = '''
        query {
            allMedia {
                id
                filePath
                description
            }
        }
    '''
    executed = client.execute(query)
    assert 'errors' not in executed
    assert isinstance(executed['data']['allMedia'], list)


@pytest.mark.django_db
def test_update_media():
    client = Client(schema)
    create_mutation = '''
        mutation {
            createMedia(filePath: "/path/to/media", description: "Test media file") {
                media {
                    id
                    filePath
                    description
                }
            }
        }
    '''
    executed = client.execute(create_mutation)
    media_id = executed['data']['createMedia']['media']['id']

    update_mutation = f'''
        mutation {{
            updateMedia(id: {media_id}, description: "Updated media description") {{
                media {{
                    id
                    filePath
                    description
                }}
            }}
        }}
    '''
    executed = client.execute(update_mutation)
    assert 'errors' not in executed
    assert executed['data']['updateMedia']['media']['description'] == 'Updated media description'


@pytest.mark.django_db
def test_delete_media():
    client = Client(schema)
    create_mutation = '''
        mutation {
            createMedia(filePath: "/path/to/media", description: "Test media file") {
                media {
                    id
                    filePath
                    description
                }
            }
        }
    '''
    executed = client.execute(create_mutation)
    media_id = executed['data']['createMedia']['media']['id']

    delete_mutation = f'''
        mutation {{
            deleteMedia(id: {media_id}) {{
                media {{
                    id
                    description
                }}
            }}
        }}
    '''
    executed = client.execute(delete_mutation)
    assert 'errors' not in executed
    assert executed['data']['deleteMedia']['media']['id'] == media_id
