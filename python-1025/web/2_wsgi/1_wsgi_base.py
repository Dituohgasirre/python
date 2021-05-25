#!/usr/bin/env python3

from wsgiref.simple_server import make_server
from db import Db

def student_data(env):
    get = {}
    if env['QUERY_STRING']:
        for field in env['QUERY_STRING'].split("&"):
            d = field.split('=')
            get[d[0]] = d[1]
    page = get['page'] if 'page' in get else '1'

    #  print("<p>page: %s, %s</p>" % (page, get))

    db = Db("oa")
    data = db.query("select s.name sname, c.name cname, o.name oname "
                    "from student s "
                    "inner join class c on s.cid=c.id "
                    "inner join school o on s.sid=o.id "
                    "limit %s, 10" % ((int(page) - 1) * 10))
    html = ""
    for row in data:
        html += "<tr>"
        html += "<td>%s</td>" % row['sname']
        html += "<td>%s</td>" % row['cname']
        html += "<td>%s</td>" % row['oname']
        html += "</tr>"

    return """
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
    """ % (html)


def client_handler(env, response):
    s = "中国"
    for x in env:
        s += "<p>%s: %s</p>" % (x, env[x])

    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        %s%s
    </body>
    </html>
    """ % ("<h1>hello world</h1>", s)

    response('200 OK', [("Content-Type", 'text/html')])
    #  return [html.encode()]
    return [student_data(env).encode()]

if __name__ == "__main__":
    httpd = make_server("0.0.0.0", 8000, client_handler)
    httpd.serve_forever()

