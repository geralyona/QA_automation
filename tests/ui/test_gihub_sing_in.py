import pytest

def test_sing_in_pom(GitHub_UI_App):
    login_page = GitHub_UI_App.LoginPage

def test_sing_in_pom(github_ui_app):
    login_page = github_ui_app.LoginPage
    login_page.go_to()
    login_page.try_sign_in('username', 'password')