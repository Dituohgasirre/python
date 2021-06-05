#!/usr/bin/env python3


from common import imp
from config import Config
from request import Request


class Route:

    def __init__(self, env):
        #  /控制器名/方法名/name/kyo/age/13/page/3/size/16
        info = env['PATH_INFO'].split('/')
        info_len = len(info)
        self.controllerName = info[1] or 'index'
        self.methodName = info[2] if info_len > 2 and info[2] else 'index'
        self.kargs = {}

        if info_len > 2:
            flag = False
            for v in info[3:]:
                if flag:
                    self.kargs[k] = v
                else:
                    k = v
                flag = not flag

        Request.Controller = self.controllerName
        Request.Method = self.methodName

    def distribute(self):
        #  print(self.controllerName, self.methodName, self.kargs)
        try:
            call = imp(self.controllerName, self.methodName,
                       Config.CONTROLLER_NAME)
        except:
            from exception import MVCException
            call = MVCException.route(self.controllerName,
                                      self.methodName, self.kargs)

        return call, self.kargs



