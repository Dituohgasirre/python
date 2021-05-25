#!/usr/bin/env python3


import MySQLdb


class Db:

    def __init__(self, dbname, user='root', passwd='123123',
                 host='localhost', port=3306, charset='utf8', **kwargs):
        self.conn = MySQLdb.connect(host=host, port=port, user=user,
                                    passwd=passwd, database=dbname,
                                    charset=charset)
        self.cursorArgs = MySQLdb.cursors.DictCursor
        self.__dict__.update(kwargs)
        self.cursor = self.conn.cursor(self.cursorArgs)
        self.isExitRun = False

    def __getattr__(self, name):
        if name in self.__dict__:
            return self.__dict__[name]
        o = getattr(self.cursor, name, None)
        if o is None:
            return getattr(self.conn, name)
        return o

    def query(self, sql, args=None):
        self.cursor.execute(sql, args)
        return self.fetchall()

    def row(self, sql, args=None):
        data = self.query(sql, args)
        if len(data) > 0:
            return data[0]
        return None

    def col(self, sql, args=None):
        data = self.row(sql, args)
        if not data:
            return None
        return list(data.values())[0]

    def exit(self):
        if self.isExitRun:
            return
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        self.isExitRun = True

    def __del__(self):
        self.exit()

    def __enter__(self):
        return self.cursor

    def __exit__(self, e_type, e_value, e_tb):
        self.exit()

if __name__ == "__main__":
    def withTest():
        with Db('company') as c:
            c.execute("select * from emp")
            while True:
                row = c.fetchone()
                if not row:
                    break
                print(row['ename'])
            print("----------------------")
            c.scroll(-3)
            for row in c.fetchall():
                print(row['ename'])

            print("----------------------")
            c.scroll(0, mode='absolute')
            #  print(c.fetchall())

    db = Db('company')
    #  db.execute("select * from emp")
    print("emp count: ", db.col("select count(*) from emp"))
    print("wangwu: ", db.row("select * from emp where ename='wangwu'"))

    for row in db.query("select * from emp"):
        print(row['ename'])

