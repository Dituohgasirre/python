#!/usr/bin/env python3


from http import HTTPStatus
from config import Config


class Response:

    def __init__(self, body, status=200, header={}, **kwargs):
        status_txt = HTTPStatus(status).name.replace('_', ' ')
        self.status = "%d %s" % (status, status_txt)
        self.code = status
        self.header = {'Content-Type': 'text/html; charset=utf-8'}
        self.header.update(header)
        self.header = list(self.header.items())
        self.body = body


class ErrorResponse(Response):

    def __init__(self, body, **kwargs):
        Response.__init__(self, body, Config.DEBUG_STATUS, **kwargs)


class Redirect(Response):

    def __init__(self, url, **kwargs):
        Response.__init__(self, '', 303, header={'Location': url}, **kwargs)


class StaticResponse(Response):

    def __init__(self, path, accept, **kwargs):
        body = None

        with open(path, 'rb') as f:
            body = f.read()

        header = {'Content-Type': accept}

        Response.__init__(self, body, header=header, **kwargs)

