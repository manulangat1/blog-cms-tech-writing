from email.mime import base
import imp
import pytest
from django.urls import reverse

from apps.blogauthentication.serializers import RegisterSerilizer

# from apps.


@pytest.mark.django_db
def test_register_api(api_client):
    url = reverse("register_api")
    payload = {
        "username": "name",
        "first_name": "manu",
        "last_name": "manu",
        "email": "alaa@gmail.com",
        "password": "3050manu",
    }
    response = api_client.post(url, payload)
    assert response.status_code == 201


@pytest.mark.django_db
def test_user_login_success(api_client, base_user, create_user, test_password):
    url = reverse("login_api")
    payload = {"username": f"{base_user.email}", "password": f"{base_user.password}"}
    print(base_user)
    response = api_client.post(url, payload)
    assert response.status_code == 200


@pytest.mark.django_db
def test_auth_view(api_client, create_user, test_password):
    user = create_user()
    url = reverse("get_profile_api")
    api_client.login(username=user.username, password=test_password)
    response = api_client.get(url)
    print(response)
    assert response.status_code == 403
