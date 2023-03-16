import pytest
from src.applications.models.user import User


@pytest.fixture()
def user():
    # before test
    user2 = User(42)
    # pass user
    yield user2
    #after test
    print('Remove user')
    user2.remove()