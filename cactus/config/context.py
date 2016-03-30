#coding:utf-8
from cactus.config.router import ConfigRouter

class ConfigContext(object):
    """
    A template context object to read from the config router.
    """

    def __init__(self, config_router):
        """
        Initialise with a config router.
        """
        self.config = config_router

    def __getitem__(self, key):
        """
        Provide subscript access for inside templates. Nicely return an empty
        string if there is no value for the given key.
        """
        return self.config.get(key, default='')
