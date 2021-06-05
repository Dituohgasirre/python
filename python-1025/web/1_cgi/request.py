#!/usr/bin/env python3

import os

print('Content-Type: text/html\n')

#  for e in os.environ:
    #  print('<h3><span style="color: red">%s:</span> %s</h3>' % (e, os.environ[e]))

get = {}
for field in os.environ['QUERY_STRING'].split("&"):
    d = field.split('=')
    get[d[0]] = d[1]

for f in get:
    print('<h3><span style="color: red">%s:</span> %s</h3>' % (f, get[f]))

