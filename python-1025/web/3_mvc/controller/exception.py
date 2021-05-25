#!/usr/bin/env python3


from exception import MVCException
from response import ErrorResponse


def route(request):
     mes = MVCException.default(back=True)
     return ErrorResponse("<h1>我自己的路由错误处理: %s</h1>" % mes)


def call():
     mes = MVCException.default(back=True)
     return ErrorResponse("<h1>我自己的函数调用错误处理: %s</h1>" % mes)

