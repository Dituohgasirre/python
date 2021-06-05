#!/usr/bin/env python3


from libs.mvc import MVC
import os


application = MVC(os.getcwd(), 'libs', 'configs')


if __name__ == '__main__':
    print("pid = %d" % os.getpid())
    from wsgiref.simple_server import make_server
    make_server("0.0.0.0", 2000, application).serve_forever()
