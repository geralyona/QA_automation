import pytest
from src.config.config import config
from src.applications.models.user import User
from src.applications.api.github_api_client import GitHubApiClient
from src.applications.ui.github_ui_app import GitHubUI
from src.providers.service.browsers.browsers_provider import BrowsersProvider

@pytest.fixture(scope="session")
def user():
    # before test
    print("Create user")
    user = User(42)

    # pass user object to test
    yield user

    # after test
    print("Remove user")
    user.remove()


@pytest.fixture
def github_api_client():
    github_api_client = GitHubApiClient()
    github_api_client.login(CONFIG.get("USERNAME"), CONFIG.get("PASSWORD"))

    yield github_api_client

    github_api_client.logout()


@pytest.fixture
def github_ui_app():
    browser = CONFIG.get("BROWSER")
    driver = BrowsersProvider.get_driver(browser)


    ui_app = GitHubUI(driver)

    yield ui_app

    ui_app.quit()
