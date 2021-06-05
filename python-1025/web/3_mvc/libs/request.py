#!/usr/bin/env python3


from urllib.parse import parse_qs
from cgi import FieldStorage
from common import upload_save
import os


class Request:

    __instance = None

    def __new__(cls, *args, **kwargs):
        if Request.__instance is None:
            Request.__instance = object.__new__(cls)
        return Request.__instance

    def __init__(self, env):
        env['PATH_INFO'] = env['PATH_INFO'].encode("iso-8859-1").decode('utf8')
        Request.env = env
        Request.method = env['REQUEST_METHOD']
        Request.IS_POST = bool(Request.method == 'POST')
        Request.IS_GET = bool(Request.method == 'GET')
        Request.IS_PUT = bool(Request.method == 'PUT')
        Request.IS_DELETE = bool(Request.method == 'DELETE')

        Request.get = self.parse_get(env['QUERY_STRING'])
        Request.length = int(env.get('CONTENT_LENGTH', 0) or 0)
        Request.ip = env['REMOTE_ADDR']
        Request.type = env['HTTP_ACCEPT']
        Request.agent = env['HTTP_USER_AGENT']
        Request.PathInfo = env['PATH_INFO']
        qs = '?' + env['QUERY_STRING'] if env['QUERY_STRING'] else ''
        Request.url = "http://%s%s%s" % (env['HTTP_HOST'], env['PATH_INFO'], qs)

        if not hasattr(FieldStorage, 'save'):
            FieldStorage.save = upload_save

        Request.post, Request.files = self.parse_post(env)

    def parse_post(self, env):
        def _postVal(post, o):
            if o.name not in post:
                return o.value          #第一次

            l = [o.value]
            if isinstance(post[o.name], list):
                l += post[o.name]       #后面
            else:
                l.append(post[o.name])  #第二次

            return l

        post = {}
        files = {}
        if Request.method != 'POST':
            return post, files

        formdata = FieldStorage(environ=env, fp=env['wsgi.input'])
        for o in formdata.value:
            if o.filename:
                o.size = Request.length
                o.ext = os.path.splitext(o.filename)[-1]
                files[o.name] = o
            else:
                post[o.name] = _postVal(post, o)

        return post, files


    def parse_get(self, qs):
        x = {}
        for k, v in parse_qs(qs).items():
            x[k] = v[0] if len(v) == 1 else v
        return x
