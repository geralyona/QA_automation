import pytest
from src.config.config import config
from src.applications.models.user import User
from src.applications.api.github_api_client import GitHubApiClient


@pytest.fixture()
def user():
    # before test
    user2 = User(42)
    # pass user
    yield user2
    #after test
    #print('Remove user')
    user2.remove()

@pytest.fixture()
def github_api_client():
    github_api_client = GitHubApiClient()
    username = config.get("USERNAME")
    github_api_client.login(username, config.get("PASSWORD"))

    yield github_api_client

    github_api_client.logout(username)
