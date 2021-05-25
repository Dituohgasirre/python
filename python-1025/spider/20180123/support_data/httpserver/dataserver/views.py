import sys
import os
import json
from datetime import datetime

from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def post(request, kind):
    if kind == 'message':
        res = HttpResponse('recv: %s' % str(dict(request.POST)))
    elif kind == 'file':
        res = HttpResponse('failed to save file')
        res.status_code = 500
        for f in request.FILES.values():
            with open('files/upload/%s' % f.name, 'wb') as dst:
                for chunk in f.chunks(chunk_size=262144):
                    dst.write(chunk)
                res = HttpResponse('file saved')
    return res


def get(request, kind):
    if kind == 'xml':
        text = '<book><title>Python</title><price>9.99</price></book>'
        res = HttpResponse(text, content_type='text/xml')
    elif kind == 'json':
        data = {'name': 'Alice', 'age': 25, 'gender': 'Female'}
        data = json.dumps(data)
        res = HttpResponse(data, content_type='application/json')
    elif kind == 'image':
        img = open('files/pub/wildfire.jpg', 'rb').read()
        res = HttpResponse(img, content_type='image/jpeg')
    elif kind == 'file':
        path = 'files/pub/data.bin'
        # path = 'files/pub/bigfile'
        res = StreamingHttpResponse(
                read_bigfile(path),
                content_type='application/octet-stream')
        bname = os.path.basename(path)
        res['Content-Disposition'] = 'attachment; filename=%s' % bname
        res['Content-Length'] = os.path.getsize(path)
    else:
        text = '<html><body><h1>Behold, requests!</h1></body></html>'
        res = HttpResponse(text)
    return res


def read_bigfile(path, bs=262144):
    with open(path, 'rb') as f:
        while True:
            chunk = f.read(bs)
            if chunk:
                yield chunk
            else:
                break
