#!/usr/bin/env python3

import sys
import os
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
sys.path.append("/kyo/python/libs")

def response():
    get = {}
    if os.environ['QUERY_STRING']:
        for field in os.environ['QUERY_STRING'].split("&"):
            d = field.split('=')
            get[d[0]] = d[1]
    page = get['page'] if 'page' in get else '0'

    print("<p>page: %s, %s</p>" % (page, get))

    from db import Db
    db = Db("oa")
    data = db.query("select s.name sname, c.name cname, o.name oname "
                    "from student s "
                    "inner join class c on s.cid=c.id "
                    "inner join school o on s.sid=o.id "
                    "limit %s, 10" % (int(page) * 10))
    html = ""
    for row in data:
        html += "<tr>"
        html += "<td>%s</td>" % row['sname']
        html += "<td>%s</td>" % row['cname']
        html += "<td>%s</td>" % row['oname']
        html += "</tr>"

    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title></title>
        <!-- 最新版本的 Bootstrap 核心 CSS 文件 -->
        <link rel="stylesheet" href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    </head>
    <body>
        <table class="table table-striped table-bordered table-responsive text-center">
        <thread>
        <tr>
            <th>学生姓名</th>
            <th>班级名称</th>
            <th>学校名称</th>
        </tr>
        </thread>
        %s
        </table>
        <nav aria-label="Page navigation">
            <ul class="pagination">
                <li>
                <a href="#" aria-label="Previous">
                <span aria-hidden="true">&laquo;</span>
                </a>
                </li>
                <li><a href="?page=1">1</a></li>
                <li><a href="?page=2">2</a></li>
                <li><a href="?page=3">3</a></li>
                <li><a href="?page=4">4</a></li>
                <li><a href="?page=5">5</a></li>
                <li>
                <a href="#" aria-label="Next">
                <span aria-hidden="true">&raquo;</span>
                </a>
                </li>
            </ul>
        </nav>
        <!-- 最新的 Bootstrap 核心 JavaScript 文件 -->
        <script src="https://cdn.bootcss.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
    </body>
    </html>
    """ % (html))

try:
    print("Content-Type: text/html\n")
    #  print("<h3>hello world</h3>")
    #  print("<p>Path: %s</p>" % sys.path)
    print("<p>Version: %s</p>" % sys.version)
    print("<p>encode: %s</p>" % sys.getdefaultencoding())
    response()
except Exception as e:
    print('<p>%s</p>' % e)

