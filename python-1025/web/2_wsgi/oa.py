#!/usr/bin/env python3

from db import Db
from page import Page

class Oa:
    def __init__(self, env):
        self.db = Db('oa')
        self.env = env
        self.GET = self.get_qs(env)
        if 'op' in self.GET:
            getattr(self, 'o_' + self.GET['op'])()
        self.page = Page(self.GET)

    def o_del(self):
        self.db.query("delete from student where id=%s", [self.GET['id']])

    def get_qs(self, env=None):
        env = env or self.env
        get = {}
        if env['QUERY_STRING']:
            for field in env['QUERY_STRING'].split("&"):
                d = field.split('=')
                get[d[0]] = d[1]
        return get

    def tpl(self, title, body):
        return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>%s</title>
            <!-- 最新版本的 Bootstrap 核心 CSS 文件 -->
            <link rel="stylesheet" href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
        </head>
        <body>
            <div class="container">
            <div class="row" style="margin-bottom: 20px; margin-top: 20px;">
                <div class="col-lg-6 col-lg-offset-3">
                    <div class="input-group">
                        <input class="form-control" id="search" type="text" placeholder="请输入查询关键词...">
                        <span class="input-group-btn"><button class="btn btn-default"><span class="glyphicon glyphicon-search"></span></button></span>
                    </div>
                </div>
            </div>
            %s
            </div>
            <!-- 最新的 Bootstrap 核心 JavaScript 文件 -->
            <script src="https://cdn.bootcss.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
        </body>
        </html>
        """ % (title, body)

    def student(self):
        self.page.total = self.db.col("select count(*) from student")
        data = self.db.query("select s.id id, s.name sname, c.name cname, o.name oname "
                        "from student s "
                        "inner join class c on s.cid=c.id "
                        "inner join school o on s.sid=o.id "
                        "%s" % (self.page.limit()))
        html = """
            <table class="table table-striped table-bordered table-responsive text-center">
            <thread>
            <tr>
                <th>学号</th>
                <th>姓名</th>
                <th>班级</th>
                <th>学校</th>
                <th>操作</th>
            </tr>
            </thread>"""

        for row in data:
            html += "<tr>"
            html += "<td>%s</td>" % row['id']
            html += "<td>%s</td>" % row['sname']
            html += "<td>%s</td>" % row['cname']
            html += "<td>%s</td>" % row['oname']
            html += '<td><a href="?op=del&id=%s">删除</td>' % row['id']
            html += "</tr>"
        html += "</table>"

        html += self.page.fetch()

        return html

    def html(self):
        return self.tpl("学生信息管理", self.student()).encode()


