import pytest
from .models import User


@pytest.mark.django_db
def test_user():
    user_one = User.objects.create(name="user one")
    assert user_one.name == "user one"
