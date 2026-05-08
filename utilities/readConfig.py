import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "../testData/config.ini"))

class ReadConfig:
    @staticmethod
    def get_base_url():
        return config.get("basic info", "baseURL")

    @staticmethod
    def get_username():
        return config.get("basic info", "username")

    @staticmethod
    def get_password():
        return config.get("basic info", "password")