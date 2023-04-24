from src.config.config import CONFIG
from selenium.webdriver.common.by import By
import time

class LoginPage:
    URL = "/login"

    USERNAME_FLD = (By.ID, "login_field") #css xpath    
    PASSWROD_FLD = (By.ID, "password") #id
    SIGN_IN_BTN = (By.NAME, "commit") #name

    def __init__(self, app) -> None:
        self.app = app

    def go_to(self):
        self.app.driver.get(CONFIG.get("BASE_URL_UI") + LoginPage.URL)
        self.app.go_to(CONFIG.get("BASE_URL_UI") + LoginPage.URL)

    def try_sign_in(self, username, password):
        self.app.type_text(LoginPage.USERNAME_FLD, username)
        self.app.type_text(LoginPage.PASSWROD_FLD, password)

        self.app.click(LoginPage.SIGN_IN_BTN)

        time.sleep(5)

        return self
    def click_sign_up_page(self):
        sing_up_page = self.app.SignUpPage(self.app)
        sing_up_page.wait_loaded()
        return sing_up_page
    def go_to_forgot_pass_page(self):
        # return any
        pass
    def check_error_message(self):
        # return bool
        # if error exists - return True
        # else - return False
        # error_msg = self.driver.find_element(By.ID, LoginPage.USERNAME_FLD)
        error_msg = "Error"
        return error_msg == "Error"