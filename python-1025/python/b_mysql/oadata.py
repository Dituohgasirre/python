#!/usr/bin/env python3


from db import Db
from pargs import parse
from random import randint, choice, random
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
        """
        校验数据唯一性(多字段)
        """
        sql = 'select id from %s where md5sum=%%s' % table
        if bool(self.db.row(sql, [md5sum])):
            return True

        if data is not None:
            for d in data:
                if md5sum == d[-1]:
                    return True

        return False

    def getName(self):
        """
        返回随机姓名
        """
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

    def getIdList(self, table):
        """
        获取某个表所有ID转化成列表
        """
        idlist = []
        for row in self.db.query("select id from %s" % table):
            idlist.append(row['id'])
        return idlist

    def getSidList(self, sid=None, table='school'):
        """
        获取所有学校或其它表ID的列表
        """
        if sid is None:
            sid = self.getIdList(table)
        elif not (type(sid) == list or type(sid) == tuple):
            sid = [sid]
        return sid

    def loop(self, num, table, fields, getFieldData):
        """
        随机数据框架函数
        """
        addData = []
        i = 0
        while i < num:
            rowData = getFieldData()
            md5sum = self.md5(*rowData)
            if self.isExists(table, md5sum, addData):
                continue
            rowData.append(md5sum)
            addData.append(rowData)
            i += 1

        sql = 'insert %s (%s, md5sum) values (' % (table, fields)
        sql += ("%s, " * len(fields.split(','))) + '%s)'
        self.db.executemany(sql, addData)

    def randSchool(self, num=None):
        """
        随机学校数据
        """
        city = ['深圳', '广州', '佛山', '中山', '东莞', '梅州', '茂名', '汕头']
        sub = ['大学', '中学', '职业学院', '师范学院', '小学']

        num = num or self.school
        schoolNum = self.db.col('select count(*) from school')
        if num + schoolNum > len(city) * len(sub) * len(RandOaData.cnNum):
            return

        def getSchool():
            school = []
            randcity = choice(city)
            school.append(randcity + '第' + choice(RandOaData.cnNum) + choice(sub))
            school.append(randcity + "市")
            return school

        self.loop(num, 'school', "name, location", getSchool)

    def randTeacher(self, num=None, sid=None):
        """
        随机教师数据
        """
        sid = self.getSidList(sid)

        def getTeacher():
            teacher = []
            teacher.append(choice(sid))
            teacher.append(self.getName())
            teacher.append(randint(0, 1))
            return teacher

        self.loop(num, 'teacher', 'sid, name, gender', getTeacher)

    def randCourse(self, num=None, sid=None):
        """
        随机课程数据
        """
        sid = self.getSidList(sid)

        name = ['语文', '数学', '英语', '政治', '生物', '化学', '物理',
                '历史', '地理', '几何', '美术', '音乐', '体育', '计算机',
                'PHP', 'Python', 'Java', 'C', 'C++', 'Go', 'Shell', 'Ruby',
                'MySQL', 'HTML', 'CSS', 'JavaScript', 'UI', 'Django', 'Vim',
                '测试', '运维', '自动化测试', '自动化运维']

        def getCourse():
            course = []
            course.append(choice(sid))
            course.append(choice(name))
            return course

        self.loop(num, 'course', 'sid, name', getCourse)

    def randScoolObj(self, sid, table):
        """
        随机某个学校一个对象
        """
        sql = "select id from %s where sid=%%s" % table
        data = self.db.query(sql, [sid])
        if not data:
            return None
        #  print(sql, sid, data, ' -------------')
        data = choice(data)
        #  print(sql, sid, data, " ########")
        return data['id']

    def randTeacherCourse(self, num=None, sid=None):
        def getTeacherCourse():
            r = []
            while True:
                school = choice(sid)
                tid = self.randScoolObj(school, 'teacher')
                if tid is None:
                    continue
                cid = self.randScoolObj(school, 'course')
                if cid is None:
                    continue
                r.append(school)
                r.append(tid)
                r.append(cid)
                break
            return r

        sid = self.getSidList(sid)
        self.loop(num, 't_to_c', 'sid, tid, cid', getTeacherCourse)

    def randClass(self, num=None, sid=None):
        sid = self.getSidList(sid)
        name = ['语文', '数学', '英语', '政治', '生物', '化学', '物理',
                '历史', '地理', '几何', '美术', '音乐', '体育', '计算机',
                'PHP', 'Python', 'Java', 'C', 'C++', 'Go', 'Shell', 'Ruby',
                'MySQL', 'HTML', 'CSS', 'JavaScript', 'UI', 'Django', 'Vim',
                '测试', '运维', '自动化测试', '自动化运维']

        def getClass():
            c = []
            c.append(choice(sid))
            c.append(choice(name) + choice(RandOaData.cnNum) + '班')
            return c

        self.loop(num, 'class', 'sid, name', getClass)

    def randClassTeacherCourse(self, num=None, sid=None):
        def getClassTeacherCourse():
            r = []
            while True:
                school = choice(sid)
                tid = self.randScoolObj(school, 't_to_c')
                if tid is None:
                    continue
                cid = self.randScoolObj(school, 'class')
                if cid is None:
                    continue
                r.append(tid)
                r.append(cid)
                break
            return r

        sid = self.getSidList(sid)
        self.loop(num, 'c_to_tc', 'tid, cid', getClassTeacherCourse)

    def randStudent(self, num=None, cid=None):
        """
        随机教师数据
        """
        cid = self.db.query("select id,sid from class")
        if not cid:
            return

        def getStudent():
            s = []
            c = choice(cid)
            s.append(c['sid'])
            s.append(c['id'])
            s.append(self.getName())
            s.append(randint(0, 1))
            s.append('1%s%s%s' % (choice('3578'),
                                  str(randint(10000, 99999)),
                                  str(randint(1000, 9999))))
            return s

        self.loop(num, 'student', 'sid, cid, name, gender, phone', getStudent)

    def randChoose(self, num=None, sid=None):
        def getChoose():
            r = []
            while True:
                school = choice(sidList)
                cid = self.randScoolObj(school, 'course')
                if cid is None:
                    continue
                studentId = self.randScoolObj(school, 'student')
                if studentId is None:
                    continue
                print(cid, studentId)
                r.append(cid)
                r.append(studentId)
                break
            return r

        sidList = self.getSidList(sid)
        self.loop(num, 'choose', 'cid, sid', getChoose)

    def randScore(self, num=None):
        def getScore():
            r = []
            r.append(choice(chooseList))
            r.append("%s%s" % (randint(0, 100), choice(['', '.5'])))
            return r

        chooseList = self.getIdList('choose')
        self.loop(num, 'score', 'cid, score', getScore)


if __name__ == "__main__":
    def main():
        #  db = Db('company')
        #  name = input("请输入要查询的姓名: ")
            #  用户SQL注入: s' or '1'; -- k
        #  sql = "select * from emp where ename=%s"
        #  print(sql)
        #  print(db.query(sql, [name]))
        r = RandOaData()
        #  r.randSchool(100)
        #  r.randTeacher(100)
        #  r.randCourse(100)
        #  r.randTeacherCourse(100)
        #  r.randClass(100)
        #  r.randClassTeacherCourse(100)
        #  r.randStudent(1000)
        r.randChoose(100)
        #  r.randScore(1000)

        #  for s in r.db.query("select * from school"):
            #  print(s['name'], s['location'])

    main()
