#!/usr/bin/env python3


from config import Config
from response import Response
from template import Template


class MainPage:

    def __init__(self, title, **kwargs):
        self.top = Template('top', title=title, css=Config.CSS)
        self.bottom = Template('bottom', static=Config.STATIC, js=Config.JS)

    def __call__(self, func):
        self.func = func
        return self.do

    def do(self, *args, **kwargs):
        html = self.top.fetch()
        html += self.func(*args, **kwargs)
        html += self.bottom.fetch()

        return Response(html)

