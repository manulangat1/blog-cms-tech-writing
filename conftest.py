import pytest
import uuid
from pytest_factoryboy import register

from tests.factories import UserFactory

register(UserFactory)


@pytest.fixture
def base_user(db, user_factory):
    new_user = user_factory.create()
    return new_user


@pytest.fixture
def super_user(db, user_factory):
    new_user = user_factory.create(is_staff=True, is_superuser=True)
    return new_user


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()


@pytest.fixture
def test_password():
    return "strong-test-pass"


@pytest.fixture
def create_user(db, django_user_model, test_password):
    def make_user(**kwargs):
        kwargs["password"] = test_password
        if "username" not in kwargs:
            kwargs["username"] = str(uuid.uuid4())
        if "first_name" not in kwargs:
            kwargs["first_name"] = str(uuid.uuid4())
        if "last_name" not in kwargs:
            kwargs["last_name"] = str(uuid.uuid4())
        if "email" not in kwargs:
            kwargs["email"] = str("el@gmail.com")
        return django_user_model.objects.create_user(**kwargs)

    return make_user
