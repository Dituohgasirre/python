#!/usr/bin/env python3


from request import Request
from response import Response
from config import Config
from cache import Cache


class Template:

    def __init__(self, tpl_name=None, **kwargs):
        self.path = Config.ROOT + Config.VIEW_NAME + '/'
        if tpl_name is None:
            self.path += "%s/%s" % (Request.Controller, Request.Method)
        else:
            self.path += "%s" % (tpl_name)
        self.path += "." + Config.TPL_SUFFIX

        cache = Cache(self.path)
        self.html = cache.get()
        if self.html:
            return

        with open(self.path) as tplFile:
            self.html = tplFile.read().format(**kwargs)

        cache.set(self.html)

    def fetch(self):
        return self.html

    def show(self):
        return Response(self.html)

