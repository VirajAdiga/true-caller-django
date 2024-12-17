import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from caller.tests.utils import create_user, get_token
from caller.models.spam_report import SpamReport


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_spam_report(api_client):
    user = create_user()
    token = get_token(user)
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    response = api_client.post(reverse('report-spam'), {
        'phone_number': '0987654321',
        'reason': 'Spam call'
    })
    assert response.status_code == 201
    assert SpamReport.objects.filter(phone_number='0987654321').exists()
