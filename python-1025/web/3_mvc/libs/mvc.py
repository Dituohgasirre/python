#!/usr/bin/env python3


import sys
import os


class MVC:

    def __init__(self, root, core_name, config_name):
        self.root = root + '/'
        self.core_name = core_name
        self.config_name = config_name
        sys.path.append(self.root + core_name)
        #  print(sys.path)

    def httpResponse(self, response):
        self.start_response(response.status, response.header)
        if type(response.body) == bytes:
            return [response.body]
        return [response.body.encode()]

    def __call__(self, env, start_response):
        self.start_response = start_response

        from config import Config
        from request import Request
        from route import Route
        from cache import Cache
        from exception import MVCException

        config = Config(self.root, self.core_name, self.config_name)
        request = Request(env)
        if request.PathInfo.startswith(config.STATIC):
            from response import StaticResponse
            filepath = self.root + request.PathInfo
            return self.httpResponse(StaticResponse(filepath, request.type))

        cache = Cache(request.url)
        response = cache.get(pick=True)
        if response:
            return self.httpResponse(response)

        route = Route(env)
        call, kargs = route.distribute()
        #  print(call, kargs)
        try:
            response = call(request, **kargs)
        except:
            response = MVCException.call(call, kargs)

        if not Config.DEBUG_MODE and response.code == Config.DEBUG_STATUS:
            response = MVCException.illegal(response)
        else:
            cache.set(response, pick=True)

        return self.httpResponse(response)


