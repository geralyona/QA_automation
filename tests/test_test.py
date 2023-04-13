from src.config.config import config

def do_config_value_exist(name):
    value = config.get(name)
    print(name+ ": " + value)
    return value != ""


def test_user_age_is_42(user):
    assert user.age == 42

def test_config_base_url_exists():
    assert do_config_value_exist("BASE_URL")

def test_config_base_url_api_exists():
    assert do_config_value_exist("BASE_URL_API")

def test_config_base_url_ui_exists():
    assert do_config_value_exist("BASE_URL_UI")

def test_config_username_exists():
    assert do_config_value_exist("USERNAME")

def test_config_password_exists():
    assert do_config_value_exist("PASSWORD")

def test_ui_POM():
    #print(config.get("BASE_URL_UI"))
    pass