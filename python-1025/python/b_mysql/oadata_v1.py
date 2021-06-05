#!/usr/bin/env python3


from db import Db
from pargs import parse
from random import randint, choice
from hashlib import md5


class RandOaData:
    cnNum = '一二三四五六七八九十';

    def __init__(self, **kwargs):
        args, opt = parse(['S|school|1', 'c|class|1', 't|teacher|1',
                           'C|course|1', 's|student|1', 'o|score|1'])
        self.school = opt.get('school', 2)
        self.classNum = opt.get('class', 5)
        self.teacher = opt.get('teacher', 10)
        self.course = opt.get('course', 3)
        self.student = opt.get('student', 20)
        self.score = opt.get('score', 60)
        self.db = Db("oa")

    def md5(self, *args):
        data = ""
        for o in args:
            data += str(o)
        return md5(data.encode()).hexdigest()

    def isExists(self, table, md5sum, data=None):
        sql = 'select id from %s where md5sum=%%s' % table
        if bool(self.db.row(sql, [md5sum])):
            return True

        if data is not None:
            for d in data:
                if md5sum == d[-1]:
                    return True

        return False

    def randSchool(self, num=None):
        city = ['深圳', '广州', '佛山', '中山', '东莞', '梅州', '茂名', '汕头']
        sub = ['大学', '中学', '职业学院', '师范学院', '小学']

        num = num or self.school

        schoolNum = self.db.col('select count(*) from school')
        if num + schoolNum > len(city) * len(sub) * len(RandOaData.cnNum):
            return

        data = []
        i = 0
        while i < num:
            school = []
            randcity = choice(city)
            school.append(randcity + '第' + choice(RandOaData.cnNum) + choice(sub))
            school.append(randcity + "市")
            md5sum = self.md5(*school)
            if self.isExists('school', md5sum, data):
                continue
            school.append(md5sum)
            data.append(school)
            i += 1

        sql = 'insert school (name, location, md5sum) values (%s, %s, %s)'
        self.db.executemany(sql, data)

    def getName(self):
        first = ['何', '朱', '李', '王', '张', '刘', '吴', '赵', '田', '马',
                 '司徒', '欧阳', '皇甫', '南宫', '诸葛', '上官']
        name = ('驰福兴华初震泽震骏濡嘉骏锟天宇嘉彬祜梓骏轩翰贤凯骞振振骏帆'
                '蔓嘉吉晨强柔辰运鸿运振涛桓鸿谷骏暄震寅振祯翰栋运锋腾振祜骞'
                '逸运胤浩驰振星尧哲栋寅振凡蔓寅韦骏烁骏华瑞延鹏晨锋初栋腾嘉'
                '运驰驰辰鑫振然潍盛鹏博运峰蔓骏骏胤谛凯振轩信骏斌辰骏骏祥辰'
                '星翱海凡爵尧运驰盛卓强哲斌礼运贤权震骏逸嘉文骏星福祯胤日槐'
                '驰运龙睿运轩骏濡辰然鸿振桀炳栋震骏')
        x = choice(first)
        for i in range(randint(1, 2)):
            x += choice(name)

        return x

    def randTeacher(self, num=None, sid=None):
        if sid is None:
            sid = []
            for row in self.db.query("select id from school"):
                sid.append(row['id'])
        elif not (type(sid) == list or type(sid) == tuple):
            sid = [sid]

        data = []
        i = 0
        while i < num:
            teacher = []
            teacher.append(choice(sid))
            teacher.append(self.getName())
            teacher.append(randint(0, 1))
            md5sum = self.md5(*teacher)
            if self.isExists('teacher', md5sum, data):
                continue
            teacher.append(md5sum)
            data.append(teacher)
            i += 1

        sql = ('insert teacher (sid, name, gender, md5sum)'
               'values (%s, %s, %s, %s)')
        self.db.executemany(sql, data)

    def randCourse(self, num=None, sid=None):
        if sid is None:
            sid = []
            for row in self.db.query("select id from school"):
                sid.append(row['id'])
        elif not (type(sid) == list or type(sid) == tuple):
            sid = [sid]

        name = ['语文', '数学', '英语', '政治', '生物', '化学', '物理',
                '历史', '地理', '几何', '美术', '音乐', '体育', '计算机',
                'PHP', 'Python', 'Java', 'C', 'C++', 'Go', 'Shell', 'Ruby',
                'MySQL', 'HTML', 'CSS', 'JavaScript', 'UI', 'Django', 'Vim',
                '测试', '运维', '自动化测试', '自动化运维']

        data = []
        i = 0
        while i < num:
            course = []
            course.append(choice(sid))
            course.append(choice(name))
            md5sum = self.md5(*course)
            if self.isExists('course', md5sum, data):
                continue
            course.append(md5sum)
            data.append(course)
            i += 1

        sql = ('insert course (sid, name, md5sum) values (%s, %s, %s)')
        self.db.executemany(sql, data)

    def randId(self, sid, table):
        sql = "select id from %s where sid=%%s" % table
        data = self.db.query(sql, [sid])
        if not data:
            return None
        #  print(sql, sid, data, ' -------------')
        data = choice(data)
        #  print(sql, sid, data, " ########")
        return data['id']

    def randTeacherCourse(self, num=None, sid=None):
        if sid is None:
            sid = []
            for row in self.db.query("select id from school"):
                sid.append(row['id'])
        elif not (type(sid) == list or type(sid) == tuple):
            sid = [sid]

        data = []
        i = 0
        while i < num:
            r = []
            school = choice(sid)
            tid = self.randId(school, 'teacher')
            if tid is None:
                continue
            cid = self.randId(school, 'course')
            if cid is None:
                continue
            r.append(tid)
            r.append(cid)
            md5sum = self.md5(*r)
            if self.isExists('t_to_c', md5sum, data):
                continue
            r.append(md5sum)
            data.append(r)
            i += 1

        sql = ('insert t_to_c (tid, cid, md5sum) values (%s, %s, %s)')
        self.db.executemany(sql, data)


if __name__ == "__main__":
    def main():
        #  db = Db('company')
        #  name = input("请输入要查询的姓名: ")
            #  用户SQL注入: s' or '1'; -- k
        #  sql = "select * from emp where ename=%s"
        #  print(sql)
        #  print(db.query(sql, [name]))
        r = RandOaData()
        #  r.randSchool(400)
        #  r.randTeacher(1)
        #  r.randCourse(1000)
        r.randTeacherCourse(1000)
        #  for s in r.db.query("select * from school"):
            #  print(s['name'], s['location'])

    main()
