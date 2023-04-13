from src.config.providers.config_from_env_provider import ConfigFromEnvProvider


def test_config_env_provider_negative():
    conf = ConfigFromEnvProvider()
    val = conf.get("KJHKJFHSDKJFH")
    assert val is None


def test_config_env_provider_positive():
    conf = ConfigFromEnvProvider()
    val = conf.get("PATH")
    eclipse = val.find(U"C:\\Users\\Alyona\\AppData\\Local\\Programs\\Python\\Python310")
    assert eclipse > 0
