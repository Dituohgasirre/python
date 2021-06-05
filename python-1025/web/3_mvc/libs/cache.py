#!/usr/bin/env python3


from config import Config
from hashlib import md5
import pickle
import time
import os


class Cache:

    def __init__(self, cache_id):
        if not Config.TPL_CACHE:
            return
        md5sum = md5(cache_id.encode()).hexdigest()
        self.cachePath = Config.TPL_CACHE_PATH + md5sum

    def set(self, content, pick=False):
        if not Config.TPL_CACHE:
            return None

        cacheFile = open(self.cachePath, 'wb')

        if pick:
            pickle.dump(content, cacheFile)
        else:
            cacheFile.write(content.encode())

        cacheFile.close()

    def get(self, pick=False):
        if not Config.TPL_CACHE:
            return False

        if not os.path.exists(self.cachePath):
            return False

        ms = time.time() - os.path.getmtime(self.cachePath)
        if ms >= Config.TPL_CACHE_TIME:
            return False

        data = False

        cacheFile = open(self.cachePath, 'rb')

        if pick:
            data = pickle.load(cacheFile)
        else:
            data = cacheFile.read().decode()

        return data

