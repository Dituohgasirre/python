#!/usr/bin/env python3


from response import Response, Redirect
from config import Config
from template import Template
from datetime import datetime


def index(request):
    #  name[40]
    return Response('<h1>Hello World - %s</h1>' % Config.VIEW_NAME)


def cookie(request):
    s = "<h1>Test Cookie</h1>"
    for e in request.env:
        s += "<h3>%s: %s</h3>" % (e, request.env[e])

    t = datetime(2018, 3, 14, 10, 20, 30).strftime("%FT%T.000Z")
    c = "name=kyo; expires=%s; path=/student; httponly" % t

    return Response(s, header={'Set-Cookie': c})


def upload(request):
    if request.method == "POST":
        s = "<h3>"

        #  s += "POST: <br>"
        #  for k in request.post:
            #  s += "%s: %s<br>" % (k, request.post[k])
        #  s += "<br><hr><br>"

        #  s += "FILES: <br>"
        #  for k in request.files:
            #  s += "%s: %s<br>" % (k, request.files[k])
        #  s += "<br><hr><br>"

        for e in request.env:
            s += "%s: %s<br>" % (e, request.env[e])
        s += '</h3>'

        o = request.files['upfile']

        savepath = Config.ROOT + Config.UPLOAD_DIR + o.filename
        size = o.save(savepath)
        m = "成功" if size else "失败"
        return Response("<h1>上传%s...writesize = %s, type = %s, size = %s, ext = %s</h1> %s" % (m, size, o.type, o.size, o.ext, s))

    return Response(Template().fetch() + str(request.get))


def env(request):
    s = ""
    for e in request.env:
        s += "<h3>%s: %s</h3>" % (e, request.env[e])
    return Response(s)


def stu(request):
    return Redirect('/student/datalist')
    #  return Response('<h1>Hello Student</h1>')



