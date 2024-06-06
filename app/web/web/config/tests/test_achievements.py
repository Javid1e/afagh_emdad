# tests/test_achievements.py
import pytest
from graphene.test import Client
from config.schema import schema


@pytest.mark.django_db
def test_create_achievement():
    client = Client(schema)
    mutation = '''
        mutation {
            createAchievement(userId: 1, title: "Test Achievement", description: "Achievement Description") {
                achievement {
                    id
                    title
                    description
                }
            }
        }
    '''
    executed = client.execute(mutation)
    assert 'errors' not in executed
    assert executed['data']['createAchievement']['achievement']['title'] == 'Test Achievement'
    assert executed['data']['createAchievement']['achievement']['description'] == 'Achievement Description'


@pytest.mark.django_db
def test_get_achievements():
    client = Client(schema)
    query = '''
        query {
            allAchievements {
                id
                title
                description
            }
        }
    '''
    executed = client.execute(query)
    assert 'errors' not in executed
    assert isinstance(executed['data']['allAchievements'], list)
