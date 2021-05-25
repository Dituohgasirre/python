import sys
sys.path.append("/kyo/python/libs")
sys.path.append("/kyo/web/2_wsgi")
from oa import Oa

def application(env, response):
    response('200 OK', [('Content-Type', 'text/html')])
    o = Oa(env)
    return [o.html(), "<h1>Apache2 Mod WSGI....</h1>".encode()]
