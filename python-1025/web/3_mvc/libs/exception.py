#!/usr/bin/env python3


import sys
import traceback
from response import ErrorResponse
from common import imp
from config import Config

class SQLException(Exception):
    pass


class MVCException:

    @staticmethod
    def default(request=None, back=False):
        mes = '<div class="exception">'
        mes += '<h3>异常信息: </h3>'
        mes += '<p>%s</p>' % MVCException.value

        mes += '<h3>参数信息: </h3>'
        for x in MVCException.kwargs:
            mes += '<p>%s: %s</p>' % (x, MVCException.kwargs[x])

        mes += '<h3>异常栈跟踪: </h3>'
        for t in MVCException.tb:
            m = t.split('\n')
            mes += '<p style="color: red; font-weight: bold;">%s</p>' % m[0]
            mes += '<pre>%s</pre>' % m[1]
        mes += '</div>'

        if back:
            return mes

        return ErrorResponse(mes)

    @staticmethod
    def get_exc(**kwargs):
        etype, value, tb = sys.exc_info()
        MVCException.type = etype
        MVCException.value = value
        MVCException.tb = traceback.format_tb(tb)
        MVCException.kwargs = kwargs

    @staticmethod
    def get_call(name):
        try:
            call = imp(Config.EXCEPTION_NAME, name, Config.CONTROLLER_NAME)
        except:
            call = MVCException.default
        return call

    @staticmethod
    def route(controllerName, methodName, kargs):
        MVCException.get_exc(control=controllerName,
                             method=methodName, args=kargs)
        return MVCException.get_call('route')

    @staticmethod
    def call(call, kargs):
        MVCException.get_exc(call=call, args=kargs)
        return MVCException.get_call('call')()

    @staticmethod
    def illegal(response):
        #  将response对象的数据写入日志文件
        #  pass

        call = MVCException.get_call('illegal')
        if call is MVCException.default:
            return ErrorResponse("<h1>非法操作....</h1>")
        return call()


