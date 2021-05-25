#!/usr/bin/env python3

#  class Student(object):
#  class Student():
class Student:
    def __init__(self, name="未知", age=15, sex="未知", **kwargs):
        self.name = name
        self.age = age
        self.sex = sex
        self.__dict__.update(kwargs)

    def say(self):
        return "姓名: %s, 性别: %s, 年龄: %s" % (self.name, self.sex, self.age)

    def __str__(self):
        return self.say()


class SmallStudent(Student):
    def __init__(self, a, b, c, e="广州", f="13766558877", **d):
        self.address = e
        self.phone = f
        super().__init__(a, b, c, **d)

    def say(self):
        return "小学生: 地址: " + self.address + " " + super().say()

    def __str__(self):
        return self.say()


if __name__ == "__main__":
    def out(s):
        print(s.say())

    s = Student("李四", 20, '男')
    ss = SmallStudent("张三", 10, '男')

    out(s)
    out(ss)
