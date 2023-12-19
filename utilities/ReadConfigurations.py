from configparser import ConfigParser


def read_configuration(category, key):
    config = ConfigParser()
    config.read("/Users/abhaythakur/PycharmProjects/SeleniumPythonHybridFramework/configurations/config.ini")
    return config.get(category, key)
