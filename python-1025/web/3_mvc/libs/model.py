#!/usr/bin/env python3


from config import Config
from db import Db
from hashlib import md5
from exception import SQLException


class Model:

    class Field:
        def __init__(self, primary=None):
            self.primary = primary

    _db = None

    def __init__(self, **kwargs):
        if Model._db is None:
            Model._db = Db(**Config.DB_CONFIG)
            #  Model._db = Db('oa')

        self.field = []
        self.primary = None
        for k, v in self.__class__.__dict__.items():
            if isinstance(v, Model.Field):
                if v.primary:
                    self.primary = k
                self.field.append(k)

        self._limit = ""
        self._where = ""
        self._orderBy = ""

        self.classObj = self.__class__
        self.table = self.__class__.__name__.lower()

        self.__dict__.update(kwargs)

    def genMd5(self):
        data = ""
        for name in self.field:
            if name == self.primary or name == 'md5sum':
                continue
            o = getattr(self, name)
            if isinstance(o, Model.Field):
                continue
            data += str(o)
        data = ''.join(sorted(data))
        return md5(data.encode()).hexdigest()

    def exists(self):
        """
        校验数据唯一性(多字段)
        """
        sql = 'SELECT %s FROM %s WHERE md5sum=%%s' % (self.primary, self.table)
        self.md5sum = self.genMd5()
        if bool(self._db.row(sql, [self.md5sum])):
            return True

        return False

    def add(self):
        field = ''
        value = []
        for k in self.field:
            o = getattr(self, k)
            if k == self.primary or isinstance(o, Model.Field):
                continue
            field += k + ','
            value.append(o)

        field = field.rstrip(',')
        value_str = ('%s,' * len(value)).rstrip(',')

        sql = "INSERT %s (%s) VALUES(%s)" % (self.table, field, value_str)

        self._db.execute(sql, value)
        setattr(self, self.primary, self._db.lastrowid)

    def update(self):
        setstr = ''
        for k in self.field:
            o = getattr(self, k)
            if isinstance(o, Model.Field):
                continue
            setstr += "%s='%s'," % (k, o)
        setstr = setstr.rstrip(',')

        sql = "UPDATE %s SET %s WHERE %s=%s" % (self.table, setstr,
                                                self.primary,
                                                getattr(self, self.primary))
        #  print(sql)
        self.lastsql = sql
        self._db.execute(sql)


    def save(self):
        if self.exists():
            raise SQLException

        if isinstance(getattr(self, self.primary), Model.Field):
            self.add()
        else:
            self.update()
        self._db.commit()


    def where(self, con):
        self._where = " WHERE " + con
        return self

    def limit(self, num, start=None):
        if start is None:
            self._limit = ' LIMIT %d' % num
        else:
            self._limit = ' LIMIT %d, %d' % (start, num)
        return self

    def orderBy(self, field, desc=True):
        desc = 'DESC' if desc else ''
        self._orderBy = ' ORDER BY %s %s' % (field, desc)
        return self

    def count(self):
        where = self._where or ''
        order = self._orderBy or ''
        sql = 'SELECT COUNT(*) FROM %s %s %s' % (self.table, where, order)
        self.lastsql = sql
        return self._db.col(sql)

    def select(self):
        where = self._where or ''
        limit = self._limit or ''
        order = self._orderBy or ''
        sql = 'SELECT * FROM %s %s %s %s' % (self.table, where, order, limit)
        self.lastsql = sql
        self._where = self._limit = self._orderBy = ''
        objs = []
        for row in self._db.query(sql):
            objs.append(self.classObj(**row))

        return objs


    def delete(self, ids=None):
        ids = ids or getattr(self, self.primary)
        if not ids:
            return
        sql = 'DELETE FROM %s WHERE %s=%s' % (self.table, self.primary, ids)
        self._db.execute(sql)
        self._db.commit()



if __name__ == '__main__':
    class Student(Model):
        id = Model.Field(primary=True)
        sid = Model.Field()
        cid = Model.Field()
        name = Model.Field()
        gender = Model.Field()
        phone = Model.Field()
        md5sum = Model.Field()


    class Teacher(Model):
        tname = Model.Field()

    """ 添加 """
    s = Student(name='kyo', sid=17)
    s.cid = 33
    s.gender = 0
    s.phone = '13455567788'
    s.md5sum = '234234234'
    s.save()

    """ 查询和修改 """
    s = Student().where('id=1007').select()[0]
    s.cid = 34
    s.sid = 55
    s.gender = 1
    s.save()

    s.delete(1008)

    """ 查询 """
    s = Student()
    for i in s.where('sid=16').limit(10).select():
        print(i, i.name, i.gender, i.sid)

    t = Teacher()
    for i in t.where('sid=16').limit(10).select():
        print(i, i.name, i.gender, i.sid)


