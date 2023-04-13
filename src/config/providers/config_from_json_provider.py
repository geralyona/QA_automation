import json
import os
from src.config.providers.base_config import BaseConfigKeyProvider

class ConfigFromSimpleJsonProvider(BaseConfigKeyProvider):
    """
    Allows configuration through the JSON file
    """
    def __init__(self, config_path):
        """
        :param config_path: path to the json with configuration
        """
        local = str.replace(config_path, "/","\\")
        print(local) 
        real_path = os.getcwd() + "\\" + local
        real_path = config_path
        if(os.path.isfile(real_path) == False):
            print(real_path)
            print("Path at terminal when executing this file")
            print(os.getcwd() + "\n")
            return FileNotFoundError(real_path)

        with open(config_path) as json_file:
            self._config_data = json.load(json_file)

    def get(self, key):
        """
        Returns config value for the given key
        :param str key: Key to retrieve
        """
        val = self._config_data.get(key)
        return val
