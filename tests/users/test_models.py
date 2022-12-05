import pytest


def test_user_str(base_user):
    """
    Test the custom user model string repr"""

    assert base_user.__str__() == f"{base_user.username}"


def test_short_name(base_user):
    """
    Tests the short name of the user"""
    assert base_user.get_short_name() == f"{base_user.username}"
