#!/usr/bin/env python3

STATIC = '/static/'
JS = STATIC + 'js/'
CSS = STATIC + 'css/'
IMG  = STATIC + 'image/'
UPLOAD_DIR = STATIC + 'upload/'

CONTROLLER_NAME = 'controller'
VIEW_NAME = 'view'
MODEL_NAME = 'models'

DEBUG_MODE = True
DEBUG_STATUS = 404
EXCEPTION_NAME = 'exception'

TPL_SUFFIX = 'tpl'
TPL_CACHE = False
TPL_CACHE_DIR_NAME = "tpl_cache/"
TPL_CACHE_PATH = STATIC + TPL_CACHE_DIR_NAME
TPL_CACHE_TIME = 1200

DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'passwd': '123123',
    'dbname': 'oa',
    'charset': 'utf8'
}

