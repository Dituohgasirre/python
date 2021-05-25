#!/usr/bin/env python3


from response import Response, Redirect
from template import Template
from page import Page
from .mainpage import MainPage
from exception import SQLException
from models.student import View_Student, Student
from models.school import School
from models.classs import Class


@MainPage('学生管理平台')
def index(request, search="", page=1):
    where = "1";
    if search:
        from urllib.parse import unquote
        search = unquote(search)
        where = "sname like '%%%s%%' " % search
        where += " or cname like '%%%s%%'" % search
        where += " or oname like '%%%s%%'" % search

    v = View_Student()
    p = Page(page, v.where(where).orderBy('id').count(), url=request.url)
    data = v.limit(*p.limit()).select()

    html = ""
    for row in data:
        html += "<tr>"
        html += '<td><input type="checkbox"></td>'
        html += "<td>%s</td>" % row.id
        html += "<td>%s</td>" % row.sname
        html += "<td>%s</td>" % row.cname
        html += "<td>%s</td>" % row.oname
        html += "<td>"
        html += '<a class="btn btn-primary btn-xs link-modify-student" href="/student/modify/id/%s">修改</a>' % row.id
        html += '&emsp;&emsp;'
        html += '<a class="btn btn-primary btn-xs" href="/student/delete/id/%s">删除</a>' % row.id
        html += "</td>"
        html += "</tr>"

    t = Template(search=search, student_list=html, page_html=p.fetch())
    return t.fetch()


def modify(request, id=None):
    if request.IS_POST:
        try:
            Student(**request.post).save()
        except SQLException:
            return Response('<h1>更新失败</h1><br/><a href="#" onclick="history.go(-1)">返回</a>')
        return Redirect("/student")

    s = Student().where("id=%s" % id).select()[0]
    t = {}
    t['name'] = s.name
    t['phone'] = s.phone
    t['remark'] = s.remark or ""
    t['id'] = s.id
    t['gender1'] = 'checked' if s.gender == 1 else ''
    t['gender0'] = 'checked' if s.gender == 0 else ''
    t['sid_html'] = ''
    for school in School().select():
        ed = "selected" if school.id == s.sid else ""
        t['sid_html'] += '<option value="%d" %s>' % (school.id, ed)
        t['sid_html'] += '%s</option>' % school.name

    c = Class().where("id=%d" % s.cid).select()[0]
    t['cid_html'] = '<option value="%d">%s</option>' % (c.id, c.name)

    return Template(**t).show()

def getclass(request, sid):
    html = '<option value="" selected>所属班级</option>'
    for c in Class().where("sid=%s" % sid).select():
        html += '<option value="%d">' % c.id
        html += '%s</option>' % c.name
    return Response(html)


def add(request):
    if request.IS_POST:
        try:
            Student(**request.post).save()
        except SQLException:
            return Response('<h1>添加失败</h1><br/><a href="/student">返回</a>')
        return Redirect("/student")

    t = {}
    t['sid_html'] = '<option value="" selected>所属学校</option>'
    for school in School().select():
        t['sid_html'] += '<option value="%d">' % school.id
        t['sid_html'] += '%s</option>' % school.name

    return Template(**t).show()


def delete(request, id):
    Student().delete(id)
    return Redirect("/student")





