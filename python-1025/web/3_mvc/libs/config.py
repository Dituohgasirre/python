#!/usr/bin/env python3


from common import imp


class Config:

    __instance = None

    def __new__(cls, *args, **kargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, root, core_name, config_name):
        Config.ROOT = root
        Config.CORE_NAME = core_name
        try:
            Config.loadConfigFile(config_name)
        except:
            Config.loadDefaultConfig()

    @staticmethod
    def loadDefaultConfig():
        Config.STATIC = 'static/'
        Config.JS = Config.STATIC + 'js/'
        Config.CSS = Config.STATIC + 'css/'
        Config.IMG  = Config.STATIC + 'image/'
        Config.CONTROLLER_NAME = 'controller'
        Config.VIEW_NAME = 'view'
        Config.MODEL_NAME = 'model'
        Config.EXCEPTION_NAME = 'exception'
        Config.DEBUG_MODE = True
        Config.DEBUG_STATUS = 404
        Config.TPL_SUFFIX = 'tpl'
        Config.TPL_CACHE = False
        Config.TPL_CACHE_DIR_NAME = "tpl_cache/"
        Config.TPL_CACHE_PATH = Config.STATIC + Config.TPL_CACHE_DIR_NAME
        Config.TPL_CACHE_TIME = 600


    @staticmethod
    def loadConfigFile(config_name):
        m = imp(config_name)
        for name in dir(m):
            if name.startswith('_'):
                continue
            setattr(Config, name, getattr(m, name))

