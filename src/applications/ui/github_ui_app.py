from src.applications.ui.base_app import BaseAPP
from src.config.config import CONFIG
from src.applications.ui.page_objects.login_page import LoginPage
from src.providers.service.browsers.browsers_provider import BrowsersProvider


class GitHubUI(BaseAPP):

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.LoginPage = LoginPage(self)
        self.SingupPage = None

    def __init__(self) -> None:
        browser = CONFIG.get("BROWSER")
        driver = BrowsersProvider.get_driver(browser)

        super().__init__(driver)
        self.LoginPage = LoginPage(self)
        self.SingupPage = None

    def open(self):
        self.driver.get(CONFIG.get("BASE_URL_UI"))
        return self
    def check_repo_exists(repo_name):
        return True
    def quit(self):
        self.driver.quit()