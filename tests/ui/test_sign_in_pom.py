from src.config.config import CONFIG

def test_sing_in_pom(github_ui_app):
    login_page = github_ui_app.LoginPage

    login_page.go_to()
    login_page.try_sign_in(CONFIG.get("USERNAME"), CONFIG.get("PASSWORD"))

    assert login_page.check_error_message()
