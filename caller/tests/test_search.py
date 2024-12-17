import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from caller.tests.utils import create_user, get_token


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_search_by_name(api_client):
    user = create_user()
    token = get_token(user)
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    response = api_client.get(reverse('search'), {'query': 'John'})
    assert response.status_code == 200
    assert len(response.data.get('results')) > 0


@pytest.mark.django_db
def test_search_by_name_partial(api_client):
    user = create_user(name='Johnathan Doe', email='johnathan@example.com')
    token = get_token(user)
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    response = api_client.get(reverse('search'), {'query': 'John'})
    assert response.status_code == 200
    assert len(response.data.get('results')) > 0
