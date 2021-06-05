#!/usr/bin/env python3

import os
import sys

print('Content-Type: text/html\n')

print("<p>REQUEST_METHOD: %s</p>" % os.environ["REQUEST_METHOD"])
print("<p>QUERY_STRING: %s</p>" % os.environ["QUERY_STRING"])
print("<p>HTTP_ACCEPT: %s</p>" % os.environ["HTTP_ACCEPT"])
print("<p>REMOTE_ADDR: %s</p>" % os.environ["REMOTE_ADDR"])
print("<p>HTTP_HOST: %s</p>" % os.environ["HTTP_HOST"])
#  for e in os.environ:
    #  print('<h5><span style="color: red">%s:</span> %s</h5>' % (e, os.environ[e]))

if os.environ["REQUEST_METHOD"] == 'POST':
    print("<h1>POST DATA: %s</h1>" % sys.stdin.read())
    print('<a href="post.py">Return</a>')
    exit(0)

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <form action="?op=add" method="POST">
    <input type="text" name="username">
    <input type="password" name="password">
    <input type="submit">
    </form>

</body>
</html>
""")

