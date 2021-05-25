from oa import Oa

def application(env, response):
    response('200 OK', [('Content-Type', 'text/html')])
    srvName = "uWSGI Web Server"
    if env['SERVER_NAME'] == '_':
        srvName = "Nginx Proxy"
    elif env['SERVER_NAME'] in 'uwc':
        srvName = "Apache Proxy"

    srvName = '<h1>%s</h1>' % srvName

    o = Oa(env)
    #  s = ""
    #  for e in env:
        #  s += '<p><span style="color:red">%s: </span>%s</p>' % (e, env[e])
    return [o.html(), srvName.encode()]

#  if __name__ == '__main__':
    #  application()
